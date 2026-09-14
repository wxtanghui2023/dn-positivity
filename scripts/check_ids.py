#!/usr/bin/env python3
"""check_ids.py — dn-project 编号撞车检查器（提交前必跑）

PURPOSE
  本项目惯例：**一个编号 = 一个探索项（E-item / V-item）**，故**同一项的 doc 与脚本共享编号**
  （例：E100 的 `docs/E100-*.md` ＋ `scripts/E100_*.py/.txt`）⟹ **同号多文件不是撞车**。
  真正的撞车定义为二者之一：
    (A) 同一编号出现在 **≥2 个不同 doc（.md）** ⟹ 同号两物 ⛔
    (B) 台账 `docs/ID-CLAIMS.tsv` 中同一编号被 **≥2 个 stream** 领用 ⛔
  另报告（非致命）：(C) 只有脚本没有 doc ⟹ 可能在制品 ⚠️；(D) 有文件但无领用记录 ⚠️

INPUT     : docs/*.md, scripts/*, docs/ID-CLAIMS.tsv
OUTPUT    : 标准输出报告；退出码 0=无致命撞车, 1=有致命撞车, 2=环境异常
DISCIPLINE: 只读；不做任何写入；**只遍历 docs/ 与 scripts/ 两个显式目录**（禁全盘 find）
USAGE     : python3 scripts/check_ids.py [--quiet]
"""
import collections
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 编号族：单个大写字母 + 3 位数字（E###、V### 等），后接 - 或 _
PAT = re.compile(r"^([A-Z]\d{3})[-_]")


def scan(subdirs):
    docs, scripts = collections.defaultdict(list), collections.defaultdict(list)
    for sub in subdirs:
        for p in glob.glob(os.path.join(ROOT, sub, "*")):
            name = os.path.basename(p)
            m = PAT.match(name)
            if not m:
                continue
            (docs if name.endswith(".md") else scripts)[m.group(1)].append(f"{sub}/{name}")
    return docs, scripts


def main():
    quiet = "--quiet" in sys.argv
    docs, scripts = scan(["docs", "scripts"])

    ledger_path = os.path.join(ROOT, "docs", "ID-CLAIMS.tsv")
    ledger = collections.defaultdict(set)
    if os.path.exists(ledger_path):
        with open(ledger_path, encoding="utf-8", errors="replace") as f:
            for line in f:
                parts = line.rstrip("\n").split("\t")
                if len(parts) >= 2 and PAT.match(parts[0] + "-"):
                    ledger[parts[0]].add(parts[1])

    fatal = []
    warn = []

    # (A) 同号 ≥2 doc
    for k, v in sorted(docs.items()):
        if len(v) > 1:
            fatal.append((k, "同号 ≥2 doc", v))
    # (B) 台账同号 ≥2 stream
    for k, v in sorted(ledger.items()):
        if len(v) > 1:
            fatal.append((k, "台账同号多 stream", sorted(v)))
    # (C) 只有脚本没有 doc
    for k in sorted(set(scripts) - set(docs)):
        warn.append((k, "只有脚本，无 doc（可能在制品）", scripts[k]))
    # (D) 有文件无领用
    for k in sorted((set(docs) | set(scripts)) - set(ledger)):
        warn.append((k, "无领用记录", sorted(docs.get(k, []) + scripts.get(k, []))))

    print(f"[check_ids] 编号 {len(set(docs) | set(scripts))} 个｜台账 {len(ledger)} 条｜"
          f"doc {sum(len(v) for v in docs.values())} 个｜脚本 {sum(len(v) for v in scripts.values())} 个")
    if fatal:
        print(f"[check_ids] ⛔ 致命撞车 {len(fatal)} 处：")
        for k, why, v in fatal:
            print(f"  {k}: {why}")
            for p in v:
                print(f"     - {p}")
    else:
        print("[check_ids] ✓ 无致命撞车（同号 doc 唯一 ＋ 台账无冲突）")
    if not quiet and warn:
        print(f"[check_ids] ⚠️ 提示 {len(warn)} 处：")
        for k, why, v in warn:
            print(f"  {k}: {why} -> {', '.join(v[:3])}")
    if not os.path.exists(ledger_path):
        print("[check_ids] ⚠️ 台账 docs/ID-CLAIMS.tsv 不存在（用 scripts/id_claim.sh 领号创建）")
    return 1 if fatal else 0


if __name__ == "__main__":
    sys.exit(main())
