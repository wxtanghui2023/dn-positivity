#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
nogo_gate.py —— 【强制查重门】任何新推导方向开工前的第一道程序
（唐先生 2026-09-14 13:19 指令：「任何一个新的推导方向，首先必须对比已有的 NO-GO 地图，避免重新掉坑」）

用法：
  python3 scripts/nogo_gate.py "方向名" 关键词1 关键词2 ... [--obj 对象名1 对象名2 ...]

  --obj 之后的词按【对象名/代号】检索（E112 教训：技术词检索会漏）
  其余词按【技术词】检索

输出：A 对象名命中 / B 技术词命中 / C 结论模板（必须由人填写判定）
纪律：只扫指定地图文件（不递归大目录，不扫 fn_backup/ fupeng/ github/ quant-system/ .git）
退出码：0 = 无命中（可用）；1 = 有命中（必须先读命中处再判定，不得直接开工）
"""
import os
import re
import sys

MAPS = [
    "docs/MASTER-NOGO-AND-LIVE-PATHS.md",
    "docs/CLOSED-ROUTES-MAP.md",
    "docs/GAP-COORDINATES-positivity.md",
    "docs/POS1-positivity-dichotomy.md",
    "docs/POS2-positivity-paradigm-closure.md",
    "docs/POS3-provably-positive-mechanisms-enumeration.md",
    "docs/NOGO-QUOTIENT-N1-N7.md",
    "docs/NOGO-registry-and-screens.md",
    "docs/RH-prior-NOGO-checklist-2026-09-09.md",
    "docs/E18-NOGO-ALIGNMENT.md",
    "docs/E103-T1-monopoly.md",
    "docs/E104-limit-procedure-classification.md",
    "docs/E105-relational-limit-necessity.md",
    "docs/E106-CACC-sharpening.md",
    "docs/E159-E141-E158-closing-index.md",
    "docs/EXPLORATION-POINTS-REGISTER.md",
    "docs/INDEX-BY-DIRECTION.md",
]


def scan(terms, maps, root="."):
    hits = {}
    for m in maps:
        p = os.path.join(root, m)
        if not os.path.exists(p):
            continue
        try:
            with open(p, encoding="utf-8") as fh:
                for i, line in enumerate(fh, 1):
                    for t in terms:
                        if re.search(t, line, re.I):
                            hits.setdefault(t, []).append((m, i, line.strip()[:150]))
        except Exception as e:
            print("  [warn] %s: %s" % (m, e))
    return hits


def show(title, hits):
    print("\n" + "=" * 72)
    print(title)
    print("=" * 72)
    if not hits:
        print("  —— 零命中")
        return 0
    n = 0
    for t, lst in hits.items():
        print("\n  [词] %s   （%d 处）" % (t, len(lst)))
        for m, i, text in lst[:6]:
            print("    %s:%d  %s" % (m, i, text))
        if len(lst) > 6:
            print("    ... 共 %d 处" % len(lst))
        n += len(lst)
    return n


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return 2
    name = args[0]
    rest = args[1:]
    terms, objs = [], []
    cur = terms
    for a in rest:
        if a == "--obj":
            cur = objs
            continue
        cur.append(a)

    print("#" * 72)
    print("# NO-GO 门：[%s]" % name)
    print("# 地图文件 %d 份（只扫这些，不递归）" % len(MAPS))
    print("#" * 72)

    n1 = show("A. 【对象名/代号】检索（E112 教训：必查）", scan(objs, MAPS) if objs else {})
    n2 = show("B. 【技术词】检索", scan(terms, MAPS) if terms else {})
    total = n1 + n2

    print("\n" + "=" * 72)
    print("C. 结论模板（必须逐项填写后才可开工）")
    print("=" * 72)
    print("""
  ⚠️ 命中数 = %d 。规则：
     · 命中 > 0  ⟹ 必须先读命中处，再判 命中 / 部分命中 / 未命中（三选一）
     · 命中 = 0  ⟹ 也不等于可开工（地图可能用不同词汇；须再按对象名过一遍）

  待填：
    ① 本方向的【对象】在档是否已审？        [ 是 / 否 ]  依据：
    ② 本方向的【机制】在档是否已判死/归位？  [ 是 / 否 ]  依据：
    ③ 落点是否属已登记的墙？                [ 哪一堵 ]   依据：
    ④ 若"未命中"：理由必须写成【可反驳】形式（为何不是同一物）：
    ⑤ 结论： [ 已归位 ⟹ 不开工 ] / [ 未归位 ⟹ 可开工，并记录 ①②③ 的逐字依据 ]
""" % total)
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
