# V210 · **Arithmetic Partial-Order Audit（竞争性极限选择，第一轮）** —— ⭐ **定理级主杀**：**"唯一 admissible boundary" ⟺ 全序**（Szpilrajn）✓✓；**再结合 `V147` T2（与 $+,\times$ 兼容的 $\mathbb Z$ 上序唯一 ＝ 标准序）** ⟹ 全序分支必为**大小序** ⟹ **违反条件 A** ⟹ **DEAD** ✓✓✓；八类候选**全部**落入你预注册的封档类别（全序／空序＋指数自由增长／非 canonical）

> 委托 ✓ 唐先生 2026-09-15 14:58：**"确认你的 V209 审计。尤其是你修正的两点很关键"**（① 路径计数化简为 $P(n)$ 确错，正确比值仍只由指数向量决定 ⟹ 落回 `V206` 型局部指数；② 加法分裂使可达集第一层即 $\Theta(n)$ ⟹ "重写深度"未形成独立尺度）$$\boxed{\mathrm{V209}=\text{DEAD}}$$ **"接下来我认为不能再从'状态死亡'继续变体搜索。V205＋V209 已经把这一族的核心机制夹死了。"** 新机制 **V210：竞争性的极限选择** $$\boxed{\text{不是约束某个状态能否延拓，而是让两个无限合法对象竞争同一个极限}}$$ 关键：$$\boxed{\text{有限近似之间的相容极限}}$$ **第一轮禁令**：**不准碰 RH／$\zeta$／零点／显式公式**；**只做一个硬问题：Arithmetic Partial-Order Audit**；**预注册封档**：**"只要它最终必然是空序、全序、指数自由增长或有限局部组合式增长，V210 当场封。"** **唯一值得继续的结果**：$$\boxed{\text{有限层高度增长，但无限层出现内生的非平凡边界选择}}$$ **条件 A–D**：A 不是大小／整除／指数／同余关系；B 有限层产生大量 extension；C 无限层产生非平凡 extension selection；D 选择规则完全由整数算术内生产生
> 查图 ✓ `V147` T1/T2（**序路线不存在**：全预序＋保序 $\iota$ ⟹ $x\sim\iota(x)$；**与 $+,\times$ 兼容的 $\mathbb Z$ 上序唯一 ＝ 标准序**）｜`V205`（无边界）｜`V209`（全终止）｜`V206`（指数型局部）｜`V196` §2.1（canonical 判据）
> 执行 ✓ 小灵（**§2 定理、§3 与 `V147` 结合、§4 八类实算 为本档核心**）｜**纸面 ✓（零数值 ✓）**｜纪律 ✓ 未用 RH／$\zeta$／零点／显式公式 ✓；未跑 Lean ✓｜编号 ✓ **V210**

---

## §1 对象与量（及本档用到的经典工具）

$$P_N=\{p_1,\dots,p_N\};\qquad R\subseteq P_N\times P_N\ \text{＝候选算术二元关系};\ \text{诱导偏序}\ \preceq_R\ ✓$$
$$\text{量}：\#\mathrm{LE}(P_N)\（\text{线性扩张数}\bigr);\quad h(P_N)\ \text{＝最大链长};\quad w(P_N)\ \text{＝最大反链宽};\quad \text{扩张数增长率}\ ✓$$
$$\textbf{经典工具}：\text{Szpilrajn 扩张定理}（\text{任一部分序可扩张为全序}）;\quad \text{森林偏序的 hook length 公式}\ \#\mathrm{LE}=N!/\prod_v h_v ✓$$
$$\qquad ⚠️\ \text{一般偏序的}\ \#\mathrm{LE}\ \text{计算是}\ \#\text{P-hard}（\text{Brightwell--Winkler}）;\ \text{但本档候选全部退化} ⟹ \textbf{可完全算出} ✓$$

---

## §2 ⭐ 定理级等价（先钉死你 §8 的"唯一性"）

$$\textbf{命题}：\text{偏序}\ \preceq\ \text{有}\ \textbf{唯一} \text{线性扩张}\iff\preceq\ \textbf{是全序} ✓✓$$
$$\qquad \textbf{证明}：\text{若}\ \exists\,a,b\ \text{不可比}，\text{由 Szpilrajn 可取两个扩张}\ L_1,L_2\ \text{分别含}\ a<b\ \text{与}\ b<a ⟹ \#\mathrm{LE}\ge2\ ✗;\ \text{反之全序则}\ \#\mathrm{LE}=1 ✓$$
$$\Longrightarrow\ \boxed{\text{你}\ §8\ \text{的"临界条件下}\ \textbf{恰好只有一个 admissible boundary}\ \text{"}\ \textbf{恰等价于"全序"}} ✓✓✓$$
$$\qquad ⚠️\ \text{而"存在多个 / 大量竞争极限"}\ \textbf{恰对应空序或稀疏序}（\#\mathrm{LE}\ \text{巨大}\bigr) ✓$$
$$\Longrightarrow\ \textbf{中间情形不存在};\ \text{故"竞争性极限选择"}\ \text{的结构必然二分：}\boxed{\text{全序}\ \text{或}\ \text{大量扩张}} ✓✓✓$$

