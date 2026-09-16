# V295 · **AF 压缩机制的 $2/3$ 来源分解（Compression Audit）** —— ⭐⭐⭐⭐⭐ **结论：$2/3$ 是"秩-迹／二阶矩信息损失"，不是"压缩维数损失"**（$r_{\rm comp}\to1$：$d=N+O(L)$）；**承载处 ＝ $R(\psi_0)=4/3$（带宽一的无条件素数侧 HS 常数）**；**正性未被使用**（惯性／秩-迹取代之）⟹ 该路线**不是 ③ 类**，但有**结构性天花板 0.68185**

$$\boxed{\frac23\ =\ \underbrace{r_{\rm comp}}_{\to1}\ \times\ \underbrace{\big(2-R(\psi_0)\big)}_{\ =\ 2-\frac43\ =\ \frac23;\ \textbf{损失全在此}}} ✓✓✓$$
$$\boxed{\text{承载行（唯一）：}\ N_0^s+o(N)\ \ge\ \operatorname{rank}P_1\ \ge\ \underbrace{4\operatorname{tr}\widetilde G-2N-\|\widetilde G\|_{\rm HS}^{2}}_{=\ (2-R(\psi)+o(1))N};\qquad \text{取}\ \psi=\psi_0\ \text{得}\ \frac23} ✓✓✓$$
$$\boxed{\text{故瓶颈}\ \ne\ \text{压缩空间，而}\ ＝\ \textbf{二阶矩预算常数}\ R(\psi)\ge\frac43\（\text{带宽}\le1）;\ \text{压低它需}\ \textbf{支撑}>1\ （\text{＝}\ `V162`\ \text{墙}）} ✓✓✓$$

> 委托 ✓ 唐先生 2026-09-16 13:10：**打 (丙)，且不把 (乙)/(丙) 分成两条线；第一刀拿 AF 的有限压缩做结构分析** ✓；**关键纠正：不要一上来问"能否 $2/3\to1$"，先问"$2/3$ 到底是压缩维数损失，还是正性利用率损失"** ✓；**硬禁令：不要直接尝试构造更大的压缩** ✓；要求逐项回答 **Compression Audit 十问**，**尤其是第 (7) 项**（$2/3$ 第一次出现在哪一行）✓✓✓
> 第一手依据（**本档现场读取，非二手**）✓ **`V185-paper-reading-notes-arXiv-2608-13637.md`**（119 行，全文读：机制 Z／P／L＋单链＋天花板＋输入清单）｜**本地 Lean 形式化** `~/lean-repro/zeta23-local/Zeta23/LinAlg/RankTrace.lean`（**Lemma R 精确形式，现场读源**）＋ `Zeta23/PairCeiling/Ceiling.lean`（抽象天花板）✓
> 执行 ✓ 小灵｜**纸面 ✓**｜纪律 ✓ 未用 RH 作推导 ✓；未跑 Lean ✓；零数值 ✓｜编号 ✓ `V295`（`id_claim.sh` ✓）

---

## §1 Compression Audit 十问（逐项回答）

