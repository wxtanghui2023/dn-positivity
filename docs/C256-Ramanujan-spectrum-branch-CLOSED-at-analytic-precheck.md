已查地图（**先查后写**）：`C255`（B2-ARITH 预检：四要求↔四墙）、`C159`/`C191`/`C192`（κ_N 定理）、`V188`（四通道穷尽＋饱和判据）、`V237-D`。关键词回查：`Ramanujan 谱分支`=0、`单位群指示谱`=0（**均本档新增**）。

D0: 本档对象 = **C-256：Ramanujan 和谱分支的解析预检闭合（含第一代非线性族）** —— 关系 = 预检判定（不立项）
D1: 0
FREEZE-ACK: 本档即冻结期内的解析预检与判定（依 §8.1；不产候选结论）

---

## §0 结论

$$\boxed{\textbf{① 唐先生的谱计算正确}✓✓（两法互验）：\widehat{c_q}(k)=\sum_n c_q(n)e^{-2\pi ikn/q}=q\cdot 1_{(\mathbb Z/q\mathbb Z)^\times}(k)✓✓}$$
$$\boxed{\textbf{② 素数}\ q：\widehat{c_q}(0)=0,\ \widehat{c_q}(k)=q\ (k\ne0)✓ \Longrightarrow \textbf{谱在单位上完全等高，无细结构}✗✓}$$
$$\boxed{\textbf{③ 结构性（}\forall q✓，非 q=13 数值破裂）：\forall q,\ \widehat{c_q}=q\cdot 1_{\text{units}}✓ \Longrightarrow \textbf{Euler／单位群结构的 Fourier 重编码}✗✓}$$
$$\boxed{\textbf{④ 判词}✓✓：\textbf{Ramanujan-spectrum branch: CLOSED at analytic pre-check.}✗✓\（\text{第四要求信息增益为零}✓）}$$
$$\boxed{\textbf{⑤ 本档增益}✓✓：\textbf{第一代非线性族【也当场闭合}】✗✓（纯解析，}\forall q✓）$$

## §1 谱计算复核（两法互验 ✓✓）

$$\text{法一（直接交换求和}✓）：\widehat{c_q}(k)=\sum_{a\in(\mathbb Z/q\mathbb Z)^\times}\sum_{n\bmod q}e^{2\pi i(a-k)n/q}=q\cdot[k\in(\mathbb Z/q\mathbb Z)^\times]✓✓$$
$$\text{法二（指示函数分解}✓）：c_q(n)=q\cdot[q\mid n]-1\ ✓ \Longrightarrow \widehat{c_q}(k)=q\cdot1-0=q\ (k\ne0)✓,\quad \widehat{c_q}(0)=q-q=0✓✓$$
$$\qquad \text{两法结果一致}✓✓ \Longrightarrow \textbf{唐先生结论确认}✓✓（\text{且}\ \forall q\ \text{成立}✓，\text{非仅素数}✓）$$

## §2 为何第四要求当场失败（结构理由 ✓✓）

$$\text{第四要求}✓：\text{算术数据}\to\text{有限谱}\to\text{谱极值/零分离}\to\textbf{反推出超出原有算术标签的新信息}✗$$
$$\qquad \text{实际}✓：c_q\overset{\mathrm{DFT}}{\longrightarrow}q\cdot1_{\text{units}}✓ \Longrightarrow \text{频谱【存在}】✓、\text{来源【自然}】✓、\text{【可逆}】✓$$
$$\qquad \qquad \textbf{但谱内部无新细结构}✗：\text{非零频率全部等高}✗；\text{「极值」无定位信息}✗；\text{「零分离」仅识别}\ k=0\ \text{与}\ k\ne0✗$$
$$\qquad \qquad \text{而}\ k=0\ \text{与}\ k\ne0\ \text{之分【正是单位群的平凡 Fourier 支撑信息}】✗✓ \Longrightarrow \textbf{信息增益为零}✓$$
$$\Longrightarrow \boxed{\text{判死理由不是「实验没看到信号」✗，而是【DFT 完全显式}】✓ \Longrightarrow \text{谱只记住}\ (\mathbb Z/q\mathbb Z)^\times✗✓}$$
$$\qquad \textbf{这比跑}\ q=13,17,19,\dots\ \text{更干净}✓✓（\forall q\ \text{一次到位}✓）$$

