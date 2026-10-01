结论: 已查地图：命中 60 处 —— 先逐条判 已DEAD/已封/已登记；命中即引既有条目，不得开新案
D0: 本档对象 = HN-C2 之 L4 判定实验（工具产物 ＋ 已证结构定理）；不主张新数学值
D1: 0 （产出 = 一条结构定理 ＋ 一条 LP 恒等读数 ＋ 一份路径天花板表 ＋ 一次未决判定）
ASSUMES: C(11,5,3)=20｜C(10,4,2)=9（库内已封闭精确值）｜Schönheim 递归 $C(v,k,t)\ge\lceil\frac vkC(v-1,k-1,t-1)\rceil$｜$\mathrm{Aut}(S_{12})$ 传递性（用于 LP 对称化）

# RESULT-2026-10-01 — HN-C2（$C(12,6,4)$）：等号结构定理 ＋ 路径天花板表 ＋ 判定实验（第二轮 UNKNOWN）

## §0 结论三条

$$\textbf{① 结构定理（新，已证）}:\ M{=}40\ \Longrightarrow\ \textbf{\text{每点恰在 20 块}}（\text{正则性}）\wedge\textbf{\text{6 个互不相交特对}}（\text{对内 }\lambda{=}10,\ \text{之间 }\lambda{=}9）\wedge\ 12\ \text{个派生设计为 }(11,5,3)\ \text{最优}$$
$$\textbf{② 路径天花板（先验裁定）}:\ \text{一阶 LP／均匀权} = \mathbf{33}（\text{对称性，实测吻合}）;\ \text{递归 Schönheim} = 2\times C(11,5,3) = \mathbf{40}（\text{＝库下限，来源查明}）;\ \text{Johnson/Delsarte} = \text{分数覆盖数同对象}$$
$$\textbf{③ 判定实验}：\text{第二轮（等号结构约束, }600\,\mathrm{s}\text{）} = \textbf{UNKNOWN};\ \text{第三轮 }3600\,\mathrm{s}\ \text{进行中} \Longrightarrow \textbf{\text{不作不存在证据}} ⚠️$$

## §1 判定实验读数（实测 ✓）

| 版本 | 时限 | 冲突 | 分支 | 判定 |
|---|---|---|---|---|
| ① 仅覆盖＋总数 | 300 s | 3,456,004 | 37,921,730 | UNKNOWN |
| ② ＋等号结构约束 | 600 s | **97,379**（↓35×） | **9,489,229**（↓4×） | UNKNOWN |
| ③ ＋更长时限（3600 s／8 workers） | 3600 s | 运行中 | 运行中 | ⏳ |

$$\Longrightarrow\ \text{等号结构约束\ \textbf{确实压缩搜索空间}（冲突 ↓35×、分支 ↓4×）}，但 600 s 不足；三出口与判定一览见 §2 ✓$$

## §2 三出口（第三轮将给出）

$$\textbf{INFEASIBLE}\ \Longrightarrow\ C(12,6,4)=41\ \textbf{\text{精确}}（\text{gap 闭合};\ \text{库下限 }40\to41）;\qquad \textbf{FEASIBLE}\ \Longrightarrow\ \textbf{\text{40 块显式设计}}（\text{记录改进 }41\to40）;\qquad \textbf{UNKNOWN}\ \Longrightarrow\ \text{未决}$$
**纪律** ✓：UNKNOWN **不作**不存在证据；FEASIBLE 须逐项复核（每点度＝20／特对 λ＝10·9／覆盖 495/495）

## §3 制度产出（本档连带 ✓）

$$\text{(i) }\textbf{\text{天花板前置}}（§2.5）:\ \text{动手前先算路径上限},\ \le\text{目标者一律排除};\quad \text{(ii) }\textbf{\text{三重前置}}（§2.6）:\ \text{理论}\to\text{量级}\to\text{前提/可行性},\ \text{过关才算};\quad \text{(iii) }\textbf{\text{逻辑可杀预筛}}（§2.7）;\quad \text{(iv) }\textbf{\text{已试判定前置}}（§2.8）$$

## §4 边界与纪律

$$\textbf{(D1)}\ \text{不主张新数学值} ✓;\ \textbf{(D2)}\ \text{读数皆实跑可复核（}scripts/\text{＋}out/\text{）} ✓;\ \textbf{(D3)}\ \text{未取禁用原文／未碰 RH} ✓$$

## §5 【技术词回查】

```
技术词 等号结构     命中文件数=10   :: ./C207-T13A-YI-4-continuous-family-exclusion-renaming-and-T13B2-seal.md ./WITAUDIT-2026-09-28-neighbourhood-nesting-audit-A0-vs-C0.md ./PRESSURE-2026-09-29-M106-inequality-slack-table-and-one-equality-conflict.md 
技术词 天花板前置  命中文件数=1    :: ./pilot-HN-C2-C12-6-4-STATE.md
```

ROUTE-CHECK: <全部>=NEW
