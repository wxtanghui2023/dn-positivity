#!/usr/bin/env python3
"""契约一致性检查器（Gate C · C5）—— 实现验收契约 §2.3 的五项检查。

用法:
    python3 check_consistency.py <package_dir> [--negative-control]

检查项:
  c1  数量由数据源生成      —— 从 artefact_hashes 实际键集计数
  c2  摘要与实际文件相符    —— 逐条目核对 SHA-256
  c3  清单覆盖与排除规则    —— SHA256SUMS.txt 覆盖范围 / 是否含 JSON 自身
  c4  声明与数据源一致      —— MD/JSON 中的数量声明 == 数据源计数
  c5  负控（需 --negative-control）—— 在一次性副本中把声明改错，c4 必须失败

退出码: 0 = 全部通过; 1 = 存在失败项。无网络访问，无副作用（负控在 /tmp 副本内进行）。
"""
import hashlib
import json
import os
import re
import shutil
import sys
import tempfile

EXIT_OK = 0
EXIT_FAIL = 1


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def find_hash_json(pkg):
    """定位含 artefact_hashes 的 JSON（优先 *PREREGISTRATION*.json）。"""
    best = None
    for n in sorted(os.listdir(pkg)):
        if not n.endswith('.json'):
            continue
        try:
            d = json.load(open(os.path.join(pkg, n), encoding='utf-8'))
        except Exception:
            continue
        if isinstance(d, dict) and isinstance(d.get('artefact_hashes'), dict):
            if best is None or ('PREREGISTRATION' in n and 'PREREGISTRATION' not in best[0]):
                best = (n, d)
    return best


def digest_of(v):
    if isinstance(v, str):
        return v
    if isinstance(v, dict):
        for k in ('sha256', 'sha', 'hash', 'digest'):
            if isinstance(v.get(k), str):
                return v[k]
    return None


def declared_counts(pkg):
    """收集 Markdown 中与「哈希」相关的数量声明（形如 '26 项'）。"""
    out = []
    for n in sorted(os.listdir(pkg)):
        if not n.endswith('.md'):
            continue
        text = open(os.path.join(pkg, n), encoding='utf-8').read()
        for m in re.finditer(r'(\d+)\s*项', text):
            line = text[:m.start()].split('\n')[-1] + text[m.start():m.end() + 20].split('\n')[0]
            if not (('哈希' in line) or ('hash' in line.lower())):
                continue
            # 历史提及（描述旧缺陷/旧版本）不是本版声明，不得计入
            if any(k in line for k in ('仍写', '旧', '曾', '原', '修复前', 'D-5', '不再是')):
                continue
            out.append({'file': n, 'value': int(m.group(1)), 'context': line.strip()[:90]})
    return out


