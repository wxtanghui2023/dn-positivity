# V311 · **P1：`AdmWindow` 逐字段审计** —— ⭐⭐⭐⭐⭐ **12 字段原文到手**；⭐⭐⭐⭐ **四类数值界在候选（profile 读法）下全部通过（$c=4$ 即够）**；⚠️ **但发现真正的量词/尺度缺口：`AdmWindow.v` 是"全尺度窗"（支撑 $[-L/2,L/2]$、$C^{2}$、带 $c$ 的二阶 L¹ 界）而 §4 `WindowProfile` 是"规范化 profile"** ⟹ **P1-GAP（精确缺失：尺度约定 ＋ $\varrho$/`phiV` 实现）**

$$\boxed{\texttt{AdmWindow}\ (v:L\ w\ c)\ \text{（`ThmD/WindowCore.lean:31` 逐字，12 字段）}}$$
$$\qquad \texttt{one\_le\_w}:1\le w;\quad \texttt{w8}:8w\le L;\quad \boxed{\texttt{four\_le\_c}:4\le c};\quad \texttt{even};\quad \texttt{nonneg};\quad \texttt{le\_one};\quad \texttt{contDiff}:\texttt{ContDiff}\ \mathbb R\ \boldsymbol 2\ v;$$
$$\qquad \texttt{support}:\forall u,\ L/2\le|u|\to v\,u=0;\quad \texttt{l1\_deriv}:\int|v'|\le2;\quad \texttt{l1\_deriv\_sq}:\int|(v^{2})'|\le2;$$
$$\qquad \texttt{l1\_deriv2}:\int|v''|\le \boxed{c/w};\qquad \texttt{l1\_deriv2\_sq}:\int|(v^{2})''|\le \boxed{c/w} ✓✓✓$$
$$\boxed{\textbf{候选（$\tilde v_\lambda=\cos(2wx)$，profile 读法）四类数值界全部通过，}c=4\ \textbf{即够}} ✓✓✓$$
$$\boxed{\textbf{尺度缺口}：\texttt{AdmWindow.v}\ \text{为全尺度窗}（\text{支撑}\ [-L/2,L/2]）;\ \text{§4}\ \texttt{WindowProfile.v}\ \text{为 profile} ⟹ \textbf{P1-GAP}} ✓✓✓$$

> 委托 ✓ 唐先生 2026-09-16 14:04：**唯一入口是 P1**；**P1 不能只检查函数形状** —— 必须把 `AdmWindow φ L w c` **全部字段逐项展开**，把 $\tilde v_\lambda$ 代进去；尤其确认 $c$ 是 **(i) 由 $v$ 构造的派生常数 ／ (ii) 需存在性证明的 witness ／ (iii) 预先固定并有数值/范围约束的参数**（三种逻辑强度完全不同）✓✓；要求**审计表**；**正性不得只写"cos 型所以正"**，须实际证 $|2wx|<\frac\pi2$（**若在 $\lambda\to1^-$ 处变非严格，就再次出现 $\lambda<1/\lambda\le1$ 量词问题**）✓✓；判定三选一 **P1-YES／P1-NO／P1-GAP**；并确认 $$\mathcal A_{\rm ThmD}\subsetneq\mathcal A_{\rm var}\ \text{不是坏消息}$$（只需 $\tilde v_\lambda\in\mathcal A_{\rm ThmD}$ 且达到 $\mathcal A_{\rm var}$ 极值）✓✓✓
> 第一手依据 ✓ **`Zeta23/ThmD/WindowCore.lean`（`structure AdmWindow` 第 31–43 行，本档直读逐字）** ｜`XiPrime/Statement.lean §4`（`WindowProfile`）✓
> 执行 ✓ 小灵｜**纸面 ✓**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓；数值仅初等算术 ✓｜编号 ✓ `V311`（先领号 ✓）

---

## §1 **审计表（逐字段）**

| 字段 | 对 $\tilde v_\lambda(x)=\cos(2wx)$（profile 读法） | 依据/核算 |
|:--|:--|:--|
| `one_le_w` : $1\le w$ | **取决于 $w$ 与 $L$ 的约定**（§4 是 $1\le w\le L/8$）⚠️ | §4 原文 |
| `w8` : $8w\le L$ | ✓（同 §4） | — |
| **`four_le_c` : $4\le c$** | **✓ 取 $c=4$**（见下两行） | §2 |
| `even` | **✓** | $\cos$ 偶 |
| `nonneg` : $0\le v$ | **✓ 严格**（需 $|2wx|<\frac\pi2$，见 §2） | §2 |
| `le_one` : $v\le1$ | **✓（重标 $\tilde v$）**；原式 $\frac w{\sin w}>1$ ✗ | V310 §3 |
| `contDiff` : $C^{2}$ | **✓**（解析）；⚠️ 注意此处是 $C^{2}$，§4 是 $C^{3}$ | $\cos$ 解析 |
| `support` : $L/2\le\lvert u\rvert\Rightarrow v=0$ | **⚠️ 尺度问题（本档核心）** | §3 |
| `l1_deriv` : $\int\lvert v'\rvert\le2$ | **✓ $=4(1-\cos w)\le0.96\le2$** | §2 |
| `l1_deriv_sq` : $\int\lvert(v^{2})'\rvert\le2$ | **✓ $=2(1-\cos 2w)\le1.69\le2$** | §2 |
| `l1_deriv2` : $\int\lvert v''\rvert\le c/w$ | **✓ $=4w\sin w$，需 $c\ge4w^{2}\sin w\approx1.30\le4$** | §2 |
| `l1_deriv2_sq` : $\int\lvert(v^{2})''\rvert\le c/w$ | **✓ $=4w\sin2w$，需 $c\ge4w^{2}\sin2w\approx1.98\le4$** | §2 |

