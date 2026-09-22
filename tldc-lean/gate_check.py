#!/usr/bin/env python3
import re, pathlib
def strip_comments(s):
    s = re.sub(r"/-.*?-/", "", s, flags=re.S)
    s = re.sub(r"--[^\n]*", "", s)
    return s
def read(p):
    return pathlib.Path(p).read_text(encoding="utf-8")

core, inter = read("TLDC/Core.lean"), read("TLDC/Interface.lean")
a2, liv = read("TLDC/Instances/A2.lean"), read("TLDC/Instances/Liouville.lean")
cc, ic = strip_comments(core), strip_comments(inter)
ca, cl = strip_comments(a2), strip_comments(liv)

print("===== G1 唯一 Core =====")
decls = re.findall(r"theorem\s+no_failure\b", cc + ic + ca + cl)
print("  ① 全仓 theorem no_failure 精确定义处 = %d   (须 = 1)" % len(decls))
wf = {}
for p in ["TLDC/Core.lean", "TLDC/Instances/A2.lean", "TLDC/Instances/Liouville.lean"]:
    wf[p] = len(re.findall("lt_wfRel", strip_comments(read(p))))
print("  ② 良基引用分布 = %s" % wf)
inst_decl = len(re.findall(r"theorem\s+no_failure\b", ca + cl))
calls = ca.count("TLDC.no_failure_of_slots") + cl.count("TLDC.no_failure_of_slots")
print("  ③ 实例内自行定义 theorem no_failure = %d (须 0)；实例调用核次数 = %d" % (inst_decl, calls))

print("===== G2 Core 零污染（去注释后）=====")
bad = ["Prime", "prime", "Liou", "Fermat", "group", "Brahmagupta", "Euclid", "Target", "IsGood", "ZMod", "H", "q", "p"]
for code, name in [(ic, "Interface.lean"), (cc, "Core.lean")]:
    hits = {}
    for t in bad:
        n = len(re.findall(r"\b" + re.escape(t) + r"\b", code))
        if n: hits[t] = n
    print("  %s 禁用词命中 = %s" % (name, hits if hits else "无"))
print("  Core 去注释后的全部标识符 = %s" % sorted(set(re.findall(r"[A-Za-z_][A-Za-z0-9_.]*", cc))))

print("===== G3 A2 层 =====")
print("  ① 三声明齐备: derive_Target=%s reenter_P=%s a2_no_failure=%s" % (
    "theorem derive_Target" in a2, "theorem reenter_P" in a2, "theorem a2_no_failure" in a2))
seg = re.search(r"theorem derive_Target.*?(?=\ntheorem|\Z)", strip_comments(a2), flags=re.S).group(0)
print("  ② derive_Target 中反证假设 h 的引用 = %d  (须 0)" % len(re.findall(r"\bh\b", seg)))
print("  ③ a2_no_failure 调用核 = %d 处" % a2.count("TLDC.no_failure_of_slots"))

print("===== G4 Liouville 层 =====")
print("  ① 层内三声明: H_of_inner=%s outer_induction=%s step_via_core=%s" % (
    "theorem H_of_inner" in liv, "theorem outer_induction" in liv, "theorem liouville_step_via_core" in liv))
print("  ② 层内 lt_wfRel 次数 = %d  (须 >= 1，外层强归纳在本层)" % len(re.findall("lt_wfRel", cl)))
hits = {}
for t in ["IsGood", "liouville_exact", "H"]:
    n = len(re.findall(r"\b" + t + r"\b", cc))
    if n: hits[t] = n
print("  ③ 核内 IsGood/exact/H 命中 = %s  (须空)" % (hits if hits else "无"))
print("  ④ Liouville 层调用核 = %d 处 (步内调用)" % liv.count("TLDC.no_failure_of_slots"))

print("===== G5 双实例共享 =====")
print("  ① import TLDC.Core: A2=%s Liouville=%s" % ("import TLDC.Core" in a2, "import TLDC.Core" in liv))
mods = sorted(x.name for x in pathlib.Path("TLDC").glob("*.lean"))
print("  ② TLDC 顶层模块 = %s" % mods)
print("  ③ 全仓 import TLDC.Core 的文件数 = %d" % len([p for p in pathlib.Path(".").rglob("*.lean") if "import TLDC.Core" in p.read_text(encoding="utf-8")]))