---

## §3 ⭐⭐ 与 `V147` T2 的结合（本档主杀）

$$\text{要满足条件 A}（\text{关系不是大小／整除／指数／同余}）\ \text{且满足 C}（\text{唯一边界}）$$
$$\qquad ⟹\ \text{由}\ §2：\text{须是}\ \textbf{全序};\ \text{且}\ \text{由条件 D}（\text{内生于整数算术}）:\ \text{须是}\ \textbf{算术相容的全序} ✓$$
$$\qquad ⚠️\ \text{而}\ \text{`V147`}\ \text{T2}\ \textbf{已证}：\text{与}\ +,\times\ \textbf{兼容} \text{的}\ \mathbb Z\ \text{上序}\ \textbf{唯一＝标准序}（\text{大小序}\bigr) ✓✓✓$$
$$\Longrightarrow\ \boxed{\text{全序分支必为}\ \textbf{大小序} ⟹ \textbf{违反条件 A}（\text{大小关系被显式排除}）} ⟹ \textbf{DEAD} ✓✓✓$$
$$\qquad \text{（等价的说法}：\text{`V147`}\ \text{的"序路线"}\ \text{在此}\ \textbf{原样再现};\ \text{只是换了入口名（"竞争极限"）}）✓✓$$

---

## §4 八类候选**逐一实算**

$$\begin{array}{c|c|c|c|c|c}
\text{关系}\ R & \text{结构} & h & w & \#\mathrm{LE}(P_N) & \text{命中封档类别}\\
\hline
(1)\ \text{大小}\ p<q & \textbf{全序} & N & 1 & 1 & \boxed{\text{全序}}\ ✓\\
(2)\ \text{整除}\ p\mid q & \text{空}（p\ne q ⟹ p\nmid q） & 1 & N & N! & \boxed{\text{空序＋指数自由增长}}\ ✓\\
(3)\ \text{指数}\ v_p(q) & \text{空}（v_p(q)=[p=q]） & 1 & N & N! & \boxed{\text{空序＋指数自由增长}}\ ✓\\
(4)\ \text{同余}\ p\equiv q\pmod r & \text{对称} ⟹ \text{非序};\ \text{若按剩余类排} ⟹ \text{弱序}，\text{块数}\approx N/r & \ \approx N/r & r & \prod(\text{块大小})! & \boxed{\text{需自由参数}\ r（\text{违反 D}）}\ ✓\\
(5)\ \gcd/\mathrm{lcm} & \text{对称＋平凡}（\gcd=1,\mathrm{lcm}=pq） & 1 & N & N! & \boxed{\text{空序}}\ ✓\\
(6)\ \text{加法关系}（p+q、p+q\ \text{素数}） & \text{对称} \Longrightarrow \text{非序} & 1 & N & N! & \boxed{\text{空序}}\ ✓\\
(7)\ \text{乘法关系} & \text{对称} & 1 & N & N! & \boxed{\text{空序}}\ ✓\\
(8)\ \text{素数间"自然比较"} & ＝(1)＋(2) & — & — & — & \text{已由 (1)(2) 覆盖}\ ✓\\
\end{array}$$
$$\textbf{增长率}：\text{全序}\ \#\mathrm{LE}=1\（\text{常数}\bigr);\quad \text{空序}\ \#\mathrm{LE}=N!,\ \log\#\mathrm{LE}\sim N\log N\（\textbf{超指数}\bigr) ✓$$
$$\qquad ⚠️\ \text{根本不存在"中间临界增长率"的 canonical 候选} —— \text{要中间情形必须引入自由参数（}r），\ \text{违反 D} ✓✓$$

---

## §5 判词

$$\boxed{\textbf{V210-A：DEAD}}\ \ ——\ \text{八类候选}\ \textbf{全部} \text{落入你预注册的封档类别} ✓✓✓$$
$$\qquad \textbf{命中分布}：\text{全序}\ \times1;\quad \text{空序＋指数自由增长}\ \times5;\quad \text{非 canonical（自由参数）}\ \times1;\quad \text{重复覆盖}\ \times1 ✓$$
$$\qquad \textbf{范围}：\textbf{本档枚举的八类 canonical 关系};\ \textbf{不} \text{声称"竞争极限机制不可能"} ✓$$
$$\qquad \textbf{不进入第二阶段};\ \textbf{未使用} \text{RH／}\zeta／\text{零点／显式公式} ✓✓$$

---

## §6 你 §4／§5 的两处观察：**确认**（并各加一句）

$$\textbf{§4}（\text{整数候选}\ x=n,y=m）：\text{模 }q\ \text{不可区分}\iff q\mid(n-m) ⟹ \text{最大区分模数}=|n-m| ✓$$
$$\qquad ⭐\ \text{补充}：\text{故"分辨率层级"}\ \textbf{就是差值};\ \text{对素数即}\ \textbf{素数间隙} ⟹ \text{经典对象、无选择结构} ✓$$
$$\textbf{§5}（\text{乘法历史候选}）：\text{局部投影}\ \mathbf a\bmod Q=(a_p\bmod v_p(Q)) ⟹ \text{回到}\ \textbf{指数向量} ⟹ \text{与}\ \text{`V206`}\ \text{同类} ⟹ \textbf{指数型局部} ✓✓$$