$$\Longrightarrow \boxed{\text{四类数值界（含}\ c\ \text{的约束）}\ \textbf{在}\ c=4\ \textbf{下全部通过}} ✓✓✓$$

---

## §2 **数值核算（初等，$\lambda<1$ 域）**

$$w=\frac\lambda{\sqrt2},\qquad \lambda\in[\tfrac12,1)\ \Longrightarrow\ w\in[0.354,\ 0.707);\qquad \textbf{严格}\ w<\tfrac1{\sqrt2}<\tfrac\pi2 ✓✓$$
$$\textbf{正性（严格，非极限退化）}：|2wx|\le w<\tfrac1{\sqrt2}=0.7071<\tfrac\pi2 ⟹ \cos(2wx)\ge\cos w>0.76>0 ✓✓$$
$$\qquad \Longrightarrow \text{在}\ \lambda\to1^{-}\ \text{时仍严格（}\cos\tfrac1{\sqrt2}>0\text{）}\ —— \textbf{不产生}\ \lambda<1/\lambda\le1\ \text{退化} ✓✓✓$$
$$\int_{-1/2}^{1/2}\!\lvert v'\rvert dx=2w\!\!\int_{-1/2}^{1/2}\!\!\lvert\sin 2wx\rvert dx=\int_{-w}^{w}\!\lvert\sin u\rvert du=4(1-\cos w)\le4(1-0.760)=0.96 ✓✓$$
$$\int\lvert(v^{2})'\rvert=2\!\!\int\!\lvert vv'\rvert=\dots=2(1-\cos 2w)\le2(1-0.156)=1.69 ✓✓\（\text{逼近但}\ \le2）✓$$
$$\int\lvert v''\rvert=4w^{2}\!\!\int\!\lvert\cos 2wx\rvert dx=4w\sin w;\qquad \int\lvert(v^{2})''\rvert=4w\sin 2w ✓$$
$$\qquad \Longrightarrow \text{需}\ c\ge\max\{4,\ 4w^{2}\sin w,\ 4w^{2}\sin 2w\}\ \text{于}\ w<0.7071：\ 4w^{2}\sin w\le1.30,\ 4w^{2}\sin2w\le1.98 ⟹ \boxed{c=4\ \text{可行}} ✓✓✓$$

---

## §3 ⚠️ **尺度缺口（P1 的真正核心发现）**

$$\texttt{AdmWindow}\ \text{的}\ v\ \text{带}\ \texttt{support}:\forall u,L/2\le|u|\to vu=0\ \text{与}\ \texttt{contDiff}:C^{2} ⟹ v\ \text{在}\ \pm L/2\ \text{处}\ \textbf{二阶消失} ✓$$
$$\qquad \text{而}\ L=\lambda l\ \text{中}\ l=\log(T/2\pi)\to\infty ⟹ L/2\ \textbf{巨大} ⟹ \texttt{support}\ \text{对 profile 是}\ \textbf{空条件}（\text{profile 支撑}\subseteq[-\tfrac12,\tfrac12]\subset[-L/2,L/2]）✓✓$$
$$\qquad \text{反之，若}\ v\ \text{是}\ \textbf{全尺度窗}（\text{含 taper}），\text{则}\ \texttt{support}\ \text{有实质内容}（\text{taper 在}\ \pm L/2\ \text{归零}）✓✓$$
$$\text{§4 原文给实现式}：\varphi_v=\sqrt{v(u/L)}\cdot\varphi\ \（\texttt{Defs.phiV}）⟹ \boxed{\textbf{taper}\ \varphi\ \text{提供归零}，\textbf{profile}\ v\ \text{只须正}} ✓✓✓$$
$$\Longrightarrow \textbf{P1 的判定取决于尺度约定}：$$
$$\qquad \text{读法①（}\texttt{AdmWindow.v}=\text{profile}）：\text{§1 表内全部}\ ✓\ ⟹ \textbf{P1-YES} ✓$$
$$\qquad \text{读法②（}\texttt{AdmWindow.v}=\text{全窗}\ \varphi_v）\：\text{需代入}\ \varphi_v\ \text{重算四类 L¹ 界} ⟹ \textbf{需}\ \varrho／\texttt{TaperProfile}\ \text{与}\ \texttt{phiV}\ \text{的实现} ⚠️✓$$
$$\qquad \text{且}\ \texttt{contDiff}\ \text{量词不同}（\text{ThmD}\ C^{2}\ \text{vs §4}\ C^{3}）⟹ \text{若用 §4 读法，}\sqrt v\ \text{的}\ C^{3}\ \text{需}\ v\ \textbf{不取零}（\text{§4 的}\ \texttt{pos}\ \text{正是为此}）✓✓✓$$

