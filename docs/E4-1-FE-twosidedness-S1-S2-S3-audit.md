# E4-1（辛-1）— **函数方程双侧性是否结构性必然**：S1 → S2 → S3 审计

> 唐先生 2026-09-16 17:52 拍板。**只开 S1/S2/S3，不开候选机制。**
> 目标：攻击目前唯一明确的「线强制障碍」——**FE 的双侧性**。（不研究几何侧停滞，留给辛-2。）

---

## 0. 立题修正（唐先生指定）
$$\textbf{不是}\ \text{泛泛研究函数方程}，\text{而是问}：\boxed{\text{FE 的双侧性是否是结构性必然}}$$
$$\text{已知}：\xi(s)=\xi(1-s),\ \xi(\bar s)=\overline{\xi(s)}\ \Longrightarrow\ \text{若}\ \rho\ \text{为零点，则}\ \rho,\ 1-\rho,\ \bar\rho,\ 1-\bar\rho\ \text{皆为零点}$$
$$\qquad\text{（DLMF §25.10 明确记录非平凡零点关于实轴与临界线的对称性 —— 唐先生引文，本档未重验）}$$
$$\text{设}\ \rho=\tfrac12+\delta+it \Longrightarrow 1-\rho=\tfrac12-\delta-it \Longrightarrow \text{单一 involution 产生}\ \boxed{\delta\leftrightarrow-\delta}$$

---

## S1 — FE 对称性定理化（**预期：快速得到局部 DEAD**）

### S1.1 定理（本档，初等，可 Lean 化）
$$\text{设}\ P\ \text{为关于零点的性质／可容许性条件，满足}\quad P(s)\Longrightarrow P(1-s)\quad\text{与}\quad P(s)\Longrightarrow P(\bar s)$$
$$\text{则}\ P\ \text{在}\ G：＝\langle s\mapsto1-s,\ s\mapsto\bar s\rangle\cong C_2\times C_2\ \text{下}\ \textbf{不变}：\ P(s)\Longrightarrow P(1-\bar s)$$
$$\qquad\text{（复共轭} + \text{FE 复合：}P(s)\to P(\bar s)\to P(1-\bar s)\ ✓）$$
$$\textbf{推论（S1 主结论）}：\text{任何}\ \textbf{仅由 FE（及复共轭）保持} \text{的可容许性条件，}\ \textbf{不能选择}\ \delta\ge0\ \text{或}\ \delta\le0$$
$$\qquad\text{即它作用在四元组}\ \{\tfrac12\pm\delta\pm it\}\ \text{上} \Longrightarrow \text{不含}\ \delta\ \text{的符号信息}$$

### S1.2 精确形式（取代"对称性直觉"）
$$\text{设可容许类}\ \mathscr C\ \text{满足}\ \mathscr C(Z)\Longrightarrow\mathscr C(gZ)\ (\forall g\in G)。\ \text{若}\ \mathscr C\ \text{能推出}\ \mathrm{Re}\,\rho=\tfrac12，\text{则须：}$$
$$\qquad\boxed{\text{线强制}\ \Longrightarrow\ \text{必须出现}\ \textbf{额外的非对称信息}（G\text{-非不变量}）}$$
$$\text{理由}：\text{"}\delta\ne0\text{"这一信息的载体必须}\ \textbf{破坏}\ \delta\leftrightarrow-\delta\ \text{不变性}；G\text{-不变条件对其整个轨道（含}\ 1-\rho\ \text{与}\ \rho\ \text{两者）}\ \textbf{一视同仁}✓$$
$$\Longrightarrow\ \boxed{\text{S1：}\textbf{FE-only}\ \not\Rightarrow\ \text{line enforcement}}\quad(\textbf{局部 DEAD，完全形式化，不使用任何 RH 假设})$$

---

## S2 — 加入 Euler product 后，是否自动产生破对称量