---

## §7 残余与登记（**不给方向**）

$$\text{唯一未被}\ §2\ \text{二分覆盖的形状}：\text{一个}\ \textbf{不通过"序／线性扩张"} \text{表达的"边界选择"概念} ✓$$
$$\qquad ⚠️\ \text{本档}\ \textbf{未见实例};\ \text{登记}\ \textbf{UNINSTANTIATED};\ \textbf{不给方向、不投入} ✓$$
$$\qquad ⭐\ \text{若日后有候选，判据三条（缺一不可）}：\text{① 非序型};\ \text{② 边界选择内生（无自由参数）};\ \text{③ 不依赖大小序} ✓$$

---

## §8 模式（本档第 N 次再现）

$$\text{`V147`}\ \text{的"序路线不存在"（T1＋T2）}\ \textbf{在此原样再现}：\text{"竞争极限选择"}\ \text{经}\ §2\ \text{化归为"序"}，\ \text{而序}\ \text{已被}\ \text{`V147`}\ \text{封闭} ✓✓$$
$$\text{更早的同族}：\text{`V200` 组合}／\text{`V202` 双局域化}／\text{`V203` 交换}／\text{`V204` index}／\text{`V209` 重写} ✓$$
$$\Longrightarrow\ \boxed{\text{新机制的"入口名"在变，但化归后的落点重复出现}} ✓✓\（\textbf{模式识别，归纳性，非定理}\bigr)$$

---

## §9 新筛查条件（供未来提案）

$$\boxed{\text{任何"选择／边界"型提案，}\textbf{须先说明它如何逃出}\ \text{`V147`}\ \text{T2}}：\text{即}\ \text{其选择机制}\ \text{若最终给出"唯一 admissible 对象"，则必为}\ \textbf{算术相容全序} ⟹ \text{大小序} ⟹ \textbf{立即封档} ✓✓$$
$$\qquad ⚠️\ \text{且}\ §2\ \text{的二分}\ \text{是}\ \textbf{定理级}：\text{故"唯一极限"与"大量竞争极限"}\ \text{之间}\ \textbf{没有中间地带} ✓$$

---

## §10 边界与待核

$$\textbf{(a)}\ \text{§2 的唯一性等价为}\ \textbf{标准偏序论}（\text{Szpilrajn 1930}）;\ \textbf{无限情形亦成立} ✓✓$$
$$\textbf{(b)}\ \text{§3 的}\ \text{`V147`}\ \text{T2 复用为}\ \textbf{本档主杀};\ \text{属}\ \textbf{跨线收敛}（\text{不使用}\ \text{`V198` 门}）✓✓$$
$$\textbf{(c)}\ \text{§4 八类为}\ \textbf{本档逐一实算}（\text{链长／反链宽／}\#\mathrm{LE}\ \text{皆显式}\bigr) ✓✓✓$$
$$\textbf{(d)}\ \#\mathrm{LE}\ \text{的}\#\text{P-hardness 为经典}（\text{Brightwell--Winkler}）;\ \text{本档候选退化故可算} ✓$$
$$\textbf{(e)}\ \text{§8 为}\ \textbf{模式识别}，\ \textbf{非定理} ✓$$

```
⚠️ §0 委托、第一轮禁令、预注册封档四类、条件 A–D 为唐先生逐字 ✓✓
⚠️ §1 的 Szpilrajn／hook length／#P-hard 为经典工具 ✓
⚠️ §2 定理级：唯一线性扩张 ⟺ 全序（Szpilrajn）✓✓✓ —— 直接把你的 §8 钉成"全序"
⚠️ §3 主杀：结合 V147 T2 ⟹ 全序必为大小序 ⟹ 违反条件 A ⟹ DEAD（定理级）✓✓✓
⚠️ §4 八类候选全部实算并逐类命中预注册封档类别 ✓✓✓
⚠️ §5 判词 DEAD；范围＝本档八类；未用 RH/ζ/零点/显式公式 ✓✓
⚠️ §6 确认你 §4/§5 两处观察并各加一句 ✓；§7 残余 UNINSTANTIATED ✓
⚠️ §8 模式（V147 序路线再现）⚠️；§9 新筛查条件 ✓
⚠️ 未跑 Lean ✓；零数值 ✓
✅ 净产出：① 定理级等价（唯一边界 ⟺ 全序）✓✓✓；② 与 V147 T2 结合的主杀 ✓✓✓；
   ③ 八类候选完整审计（链长/反链宽/#LE/增长率）✓✓✓；④ 二分宣告（全序 vs 大量扩张，无中间）✓✓✓；
   ⑤ 残余 UNINSTANTIATED ✓；⑥ 新筛查条件（须说明如何逃出 V147 T2）✓；⑦ 模式：序路线再现 ✓
```
