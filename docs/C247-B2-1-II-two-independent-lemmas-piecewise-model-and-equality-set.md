已查地图（**先查后写**）：查 `C-246`（两缺口）、`C-245`（常数链＋三阶界）、`C-244`（恒等式）、`C-243`（一维归约）。回查见 §6 ✓

D0: 本档对象 = **C-247：两个严格独立 Lemma（A 精确分段二次模型／B 完整等号集）** —— 关系 = 缺口补齐
D1: 0
FREEZE-ACK: 本档即冻结期内的推导与判定（依 §8.1；不产候选结论）

---

## §0 结论

$$\boxed{\textbf{Lemma A}✓✓：\text{两支二阶系数【全部为凸}】✓✓（\text{五个 }j\ \text{无一例外}✓） \Longrightarrow \text{极小【完全闭式}】✓✓}$$
$$\boxed{\textbf{Lemma B}✓✓：\text{完整等号集}\ \mathcal E=\{0\}\cup\{y_0\}=\{0,\tfrac{2\pi m}{11}\}✓✓\ \textbf{【只有两个点}】✓✓}$$
$$\boxed{\textbf{纠正我自己的预判}✗✓：\text{"两支可能有凹支"}\ ✗ \Longrightarrow \text{实测【全凸}】✓✓（\text{故极小只需顶点＋边界}✓）}$$
$$\boxed{\textbf{诚实}✗：\text{分段模型【单独】不是下界}✗（\text{差}\sim10^{-4}\text{–}10^{-3}✓） \Longrightarrow \text{必须带 C-245 的三阶余项}✓✓}$$

## §1 Lemma A：精确分段二次模型（本档 ✓✓）

$$M_{2,j}(\eta,\zeta)=\varrho_j\eta+\tfrac{r_{2,j}}2\eta^2+\bigl|\zeta+\upsilon_j\eta+\tfrac{q_{2,j}}2\eta^2\bigr|✓$$
$$\text{按绝对值内部符号分两支}✓（A(\eta):=\zeta+\upsilon\eta+\tfrac{q_2}2\eta^2✓）：$$
$$\qquad S_\pm=\varrho\eta+\tfrac{r_2}2\eta^2\pm A(\eta)=\pm\zeta+(\varrho\pm\upsilon)\eta+\tfrac{r_2\pm q_2}2\eta^2✓✓$$
$$\qquad \text{顶点}\ \eta^*_\pm=-\dfrac{\varrho\pm\upsilon}{r_2\pm q_2}✓✓\qquad \text{区域}\ \pm A(\eta)\ge0✓（\text{二次不等式，显式}✓）$$
$$\Longrightarrow \boxed{\min_\eta M_{2,j}=\min\Bigl\{\min_{\mathcal R_+}S_+,\ \min_{\mathcal R_-}S_-\Bigr\}}✓✓$$

$$\textbf{本档实测}✓✓：\textbf{两支二阶系数全部为凸}✗✓（\text{纠正预判}✓）：
```
   j=1 d=-4.5 : (r₂+q₂)/2=+47.975 凸 │ (r₂−q₂)/2=+0.480 凸
   j=2 d=-0.5 : +17.271 凸          │ +11.994 凸
   j=3 d=-1.5 : +23.508 凸          │ +7.676 凸
   j=4 d=-2.5 : +30.704 凸          │ +4.318 凸
   j=5 d=-3.5 : +38.859 凸          │ +1.919 凸
```
$$\Longrightarrow \textbf{极小完全闭式}✓✓：\min=\min\bigl\{\text{可行顶点值},\ A(\eta)=0\ \text{边界值}\bigr\}✓✓$$
$$\qquad（\text{因两支凸}✓，\text{极小或在内点（顶点）或在区域边界}A=0✓；\text{且边界上}S_+=S_-✓✓）$$
$$\qquad \Longrightarrow \textbf{piecewise quadratic/rational 显式公式}✓✓（\text{非数值极小化}✓，\text{满足唐先生要求}✓）$$

$$\textbf{⚠️ 但}✗：\text{模型【单独】不等于下界}✗ —— \min_\zeta[\tilde\Psi-\text{分段模型}]=-1.0\times10^{-4}\sim-9.8\times10^{-4}✗$$
$$\qquad \text{差值量级}\sim10^{-4}\text{--}10^{-3}✓ \Longrightarrow \textbf{恰为三阶量级}✓✓ \Longrightarrow \text{必须使用带余项的形式}✓✓：$$
$$\qquad \tilde\Psi_j(\zeta)\ \ge\ \min_\eta\bigl[M_{2,j}(\eta,\zeta)-(C_q+C_r)|\eta|^3\bigr]✓（\text{C-245}✓，C_q=C_r=\tfrac{(\frac{11}2+|d|)^3}6✓）$$

## §2 Lemma B：完整等号集（本档 ✓✓）