def run_checks(pkg):
    r = {'package': os.path.basename(os.path.abspath(pkg))}
    hj = find_hash_json(pkg)
    if not hj:
        return {'ok': False, 'reason': 'NO_ARTEFACT_HASHES_JSON'}
    json_name, doc = hj
    art = doc['artefact_hashes']

    # c1 —— 数据源计数
    n = len(art)
    r['c1_count_from_data_source'] = n
    r['c1_source_file'] = json_name

    # c2 —— 摘要逐项核对
    missing, mismatch, ok = [], [], 0
    for rel, val in art.items():
        want = digest_of(val)
        cand = [os.path.join(pkg, rel), os.path.join(pkg, os.path.basename(rel))]
        hit = next((c for c in cand if os.path.isfile(c)), None)
        if not hit:
            missing.append(rel)
            continue
        got = sha256_file(hit)
        if want and got != want:
            mismatch.append({'path': rel, 'expected': want, 'actual': got})
        else:
            ok += 1
    r['c2_verified'] = ok
    r['c2_missing'] = missing
    r['c2_mismatch'] = mismatch
    r['c2_pass'] = (not missing) and (not mismatch)

    # c3 —— 清单覆盖与排除规则
    sums = os.path.join(pkg, 'SHA256SUMS.txt')
    covered, includes_json, sums_pass = [], False, True
    if os.path.isfile(sums):
        for line in open(sums, encoding='utf-8'):
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            parts = line.split(None, 1)
            if len(parts) == 2:
                p = parts[1].lstrip('*').strip()
                covered.append(p)
                if os.path.basename(p) == json_name:
                    includes_json = True
        # 清单内每条必须实际匹配
        for p in covered:
            f = os.path.join(pkg, p)
            if os.path.isfile(f):
                want = next((l.split()[0] for l in open(sums, encoding='utf-8')
                             if l.strip().endswith(p)), None)
                if want and sha256_file(f) != want:
                    sums_pass = False
    else:
        sums_pass = False
    present = set()
    for dp, _, ns in os.walk(pkg):
        for fn in ns:
            if fn == '__pycache__' or fn.endswith('.pyc'):
                continue
            rel = os.path.relpath(os.path.join(dp, fn), pkg)
            if rel == 'SHA256SUMS.txt':
                continue
            present.add(rel)
    r['c3_uncovered_files'] = sorted(present - set(covered))
    r['c3_sums_entries'] = len(covered)
    r['c3_includes_json'] = includes_json
    r['c3_sums_digests_pass'] = sums_pass
    r['c3_pass'] = bool(covered) and sums_pass

    # c4 —— 声明与数据源一致
    decl = declared_counts(pkg)
    r['c4_declared'] = decl
    bad = [d for d in decl if d['value'] != n]
    r['c4_mismatched_declarations'] = bad
    r['c4_pass'] = (not bad)

    r['ok'] = bool(r['c2_pass'] and r['c3_pass'] and r['c4_pass'])
    r['summary'] = {'c1': n, 'c2_pass': r['c2_pass'], 'c3_pass': r['c3_pass'],
                    'c4_pass': r['c4_pass'],
                    'claims': sorted({d['value'] for d in decl})}
    return r


def negative_control(pkg):
    """在一次性副本中把数量声明改错，确认 c4 必须失败。"""
    n = len(find_hash_json(pkg)[1]['artefact_hashes'])
    tmp = tempfile.mkdtemp(prefix='c5neg-')
    try:
        dst = os.path.join(tmp, os.path.basename(os.path.abspath(pkg)))
        shutil.copytree(pkg, dst)
        wrong = n + 1
        patched = []
        for fn in sorted(os.listdir(dst)):
            if not fn.endswith('.md'):
                continue
            p = os.path.join(dst, fn)
            lines = open(p, encoding='utf-8').read().split('\n')
            out, hit = [], 0
            for ln in lines:
                if (('哈希' in ln) or ('hash' in ln.lower())) and not any(
                        k in ln for k in ('仍写', '旧', '曾', '原', '修复前', 'D-5', '不再是')):
                    new_ln = re.sub(r'\d+(?=\s*项)', str(wrong), ln)
                    if new_ln != ln:
                        hit += 1
                        ln = new_ln
                out.append(ln)
            if hit:
                open(p, 'w', encoding='utf-8').write('\n'.join(out))
                patched.append('%s(hits=%d)' % (fn, hit))
        res = run_checks(dst)
        return {'wrong_value': wrong, 'patched_files': patched,
                'c4_pass_under_wrong_declaration': res.get('c4_pass'),
                'detected': res.get('c4_pass') is False,
                'c2_still_pass': res.get('c2_pass'), 'c3_still_pass': res.get('c3_pass')}
    finally:
        shutil.rmtree(tmp, ignore_errors=True)


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return EXIT_FAIL
    pkg = argv[1]
    res = run_checks(pkg)
    if '--negative-control' in argv:
        res['c5_negative_control'] = negative_control(pkg)
        # 负控判据 = 仅"被检出"（副本中 MD 被改写会使 c2 失配，这是正确行为，不作为失败）
        res['ok'] = bool(res.get('ok') and res['c5_negative_control']['detected'])
    print(json.dumps(res, indent=1, ensure_ascii=False))
    return EXIT_OK if res.get('ok') else EXIT_FAIL


if __name__ == '__main__':
    sys.exit(main(sys.argv))
