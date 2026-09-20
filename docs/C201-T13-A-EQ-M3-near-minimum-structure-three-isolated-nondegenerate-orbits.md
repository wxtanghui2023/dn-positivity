已查地图（**先查后写**）：查 `C-161`（M=3 局部单纯形签名）、`C-176`（上界）、`C-178`（下界 0.75）、`C-195`（下界 0.76）、`C-200`（T13-B2 等号集）。回查见 §5 ✓

D0: 本档对象 = **T13-A-EQ 第一刀**：$M=3$（窗口 $5M=15$）**近极小层的几何类型判别**（候选轨道 ＋ active set ＋ 梯度秩 ＋ 严格正凸组合 ＋ 二阶方向）—— 关系 = 结构定位（不预设等号集）
D1: 0
FREEZE-ACK: 本档即冻结期内的收束与登记（依 §8.1；不产候选结论）

---

## §0 ⚠️ 先纠一处载重细节（唐先生命题里的窗口）

$$\text{唐先生写}\ M=3\ \text{用}\ k\le10✗\ ——\ (\text{RP}_M)\ \text{的窗口是}\ 5M✓ \Longrightarrow M=3\ \text{应为}\ \boxed{k\le15}✓✓$$
$$\qquad \text{用}\ k\le10\（=3.33M）\ \text{是}\ \textbf{另一个问题}✓（\text{旧扫描}：M{=}3\ \text{时}\ W{=}3M\to0,\ W{=}5M\to0.777,\ W{=}10M\to1.201✓）$$
$$\qquad \text{本档全部按}\ \boxed{k\le5M=15}✓\ \text{执行}✓$$

## §1 数据（Phase A/B：$80^3$ 网格 ＋ 550 起点精修 ＋ 模 $S_3$ 聚类）

$$\text{网格（}512{,}000\ \text{点）最小}\ F=0.809016994=\cos36^\circ=\tfrac{1+\sqrt5}{4}✓\ （\text{与}\ \texttt{C-187}\ \text{的无阻尼}M{=}3\ \text{值一致}✓）$$
$$\text{精修后最佳}\ F=\mathbf{0.7640811032}✓（22/550\ \text{起点命中}✓，\text{与}\ \texttt{C-156}\ \text{的}\ 0.764081\ \text{一致}✓）$$
$$\qquad \Longrightarrow \textbf{近极小层存在多个局部极小簇}✓（\text{模}\ S_3\ \text{去重后 51 簇，值域}\approx[0.7641,\ 0.7773]✓）$$

## §2 ⭐ Phase C：四类判别（活动容差 $\mathrm{tol}=10^{-5}$；LP 已修正）

| # | $F(x)$ | active $A$ | $\vert A\vert$ | $\mathrm{rank}(\Delta)$ | $\lambda_{\min}$（LP） | $c$ | 局部极小？ | **分类** |
|---|---|---|---|---|---|---|---|---|
| **0** | $\mathbf{0.7640811032}$ | $\{1,5,11,13\}$ | **4** | **3** | $\mathbf{+2.605\times10^{-2}}$ | $\mathbf{+0.560385}$ | **是 ✓** | **A. 孤立非退化** ✓✓ |
| 1 | $0.7642588835$ | $\{1,5,13\}$ | 3 | 2 | none | $-0.7508$ | 否 ✗（可降 $5.6\times10^{-5}$） | 伪簇 ✗ |
| 2 | $0.7692448616$ | $\{1,11,13\}$ | 3 | 2 | none | $-0.8165$ | 否 ✗（可降 $5.2\times10^{-3}$） | 伪簇 ✗ |
| **3** | $\mathbf{0.7755338917}$ | $\{2,7,10,15\}$ | **4** | **3** | $\mathbf{+5.648\times10^{-2}}$ | $\mathbf{+1.250005}$ | **是 ✓** | **A. 孤立非退化** ✓✓ |
| 4 | $0.7757131181$ | $\{2,10,15\}$ | 3 | 2 | none | $-1.608$ | 是（但 KKT 失败 ✗ ⟹ 存疑） | D/待核 ⚠️ |
| **5** | $\mathbf{0.7768817151}$ | $\{1,3,13,15\}$ | **4** | **3** | $\mathbf{+3.808\times10^{-2}}$ | $\mathbf{+0.755066}$ | **是 ✓** | **A. 孤立非退化** ✓✓ |
| 6–11 | $0.7769\sim0.7772$ | 均 $\vert A\vert=3$ | 3 | 2 | none | $-0.73\sim-2.30$ | 否 ✗（可降 $3\times10^{-5}\sim4\times10^{-4}$） | 伪簇 ✗ |

$$\textbf{判别标准（唐先生四分类）}：\text{A}=\{|A|=M+1=4,\ \lambda_{\min}>0,\ c>0,\ \mathrm{rank}(\Delta)=M=3\}✓；\text{D}=\{|A|\le M\ \text{或}\ c\le0\}✓$$

## §3 ⭐ 结论：$M=3$ 近极小层的几何类型