$$\mathcal E:=\{y\in[0,\pi]:r(y)=0\ \text{且}\ q(y)=0\}✓,\qquad q(y)=\sin\tfrac{11y}2\sin(dy)✓,\quad r(y)=c_0+\cos\tfrac{11y}2\cos(dy)✓$$
$$\textbf{显式求解}✓：q(y)=0 \iff \sin\tfrac{11y}2=0\ \text{或}\ \sin(dy)=0✓$$
$$\qquad \text{族 1}：\tfrac{11y}2=\pi m\Longrightarrow y=\tfrac{2\pi m}{11}✓；\text{再要求}\ c_0+(-1)^m\cos(\tfrac{2\pi md}{11})=0✓$$
$$\qquad \text{族 2}：dy=\pi l\Longrightarrow y=\tfrac{\pi l}d✓；\text{再要求}\ c_0+\cos(\tfrac{11\pi l}{2d})(\pm1)=0✓$$
$$\textbf{枚举结果}✓✓（\text{五个 }j\ \text{均为}✓）：$$
```
   j=1 (d=-4.5): |E|=2   位置/π = 0.000000, 0.909091  (= 2π·5/11)
   j=2 (d=-0.5): |E|=2               0.000000, 0.181818  (= 2π·1/11)
   j=3 (d=-1.5): |E|=2               0.000000, 0.727273  (= 2π·4/11)
   j=4 (d=-2.5): |E|=2               0.000000, 0.363636  (= 2π·2/11)
   j=5 (d=-3.5): |E|=2               0.000000, 0.545455  (= 2π·3/11)
```
$$\Longrightarrow \boxed{\mathcal E=\{0,\ y_0\}✓✓\ \textbf{【只有两个点}】✓✓}\qquad（\text{故远区只需排除【两个】邻域}✓✓）$$
$$\qquad \textbf{这纠正了 C-246 三的担心}✗✓：\text{当时以为等号集是整条 11-格}✗（\text{因只固定}\ y_0\ \text{未枚举}✓） \Longrightarrow \textbf{实为两点}✓✓$$

## §3 结构纪律（唐先生指定 ✓）

$$\textbf{不假设数值同构}✗，\text{只证【同结构公式}】✓：\text{实测五个 }j\ \text{的}\ \varrho,\upsilon\ \text{符号【相同}】✓（\text{均正}✓），$$
$$\qquad \text{但}\ d\ \text{不同}✓ \Longrightarrow r_2,q_2\ \text{不同}✓ \Longrightarrow \textbf{数值模型不同}✓✓（\text{须逐 }j\ \text{给出}✓）$$
$$\qquad \text{而结构公式}\ \lambda=\varrho\tau/\upsilon✓（\text{C-244}✓）\ \text{与}\ \eta^*_\pm=-\tfrac{\varrho\pm\upsilon}{r_2\pm q_2}✓\ \text{同型}✓✓ \Longrightarrow \textbf{机械可复制}✓✓$$

## §4 状态

| 项目 | 状态 |
|---|---|
| Lemma A（分段二次模型，全凸，闭式极小） | ✓✓ **本档完成** |
| Lemma B（完整等号集 = 两点） | ✓✓ **本档完成** |
| 模型单独为下界 | ✗ 否（须带三阶余项，已明示） |
| 远区 gap（须 ≥ $\zeta_{max}=0.2974$） | ⬜ 待定（现在只需处理两个邻域） |
| 每等号点局部 Taylor（同结构） | ⬜ 待补（机械） |
| Case II | ⬜ 尚未盖章 |
| Case I 严格常数版 | ✗ |

$$\textbf{本档价值}✓✓：\text{两缺口各得一个干净 Lemma}✓✓ \text{；A 给出闭式极小}✓✓\text{；B 把等号集从担心是无穷多降到恰好两点}✓✓$$

## §5 遗留与下一步

$$\textbf{遗留 1}✓：\text{远区 gap 阈值问题}✗✓：\text{要求}\ r+|q|\ge\zeta_{max}=0.2974✓\text{，而近等号点处 gap 线性增长（斜率}\sim0.28✓\text{）}$$
$$\qquad \Longrightarrow \text{需}\ \delta\sim1.06✓\text{，而两等号点间距}\sim0.29\text{--}2.86✓ \Longrightarrow \textbf{邻域可能重叠}✗✓ \Longrightarrow \text{远区须用带耦合的处理}✓✓（\text{不能只用}\delta_*✓）$$
$$\textbf{遗留 2}✓：\text{把 A 的闭式极小与 C-245 三阶余项合并，得显式}\ L_j(\zeta)✓✓$$
$$\textbf{下一步}✓：\text{（i）给两等号点的局部 Taylor（同结构}✓\text{）；（ii）远区改用}\Phi=r+|\zeta+q|\ \text{的精确下界}✓（\text{含耦合}✓）$$

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 分段二次全凸闭式     命中文件数=1  ::  ./C247-B2-1-II-two-independent-lemmas-piecewise-model-and-equality-set.md
技术词 等号集两点枚举       命中文件数=1  ::  ./C247-B2-1-II-two-independent-lemmas-piecewise-model-and-equality-set.md
技术词 邻域重叠阈值         命中文件数=1  ::  ./C247-B2-1-II-two-independent-lemmas-piecewise-model-and-equality-set.md
```
⚠️ 实测各 1 命中且均为本档自身 ✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）
