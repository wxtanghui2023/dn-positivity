已查地图（**先查后写**）：`IMPL-1`（二分定理落点＝LP 取值定理）、`CEILING-AUDIT-3`、`C-74`、`V185`／`V186`、`EXTERNAL`：`lean-frontier-audit/{Defs,Grid,Ceiling}.lean` ＋ `lp/ceiling_lp_recompute.py`（**已本地复算**）。关键词回查：`方法能力陈述`＝0、`对偶重述`＝0、`marks 几何`＝0 ⟹ 均本档新增 ✓。**结论**：⭐ 唐先生 23:12「继续」⟹ **执行复算成功（数字逐位对上）** ✓✓，但得**两条修正** ✓✓：**(甲) ⭐ `Ceiling.lean` 的真实结构不是"所有律 p≥0.682"，而是"证书值 ≤ 该构型自身的 p₁ ＋ 稳定误差"**——即天花板是**方法能力陈述**（证书族打不过已知最好的律），**不是**对真 `p^{*}` 的下界 ✓✓；**(乙) ⭐ 反推实测 `target−2/3 = 1.52\times10^{-2} \gg \delta_{\text{box}} = 2.09\times10^{-5}`** ⟹ 目标**不能**写成"`2/3` ＋ 证书缺陷" ⟹ **`p_{\min}` 本身 `\approx0.6818` ＝律自身简单点比例** ⟹ **\textbf{对偶侧只是主原的重述}**（前沿自己也这样写）✓✓ ⟹ 故 `IMPL-1` §4 的"对偶证书 ⟹ 独立确认"**必须弱化** ✓。**(丙) 附加结构性事实**：`r(1)\ne0` 时 **LP 无界**（HiGHS 实测 `Unbounded`）⟹ 证书**必须** band-limited ✓✓

FREEZE-ACK: 本档即冻结期内的复算与结构核验（依 `§8.1`；不产候选结论）

D0: 本档对象 = **前沿 LP 的本地独立复算 ＋ 两条修正（方法能力陈述／对偶重述）＋ 无界性结构事实** —— 关系 = 复算与结构核验，非新机制
D1: 0

# IMPL-2 · **复算成功 ＋ 两条修正**

> **时间**：2026-09-18 23:12 唐先生：**「继续」** ⟹ 执行复算 ✓

---

## §0 结论（先行）

$$\textbf{(甲)}\ ⭐\ \text{`Ceiling.lean`}\ \text{的真实结构}：\text{证书值}\ v\le p_1+\text{稳定误差}\（p_1＝\textbf{该构型自身} \text{的简单点比例}）\Longrightarrow \textbf{方法能力陈述}✓✓$$
$$\textbf{(乙)}\ ⭐\ \text{反推实测}：\text{target}-\tfrac23=1.52\times10^{-2}\gg\delta_{\text{box}}=2.09\times10^{-5} \Longrightarrow \textbf{对偶侧只是主原的重述}✓✓$$
$$\textbf{(丙)}\ \text{结构性事实}：r(1)\ne0\ \text{时 LP}\ \textbf{无界} \Longrightarrow \text{证书必须 band-limited}✓✓$$

---

## §1 复算实测（**数字逐位对上**）

$$\text{运行}：\texttt{python3 lp/ceiling\_lp\_recompute.py}（本地，退出正常，输出 JSON 已重写）✓$$
$$\delta_{\text{box}}(B=8.2)=2.0854\times10^{-5};\quad \delta_{\text{box}}(B=1.0)=2.5431\times10^{-6}\quad（\textbf{与存储 JSON 逐位一致}）✓✓$$
$$\text{缺陷实测}：1-x^2\Rightarrow3.8147\times10^{-6};\ x(1-x)\Rightarrow1.2716\times10^{-6};\ 1-x\Rightarrow2.5431\times10^{-6};\ 1-x^4\Rightarrow6.3578\times10^{-6}✓$$
$$\texttt{tau\_max}=2^{-132}\ \text{型量};\quad p_0=0.681828687463831474\ldots;\quad S(256)=211.4320091424858✓$$
$$\Longrightarrow ⭐\ \textbf{可复现性成立}（independent recompute 第一步 ✓）$$

## §2 ⭐ 修正（甲）：`Ceiling.lean` 的真实结构（逐字级）

$$\text{定理（`ceiling\_of\_valid\_at`，结构）}：\text{若证书在构型上}\ \textbf{有效}：c_0+\sum_j s_j\,r(j/N)\le p_1,$$
$$\qquad \text{则}\quad c_0+\int_0^1 r(x)\,x\,dx\ \le\ p_1+|r(1)||D(1)|+|r'(1)||E(1)|+\sup|E|\int_0^1|r''|✓✓$$
$$\Longrightarrow ⭐\ \text{右边}\ \textbf{含}\ p_1\ \text{本身} \Longrightarrow \text{这不是"所有律}\ p\ge0.682\text{"，而是}\ \textbf{"证书值}\le\text{该律自己的}\ p_1+\text{小误差"}✓✓$$
$$\Longrightarrow \textbf{天花板＝方法能力上限}（\text{bandwidth-one 证书族}\ \textbf{打不过已知最好的律}）✓✓$$
$$\qquad ⚠️\ \text{与}\ \text{`V188` §2／`CEILING-AUDIT-3`}\ \text{的架构一致；}\ \text{但}\ \textbf{"对真}\ p^{*}\ \text{的下界"这一读法须撤回}✓✓$$

