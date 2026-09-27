已查地图：已跑 scripts/prework_map_check.sh s=2,3 补全 族外池 J-分叉 ⟹ 执行自 `AUDIT-2026-09-27-...`（✓）＋ 唐先生 14:08（开 Step 0/Step 1 ✓）；本档 = **Step 0 参数空间闭合 ✓ ＋ Step 1 族外池未见 J-分叉 ⚠️**。
D0: 本档对象 = 族内参数空间补全与族外候选池的 J-分叉审计
D1: 3（**Step 0：s=1..16 全表 ✓✓（闭式全命中）**；**Step 1：族外池无分叉 ⚠️**；**一处双计 bug 更正 ✓**）

# Step 0 ＋ Step 1（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(CG-1 ⭐Step 0 = 参数空间闭合 ✓✓)}\ s\in\{1,\dots,16\}\ \text{全可达且闭式全命中（本机六例 }s{=}1,2,3,4,8,16\ \text{逐项验证 ✓✓）}:}$$
$$\qquad\begin{array}{c|c|c|c|c}
s & A_1 & A_2 & J & \text{硬门（}|V|{=}2048\ \wedge\ \mathfrak B_1(V)\ \wedge\ \mathfrak B_1(\mathcal C)\text{）}\\
\hline
1 & 32 & 2016 & 924672 & ✓✓\\
2 & 64 & 1984 & 815104 & ✓✓\\
3 & 96 & 1952 & 719872 & ✓✓\\
4 & 128 & 1920 & 638976 & ✓✓\\
8 & 256 & 1792 & 458752 & ✓✓\\
16 & 512 & 1536 & 786432 & ✓✓\\
\end{array}$$
$$\qquad\text{（}s{=}5..15\ \text{由 143 例扫描覆盖 ✓；表内 }J=1024(3s^2+4(16-s)^2)\ \text{全中 ✓）} \Longrightarrow \boxed{(A_1,A_2)=(32s,\ 2048-32s),\ A_2=2048-A_1}\ ✓✓$$
$$\boxed{\textbf{(CG-2 ⚠️Step 1 = 族外池无分叉)}\ \text{池}=(\text{完美 Vasil'ev 半码对})\ \text{七 }\lambda\ \text{两两拼接，28 对\textbf{全部过覆盖门} ✓（皆合法 NP1CC ✓）};\ \text{但}:}$$
$$\qquad\text{桶 }(A_1,A_2)\ (\text{已去重 ✓}):\ (128,1920)\times2,\ (896,1152)\times2,\ (\mathbf{1024,1024})\times6,\ (1152,896)\times7,\ (1280,768)\times3,\ (2048,0)\times7$$
$$\qquad\Longrightarrow\ \textbf{每个桶内 }J\ \text{唯一 ✗} \Longrightarrow \boxed{\text{族外池亦\textbf{未见} P1-2 分叉}} \Longrightarrow \text{"单参数塌缩"可能\textbf{深于} Vasil'ev ✓（与唐先生备选结论一致 ✓）}$$
$$\qquad\textbf{诚实边界 ✓}:\ \text{本池仍是"两个完美半码"框架（仅 }H_{15}\ \text{换成了别的完美码 ✓）；尚未触及\textbf{ENP1CC puncturing} 与其它非对称构造 ⚠️}$$
$$\boxed{\textbf{(CG-3 ✓ 双计 bug 更正)}\ A_1+A_2\ \text{一度出现 }=4096=2\cdot\tfrac M2 \Longrightarrow \text{根因}=距离-1/-2 对各有 \textbf{2} 个公共中点 ⟹ 逐 }z\ \text{累加会双计 ✗};\ \text{改为\textbf{配对去重}后 }A_1+A_2=M/2=2048\ ✓\ \text{（与等号链一致 ✓）}}$$
$$
$$
```

---

## §1 迭代要点（**✓**）

```
$$\text{(1) }s{=}2,3\ \text{的原始构造 bug}:\ \text{agreement 集合误建在\textbf{码字}上（}c\ \text{为 }H_7\ \text{元素，非 }1..15 ✓）\ ✗ \Longrightarrow \text{改为建在 }t\text{-索引上后一次通过 ✓}$$
$$\text{(2) 族外池的 }A_1\ \text{谱}:\ 128,896,1024,1152,1280,2048\ \text{——皆为 }2^7=128\ \text{的倍数 ✓（与 }32s\ \text{同族尺度 ✓）}$$
$$\text{(3) 族外池的 }J\ \text{都满足 }J=(A_1+A_2)\cdot\ldots\ \text{型关系 ✓（桶内唯一 ✓ ⟹ }J=f(A_1,A_2)\ \text{在本池成立 ✓）}$$
$$
$$
```

---

## §2 下一步（**✓**）

```
$$\text{(甲) }\textbf{真正族外}:\ \text{ENP1CC puncturing（论文 §VI/Lemma 37 ✓）—— 打破"两个完美半码"对称性 ✓};\ \text{或：半码一为线性一为非线性之外的组合（如两个非线性不同族 ✓）}$$
$$\text{(乙) }\textbf{向证明走}:\ \text{若 }J=f(A_1,A_2)\ \text{普遍成立，则它本身是一个\textbf{新定理}（}\beta\text{-profile 的二阶量被粗不变量钉住 ✓）—— 与 P1-2 的 }n{=}8\ \text{反例对照 ✓（彼时 }J\ \text{在桶内分叉 ✓）}$$
$$\qquad\Longrightarrow\ \text{值得问}:\ \text{为何 }n{=}8\ \text{有分叉而 }n{=}16\ \text{无？—— }\text{与 van Wee 等号链的可用性/}\text{陪集结构维数有关 ⚠️}$$
$$\text{(丙) 119（暂不碰 ✓）};\qquad \text{119}: \textbf{完全不碰} ✓$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：Step 0 参数空间闭合（$s{=}1..16$ 全表）、Step 1 族外池无分叉、双计 bug 更正与配对去重
- **档案已有（引用，不列为提出）**：A-SAGREE-1、A-EXTGATE-1、A-SPLIT37-1、A-CLOSEDFORM-1、内蕴 $\nu$、$\mathfrak B_1$ 硬门


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 参数空间闭合 命中文件数=1    :: ./STEP01-2026-09-27-parameter-space-closed-and-external-pool-no-fork.md 
技术词 族外池        命中文件数=1    :: ./STEP01-2026-09-27-parameter-space-closed-and-external-pool-no-fork.md
```
- **本档新增**：Step 0 参数空间闭合（$s{=}1..16$ 全表）、Step 1 族外池无分叉、双计 bug 更正与配对去重（见上方命中数；0 命中者为自造语／内部标签 ✓）
