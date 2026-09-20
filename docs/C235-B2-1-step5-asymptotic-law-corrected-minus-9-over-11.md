已查地图（**先查后写**）：查 `C-234`（B2-1 框架 + w→∞ leading 结构）、`C-233`（审计条款）、`C-193`/`C-199`（w=1,2 锚点）。回查见 §7 ✓

D0: 本档对象 = **B2-1 Step 5：$w\to\infty$ 渐近律的严格化与【纠正】**（含唐先生 degree-9 闭包的复核＋一个被伪证测试否定的候选＋正确结果）—— 关系 = 解析结果
D1: 0
FREEZE-ACK: 本档即冻结期内的解析推导与登记（依 §8.1；不产候选结论）

---

## §0 ⭐ 三行结论

$$\boxed{\textbf{① 唐先生的 degree-9 代数闭包：复核【全部通过}】✓✓\ \text{（但它是【归约问题】的常数，不是 }g_w\ \text{的 }O(1)\ \text{项}✗）}$$
$$\boxed{\textbf{② 候选 }C_\infty=-0.9757647554\ldots\ \textbf{被伪证测试【否定}】✗✗\ \text{（diff}\to+0.1624\neq0✗）}$$
$$\boxed{\textbf{③ 正确结果}✓✓：g_w(10)=w\kappa_{10}-\tfrac9{11}-\tfrac{\kappa_{10}}2\bigl(\tfrac{2}{11\sin\theta_0}\bigr)^2\tfrac1w+O(w^{-2})✓\ \text{（常数【有理}】-\tfrac9{11}=-0.81818\ldots✓）}$$

## §1 唐先生 degree-9 闭包的独立复核（全部通过 ✓）

$$\text{临界方程}\ \sin\varphi+10\sin10\varphi=0✓\ \text{与}\ \sin10\varphi=\sin\varphi\,U_9(\cos\varphi)✓ \Longrightarrow 10U_9(x)+1=0✓,\ x=\cos\varphi✓$$
$$U_9(x)=512x^9-1024x^7+672x^5-160x^3+10x✓\（\text{sympy 逐项相同}✓\）$$
$$\Longrightarrow 5120x^9-10240x^7+6720x^5-1600x^3+100x+1=0✓✓$$
$$\text{数值}：x^*=\cos\varphi^*=-0.9519981185245958239673✓\ \text{（与唐先生给值一致}✓）；\text{多项式在 }x^*\ \text{处}=9.37\times10^{-23}✓$$
$$\text{不可约}✓：\texttt{sympy.factor}\ \text{返回原式}✓ \Longrightarrow [\mathbb Q(x^*):\mathbb Q]=9✓✓$$
$$T_{10}(x)=512x^{10}-1280x^8+1120x^6-400x^4+50x^2-1✓ \Longrightarrow C_\infty=\tfrac{x^*+T_{10}(x^*)}2=-0.975764755408187787121321380217✓$$
$$\qquad（\text{与唐先生给值一致}✓）；\text{其 9 次多项式在 }C_\infty\ \text{处}=1.45\times10^{-33}✓\ \text{且不可约}✓$$
$$\textbf{额外教训}✓（\text{PSLQ 假阴性的【第二个】原因}✗）：C_\infty\ \text{多项式系数最大}\ 2.6\times10^{15}✓ > \text{我设 maxcoeff}=10^{12}✗$$
$$\qquad \Longrightarrow \text{即使次数够也找不到}✓ \Longrightarrow \textbf{规则}：\text{PSLQ 的 maxcoeff 必须} \ge \text{目标系数量级}✓$$

## §2 ⚠️ 但伪证测试**否定了** $C_\infty$ 作为 $O(1)$ 项（关键 ✗）

