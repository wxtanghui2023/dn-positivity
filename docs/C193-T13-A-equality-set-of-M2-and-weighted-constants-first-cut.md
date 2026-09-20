已查地图（**先查后写**）：查 `TARGETS-CONJECTURES-ROUNDABOUT-ATTACK.md` L132（T13 条目）、`WORKPLAN` B2（"写 Cassels 型 b_j 权重的单点最优常数"）、`C-152`／`C-154`（M=2 三段拼装）、`C-192`（κ_N 等号集）。回查见 §5 ✓

D0: 本档对象 = **T13 两项**：(A) M=2 等号集的完整刻画（**新定理**，由 `C-152` 两件装备直接给出）＋ (B) Cassels 型加权常数族 $g_w$ 的首轮数值刻画 —— 关系 = 新构造 ＋ 数值刻画
D1: 0
FREEZE-ACK: 本档即冻结期内的收束与登记（依 §8.1；不产候选结论）

---

## §1 T13-A ⭐ 定理（新）：M=2 的等号构型 = 本原 6 次根与本原 4 次根

$$\textbf{定理}：\text{在}\ (\varphi_1,\varphi_2)\in[0,\pi]^2\ \text{上}$$
$$\qquad \max_{1\le k\le10}\big[\cos k\varphi_1+\cos k\varphi_2\big]=\tfrac12\iff\{\varphi_1,\varphi_2\}=\Big\{\tfrac{\pi}{3},\ \tfrac{\pi}{2}\Big\}✓✓（\text{无序对}）✓$$
$$\text{即等号集恰为}\ \textbf{两点}\ \big(\tfrac{\pi}{3},\tfrac{\pi}{2}\big)\ \text{与}\ \big(\tfrac{\pi}{2},\tfrac{\pi}{3}\big)✓，\text{无曲线、无其它点}✓$$

### §1.1 证明（直接复用 C-152 的两件装备，零新计算）

$$\textbf{① 局部刚性}（C-152 §2）：\text{设中心}\ x_\ast=(\pi/3,\pi/2)✓，\text{则对}\ \|\delta\|<\rho：$$
$$\qquad \max_{k\in A}F_k\ \ge\ \tfrac12+c\rho-32\rho^2✓,\qquad c=\frac{28\sqrt{1677}}{559}=2.0512224\ldots✓$$
$$\qquad \Longrightarrow\ \text{对}\ 0<\|\delta\|<\frac{c}{32}=0.0641007\ \mathrm{rad}=3.6727^\circ：F>\tfrac12✓（\text{严格}）✓$$
$$\qquad \Longrightarrow\ \textbf{该球内}只有中心取等✓（\text{镜像球同理}）✓$$
$$\textbf{② 远场严格}（C-152 §3）：\text{在}\ 1^\circ\ \text{邻域之外}\ F\ge0.527832>1/2✓✓$$
$$\textbf{③ 覆盖}：\text{任一点或落在}\ 1^\circ\ \text{邻域外（属①？否）}⟹\text{由②}>1/2✓；\text{或落在}\ 1^\circ\ \text{邻域内}$$
$$\qquad \Longrightarrow 1^\circ<3.6727^\circ\ \text{符合①的半径}⟹\text{由①只有中心取等}✓$$
$$\qquad \Longrightarrow \textbf{等号集恰为两中心}✓✓\qquad\square$$

### §1.2 ⭐ 结构识别：与 C-192 同型

$$\frac{\pi}{3}=\frac{2\pi}{6}\ \（\text{本原 6 次单位根}\ \gcd(1,6)=1✓）✓,\qquad \frac{\pi}{2}=\frac{2\pi}{4}\ \（\text{本原 4 次}\ \gcd(1,4)=1✓）✓$$
$$\Longrightarrow \textbf{等号构型 = 本原 6 次根 ＋ 本原 4 次根}✓\ —— \text{与}\ \texttt{C-192}\ \text{的"等号点 = 本原}\ (N+1)\ \text{次根"同一模式}✓✓$$
$$\qquad \text{且}\ 12=\mathrm{lcm}(6,4)\ \text{正是}\ \texttt{C-153}\ \text{中}\ 7g_5+5g_7=0\ \text{的那个}\ 12✓\（k+k'=12\ \text{结构}）✓✓$$
$$\Longrightarrow \text{两个独立线索（等号角／梯度共线）指向同一个}\ \mathrm{lcm}\ \text{结构}✓✓$$

## §2 T13-B Cassels 型加权最优常数（首轮数值）

$$\text{定义}：g_w(N):=\inf_{\varphi_1,\varphi_2}\max_{1\le k\le N}\big[w\cos(k\varphi_1)+\cos(k\varphi_2)\big]✓,\qquad w\ge1✓（\text{Cassels 型：权重比}\ w✓）$$