## §3 ⭐ 修正（乙）：反推实测 ⟹ **对偶只是重述**

$$\text{关系}：\text{真实 LP 值}=p_{\min}+\delta_{\text{box}} \Longrightarrow p_{\min}=\text{target}-\delta_{\text{box}}✓$$
$$\text{实测}：p_{\min}=0.6818078\quad（\text{与记录}\ p_0\ \text{差}\ -2.08\times10^{-5}＝\delta_{\text{box}}）✓$$
$$\text{对照}：\text{target}-\tfrac23=0.0151620\quad\gg\quad\delta_{\text{box}}\approx2.1\times10^{-5}✓✓$$
$$\Longrightarrow ⭐\ \textbf{目标不能写成"}\tfrac23+\text{证书缺陷}\text{"}（缺陷\sim10^{-5}\sim10^{-3}，\text{而缺口}\sim1.5\times10^{-2}）✓✓$$
$$\Longrightarrow ⭐⭐\ p_{\min}\ \textbf{本身} \text{必须}\approx0.6818，\ \text{而记录值}\ p_0=1-a_N\ \text{正落在此} \Longrightarrow \textbf{目标值＝律自身简单点比例＝主原 LP 最优值};\quad \textbf{证书（对偶）只是它的重述}✓✓✓$$
$$\qquad ⚠️\ \text{此为}\ \textbf{前沿自己脚本的结论}（\text{本档引用}），\ \text{且由本档}\ \textbf{复算实测确认}✓✓$$

## §4 ⭐ 前沿脚本给出的关键判定（本档引用，未独立复核）

$$\text{整数位置} \Longrightarrow S(256)=|\sum m_i|^2/N=N=256;\quad \text{而包络给}\ S(256)=211.432\neq256✓$$
$$\Longrightarrow \textbf{最优律的原子位置必非整数}（\bmod 256） \Longrightarrow \textbf{Parseval 刚性失效}✓✓$$
$$\Longrightarrow \text{故}\ p\ \text{与}\ S\ \text{之间}\ \textbf{没有可硬算的刚性耦合} \Longrightarrow \text{包络}\ \textbf{不 pin}\ p \Longrightarrow \text{缺}\ \textbf{marks 几何}✓✓$$
$$\qquad （\text{脚本逐字}：\text{"这正是缺失的 marks 几何"}\text{）}✓$$

## §5 对 `IMPL-1` 的更正 ＋ 剩余可攻点

$$\textbf{更正}：\text{`IMPL-1` §4 的 "(对偶)给出对偶可行解}\Longrightarrow\textbf{独立确认天花板}"\ \textbf{须弱化}：$$
$$\qquad \text{对偶可行解}\ \textbf{不给} \text{独立下界};\ \text{它}\ \textbf{重述} \text{主原最优值}✓✓$$
$$\textbf{剩余可攻点（诚实清单）}：$$
$$\qquad \text{(i)}\ ⭐\ \textbf{primal 侧}：\text{能否给出一个}\ \textbf{律}\ \text{使}\ p<p_0？\（\text{需 marks 几何}）✓$$
$$\qquad \text{(ii)}\ \text{能否}\ \textbf{收紧约束集}（\text{用比包络更强的信息}）\Longrightarrow \text{把}\ p\ \text{真正 pin 住}✓$$
$$\qquad \text{(iii)}\ \text{能否证明"}\textbf{整数位置假设}\text{"的某个变体}（\text{若成立则 Parseval 复活}）✓$$
$$\qquad \text{(iv)}\ ⚠️\ \textbf{不可} \text{再做}\ \textbf{"对偶侧加强"} \text{——本档实测已示其为重述}✓✓$$

## §6 边界与回查

- ⚠️ §1 为**本档实测**（可复现）✓；§2 §3 引 `Ceiling.lean` 与前沿脚本结论，**逐字级** ✓
- ⚠️ §4 为**引用**（前沿脚本自述），本档**未独立复核** Parseval 论断 ✓
- ⚠️ **不声称**天花板有错；**不声称**能构造更小的律；**不声称**与 RH 相关（只关乎证书类）✓
- **未用** RH 作推导；**未取** RH 输入 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）；⚠️ 复算**未出现**"结果异常"（历史 11 次教训未触发）✓

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 23:1x）`[纪律]`（先跑后写）

```
技术词 方法能力陈述     命中文件数=0  ⟹ 本档新增
技术词 对偶重述        命中文件数=0  ⟹ 本档新增
技术词 marks 几何      命中文件数=0  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