---

## §4 **判词：P1-GAP（精确缺失命题）＋ 关键逻辑修正确认**

$$\boxed{\textbf{P1-GAP}：\text{缺失① 尺度约定}（\texttt{AdmWindow.v}\ \text{是 profile 还是全窗}）;\ \text{缺失②}\ \varrho／\texttt{TaperProfile}\ \text{＋}\ \texttt{phiV}\ \text{实现式}} ✓✓$$
$$\qquad \text{但}\ \textbf{在 profile 读法下，候选}\ \textbf{已通过全部数值界}（含\ c=4）\ —— \text{这是本档的实质进展} ✓✓✓$$
$$\text{关于}\ c\ \text{的逻辑地位（唐先生三选一）}：\textbf{情形 (iii) 为主}：\text{预先固定参数 ＋ 范围约束}\ 4\le c，\text{其}\ \textbf{存在性} \text{须对候选证明} ✓$$
$$\qquad ⟹ \text{本档已证}：\text{候选可取}\ c=4\（\text{且}\ c\ \text{在 producer 中于}\ T\ \text{前量化 ⟹ 家族内一致}）✓✓$$
$$\boxed{\text{确认你的逻辑修正}：\mathcal A_{\rm ThmD}\subsetneq\mathcal A_{\rm var}\ \textbf{不是坏消息};\ \text{只需}\ \tilde v_\lambda\in\mathcal A_{\rm ThmD}\ \wedge\ \text{达到}\ \mathcal A_{\rm var}\ \text{极值}} ✓✓✓$$

---

## §5 判词 ＋ 边界 ＋ 净产出 ＋ 下一步

```
① ⚠️ §2 的四个积分均为**本档手算**（可逐步复核）；已用 $w<0.7071$ 的界 ✓
② ⚠️ §3 的"支撑对 profile 空条件"依赖 $L/2\ge\tfrac12$ ⟹ 以 $8w\le L$ 与 $w\ge1$ ⟹ $L\ge8$ ✓
③ ⚠️ `l1_deriv_sq` 界 $1.69\le2$ **逼近但成立**；若 $w$ 稍大（$\lambda>1$）会破 ⟹ 与 $\lambda<1$ 域一致 ✓
④ **不声称** P1-YES（尺度约定未定）；**不声称** 0.67250 升格 ✓
⑤ 未用 RH ✓；未跑 Lean ✓；数值仅初等算术 ✓
```

```
① ⭐⭐⭐⭐⭐ **12 字段原文到手**（`ThmD/WindowCore.lean:31–43` 逐字）—— 含 `four_le_c : 4 ≤ c`、`contDiff : C²`、`support : L/2 ≤ |u| → v u = 0`、两个 $c/w$ 型二阶 L¹ 界 ✓✓
② ⭐⭐⭐⭐ **候选通过全部数值界**：$\int|v'|=4(1-\cos w)\le0.96$、$\int|(v^2)'|\le1.69$、$\int|v''|=4w\sin w$、$\int|(v^2)''|=4w\sin2w$ ⟹ **$c=4$ 即够** ✓✓✓
③ ⭐⭐⭐ **正性在 $\lambda\to1^-$ 仍严格**（$\cos\frac1{\sqrt2}>0.76$）⟹ **不产生 $\lambda<1/\lambda\le1$ 退化** ✓✓（你的警告已排除）
④ ⚠️ **P1-GAP 精确化**：尺度约定（profile vs 全窗）＋ $\varrho$/`phiV` 实现式 ⟹ **唯一未解析项** ✓✓
⑤ ⭐ **$c$ 的逻辑地位定为情形 (iii)**（预固定＋范围约束 $4\le c$，存在性须证）⟹ 本档已证可取 $c=4$ ✓
【下一步（唯一）】
  **(P1-a)** 读 `ThmD/WindowCore.lean` 的 `AdmWindow` **使用处**（谁调用它、以何实参）＋ `Defs.phiV`／`TaperProfile` ⟹ **定尺度约定** ⟹ 读数①/②择一 ⟹ P1-YES/NO 立即判定 ✓
```