$$\textbf{(1) }V_T：＝\mathbb C^{d},\ d：＝\Big\lfloor \tfrac{LT}{2\pi}\Big\rfloor,\ L=\log\tfrac{T}{2\pi}\ ⟹\ \boxed{d=N(T,2T)+O(L)} ✓$$
$$\qquad \text{（Gabor 调制点}\ \alpha_k=T+\tfrac{2\pi k}{L};\ \text{每零给}\ v_\rho=\big(\widehat\phi(\gamma_\rho-\alpha_k)\big)_{k<d}\in\mathbb C^d\ ⟹ \textbf{这就是"压进}\ d\ \text{维"}）✓$$
$$\textbf{(2) }W_T：\text{即}\ \widetilde G\ \text{所在的}\ \mathbb C^d\（\text{同一空间}）;\ \text{"压缩"}\ ＝\ \text{从"全体零点数据"到}\ \mathbb C^d\ \text{的 Gabor 框架化} ✓$$
$$\qquad \widetilde G：＝\tfrac1{aL^{2}}\sum_{\Re\gamma_\rho\in I'}m_\rho v_\rho v_\rho^{\mathsf T},\qquad P：＝\tfrac1{aL^{2}}\sum_{\rho\in\mathrm{on}}m_\rho v_\rho v_\rho^{\mathsf T}\ (\succeq0),\qquad Q：＝\widetilde G-P ✓$$
$$\textbf{(3) }P_T：\ \textbf{不是正方向计数}，\text{而是}\ \boxed{\operatorname{rank}P_1}\ \text{（"简单在线部分"的秩下界）} ⟹ \textbf{目标函数是秩} ✓✓$$
$$\textbf{(4) }D_T=\dim V_T=d=N(T,2T)+O(L)\sim N ✓$$
$$\textbf{(5) }C_T=\dim W_T\sim d\sim N ⟹ \boxed{r_{\rm comp}=\tfrac{C_T}{D_T}\to1}\ \textbf{（压缩几乎不损失维数）} ✓✓✓$$
$$\textbf{(6) }P_T\ \text{的下界来源}：\textbf{Lemma R（秩-迹不等式，c=2 形式，Lean 逐字）}：$$
$$\qquad P\succeq0,\ \operatorname{rank}P\le r,\ n_+(Q)\le b\ \Longrightarrow\ \boxed{r\ \ge\ 2\operatorname{tr}P+4\operatorname{tr}Q-4b-\|P+Q\|_{F}^{2}} ✓✓$$
$$\qquad \text{配 (Z) 的签名记账}\ \operatorname{tr}P_1+2n_+(Q')\le N\（\text{功能方程把离轴对配成签名}(1,1)\ \text{的 block}）⟹ b\le\tfrac{N-\operatorname{tr}P_1}2：$$
$$\qquad \qquad r\ \ge\ 2\operatorname{tr}P_1+4\operatorname{tr}Q'-4\cdot\tfrac{N-\operatorname{tr}P_1}{2}-\|\widetilde G\|_F^{2}\ =\ \boxed{4\operatorname{tr}\widetilde G-2N-\|\widetilde G\|_{\rm HS}^{2}} ✓✓✓\ \text{（与论文单链逐步吻合）}$$
$$\textbf{(7) ⭐⭐ }2/3\ \text{第一次出现的那一行}：\text{在}\ \textbf{(P) 代入}\ \operatorname{tr}\widetilde G=N+o(N)\ \text{与}\ \|\widetilde G\|_{\rm HS}^{2}=\big(R(\psi)+o(1)\big)N\ \text{之后}：$$
$$\qquad \operatorname{rank}P_1\ \ge\ \big(4-2-R(\psi)-o(1)\big)N\ =\ \big(2-R(\psi)-o(1)\big)N;\qquad \psi=\psi_0\ \Longrightarrow\ R(\psi_0)=\tfrac43\ \Longrightarrow\ \boxed{\tfrac23} ✓✓✓$$
$$\qquad \text{故}\ 2/3\ \text{的}\ \textbf{第一来源}\ ＝\ \boxed{R(\psi_0)=\tfrac43}\ \text{（Montgomery 无条件素数侧二阶矩常数，带宽}\le1）✓✓✓$$
$$\textbf{(8) 该行用到了什么}：\textbf{维数？否};\ \textbf{正性？否};\ \text{用的是}\ \boxed{\textbf{trace}+\textbf{rank}+\textbf{Hilbert–Schmidt 范数}}\ \text{＋ 签名（惯性）记账} ✓✓$$
$$\qquad \text{（论文自述：}\textbf{用惯性／签名＋秩-迹取代正性};\ P\succeq0\ \text{仅为 Lemma R 的假设，}\textbf{不承担数学载荷}）✓✓$$
$$\textbf{(9) 换成最优可能值是否得}\ 1-o(1)？\ \textbf{否}：\text{要}\ 2-R\ge1\ \text{需}\ R\le1，\text{而带宽}\le1\ \text{时}\ R(\psi_0)=\tfrac43，\text{且}\ \textbf{带宽一证书类天花板}\approx0.68185 ✓$$
$$\qquad \text{论文 Remark 1.1 量化路线图}：0.70／0.80／0.90\ \text{需 Fourier 支撑约}\ 1.04／1.26／1.70 ⟹ \textbf{必须突破带宽一} ✓✓$$
$$\textbf{(10) 最后一步是否恰好等价于 Weil 正性？}\ \textbf{否} ✓✓✓$$
$$\qquad \text{① 本文}\ \textbf{不用正性}（惯性／秩-迹取代）;\ \text{② 该路线有}\ \textbf{结构性天花板}\ (<1)\（0.68185）⟹ \text{故它}\ \textbf{不是 ③ 类}（非 RH 等价）\ \text{而是}\ \textbf{单边比例路线} ✓✓$$

---

## §2 ⭐⭐⭐ 分解结论（回答唐先生的核心提问）

$$\boxed{\text{答案}：2/3\ \textbf{不是"压缩维数损失"}，而是\ \textbf{"秩-迹／二阶矩信息损失"}} ✓✓✓$$
$$\qquad \text{几何压缩率}：r_{\rm comp}=\tfrac{C_T}{D_T}\ \to\ 1\ \text{（}d=N+O(L)：\text{压缩几乎无损}）✓✓$$
$$\qquad \text{"利用率"}：r_{\rm pos}：＝\tfrac{P_T}{C_T}\ \to\ 2-R(\psi_0)\ =\ \tfrac23\ \text{（全部损失在此）}✓✓$$
$$\qquad \Longrightarrow \tfrac23\ =\ 1\times\tfrac23 ⟹ \textbf{瓶颈不在被压缩掉的空间，而在"能读出多少谱信息"} ✓✓✓$$
$$\qquad ⚠️\ \text{标签更正}：\text{唐先生的第二项命名为"}\textbf{正性利用率}\text{"}\ \textbf{不适用} —— \text{本文}\ \textbf{根本不用正性};\ \text{准确名称是}\ \boxed{\textbf{秩-迹／二阶矩利用率}} ✓✓$$

---

## §3 ⭐⭐⭐ 由审计得到的**三条结构结论**

$$\textbf{(C1) 唐先生的硬禁令被审计证实}：\text{压缩维数}\ \textbf{几乎无损}（r_{\rm comp}\to1）⟹ \textbf{"构造更大压缩空间"}\ \textbf{不是瓶颈} ✓✓✓$$
$$\qquad \Longrightarrow \textbf{且}\ \text{由 §1(9)：即便把压缩做到极致，带宽}\le1\ \text{仍卡在}\ 0.68185 ⟹ \textbf{提高压缩率的路是死路} ✓✓$$
$$\textbf{(C2) 瓶颈}\ ＝\ \textbf{二阶矩预算}\ R(\psi)\ge\tfrac43\ \text{（带宽}\le1）⟹ \text{压低它}\ \textbf{必须支撑}>1\ \text{（＝}\ `V162`\ \text{的"support}>1\ \text{墙"）} ✓✓✓$$
$$\qquad ⟹ \boxed{\textbf{三向统一}：\text{AF 的}"2/3\to1"\ \Longleftrightarrow\ \text{支撑}>1\ \text{的无条件化}\ \Longleftrightarrow\ \text{档案}\ `V162`\ \text{墙}\ \Longleftrightarrow\ \text{前沿 k=3 矩缺口（差}\ T^{1/3}）}} ✓✓✓$$
$$\qquad \qquad \text{（即：}\textbf{无需问"能否}\ 2/3\to1\text{"};\ \text{问题}\ \textbf{等价于}"支撑>1\ \text{能否无条件"}）✓✓$$
$$\textbf{(C3) (丙) 的第一个非局部核已被}\textbf{显式给出并量化}：\ \boxed{K_T(x,y)=\langle P_Tx,\ P_Ty\rangle},\ P_T\ ＝\ \text{Gabor 调制窗的全局投影} ✓✓$$
$$\qquad \text{它}\ \textbf{确是非局部}（\text{全局投影，非逐零点算子}）;\ \text{其增益}\ \textbf{已被量化}：\tfrac5{12}\to\tfrac23\to0.67250\（\le0.68185）⟹ \textbf{非局部核确有增益，但带宽}\le1\ \text{时}\ \textbf{可证达不到 1} ✓✓✓$$

