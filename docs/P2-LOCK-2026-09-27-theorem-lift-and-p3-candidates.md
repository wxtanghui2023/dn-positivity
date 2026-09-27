已查地图：已跑 scripts/prework_map_check.sh P2 锁 定理提升 P3 候选 ⟹ 执行自 `P2-N16-2026-09-27-...`（✓）＋ 唐先生 13:26（P2=PASS/THEOREM LIFT ✓；P3 不测 n=32 ✓）；本档 = **谱核验 ＋ P2 锁定 ＋ P3 候选提案** ✓。
D0: 本档对象 = P2 最终状态与下一关候选
D1: 2（**秩层谱核验 ✓✓**；**P3 三候选（含 P1 三要素 ✓）**）

# P2 锁定与 P3 提案（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(BQ-1 谱核验 ✓✓)}\ \textbf{全部 }105\ \text{个对换} \Longrightarrow d'=1\ ✓✓\ \text{（105/105 ✓）};\qquad \textbf{全部 }455\ \text{个 3-循环} \Longrightarrow d'=2\ ✓✓\ \text{（455/455 ✓）}}$$
$$\qquad\text{特例（\textbf{唐先生为 1-based 坐标 ✓，我核出}）:\ 4\text{-循环 }(1\,2\,3\,4)_{1\text{-based}}=(0\,1\,2\,3)_{0\text{-based}} \Longrightarrow d'=3\ ✓;\ 5\text{-循环 }(1\,2\,3\,4\,8)_{1\text{-based}}=(0\,1\,2\,3\,7)_{0\text{-based}} \Longrightarrow d'=4\ ✓✓}$$
$$\qquad\Longrightarrow\ \textbf{秩层 }d'=0,1,2,3,4\ \text{全部实例化} ✓✓\ \text{（}\mathrm{id},\ \text{对换},\ \text{3-循环},\ \text{4-循环},\ \text{5-循环}\ ✓\text{）}$$
$$\boxed{\textbf{(BQ-2 P2 锁 = PASS / THEOREM LIFT ✓✓)}\ \text{计算只承担两事}:\ \text{(i) }n=16\ \text{独立核验};\ \text{(ii) 补出秩层实例};\ \text{决定结论的是\textbf{维数无关证明}} ✓}$$
$$\qquad\boxed{\text{维数无关定理}:\ \text{Theorem-13 型 }C=(H,0)\cup(\pi H+e,1),\ H=H_{2^m-1}\ \Longrightarrow\ q_v=2^{\,2^m-1-m-d'}\mathbf 1_{v\in(s+\mathrm{Im}f)\cap(\mathbb F_2^m\setminus\{0\})}\ ✓✓}$$
$$\qquad\Longrightarrow\ \text{资产从"}"n=8\ \text{的 support-2 fingerprint\text{"} \Longrightarrow \textbf{"Theorem-13 全系列的 quantized syndrome-alignment invariant"} ✓✓$$
$$
$$
```

---

## §1 秩层谱（**✓ 本机核验 ＋ 唐先生数据 ✓**）

```
$$\begin{array}{c|c|c|c}
\text{置换类型} & \text{数量} & d' & \text{核验}\\
\hline
\mathrm{id} & 1 & 0 & ✓\\
\text{对换} & 105 & 1 & \textbf{105/105 ✓✓}\\
\text{3-循环} & 455 & 2 & \textbf{455/455 ✓✓}\\
\text{4-循环 }(0\,1\,2\,3) & \text{例} & 3 & ✓\\
\text{5-循环 }(0\,1\,2\,3\,7) & \text{例} & 4 & ✓\\
\end{array}$$
$$\text{（注 ✓：每个 4-元素集有 6 个 4-循环、每 5-元素集有 24 个 5-循环，我只取一个方向核验代表性例子 ✓）};\ \text{4-循环 }(0\,1\,2\,3)\ \text{与 }(1\,2\,3\,4)\ \text{给出不同 }d'\ (3\ \text{vs}\ 2)\ \text{—— 说明 }d'\ \text{依赖坐标的 }\mathbb F_2^4\text{-标签位置 ✓}$$
$$
$$
```

---

## §2 n=16 修正表（**✓ 双方现已一致 ✓**）

```
$$\begin{array}{c|c|c|c|c|c|c}
d' & s\in\mathrm{Im}f & \lambda=2^{11-d'} & |S| & A_2 & A_1=2048-A_2 & J=A_2^2/|S|\\
\hline
0 & \top & 2048 & 0 & 0 & 2048 & —\\
0 & \bot & 2048 & 1 & 2048 & 0 & 2^{22}\\
1 & \top & 1024 & 1 & 1024 & 1024 & 2^{20}\\
1 & \bot & 1024 & 2 & 2048 & 0 & 2^{21}\\
2 & \top & 512 & 3 & 1536 & 512 & 3\cdot2^{18}\\
2 & \bot & 512 & 4 & 2048 & 0 & 2^{20}\\
3 & \top & 256 & 7 & 1792 & 256 & 7\cdot2^{16}\\
3 & \bot & 256 & 8 & 2048 & 0 & 2^{19}\\
4 & \top & 128 & 15 & 1920 & 128 & 15\cdot2^{14}\\
4 & \bot & 128 & 16>15 & \textbf{不可达} ✗ & — & —\\
\end{array}$$
$$\textbf{关键 ✓}:\ A_1+A_2=|H_{15}|=2048\ ✓\ \text{（总半码大小，非 16 ✓ —— 唐先生已更正 ✓）};\ (4,\bot)\ \text{不可达因 }\mathrm{Im}f=\mathbb F_2^4\Longrightarrow s\in\mathrm{Im}f\ \text{恒真}\ ✓$$
$$
$$
```

---

## §3 P3 候选（**禁计算 ✓，遵 AMEND-32/33 三要素 ✓**）

```
$$\textbf{候选 P3-α（推荐 ✓）: 与 NP1CC 论文}\ \S IV\ \text{的\textbf{距离分布定理}对照}$$
$$\qquad\text{① 目标变量}:\ \text{NP1CC 的距离分布 }A_2\ \text{（我们给出精确值集 }\{2048,1024,512,256,128,0\}\ \text{按 }(d',s)\ \text{索引 ✓）};\qquad \text{② 约束方向}:\ \text{文献说"零化 NP1CC 恰有两种重量分布"（Boruchovsky–Etzion–Roth }\S IV\ ✓\text{）} \Longrightarrow \text{我们的 }(d',s)\ \text{索引是否\textbf{细化}它} ✓/\text{重编码} ✗$$
$$\qquad\text{③ 显式 P1 攻击点}:\ source\text{-first 读该文 }\S IV\ \text{的重量分布定理 ⟹ 逐项对照 }(d',s)\ \text{分类};\ \text{若其"两种"可由我们九类塌缩得到 ⟹ 重编码 STOP ✗};\ \text{若不能 ⟹ \textbf{细化新结果} ✓}$$
$$\textbf{候选 P3-β: 分类剪枝}$$\
$$\qquad\text{① 目标变量}:\ n=16\ \text{的 NP1CC 不等价类计数};\qquad \text{② 约束方向}:\ (d',s)\ \text{是否给出\textbf{不等价不变量}（若两类 }(d',s)\ \text{不同 ⟹ 必不等价 ✓）};\qquad \text{③ P1}:\ \text{证 }(d',s)\ \text{是等价不变量（由 }A_2\ \text{定 ⟹ 已隐含 ✓）} \Longrightarrow \text{分类至少分成 }9\ \text{块 ✓}$$
$$\textbf{候选 P3-γ（最硬 ✓ 但最险 ⚠️）: 对齐量子化能否给出\textbf{任一独立上/下界}}$$
$$\qquad\text{① 目标变量}:\ \text{某个 }K(n,R)\ \text{或 multicovering 界};\qquad \text{② 方向}:\ \text{对齐约束是\textbf{最优码}性质 ⟹ 直接给 }K\ \text{的界似不可行 ⚠️（须先找到"最优性 ⟹ 量化 ⟹ 某计数界"的桥 ✓）};\qquad \text{③ P1}:\ \text{先证/否证该桥存在 ⟹ 若无桥则本条 DROP ✓}$$
$$
$$
```

---

## §4 边界（诚实标注）

- §1 为本机核验（105/455 全 ✓✓）＋ 唐先生特例（1-based ✓）；§2 为**双方一致表** ✓；§3 为**候选提案（未执行 ✓，禁计算 ✓）**
- **未**测 $n=32$ ✓（遵唐先生 ✓）；**未**声称任何新结果 ✗（P3-α 待 source-first 对照 ✓）
- **119**：完全不碰 ✓

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：秩层谱核验、P2/THEOREM LIFT 锁定、P3 三候选
- **档案已有（引用，不列为提出）**：A-ALIGNTHM-1、Theorem 13、$d'$、$|S|$、$J=A_2^2/|S|$、NP1CC


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 秩层谱核验  命中文件数=1    :: ./P2-LOCK-2026-09-27-theorem-lift-and-p3-candidates.md 
技术词 P3 三候选     命中文件数=1    :: ./P2-LOCK-2026-09-27-theorem-lift-and-p3-candidates.md
```
- **本档新增**：秩层谱核验、P2/THEOREM LIFT 锁定、P3 三候选（见上方命中数；0 命中者为自造语／内部标签 ✓）