## §3 ⭐ 本档增益：第一代非线性族也当场闭合（纯解析 ✓✓）

$$\textbf{对象甲}✓：c_q(n)c_q(n+h)\ \（\text{素数}\ q\ ✓）=\begin{cases}(q-1)^2,&q\mid n\ \text{且}\ q\mid n+h\\ -(q-1),&\text{恰一个整除}\\ 1,&\text{皆不整除}\end{cases}✓$$
$$\qquad q\mid h \Longrightarrow \text{仅依赖}\ [q\mid n]✓；\qquad q\nmid h \Longrightarrow \text{仅依赖}\ (n\bmod q)✓$$
$$\qquad \Longrightarrow \boxed{\text{乘积【只依赖}\ n\bmod q]✓ \Longrightarrow \text{其谱＝周期}\ q\ \text{指示函数的 DFT}\Longrightarrow \textbf{落在门槛内}✗✓}$$
$$\textbf{对象乙}✓：\bigl|\widehat{c_qf}(k)\bigr|^2=q^2\bigl|\sum_{a\in\text{units}}\hat f(k-a)\bigr|^2✓\ \text{只涉单位群}✓ \Longrightarrow \text{同上}✗✓$$
$$\textbf{对象丙}✓：\sum_n c_q(n)c_q(n+h)W(n)=\sum_{r\bmod q}(\text{常值})\sum_{n\equiv r}W(n)✓ \Longrightarrow \textbf{无跨尺度耦合}✗✓$$
$$\Longrightarrow \boxed{\textbf{第一代非线性族全部当场 CLOSED}✗✓（\text{按唐先生预注册门槛}✓）}$$

## §4 门槛的正式形式（本档固化 ✓✓）

$$\boxed{\text{硬门槛}✓：\text{若新谱量最终只化成}\ \gcd/\text{单位群}/\text{Euler 因子}\ \Longrightarrow \textbf{立即 CLOSED}✗✓}$$
$$\qquad \text{理由}✓：\text{否则很容易再次掉回已封的}\ \textbf{KILL-2}：\text{乘性结构回归 Euler}✗✓$$
$$\textbf{正向刻画}✓（\text{唐先生提议}✓）：\text{需要【有自然算术来源、但 Fourier 化后仍保留非平凡跨尺度耦合}】\ \text{的对象}✓$$
$$\qquad ⚠️\ \textbf{诚实提示}✗✓：\text{该正向刻画与}\ \texttt{V188}\ \text{的六条原型要求【同形}】✓（\text{非局部／跨尺度／有 arithmetic origin／非人为 RH 等价／\dots}✓）$$
$$\qquad \qquad \Longrightarrow \textbf{该 spec 已在档}✓，\text{且}\ \texttt{V188}\ \text{的四通道穷尽表自注为【任何未来提案的第一道分类器}】✓✓$$
$$\qquad \qquad \text{依}\ \texttt{C-116}：\text{此提示【不构成否决}】✓，\text{仅登记为「spec 回到原型」✓}$$

## §5 边界

$$\textbf{① 本档为解析预检判定}✓，\text{不立项}✗、\text{不产候选结论}✗；\textbf{② 未跑数值}✓（\text{遵唐先生「先做解析预检」✓}）$$
$$\textbf{③ 未用 RH}✓；\text{未改他档}✓；\textbf{④ 不声称整条「算术}\to\text{有限谱」路线不可能}✗（\text{只判 Ramanujan 谱分支与其第一代非线性族}✓）$$
$$\textbf{⑤ 本档为本周【第五次}】\text{「把提议翻译成档案词汇再先搜索」救下的坑}✓✓$$

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 Ramanujan谱分支      命中文件数=1 :: ./C256-Ramanujan-spectrum-branch-CLOSED-at-analytic-precheck.md
技术词 单位群指示谱         命中文件数=1 :: ./C256-Ramanujan-spectrum-branch-CLOSED-at-analytic-precheck.md
技术词 第一代非线性族       命中文件数=1 :: ./C256-Ramanujan-spectrum-branch-CLOSED-at-analytic-precheck.md
```
⚠️ 各 1 命中且均为本档自身 ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓
