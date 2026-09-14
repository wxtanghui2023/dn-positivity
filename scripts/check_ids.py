#!/usr/bin/env python3
"""check_ids.py — dn-project 编号撞车检查器（提交前必跑）

PURPOSE
  本项目惯例：**一个编号 = 一个探索项**（E-item / V-item）⟹ 同一项的 doc 与脚本**共享**编号
  （例：E100 的 `docs/E100-*.md` ＋ `scripts/E100_*.py/.txt`）⟹ **同号多文件不是撞车**。
  致命撞车 = 三者之一：
    (A)  同一编号出现在 **≥2 个不同 doc（.md）**
    (B)  台账 `docs/ID-CLAIMS.tsv` 中同一编号被 **≥2 个 stream** 领用
    (B') 台账中同一编号、同一 stream 出现 **≥2 个 slug**（一号两物）
  ⚠️ **扫描范围 ＝ 工作树 ∪ git 索引/HEAD** —— 用于捕获"只 `git add` 新路径、旧路径残留在索引"式
     的**隐性撞车**（本日实际发生过一次：V110→V111 迁号只 add 新路径 ✗）。
  非致命提示：
    (C) 只有脚本、无 doc（可能在制品）
    (D) 有文件但无领用记录
    (E) 索引中有该路径但工作树已缺失（残留，需 `git add -u <路径>` 补提交删除）

INPUT     : docs/*.md, scripts/*, git ls-files（docs/ scripts/）, docs/ID-CLAIMS.tsv
OUTPUT    : 标准输出报告；退出码 0=无致命撞车, 1=有致命撞车, 2=环境异常
DISCIPLINE: 只读；不写入任何文件；只遍历 docs/ 与 scripts/ 两个显式目录（禁全盘 find）
USAGE     : python3 scripts/check_ids.py [--quiet]
"""
import collections
import glob
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAT = re.compile(r"^([A-Z]\d{3})[-_]")
ALIAS_STREAM = "legacy-alias"


def worktree():
    docs, scripts = collections.defaultdict(list), collections.defaultdict(list)
    for sub in ("docs", "scripts"):
        for p in glob.glob(os.path.join(ROOT, sub, "*")):
            name = os.path.basename(p)
            m = PAT.match(name)
            if not m:
                continue
            (docs if name.endswith(".md") else scripts)[m.group(1)].append(f"{sub}/{name}")
    return docs, scripts


def tracked():
    try:
        out = subprocess.run(
            ["git", "ls-files", "docs", "scripts"],
            cwd=ROOT, capture_output=True, text=True, check=True,
        ).stdout
    except Exception:
        return []
    return [l.strip() for l in out.splitlines() if l.strip()]


def main():
    quiet = "--quiet" in sys.argv
    docs, scripts = worktree()
    tracked_paths = tracked()
    tracked_ids = set()
    stale = []
    for rel in tracked_paths:
        name = os.path.basename(rel)
        m = PAT.match(name)
        if not m:
            continue
        sub, i = rel.split("/", 1)[0], m.group(1)
        tracked_ids.add((i, rel))
        if not os.path.exists(os.path.join(ROOT, rel)):
            stale.append(rel)
        bucket = docs if name.endswith(".md") else scripts
        if rel not in bucket[i]:
            bucket[i].append(rel)

    ledger_path = os.path.join(ROOT, "docs", "ID-CLAIMS.tsv")
    ledger = collections.defaultdict(set)
    slugmap = collections.defaultdict(set)
    if os.path.exists(ledger_path):
        with open(ledger_path, encoding="utf-8", errors="replace") as f:
            for line in f:
                parts = line.rstrip("\n").split("\t")
                if len(parts) >= 2 and PAT.match(parts[0] + "-") and parts[1] != ALIAS_STREAM:
                    ledger[parts[0]].add(parts[1])
                    slugmap[parts[0]].add(parts[2] if len(parts) > 2 else "")

    fatal, warn = [], []
    for k, v in sorted(docs.items()):
        if len(v) > 1:
            fatal.append((k, "同号 ≥2 doc（工作树∪索引）", sorted(v)))
    for k, v in sorted(ledger.items()):
        if len(v) > 1:
            fatal.append((k, "台账同号多 stream", sorted(v)))
    for k, v in sorted(slugmap.items()):
        if len(v) > 1:
            fatal.append((k, "台账同号同流多 slug（一号两物）", sorted(v)))
    for k in sorted(set(scripts) - set(docs)):
        warn.append((k, "只有脚本，无 doc（可能在制品）", sorted(scripts[k])))
    for k in sorted((set(docs) | set(scripts)) - set(ledger)):
        warn.append((k, "无领用记录", sorted(docs.get(k, []) + scripts.get(k, []))))
    if stale:
        warn.append(("-", "索引中有但工作树缺失（残留，用 `git add -u <路径>` 补提交删除）", sorted(stale)))

    print(f"[check_ids] 编号 {len(set(docs) | set(scripts))} 个｜台账 {len(ledger)} 条｜"
          f"doc {sum(len(v) for v in docs.values())} 个｜脚本 {sum(len(v) for v in scripts.values())} 个"
          f"｜索引跟踪 {len(tracked_ids)} 个")
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
            print(f"  {k}: {why} -> {', '.join(v[:3])}" + (" ..." if len(v) > 3 else ""))
    if not os.path.exists(ledger_path):
        print("[check_ids] ⚠️ 台账 docs/ID-CLAIMS.tsv 不存在（用 scripts/id_claim.sh 领号创建）")
    return 1 if fatal else 0


if __name__ == "__main__":
    sys.exit(main())