---

## §4 判词 ＋ 边界 ＋ 净产出 ＋ 下一步

$$\boxed{\textbf{V295 判词}：\text{① }2/3\ ＝\ r_{\rm comp}(\to1)\times(2-R(\psi_0))（\textbf{损失全在秩-迹/二阶矩}）;\ \text{② 承载处＝带宽一无条件 HS 常数}\ R(\psi_0)=\tfrac43;\ \text{③ 正性未用（非 ③ 类）};\ \text{④ 天花板 0.68185 ⟹ 压缩加维是死路};\ \text{⑤ 瓶颈＝"支撑>1 无条件化"（三向统一）}} ✓✓✓$$

```
① ⚠️ 本档依据 `V185`（**阅读笔记**，其自标"未独立复核任何证明步骤"）＋ 本地 Lean **源码文本**（未跑构建）⟹ 常数与结构为**原文转述**，未复算 ⚠️
② ⚠️ §1(6) 的逐步吻合为**本档推导**（用 c=2 形式 ＋ 签名记账反推论文单链）⟹ 已自洽，但未与论文 §3–§4 逐行核对 ⚠️
③ ⚠️ 天花板 0.68185 依赖外部数值包络假设 `EnclOK`（`V185` §8(ii)）⚠️
④ ⚠️ 本档**不声称** AF 的证明正确／不正确；亦**不外推**"任何非局部核都达不到 1"（N1）✓
⑤ 未用 RH 作推导 ✓；未跑 Lean ✓；零数值 ✓
```