$$\text{测试}：\text{比较}\ g_w\ \text{与}\ w\kappa_{10}+C_\infty✓\ \text{（网格+细化，属【伪证测试】非扫描✓）}$$
```
   w        g_w              w·κ+C_∞          diff        φ1/π      φ2/π
  50    41.108319535529   41.086911886151  +2.141e-02  0.3635757  0.1757950
 200   167.324293444781  167.274941810828  +4.935e-02  0.3636008  0.1666641
 500   419.807904195657  419.651001660182  +1.569e-01  0.1816052  0.9989998
10000 8411.722003927445 8411.559563556404  +1.624e-01  0.1818072  0.9999971
```
$$\Longrightarrow \text{diff}\to+0.1624\neq0✗✗ \Longrightarrow \textbf{C}_\infty\ \text{不是 }g_w\ \text{的 }O(1)\ \text{项}✗$$
$$\textbf{诊断}✓✓：\varphi_2/\pi\to0.9999971\to1✓ \Longrightarrow \textbf{最优点} \varphi_2\to\pi✓ \Longrightarrow \text{此时}\ \cos\varphi_2=-1✓ \Longrightarrow k=1\ \text{不再绑定}✗$$
$$\qquad \Longrightarrow \text{C-234 §3 的"leading active set}=\{1,10\}"\ \text{前提在该 regime 失效}✗✓$$

## §3 ⭐ 归约中的两处修正（本档给出 ✓）

$$\textbf{修正 A}✓（\text{代数滑步}✗）：\text{两分支的扰动系数是}\ \cos(\theta_0+\varepsilon)=\kappa-\sin\theta_0\varepsilon✓\ \text{与}\ \cos10(\theta_0+\varepsilon)=\kappa+10\sin\theta_0\varepsilon✓$$
$$\qquad \text{即}\ (-1,\ +10)✓\ \textbf{不是}\ (\mp\tfrac{11}2,\pm\tfrac{11}2)✗ \Longrightarrow \text{消 }a\ \text{给}\ C=\frac{10\cos\varphi_2+\cos10\varphi_2}{11}✓\ \textbf{而非}\ \frac{\cos\varphi_2+\cos10\varphi_2}2✗$$
$$\textbf{修正 B}✓（\text{更根本}✗）：\text{在}\ \varphi_2=\pi\ \text{时} k=1\ \text{分支被}\ -1\ \text{压低}⟹ \textbf{绑定对变为}\ \{k=1\ \text{（}\cos\varphi_2=-1\text{）}\ \text{与}\ k=10\ \text{（}\cos10\varphi_2=+1\text{）}\}✓✓$$
$$\qquad \text{tie}：w\cos\varphi_1-1=w\cos10\varphi_1+1⟹ w[\cos\varphi_1-\cos10\varphi_1]=2✓✓$$

## §4 ⭐⭐ 正确结果（解析 ＋ 数值双重确认 ✓✓）

$$\text{写}\ \varphi_1=\theta_0+\varepsilon✓,\ \text{展开}：\cos\varphi_1-\cos10\varphi_1=-11\sin\theta_0\,\varepsilon+\tfrac{99\kappa}{2}\varepsilon^2+O(\varepsilon^3)✓$$
$$\text{tie}\Longrightarrow w\bigl[-11\sin\theta_0\varepsilon+\tfrac{99\kappa}2\varepsilon^2\bigr]=2✓ \Longrightarrow \varepsilon=\frac{a}{w}✓,\ a=-\frac{2}{11\sin\theta_0}+O(w^{-1})✓✓$$
$$\text{取值}\ V=w\cos\varphi_1-1=w\kappa-a\sin\theta_0-\frac{\kappa a^2}{2w}-1+O(w^{-2})✓$$
$$\Longrightarrow \boxed{\ g_w(10)=w\kappa_{10}-\frac9{11}-\frac{\kappa_{10}}2\Bigl(\frac{2}{11\sin\theta_0}\Bigr)^2\frac1w+O(w^{-2})\ }✓✓$$
$$\qquad \frac9{11}=0.8181818\ldots✓\（\textbf{有理常数}✓✓）；\ \frac{\kappa_{10}}2\bigl(\tfrac2{11\sin\theta_0}\bigr)^2=0.0475907\ldots✓$$

**数值确认（固定 $\varphi_2=\pi$ 的一维问题，非网格扫描 ✓）**：
```
   w       g_w(φ2=π)         w·κ−9/11           diff         φ1/π
   50    41.235883945583   41.244494823377  -8.611e-03   0.17976833
  100    83.302653660528   83.307171464936  -4.518e-03   0.18077162
 1000   840.434877822778  840.435351012999  -4.732e-04   0.18171138
10000  8411.717098946834 8411.717146493631 -4.755e-05   0.18180748
50000 42061.858450227439 42061.858459740877 -9.513e-06  0.18181604
```
$$\Longrightarrow \text{diff}\cdot w\approx-0.04755\ \text{恒定}✓✓ \Longrightarrow \text{与解析 }1/w\ \text{系数}-0.0475907\ \textbf{吻合到 4 位}✓✓$$
$$\textbf{且}\ \varphi_1\ \text{的预测}\ \theta_0-\frac{2}{11\sin\theta_0}\frac1w\ \text{独立得到确认}✓✓：$$
$$\qquad w=10000：\text{实测}\ 0.1818074795✓\ \text{预测}\ 0.1818074770✓\ \text{差}+7.9\times10^{-9}✓✓$$
$$\qquad w=50000：\text{实测}\ 0.1818160410✓\ \text{预测}\ 0.1818160409✓\ \text{差}+3.2\times10^{-10}✓✓（\text{比值}\sim1/w^2✓✓）$$

## §5 与 $C_\infty$ 的关系（诚实说明 ✓）

$$C_\infty\ \text{是【归约问题}\ \inf_{a,\varphi_2}\max\{\cdots\}\ \text{的常数}✓\ \text{—— 该归约假设两项系数为}\ \mp\tfrac{11}2✗（\text{见 §3 修正 A}✓）$$
$$\qquad \text{若改用真实系数}\ (-1,+10)✓\ \text{并允许}\ \varphi_2\ \text{自由}✓，\text{得}\ \min_{\varphi_2}\frac{10\cos\varphi_2+\cos10\varphi_2}{11}✓\ \text{—— 但该 min 与最优点}\ \varphi_2=\pi\ \text{不符}✗$$
$$\qquad \text{因}\ \varphi_2\neq\pi\ \text{会改变【绑定结构】}✓，\text{故"先消 }a\text{ 再对 }\varphi_2\text{ 取 min"不合法}✗✓$$
$$\Longrightarrow \textbf{结论}✓：\varphi_2=\pi\ \text{处的最优值}\ -\frac9{11}\ \textbf{才是正确的 }O(1)\ \text{常数}✓✓，\text{且它【有理}】✓$$

## §6 状态与剩余

$$\textbf{已确立}✓：g_w=w\kappa_{10}-\tfrac9{11}-\tfrac{\kappa_{10}}2\bigl(\tfrac2{11\sin\theta_0}\bigr)^2\tfrac1w+O(w^{-2})✓（\text{数值确认到 }w=5\times10^4✓）$$
$$\textbf{已否}✗：C_\infty\ \text{作为 }O(1)\ \text{项}✗；\text{"leading active set 恒为 }\{1,10\}✗"；\text{C-234 §3 的 }\varphi_2=\pi\ \text{"会破坏 tie"判断}✗$$
$$\textbf{未证}✗（下一步 ✓）：\text{① 严格证明最优点确实}\ \varphi_2\to\pi✓；\text{② 证明绑定对}\ \{1,10\}\ \text{在该 regime 恒成立}✓；\text{③ 把渐近律做【双边夹住}】✓$$
$$\qquad \text{③ 的路线}✓：\text{上界＝给出显式构型}\ (\varphi_1^*,\pi)✓；\text{下界＝对【其余 9 个分支】给出一致压低估计}✓$$

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 绑定对切换         命中文件数=1  ::  ./C235-B2-1-step5-asymptotic-law-corrected-minus-9-over-11.md
技术词 有理渐近常数       命中文件数=1  ::  ./C235-B2-1-step5-asymptotic-law-corrected-minus-9-over-11.md
技术词 系数上限假阴性     命中文件数=1  ::  ./C235-B2-1-step5-asymptotic-law-corrected-minus-9-over-11.md
```
⚠️ 实测各 1 命中且均为本档自身（检查在落档后执行）✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）

## §8 边界

$$\textbf{① 未用 RH}✓；\text{未改他档}✓；\textbf{② 数值层}：§2 的网格比较为【上界】✓，§4 的一维搜索为结构化验证✓，\text{均非证明}✗$$
$$\textbf{③ 不漏写}：\text{唐先生的 degree-9 闭包自身【正确且已验证}✓（\text{只是与 }g_w\ \text{的渐近无关}✓）$$
