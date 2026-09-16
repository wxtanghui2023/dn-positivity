# E4-3 — **从 C1／C8 推导填充结构的"形状"** ＋ 与已测绘墙的碰撞

> 唐先生 2026-09-16 17:59「继续」；按 REVIEW-E4 §6 开工。
> **纪律**：候选须从第一行证明非 E3 旧类 ⟹ 故第一步不是列候选，而是**推导形状**（什么结构才可能不落旧类）。
> **本档不命名任何候选机制。**

---

## 1. C1 的形状推论（**小定理，严格的**）

### 1.1 定理（E4-3-A）
$$\text{设}\ Z=Z(\zeta)=\{\rho\}\ \text{为零点集}。\ \text{由 FE，}\ Z\ \text{在}\ G=\langle s\mapsto1-s,\ s\mapsto\bar s\rangle\ \text{下}\ \textbf{作为集合不变}：\ gZ=Z$$
$$\text{若}\ V\ \textbf{只依赖于}\ Z\（\text{即}\ V=V(Z)\ \text{为集合的函数）}，\text{则}\ \forall g\in G:\ V(Z)=V(gZ) \Longrightarrow V\ \textbf{是}\ G\text{-不变的}$$
$$\textbf{推论}：\boxed{\text{C1}\ \Longrightarrow\ V_X\ \textbf{不可能只依赖零点集}\ Z}\quad(\text{否则立即}\ G\text{-不变、C1 失败})$$
$$\Longrightarrow\ \boxed{V_X\ \text{必须依赖}\ Z\ \textbf{之外} \text{的结构}}$$

### 1.2 对该"之外结构"的三重夹逼（承接 C2／C6／C7）
$$\text{(a) C2}\ \Longrightarrow\ \text{该结构须由}\ \textbf{算术可容许性} \text{给出（非特选}\ a）；$$
$$\text{(b) C6}\ \Longrightarrow\ \text{不得是}\ \textbf{计数／support／correlation 预算／复杂度}；$$
$$\text{(c) C7}\ \Longrightarrow\ \text{不得是}\ \textbf{呈现／编码} \text{（换表示即变者弃）}$$
$$\Longrightarrow\ \text{所余候选形状只剩一类}：\boxed{\text{附着于零点的}\ \textbf{算术（乘性）结构}，\text{且非显式公式型附着}}$$
$$\qquad\text{（显式公式型附着＝把零点与素数经显式公式配对 —— 属旧类，C6 排除）}$$

### 1.3 碰撞（档案已测绘）
$$\text{此类形状}\ =\ \text{档案}\ \textbf{V280（词-字符 span）} \text{所审的同一问题}：$$
$$\qquad k=1\ \Longrightarrow\ \zeta\text{-local}\ \Longrightarrow\ \mathrm{L1}\ (\text{已封})；\qquad k\ge2\ \Longrightarrow\ \text{相关预算墙}\ (\text{V294-A：有限阶聚合增益}\le0)$$
$$\Longrightarrow\ \boxed{\text{C1 的形状推论}\ \textbf{落在 V280／V294-A 已测绘的墙上}}（\text{本档}\ \textbf{[结构判定]}）$$

---

## 2. C8 的形状推论（**诚实读出：填满 C8 ＝ 证明 RH**）

### 2.1 读出
$$\text{设}\ \mathcal D\ge0\ \text{由}\ \textbf{算术可容许性可证}，\text{且}\ \mathcal D=0\iff\mathrm{Re}\,\rho=\tfrac12。\ \text{则：}$$
$$\qquad\text{全体零点满足}\ \mathcal D=0 \Longrightarrow \text{Re}\,\rho=\tfrac12\ \text{对一切零点} \Longrightarrow \boxed{\mathrm{RH}}\ ✓$$
$$\Longrightarrow\ \boxed{\text{成功填满 C8}\ =\ \text{证明 RH}}\quad(\text{这不是缺陷，而是}\ \textbf{C8 的准确语义})$$