```
① ⭐⭐⭐⭐⭐ **十问全部回答**；关键第 (7)：**$2/3$ 首次出现于 (P) 代入 $\operatorname{tr}\widetilde G=N$、$\|\widetilde G\|^2_{\rm HS}=R(\psi)N$ 之后，来源 ＝ $R(\psi_0)=4/3$** ✓✓✓
② ⭐⭐⭐ **核心答案**：$2/3$ **不是压缩维数损失**（$r_{\rm comp}\to1$；$d=N+O(L)$），**是秩-迹／二阶矩信息损失**；且**正性未被使用** ⟹ 标签应为"秩-迹利用率"，而非"正性利用率" ✓✓✓
③ ⭐⭐⭐ **三向统一**：AF 的 $2/3\to1$ ⟺ **支撑 >1 的无条件化** ⟺ `V162` 墙 ⟺ 前沿 k=3 矩缺口（$T^{1/3}$）✓✓✓
④ ⭐⭐ **压缩加维＝死路**（审计证实唐先生硬禁令）：即便压缩到极致，带宽 ≤1 仍卡 0.68185 ✓✓
⑤ ⭐⭐ **(丙) 的第一个非局部核已显式并量化**：$K_T(x,y)=\langle P_Tx,P_Ty\rangle$（Gabor 全局投影）⟹ 增益 $\tfrac5{12}\to\tfrac23\to0.67250$，**带宽 ≤1 时可证 <1** ✓✓
【下一步（由审计直接给出，供唐先生定）】
  (甲′) 攻 **"支撑 >1 的无条件化"**（＝三向统一的交点）—— 但须先辨明：支撑 >1 的无条件信息是否**已被证明不可能**（若可证 ⟹ 天花板升为定理；若不可证 ⟹ 唯一突破口）✓
  (乙′) 攻 **非局部核的一般分类**：把 AF 的 Gabor 核作为第一个实例，问"**带宽标签**"是否为非局部核增益的**内在上限**（即：是否存在不属任何"带宽-$k$ 证书类"的非局部核）✓
  (丙′) 接受本档结论，将 V295 作为 (丙) 的**第一份量化档案**，转向其他主线 ✓
```
