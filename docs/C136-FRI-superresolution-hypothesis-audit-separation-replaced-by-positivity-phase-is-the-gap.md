已查地图（**先查后写**）：`C-132`（F3 反例；§5 真靶子；"缺失假设＝分离下界"）、`C-133`（核维数判据）、`C-134`（三 T-I 共同结构）、`C-135`（F3 机制＝FRI 零空间；零空间滤镜）、`C-113`（β＝模长通道／γ＝相位通道）、`C-125`／`C-126`（饱和／信息位于收敛边界）、`W6`（support>1 原子墙）。关键词回查：`正性替代分离`=0、`相位可见性`=0、`Rayleigh 极限`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 11:39「甲」）**：**审 FRI／超分辨率稳定性定理的假设清单 ⟹ 对质 ζ/B2-1 能否提供。**
**结论（先行）**：$$\textbf{(一)}\ \text{文献假设三条}：\text{分离}\ \Delta\ge2\lambda_c／\text{尖峰数}\le n/4／\text{数据为}\ \textbf{复} \text{Fourier 样本（含相位）}✓$$
$$\textbf{(二)}\ ⭐⭐\ \text{承重注记（逐字，二次确认）}：\textbf{"There is no separation requirement if all }d_i\text{ are positive"}\ \Longrightarrow\ \textbf{正性可替代分离}✓✓$$
$$\textbf{(三)}\ \text{Moitra '15}：\Delta<\lambda_c\ \Longrightarrow\ \text{无估计量可区分（指数级小噪声也不行）}\ \Longrightarrow\ \text{Rayleigh 极限对}\ \textbf{复振幅} \text{情形是根本的}✓✓$$
$$\textbf{(四)}\ ⭐\ \text{我方}：\textbf{正性 ✓✓}（\text{marks}\in\{1,2\}>0;\ w_c\ge0）;\ \text{数据}＝\textbf{模长}（|\hat\mu|^2）\ \Longrightarrow\ \text{相位检索}✓✓$$
$$\textbf{(五)}\ ⟹\ \boxed{\textbf{分离不是绑定缺口};\ \textbf{真正的缺口是"相位"}}✓✓$$
$$\textbf{(六)}\ ⚠️\ \textbf{自我更正}（\text{第 8 次同类}）：\text{`C-132` §5／`C-133` 中"缺失＝分离下界"}\ \textbf{须修正}⟹\text{缺的是}\ \textbf{相位}✓✓$$

FREEZE-ACK: 本档即冻结期内的外部理论假设审计与自我更正（依 `§8.1`；不产候选结论）

D0: 本档对象 = **FRI／超分辨率假设清单审计（分离被正性替代；缺口＝相位）＋ 对 C-132/C-133 定位的更正 ＋ 新靶子（相位可见性）** —— 关系 = 审计与更正，非新机制
D1: 0

# C-136 · **甲：FRI／超分辨率假设审计 —— 分离不是缺口（正性替代它），缺口是相位**

> **唐先生 2026-09-19 11:39**：**「甲」**（审 FRI 稳定性定理的分离假设 → 对质 ζ/B2-1）✓

---

## §1 文献假设清单（**逐字**）

$$\lambda_c=\frac{2}{n-1}\quad(\text{Rayleigh 分辨率极限})✓$$
$$\textbf{Theorem 15.6 (Candès, Fernandez-Granda '14)}：\text{设分离条件}\ \Delta\ \ge\ \frac{4}{n-1}=2\lambda_c\ \text{成立};$$
$$\qquad \text{则原子范数（或全变差）最小化是}\ \textbf{精确的};\ \text{确定性结果};\ \text{至多恢复}\ n/4\ \text{个尖峰};$$
$$\qquad \text{不依赖尖峰的}\ \textbf{振幅/相位};\quad ⭐⭐\ \boxed{\text{"There is no separation requirement if all }d_i\text{ are positive"}}✓✓$$
$$\textbf{Theorem 15.7 (Moitra '15)}：\text{若}\ \Delta<\frac{2}{n-1}=\lambda_c，\text{则}\ \textbf{不存在} \text{能区分某对}\ \Delta\text{-分离信号的估计量（即使噪声指数级小）}✓✓$$
$$\text{出处}：\text{Candès–Fernandez-Granda, }\textbf{CPAM 67}(6):906\text{–}956\ (2014);\quad \text{Super-Resolution from Noisy Data, }\textbf{JFAA 19}(6):1229\text{–}1254\ (2013)✓$$
$$\qquad (\text{以上逐字取自公开讲义}\ \text{ELE520}\ \text{super\_resolution.pdf；}\ [\text{外搜·片段级}]）$$

## §2 ⭐ 对质表（假设 × 我方可得性）

$$\begin{array}{c|c|c|c}
\text{假设} & \text{文献要求} & \text{我方（\text{`B2-1`}／}\zeta\text{）} & \text{判定}\\\hline
\textbf{相位（复样本）} & \text{必须有} & ✗\ \text{只有模长}\ |\hat\mu(j)|^2 & ⭐\ \textbf{绑定缺口}\\
\textbf{正性} & \text{可替代分离} & ✓✓\ \text{marks}\in\{1,2\}>0;\ w_c\ge0 & \textbf{有利（关键资产）}\\
\text{分离}\ \Delta\ge2\lambda_c & \text{需要（无正性时）} & ✗\ \text{零点间距不无条件可控} & \textbf{次要（被正性替代）}\\
\text{尖峰数}\ \le n/4 & \text{需要} & 128\text{–}256\ (\sum m=256,\ m\in\{1,2\}) & ⚠️\ \text{数量级须另核}\\
\text{噪声} & \text{小} & \tau=3\times10^{-40}\ (\approx\text{无噪声}) & ✓\\
\end{array}✓✓$$

## §3 ⭐ 判定与新认识（可引用）

$$\boxed{\textbf{判定}：\text{分离}\ \textbf{不是} \text{绑定缺口};\ \textbf{相位是}✓✓}$$
$$\textbf{新认识（两端各替代一个假设）}：$$
$$\qquad \text{文献}：\textbf{正性 ＋ 复相位}\ \Longrightarrow\ \textbf{免分离};\qquad \text{我方}：\textbf{正性 ＋ 无相位}\ \Longrightarrow\ \textbf{需整数结构替代相位}✓✓$$
$$\qquad ⟹\ \text{"正性"与"整数性"各买入一项：文献用正性买入}\textbf{免分离};\ \text{我方用整数性买入}\textbf{无相位下的唯一性}✓✓$$
$$\text{与}\ \text{`C-113`}\ \text{对接}：\text{相位}＝\gamma\ \text{通道};\ \beta＝\text{模长通道}\ \Longrightarrow\ \text{"无相位"正是}\ \textbf{β/γ 二分}✓✓$$

## §4 ⚠️ 自我更正（第 8 次同类）

$$\text{`C-132` §5 ｝／ \text{`C-133`} §3 的"}\textbf{缺失假设＝分离（零点纵坐标差的下界）}"\ \textbf{须修正}✓✓$$
$$\qquad \text{正确表述}：\text{缺失的是}\ \textbf{相位};\ \text{分离被}\ \textbf{正性} \text{替代}（\text{我方正性成立}\Longrightarrow\text{分离本不是障碍}）✓✓$$
$$\qquad \textbf{保留}：\text{`C-132` 的反例（窗口隐形测度）}\textbf{正确、仍成立};\ \text{`C-133` 的核维数判据}\ \textbf{正确、仍成立}✓✓$$
$$\qquad \text{只改"缺什么假设"的}\ \textbf{定位}✓$$

## §5 新方向（可落地）：靶子改为**相位可见性**

$$\text{新靶子}：\textbf{能否从算术侧获得相位（位置）信息}✓$$
$$\text{已知}：\text{相位}＝\gamma\ \text{通道}，\text{受}\ \text{`W6`（support}>1）\ \text{限制}✓$$
$$\qquad ⭐\ \text{但新增一点}：\text{文献告诉我们"}\textbf{有相位就免分离}" \Longrightarrow\ \text{若能得到}\ \textbf{部分相位}（\text{例：support}\le1\ \text{窗口内的相位}），$$
$$\qquad \text{也许足以恢复"}\textbf{支撑大小/秩}" \text{这类}\ \textbf{弱} \text{结论}✓✓$$
$$\qquad ⟹\ \textbf{具体新问题}：\ \boxed{\text{support}\le1\ \text{窗口内的相位，是否足以定秩？}}✓✓$$
$$\qquad ⚠️\ \text{与}\ \text{`C-125`／`C-126`} \text{的"信息位于收敛边界"对质：可能仍被饱和挡住};\ \textbf{但这一次的靶子形状是文献支持过的}✓$$

## §6 边界与回查

- ⚠️ §1 为**公开讲义片段级**引文（二次确认同一句）；**未**逐字核 CPAM／JFAA 原文 ✓
- ⚠️ §2 表中"尖峰数"一栏 ⚠️ 标"须另核"（我方 128–256 与文献 `n/4` 的对应需按 `n` 的选取重算）✓
- ⚠️ **不声称** 相位可见性可得；**不声称** 定秩可成 ✓
- **未用** RH；**未改**任何原档（仅追加更正指针）✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 11:4x）`[纪律]`（先跑后写）

```
技术词 正性替代分离   命中文件数=0 ::  ⟹ 本档新增
技术词 相位可见性    命中文件数=0 ::  ⟹ 本档新增
技术词 Rayleigh 极限 命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