### 2.2 因此 C8 的真实形式是「符号／强度权衡」
$$\text{记输入强度参数}\ \lambda\（\text{如无条件支撑／测试函数带宽}）。\text{已知}\ \textbf{可证} \text{的下界形状为}：$$
$$\qquad\mathcal D\ \ge\ c(\lambda)>0\quad\textbf{仅当}\ |\mathrm{Re}\,s-\tfrac12|\ \ge\ \tfrac12-\tfrac{c'}{\log T}\ (\textbf{区域型})$$
$$\text{RH 级需要}：c(\lambda)>0\ \textbf{对一切}\ \delta>0\ (\textbf{线型})$$
$$\Longrightarrow\ \text{X 的任务}\ =\ \boxed{\text{把}\ \textbf{区域型可证下界} \text{升级为}\ \textbf{线型可证下界}，\text{且不得使用 RH 级输入（C5）}}$$

### 2.3 碰撞（档案已测绘）
$$\text{该升级正是}\ \textbf{V316 的}\ C^{\star}\ \text{墙}：\ \lambda\le1\Rightarrow G\le2-1/c_1^{\star}=0.672501；\ \text{要越过必须}\ \lambda>1\ (=\ \textbf{无条件支撑}>1)$$
$$\qquad\text{即 V162／V181 的 FSC-MV 墙；且 V295 已证}\ \text{非局部核增益}\ \textbf{恰等于} \text{该带宽需求}$$
$$\Longrightarrow\ \boxed{\text{C8 的形状推论}\ \textbf{与 V316／V162 墙同址}}（\text{本档}\ \textbf{[结构判定]}）$$

---

## 3. ⭐ 本档的结构性收获：**两个独立推导的缺口重合**
$$\text{E4 的缺口（线强制定位）经形状推导}\ \textbf{分裂为两只角}：$$
$$\boxed{\text{角 I（来自 C1）：零点上的非显式公式型算术结构}}\ \longrightarrow\ \text{V280／V294-A 墙}$$
$$\boxed{\text{角 II（来自 C8）：区域型}\to\text{线型的强度升级}}\ \longrightarrow\ \text{V316}\ C^{\star}／\text{V162}\ \text{墙}$$
$$\Longrightarrow\ \text{而这两堵墙}\ \textbf{正是今日 V316--V328 已测绘的墙} \Longrightarrow \textbf{缺口与已测绘墙重合}$$
$$\qquad\textbf{（这是新收获：此前 E4 的缺口与 V316 的}\lambda>1\ \text{墙} \text{是}\ \textbf{两条独立线索}，\text{现经 C1／C8 形状推导}\ \textbf{接上}）✓$$

## 4. 逻辑地位（严格标注）
$$\text{① §1.1 的推论}\ \textbf{是严格的}（\text{零点集}\ G\text{-不变}\Rightarrow\text{集合函数}\ G\text{-不变}）；$$
$$\text{② §1.2／§1.3／§2.2／§2.3／§3 的"碰撞"为}\ \textbf{[结构判定]}（\text{把形状与已测绘墙对接的推理）}，\text{非定理；}$$
$$\text{③ }\textbf{不声称}\ \text{角 I／角 II 不可填充}；\ \textbf{不声称}\ \text{缺口必有填充物；}$$
$$\text{④ 形状推导}\ \textbf{不等于候选}：\text{本档}\ \textbf{仍未命名任何机制}✓$$
$$\text{⑤ 若日后有候选，须}\ \textbf{从第一行} \text{声明它落在角 I 还是角 II，并证明它}\ \textbf{不在} \text{V280／V294／V162／Weil 之列。}$$

## 5. 判定
$$\textbf{E4-3 结果}：\text{把"线强制定位"缺口}\ \textbf{结构化} \text{为两只角，并证明二者各与一堵已测绘墙同址}$$
$$\qquad\Longrightarrow\ \text{搜索空间}\ \textbf{不再是一张空白候选表}，\text{而是}\ \textbf{两只具名的角} \Longrightarrow\ \text{下一步可逐一攻角（或判定两角皆为墙）}$$
$$\textbf{候选搜索}：\text{仍未启动候选命名；}\ \text{仅完成形状推导。}$$

## 6. 边界（N1/N2 严守）
$$\text{① 全部结论}\ \textbf{未用 RH}；零数值；\text{未跑 Lean}；\quad\text{② 档案引用（V280／V294-A／V295／V316／V162／V181）}\textbf{未逐行重验}；$$
$$\text{③ 本档}\ \textbf{不引入候选机制}（\text{纪律：候选须从第一行证明非旧类）；}\quad\text{④ 角 I／角 II 的划分为}\ \textbf{定义决策}（\text{依 C1／C8 两条源头}）。}$$

## 7. 净产出
$$\text{(i) }\textbf{E4-3-A 小定理}：\text{C1}\Longrightarrow V_X\ \text{不可能只依赖零点集（严格）；}$$
$$\text{(ii) C1 的形状推论}\ \to\ \text{"零点上的非显式公式型算术结构"} \to\ \textbf{V280／V294-A 墙}；$$
$$\text{(iii) C8 的诚实语义}\ \to\ \text{"区域型}\to\text{线型的强度升级"} \to\ \textbf{V316}\ C^{\star}／\text{V162 墙}；$$
$$\text{(iv) ⭐ 结构性收获：}\textbf{两个独立推导的缺口重合于已测绘墙}；$$
$$\text{(v) 搜索空间显式化为}\ \textbf{两只具名的角}（\text{角 I／角 II}），\text{且仍未命名候选。}$$
