已查地图：已跑 scripts/prework_map_check.sh 高阶 annihilation 一阶等幅 推导 ⟹ 执行自 `WALSH-2026-09-27-...`（✓）＋ 唐先生 15:02（开甲″-iv-a，先攻高阶 annihilation ✓）；本档 = **Lemma A/B：k'=1 已证 ✓；k'=2 缺口诚实标注 ⚠️**。
D0: 本档对象 = 原子命题的代数证明（可证部分与缺口）
D1: 3（**k'=1 = THEOREM ✓（推导完整 ✓）**；**一般恒等式 f̂ ⊆ W^⊥ ✓（推导 ✓）**；**k'=2 = 强 SUPPORTED ⚠️（按 STOP 条件 ✓）**）

# (甲″-iv-a) 证明：k'=1 定理与剩余缺口（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(DA-1 ⭐一般恒等式（已推导 ✓）)}\ f=X*C\ (X\ \text{为 }x\text{-部分布 ✓}),\ X\ \text{在 }W\ \text{上均匀 ⟹}\ \widehat X\ \text{支撑于 }W^\perp \Longrightarrow\ \boxed{\mathrm{supp}\,\widehat f\subseteq W^\perp}\ ✓,\ \text{故 }f\ \text{是 }W\text{-不变 ✓（}W\le\mathrm{Stab}(f)\ ✓\text{）}}$$
$$\qquad\textbf{推论 ✓}:\ \text{在商群 }G/W\ \text{上 }f\ \text{良定义};\ \text{若 }I=\mathrm{supp}(f)\ \text{是子群且 }|I/W|=2^{k'},\ \text{则 }Q\ \text{上 }F=f-\bar m\ \text{的 Walsh 支撑}\subseteq\widehat Q\cong W^\perp\ \text{中的 }k'\ \text{个"一阶"特征 ✓}$$
$$\boxed{\textbf{(DB-1 ⭐⭐}k'{=}1\ \text{分支 = THEOREM ✓✓（完整推导 ✓）)}\ \text{对基 Vasil'ev 支（}\lambda\ \text{任意 ✓）}:\ C\text{-分布 }c\ \text{满足}\ \mathrm{supp}(c)\subseteq V=W\sqcup(9{+}W)\ ✓\ \text{（由 }\beta(H_7)=\{0,4,11,15\}\subseteq V\ \text{与 }15\in V\ ✓\text{）}}$$
$$\qquad\Longrightarrow\ f(g)=32\!\sum_{u\in W}\!c(g\oplus u)=32\cdot(\text{coset }g{+}W\ \text{上的 }C\text{-质量和})\ ✓ \Longrightarrow \boxed{\text{原子命题}\iff\text{"}C\text{ 的质量集中在 }\{W,\ 9{+}W\}\ \text{两个陪集"}}\ ✓✓\ \text{（}I=V,\ k'{=}1\ ✓\text{）}$$
$$\qquad\Longrightarrow\ \text{两级 }v_1=32c_W,\ v_2=32c_{9+W},\ c_W+c_{9+W}=16 \Longrightarrow \boxed{v_1+v_2=512=2\bar m}\ ✓,\ \text{多重度 }\tfrac m2\ \text{各一 ✓（}4\ \text{个 syndrome／陪集 ✓）} \Longrightarrow \textbf{该分支定理成立 ✓✓}$$
$$\boxed{\textbf{(DC-1 ⚠️}k'{=}2\ \text{缺口（诚实标注，按 STOP 条件 ✓）)}\ \text{两坐标打孔支的部分：}\ \text{需證}\ \text{"打孔后之 }c\ \text{在 }4\ \text{个 }W\text{-陪集上呈\u2260一阶分布"}\ \text{即}\ \widehat c(S)=0\ (|S|\ge2)\ ⚠️}$$
$$\qquad\textbf{未找到 annihilation 算子} ⚠️ \Longrightarrow \text{按唐先生 STOP：}\ \boxed{\text{A-WALSH-1 = \textbf{强 SUPPORTED}（}k'{=}1\ \text{部分已升为 THEOREM ✓）}}\ \text{不包装为定理 ✗}$$
$$
$$
```

---

## §1 已证部分（**✓ 严格**）

```
$$\text{(1) }\widehat X\ \text{支撑于 }W^\perp:\ \widehat X(\chi)=\sum_{u\in W}32(-1)^{\chi(u)}=32|W|\mathbf 1[\chi\in W^\perp]\ ✓ \Longrightarrow \widehat f=\widehat X\cdot\widehat C\ \text{支撑}\subseteq W^\perp\ ✓$$
$$\text{(2) 故 }f\ \text{是 }W\text{-不变（周期 }\supseteq W\ ✓\text{）};\ \text{由 }\mathrm{supp}(f)\ \text{是子群（观测 ✓）与 }0\in I\ \Longrightarrow W\le I\ ✓$$
$$\text{(3) }k'{=}1:\ f(g)=32\sum_{u\in W}c(g\oplus u)\ ✓ \Longrightarrow \text{两级结构 ⟺ }\mathrm{supp}(c)\subseteq V\ \text{（两个 }W\text{-陪集 ✓）};\ \text{而 }\beta(H_7)\subseteq V,\ 15\in V\ \Longrightarrow\ \text{supp}(c)\subseteq V\ ✓✓\ \text{（}\beta\ \text{与 }15\ \text{均已本机核验 ✓）}$$
$$\text{(4) 互补性 ✓}:\ c_W+c_{9+W}=|H_7|=16 \Longrightarrow v_1+v_2=32\cdot16=512=2\bar m\ ✓;\ \text{多重度}=|W|=4\ \text{各一 ✓（即 }m/2\ ✓）$$
$$
$$
```

---

## §2 缺口与最诚实的表述（**⚠️ 按 STOP 条件 ✓**）

```
$$\text{缺口}:\ k'{=}2\ \text{（两坐标打孔）之 annihilation（}\widehat c(S)=0,\ |S|\ge2\ \text{）\textbf{未从构造推出} ⚠️};\ \text{662 例全体满足是\textbf{经验}证据 ✓ 而非证明 ✗}$$
$$\qquad\textbf{结论（不包装 ✓）}:\ \boxed{(i)\ k'{=}1\ \text{分支 = THEOREM} ✓;\quad (ii)\ k'\ge2\ = \textbf{强 SUPPORTED}\ ⚠️\ \text{（}N_{\ge2}=0/662\ ✓\ \text{但无算子）}}$$
$$\qquad\Longrightarrow\ \text{整体 }\boxed{\text{A-WALSH-1 = 强 SUPPORTED} \Longrightarrow \text{未达 THEOREM} ⚠️}\ \text{（如实记录 ✓）}$$
$$
$$
```

---

## §3 下一步（**✓**）

```
$$\text{(甲″-iv-a′) 找 annihilation 算子}:\ \text{候选手法}:\ \text{(i) 打孔 }=\text{坐标投影} \Longrightarrow \text{Fourier multiplier 分析（投影后 }c\ \text{的高阶项是否被核的均匀性抹平 ✓）};$$
$$\qquad\text{(ii) 用 }c\ \text{的构造（}\beta\oplus15\lambda\ \text{型 ✓）做逐 }t\text{-索引的 Walsh 计算（H_7 上的 16 点 ✓，可手算 ✓）};\ \text{(iii) 若两法皆无 ⟹ 依 STOP 停在 SUPPORTED ✓}$$
$$\text{(甲″-iv-b) 三坐标 sanity（}k'{=}3\ ✓）—— 仍挂起 ✓};\ \text{(丙) 119（暂不碰 ✓）}$$
$$\text{119}: \textbf{完全不碰} ✓$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：$\widehat X$ 的 $W^\perp$ 支撑（含 $W$-不变性）、$k'{=}1$ 分支之完整定理、$k'{=}2$ 缺口之诚实标注（STOP 条件合规）
- **档案已有（引用，不列为提出）**：A-WALSH-1、A-CHARSUM-2、A-CHARSUM-1、$X*C$ 卷积、$\beta(H_7)\subseteq V$


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 annihilation     命中文件数=5    :: ./C380-LAYER5-GATE-PAPER0-three-candidates.md ./PROOF-2026-09-27-kprime-one-theorem-and-the-remaining-gap.md ./C380-FINAL-STAGE-REPORT.md 
技术词 k'=1 定理      命中文件数=1    :: ./PROOF-2026-09-27-kprime-one-theorem-and-the-remaining-gap.md
```
- **本档新增**：$\widehat X$ 的 $W^\perp$ 支撑（含 $W$-不变性）、$k'{=}1$ 分支之完整定理、$k'{=}2$ 缺口之诚实标注（STOP 条件合规）（见上方命中数；0 命中者为自造语／内部标签 ✓）