$$\boxed{\ \textbf{类型 A（孤立非退化）为主}✓✓\ —— \text{至少}\ \textbf{3 个互不相同的轨道}✓（\text{模}\ S_3\ \text{去重后}）✓\ }$$
$$\qquad \text{三个已确认轨道的值}：0.7640811✓,\ 0.7755339✓,\ 0.7768817✓$$
$$\qquad \text{共同签名}：|A|=M+1=4✓,\ \mathrm{rank}(\Delta)=3\ \text{满秩}✓,\ \lambda_{\min}>0✓（\text{严格正内点}✓）,\ c>0✓$$
$$\qquad \Longrightarrow \textbf{局部一阶刚性机制可用}✓✓（\text{与}\ \texttt{C-161}\ \text{的单纯形签名一致}✓）$$

$$\textbf{二阶方向}：\text{在最佳簇处测}\ dF=F(x+\delta)-F(x)：\ |\delta|=10^{-3}\to\min dF=+5.78\times10^{-4}✓；10^{-2}\to+7.07\times10^{-3}✓$$
$$\qquad \text{线性系数}\approx0.578\to0.707✓ \Longrightarrow \textbf{线性增长}✓（\text{非二阶平坦}✗） \Longrightarrow \textbf{非退化、非连续族}✓✓$$

$$\textbf{未发现类型 C（连续族）的证据}✓；\textbf{未发现} \text{单一轨道结构}✗（\text{与}\ M=2\ \text{的"唯一轨道"形成对照}✓）$$

## §4 边界（严格保持）

$$\text{⚠️}\ \textbf{不声称}\ x^{**}\ \text{是全局最小}✗\ —— \text{账本仍只有}\ \boxed{0.76\le m_3\le0.777171}✓（\texttt{C-195}／\texttt{C-176}）✓$$
$$\qquad \text{本档数值最佳}\ 0.7640811\ \textbf{低于} \text{已证上界}\ 0.777171✗ \Longrightarrow \textbf{上界可收紧的机会}✓（\text{把}\ 0.7640811\ \text{的构型做区间认证}✓）$$
$$\qquad \text{所有簇分类均为}\ \textbf{数值}✓；\text{其中"局部极小"用再精修是否下降判定}✓，\text{非严格证明}✗$$
$$\qquad \text{类型 D 中的簇 4：KKT 失败但精修不降}✗ \Longrightarrow \textbf{存疑，标记为待核}⚠️$$
$$\qquad \textbf{未用}\ RH✓；\textbf{未改}\ 他档✓$$

## §5 本档抓到并修掉的四处自我失误

$$\textbf{① 窗口}：\text{唐先生写}\ k\le10✗，\text{应为}\ 5M=15✓ ⟹ \text{已在 §0 纠正}✓$$
$$\textbf{② 活动容差}：\text{首版用}\ 10^{-9}✗ \Longrightarrow \text{最佳簇只识别出}\ A=\{13\}✗ \Longrightarrow \textbf{报出假的}\ c=-0.49<0✗（\text{伪"退化"}）✓$$
$$\qquad \text{改用}\ 10^{-5}\ \text{后}\ A=\{1,5,11,13\}✓,\ c=+0.5404>0✓✓ \Longrightarrow \textbf{结论反转}✓（\text{这是本档最关键的一处修正}）✓$$
$$\textbf{③ LP 公式}：\text{首版把约束写成}\ \sum\lambda_k g_k=t\cdot\mathbf 1✗，\text{应为}\ =0✓ \Longrightarrow \text{LP 全失败（}\lambda_{\min}\ \text{全为 none}）✓ ⟹ \text{已修正}✓$$
$$\textbf{④ 自杀陷阱}：\texttt{pkill -f t13aeq\_...}\ \text{匹配到自身 shell}✗ ⟹ \texttt{SIGTERM}✗（\texttt{TOOLS.md}\ \text{已记录该陷阱}✓）⟹ \text{改用 PID}✓$$
$$\qquad \textbf{教训}：\text{①–③ 均为实现/参数错，非数学错}✓（\text{第}\ 16\text{–}18\ \text{次同类应验}）✓$$

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 近极小层结构   命中文件数=1    ::  ./C201-T13-A-EQ-M3-near-minimum-structure-three-isolated-nondegenerate-orbits.md
技术词 严格正凸组合   命中文件数=1    ::  ./C201-T13-A-EQ-M3-near-minimum-structure-three-isolated-nondegenerate-orbits.md
```
⚠️ 实测各 1 命中且均为本档自身（检查在落档后执行）✓ ⟹ **扣除后 0 命中** ⟹ 两项**本档首次命名** ✓（依 `C-168` §6 惯例）

## §7 下一步（可选分叉，待唐先生定）

$$\textbf{(甲)}\ \text{收紧上界}：\text{把}\ 0.7640811\ \text{构型做区间认证}✓ \Longrightarrow \text{账本}\ [0.76,\ \approx0.7641]✓（\text{廉价}）✓✓$$
$$\textbf{(乙)}\ \text{类型 A 的局部刚性}：\text{对三个已确认簇各做}\ \texttt{C-197}\ \text{式局部引理}✓（\text{签名齐备}✓）✓$$
$$\textbf{(丙)}\ \text{判别"类型 D 簇 4"}：\text{细化容差/换更严的 KKT 检验}✓$$
$$\textbf{(丁)}\ \text{远场证书}：\text{把}\ M=3\ \text{的近极小层做成类似}\ \texttt{C-199}\ \text{的全局证书}✗（\text{因多簇而成本高}⚠️）$$