### S2.1 精确提问
$$\boxed{\mathrm{EulerProduct}+\mathrm{FE}\ \stackrel{?}{\Longrightarrow}\ \exists\,\mathcal O\ \text{非}\ G\text{-invariant 且强制}\ \delta=0}$$
$$\textbf{须避免的旧路}：\text{Euler product}\to\text{explicit formula}\to\text{Weil positivity}\ \Longrightarrow\ \text{若"破对称量"最后就是 Weil 正性，}\textbf{立即回收旧类}$$

### S2.2 审计发现（本档）
$$\textbf{(a) 破对称量}\ \textbf{确实存在}：\text{Euler 积在}\ \mathrm{Re}\,s>1\ \text{收敛} \Longrightarrow \boxed{\mathrm{Re}\,s>1\ \text{无零点}}$$
$$\qquad\text{此为}\ \textbf{单侧} \text{约束（}\textbf{天然} G\text{-非不变}）✓ \Longrightarrow \text{S2 的答案}\ \textbf{不是平坦 DEAD}：\text{破对称成分存在}$$
$$\textbf{(b) 但其强度为}\ \textbf{区域型}：\text{配合经典论证得无零区}\ \mathrm{Re}\,s>1-\tfrac{c}{\log|t|}\Longrightarrow \text{距}\ 1/2\ \text{极远（与 E4-0 Φ1 判定一致）}$$
$$\textbf{(c) 类层答案（关键）}：\mathrm{EulerProduct}+\mathrm{FE}\ \textbf{不足} \text{以在类层强制临界线}：$$
$$\qquad\text{存在具备 FE 却带离线零点的对象}：\text{(i) Davenport--Heilbronn 型（无 Euler 积的完全乘性）}；$$
$$\qquad\qquad\text{(ii) Tao 给出的"修改}\ \zeta\text{"构造：仍满足 FE、解析外形相似，但有离线零点（}\textbf{缺 Euler 积，故不是 RH 反例}）$$
$$\qquad\qquad\qquad\text{（唐先生引文\\,What's new 2014-12-15；本档未重验）}$$
$$\qquad\text{与本项目既有结果一致}：\text{V286（}\chi\ \text{阶}>2\ \text{时完全乘性失效）／V287-C（已知离线构造皆破坏乘性）}$$
$$\textbf{(d) 循环警告（本档必须标注）}：\text{若把 S2 提问限制在}\ \zeta\ \text{本身}，\text{则"}\mathrm{EulerProduct}+\mathrm{FE}\Rightarrow\text{线"}\ \textbf{字面等价于 RH} \Longrightarrow \text{该形式}\ \textbf{不可用}；$$
$$\qquad\Longrightarrow\ \text{S2 必须停在}\ \textbf{类层} \text{（"对某类中所有对象，是否强制线"），\text{而类层答案见 (c)＝}\textbf{不强制}✓$$

### S2.3 S2 小结
$$\text{破对称成分}\ \textbf{存在但弱}（\text{区域型}）；\text{类层不强制线；}\ \text{对}\ \zeta\ \text{的单对象提问}\ \textbf{循环不可用}$$
$$\qquad\Longrightarrow\ \text{若要把"\text{区域型弱约束}"提升为"\text{线强制}"，\text{所需的正是一条}\ \textbf{新结构}；\ \text{而这正是 S3 的问题。}$$

---

## S3 — 破对称量能否真正"定位"（而非仅区分两侧）

### S3.1 精确要求
$$P(\delta)>P(-\delta)\ \textbf{远远不够}；\ \text{真正需要}\ \boxed{\exists\,\mathcal D\ \text{来自算术可容许性},\ \mathcal D(\delta)\ge0,\ \mathcal D(\delta)=0\iff\delta=0}$$
$$\textbf{禁止}：\text{把}\ \mathcal D(\rho)=|\mathrm{Re}\,\rho-\tfrac12|\ \text{型（RH 重写）偷偷塞入；}\ \text{也禁止等价于 Weil positive form}$$

### S3.2 审计发现
$$\text{已知"}\mathcal D\ge0\ \text{且}\ \mathcal D=0\iff\text{线}"的实例，}\textbf{全部} \text{为}\ \textbf{正性型}：$$
$$\qquad\text{Weil 显式公式判据（}\mathcal D=\text{对全部测试函数的二次型}\ge0\iff\mathrm{RH}）\ \to\ \textbf{Weil positivity} \Longrightarrow\ \textbf{回收旧类}✗$$
$$\qquad\text{其余自然候选}\to\ \text{或为 RH 重写（}\delta\ \text{的直接函数）}\to\ \text{定义循环}✗$$
$$\Longrightarrow\ \boxed{\text{S3：审计范围内}\ \mathcal D\ \text{只有正性型实现}\ (\textbf{＝Weil})\ \text{或 RH 重写} \Longrightarrow \textbf{回收旧类}}$$

---

## 4. 三闸汇总
$$\begin{array}{c|c|c}
\text{闸} & \text{结论} & \text{强度}\\ \hline
\mathrm{S1} & \text{FE-only}\ \not\Rightarrow\ \text{line enforcement} & \textbf{局部 DEAD（可形式化）}\\
\mathrm{S2} & \text{破对称成分存在但}\ \textbf{区域型弱}；\text{类层不强制；单对象提问循环} & \text{部分}\ \mathrm{DEAD}\\
\mathrm{S3} & \mathcal D\ \text{的已知实现皆为正性型（Weil）或 RH 重写} & \text{回收旧类}
\end{array}$$

## 5. ⭐ 结构性结论（唐先生预设的强结论）
$$\boxed{\text{FE 的双侧性}\ \textbf{不是偶然障碍}；\ \text{现有 Euler--FE 框架本身缺少"破双侧}\to\text{线定位"的结构}}$$
$$\text{三条支撑}：\text{(i) S1 证明}\ G\text{-不变条件携带不了}\ \delta\ \text{符号信息；}$$
$$\qquad\text{(ii) S2 证明 Euler 积只提供}\ \textbf{单侧但区域型} \text{的破对称成分（}\mathrm{Re}\,s>1\ \text{型），\text{类层不足以强制线}；}$$
$$\qquad\text{(iii) S3 证明}\ \mathcal D\ \text{的已知实现全落入正性／RH 重写（}\text{即 Weil 循环}）}$$

## 6. 边界（N1/N2 严守）
$$\text{① S1 为本档}\ \textbf{定理（初等，可 Lean 化）}，\text{尚未形式化；}$$
$$\text{② S2 的 (c) 依据 DLMF／Davenport--Heilbronn／Tao 构造（唐先生引文）＋档案 V286／V287-C，}\textbf{未逐行重验}；$$
$$\text{③ S2(d) 的"单对象提问循环"为}\ \textbf{[结构判定]}（\text{逻辑观察）；}\quad\text{④ S3 的"只有正性型实现"为}\ \textbf{审计结论（枚举型）}，\text{不构成不可能性}；$$
$$\text{⑤ }\textbf{未用 RH}；零数值；\text{未跑 Lean}；\quad\text{⑥ 本档}\ \textbf{未提出任何候选机制}（\text{唐先生指定）。}$$

## 7. 净产出
$$\text{(i) S1 定理化：}\textbf{FE-only}\not\Rightarrow\text{line enforcement}（\text{取代"对称性直觉"，可形式化）；}$$
$$\text{(ii) S2：破对称成分}\ \textbf{存在但弱}（\text{区域型}）＋类层不足＋单对象循环警告；$$
$$\text{(iii) S3：}\mathcal D\ \text{的已知实现全为 Weil／RH 重写}\Longrightarrow\text{回收；}$$
$$\text{(iv) ⭐ 结构性结论：}\textbf{现有 Euler--FE 框架缺少"破双侧}\to\text{线定位"的结构}（\text{不是偶然障碍}）；$$
$$\text{(v) 明确}\ \textbf{未提出候选}；\ \text{若将来要开候选，须由 S2/S3 的缺口反推。}$$