| $w$ | $g_w(10)$ | $g_w/w$ | 最优构型 $(\varphi/\pi)$ |
|---|---|---|---|
| 1.0 | $0.500000$ | $0.500$ | $(1/3,\ 1/2)$ ✓ 回到定理 ✓ |
| 1.2 | $0.578407$ | $0.482$ | $(0.3478,\ 0.5154)$ |
| 1.5 | $0.625406$ | $0.417$ | $(0.9075,\ 0.3592)$ |
| 2.0 | $1.000000$ | $0.500$ | $(1/3,\ 1/2)$ ← **精确整数** ✓ |
| 3.0 | $1.799343$ | $0.600$ | $(0.0857,\ 0.5943)$ |
| 5.0 | $3.246775$ | $0.649$ | $(0.6364,\ 0.1818)=(7/11,\ 2/11)$ |

$$\text{渐近行为}：g_w\ \gtrsim\ w\,\kappa_{10}-1=w\cos\tfrac{2\pi}{11}-1✓\qquad（\text{证}：\text{取}\ k\ \text{使}\ \cos k\varphi_1\ \text{最大}，\text{另一项}\ \ge-1✓）$$
$$\qquad w=5：\text{下界}\ 3.206\ \text{vs 实测}\ 3.247✓（\text{第二点确有正贡献}✓）$$

$$\textbf{结构性观察}：g_w/w\ \textbf{不单调}✗（0.500\to0.482\to0.417\to0.500\to0.600\to0.649） \Longrightarrow w\approx1.5\ \text{处有极小}✓\（\text{构型发生突变}✓）$$

## §3 与古典 Turán–Cassels 的关系（诚实定位）

$$\text{古典 Turán 第一定理}（\text{模长版，窗口}\ n，\text{实为}\ \max_{1\le\nu\le n}|\sum z_j^\nu|\ge1✓，\text{等号}=\text{正}\ n\ \text{边形}）✓\ —— \textbf{已知}✗，\text{本档不声称新}✓$$
$$\text{本档 (A) 是}\ \textbf{实部＋短窗}\ (5M)\ \text{版的等号刻画}✓\ —— \text{窗口}\ 5M\ \text{正是文献空隙}✓（\texttt{RP-M-LITERATURE-POSITIONING}）✓$$
$$\text{本档 (B) 是}\ \textbf{Cassels 型加权}\ \text{版的首轮数值}✓\ —— \text{⚠️}\ \textbf{原典不可得}（Cassels 引理档案仅 1 命中＝台账自身✓）\Longrightarrow \text{不声称逐字对应}✓，\text{定位为"Cassels 型"}✓$$

## §4 下一步（T13 续）

$$\textbf{①}\ (B)\ \text{上证书}：g_w\ \text{是}\ 2\ \text{维问题} \Longrightarrow \text{箱下界 B\&B 廉价}✓；\text{对}w\in\{1,2,3,5\}\ \text{出四门认证}✓$$
$$\textbf{②}\ (B)\ \text{闭式？}：w=2\ \text{给精确}\ 1.000000✓\ \text{暗示有理结构}✓；w\to\infty\ \text{渐近}\ w\kappa_{10}-1✓\ \text{可证}✓$$
$$\textbf{③}\ (A)\ \text{推广}：M=3\ \text{的等号集}（\text{数值极小}\approx0.7769✓） \Longrightarrow \text{同法可及}✓$$

## §5 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 等号构型        命中文件数=2    ::  ./C192-OP6-equality-set-of-kappaN-primitive-roots.md  ./E46-5C-inertia-necessity.md
技术词 加权最优常数    命中文件数=0    ::
技术词 本原根模式      命中文件数=0    ::
```

$$
\textbf{逐项判定}：$$
$$\qquad \text{「等号构型」}：2\ \text{命中}\ —— \texttt{C192}\ \text{为同义复用}✓，\texttt{E46}\ \text{是}\ \textbf{von Neumann 迹不等式的等号构型}✓（\text{不同对象}）⟹ \textbf{通用词，不计本档新增}✗✓$$
$$\qquad \text{「加权最优常数」}：0\ \text{命中} ⟹ \textbf{本档首次命名}✓✓$$
$$\qquad \text{「本原根模式」}：0\ \text{命中} ⟹ \textbf{本档首次命名}✓✓$$

⚠️ **自查记录（本档第一次成稿时写错）**：初稿 §5 把「等号构型」记为 0 命中 ✗ —— **错**✗，实测 2 命中 ✓。**先跑后写**纪律再次被违反（这是本项目第 4 次同类失误 ✓），已按实测改正 ✓。

## §6 边界

- §1 是**证明**（复用 `C-152` 的局部符号化引理 ＋ 远场证书 ✓）；①的局部部分是严格符号 ✓，②是计算机辅助（网格＋Lipschitz ✓，`C-154` 已四门审计 ✓）
- §2 全是**数值**（多起点 Nelder–Mead ✓）⟹ 只作**刻画**，未升级为定理 ✓；上界/下界方向未区分 ✓
- §3 明确标注：古典部分**已知**，本档不声称新 ✓；Cassels 原典不可得 ⟹ "Cassels 型"为自定表述 ✓
- **未用** RH；**未改**他档 ✓
