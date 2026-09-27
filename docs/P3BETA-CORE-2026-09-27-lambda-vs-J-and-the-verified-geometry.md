已查地图：已跑 scripts/prework_map_check.sh β 卷积 Fourier λ vs J 加法闭合 ⟹ 执行自 `P3BETA-CHAIN-2026-09-27-...`（✓）＋ 唐先生 13:39（推 support geometry ＋ q-flatness ✓）；本档 = **三处修正 ＋ 已验几何核 ✓**。
D0: 本档对象 = $q$ 的代数结构（卷积/Fourier）与支撑几何
D1: 2（**卷积/Fourier 修正（第三处 λ≠J ✓）**；**加法闭合 ＋ PG 几何 ＋ 双值 Fourier 已验 ✓**）

# β-Core：修正与已验证结构（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(BV-1 ⚠️ 第三处 }\lambda\ne J\textbf{)}\ \text{正确对象}:\ \boxed{q=\lambda\,\mathbf 1_{U\setminus\{0\}}},\quad \lambda=\frac{A_2}{|S|}=2^{\,n-m-d'}\ ✓;\quad J=\lambda A_2=\lambda^2|S|\ ✓\ \text{（\textbf{不是 }q=J\mathbf 1_S\ ✗}）}$$
$$\boxed{\textbf{(BV-2 ⚠️ 卷积修正（已验 ✓）)}\ \text{你的 }\S5\text{--}\S7\ \textbf{不成立} ✗:\ \mathbf q*q\ne\mu q\ \text{（因 }q(0)=0\ \text{而 }(q*q)(0)\ne0\ ✓\text{）};\ \text{正确恒等式}:}$$
$$\qquad\boxed{(q*q)(x)=\lambda(2^{d'}-2)q(x)+\lambda^2(2^{d'}-1)\delta_0(x)}\ ✓✓\ \text{（}n{=}16\ \text{两实例逐点验过 ✓）} \Longrightarrow \text{生成的代数是 }\mathrm{span}\{q,\delta_0\}\ \text{（\textbf{2 维}}，非 1 维 ✗）$$
$$\boxed{\textbf{(BV-3 ⚠️ Fourier 修正（已验 ✓）)}\ \text{正确}:\ \widehat q(\chi)=\lambda\big(2^{d'}\mathbf 1_{U^\perp}(\chi)-1\big) \Longrightarrow \boxed{\widehat q\in\{A_2,\ -\lambda\}}\ ✓✓\ \text{（\textbf{双值 ✓}，但值不是 }\{0,\mu\}\ ✗）}$$
$$\boxed{\textbf{(BV-4 ✓ 真的部分（已验 ✓✓）)}\ \textbf{加法闭合}:\ u,v\in S,u\ne v\Longrightarrow u+v\in S\ ✓;\ S\cong PG(d'-1,2)\ \text{点集}\ ✓;\ \text{直线数}=|S|(|S|-1)/6\ ✓}$$
$$
$$
```

---

## §1 修正后的对象（**✓**）

```
$$q=(\text{值}\lambda)\cdot\mathbf 1_{U\setminus\{0\}}\ ✓\ \text{（}U=\mathrm{Im}f\ ✓\text{）}\ \Longrightarrow\ q(0)=0,\ q|_{U\setminus\{0\}}=\lambda,\ q|_{U^c}=0\ ✓$$
$$\text{数值（}n{=}16\text{）}:\ d'{=}3:\ \lambda{=}256,\ A_2{=}1792,\ J{=}458752\ ✓;\qquad d'{=}4:\ \lambda{=}128,\ A_2{=}1920,\ J{=}245760\ ✓$$
$$\qquad\Longrightarrow\ \lambda\ne J\ \text{（第三次确认 ✓：}256\ne458752\ ✓,\ 128\ne245760\ ✓\text{）};\ \text{而 }\lambda=A_2/|S|\ ✓\ \text{（}1792/7{=}256\ ✓,\ 1920/15{=}128\ ✓\text{）}$$
$$
$$
```

---

## §2 已验证结构（**✓✓ 本机，两实例逐项**）

```
$$\begin{array}{c|c|c}
\text{项目} & d'{=}3\ (\text{4-循环}) & d'{=}4\ (\text{5-循环})\\
\hline
|S|=2^{d'}-1 & 7\ ✓ & 15\ ✓\\
\text{加法闭合} & ✓ & ✓\\
\text{直线数} & 7\ (\text{Fano ✓}) & 35\ (PG(3,2)\ ✓)\\
(q*q)(0)=\lambda^2(2^{d'}-1) & 458752\ ✓ & 245760\ ✓\\
(q*q)|_S=\lambda^2(2^{d'}-2) & 393216\ ✓ & 229376\ ✓\\
\widehat q\ \text{取值} & \{1792,\,-256\}\ ✓ & \{1920,\,-128\}\ ✓\\
\end{array}$$
$$\text{（第二列与 }\S1\text{ 的 }J\ \text{一致？}\ \textbf{否}\ ✗:\ (q*q)(0)=458752=J\ \text{而}\ \lambda^2(2^{d'}-1)=256^2\cdot7=458752\ \checkmark\ \text{——巧合等值，但公式是 }\lambda^2(2^{d'}-1)\ ✓）$$
$$
$$
```

---

## §3 三道 gate 与逻辑地位（**✓ 更新版**）

```
$$\textbf{Gate 1（cardinality）}:\ |S|=2^{d'}-1\ ✓\qquad \textbf{Gate 2（geometry）}:\ u\ne v\in S\Rightarrow u+v\in S\ ✓\ \text{（\textbf{新增，且已验证 ✓}）}\qquad \textbf{Gate 3（flatness）}:\ q|_S\equiv\lambda\ ✓$$
$$\textbf{逻辑地位（不变 ✓）}:\ \text{族内三者\textbf{皆为定理} ⟹ 族内无剪枝力} ✗;\ \text{其\textbf{剪枝力} =\ 检验族外候选} \Longrightarrow \text{违 gate} = \text{不属于 Theorem-13 形的\textbf{证书}} ✓$$
$$\qquad\textbf{局部反证（便宜 ✓）}:\ \text{只需找 }u\ne v\in S\ \text{使 }u+v\notin S \Longrightarrow \text{该候选不满足 Type C}(d')\ ✓;\ d'{=}2\ \text{时退化为"三点必须构成 }\mathbb F_2\text{-line"}\ ✓;\ d'{=}3\ \text{时为 Fano（7 条三点线 ✓）}$$
$$
$$
```

---

## §4 边界与下一步（**✓**）

```
- §1–§2 为本机核验（两实例 ✓）；§3 为 gate 更新 ✓；本档**修正了三处**（$\lambda$ vs $J$、卷积、Fourier ✓）并**保留并验证了**加法闭合/PG 几何/双值 Fourier ✓
- ⚠️ 与唐先生 }\S5\text{--}\S8\ \textbf{不一致处以上方为准} ✓（依据 = 两实例逐点数值 ✓）；\text{建议 }\beta\text{ 档案\textbf{统一以 }\lambda\ \text{记常值}、J\ \text{记平方和} ✓$$
- **未**声称任何块被排除 ✗；**未**涉 119 ✓
$$\text{下一步候选}:\ \text{(甲) 用 Gate 2 对 9 块做一次"族内自查"（应全过 ✓，作为一致性检验 ✓）；\ (乙) 把 }\S3\text{ 的"局部反证"写成可执行检验算法（供族外候选用 ✓）；\ (丙) 重启 119 主线的定位讨论（你说过暂不碰 ✓）}$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：$\lambda$ vs $J$ 第三处修正、卷积 $\delta_0$ 修正、Fourier 双值修正、加法闭合/PG 几何已验
- **档案已有（引用，不列为提出）**：A-ALIGNTHM-1、A-P3BETA-1、$U=\mathrm{Im}f$、$q_v$、$|S|$、$J$


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 第三处修正  命中文件数=1    :: ./P3BETA-CORE-2026-09-27-lambda-vs-J-and-the-verified-geometry.md 
技术词 加法闭合已验证 命中文件数=0    ::
```
- **本档新增**：$\lambda$ vs $J$ 第三处修正、卷积 $\delta_0$ 修正、Fourier 双值修正、加法闭合/PG 几何已验（见上方命中数；0 命中者为自造语／内部标签 ✓）
