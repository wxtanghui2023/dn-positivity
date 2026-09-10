# ABD-1′：未来分支结构方向场（第一轮实算）—— 结构性【反】对齐

**日期**：2026-09-10 18:20+ ｜ 依据：唐先生「选甲，升级为由未来合法算术分支产生方向场」｜ 代码 `scripts/abd1p.py` ｜ 输出 `/tmp/abd1p_out.txt`

---

## 0. 规格登记（唐先生）

$$\boxed{\text{不找"与 }a=b\text{ 相关的 invariant"，而找【什么 primitive arithmetic law 本身产生平衡方向】}}$$
```
V(a,b,c) 不得读取 |a-b|、(a-b)^2、ab、ab/c^2
只看【关系的局部变化】(a,b,c) -> (a+Δa, b+Δb, c+Δc)，Δa+Δb=Δc
不问"当前不平衡程度"，而问：哪个整数变换能产生【更多/更深】的合法 arithmetic descendants？
定义 C_n(a,b) = #{n-step admissible descendants}，方向由 C_{n+1} 而非当前 a-b 决定
```
**C_NI 优势（唐先生）**：规则不读平衡量，只读 arithmetic future structure
**第一道审计（唐先生指定）**：先证 $\mathcal C_n\notin\sigma(|a-b|,ab,c)$，再看 $a/b\to1$？
**失败更深的含义**：若这条也失败 ⟹ "primitive arithmetic future complexity $\not\Rightarrow$ balance" ⟹ ALIGNMENT SOURCE 才成为独立 frozen gap（但**尚不够冻结资格**）
**方向转换（唐先生）**：从"更复杂的 scalar arithmetic statistic"转到 **future constraint geometry**

---

## 1. 机器（**精确推导**的移动空间 + 只读 gcd/整除的合法性）

$$\boxed{\Delta a+\Delta b=\Delta c\iff(\Delta a,\Delta b,\Delta c)=p(1,0,1)+q(0,1,1)\ \Longrightarrow\ (a,b,c)\mapsto(a+p,\ b+q,\ c+p+q),\ (p,q)\in\mathbb Z^2}$$
**【精确】**：关系保持的整数移动就是 $\mathbb Z^2$，两参数
**合法性（只读 gcd/整除）**：L1 增量必须是 $g=\gcd(a,b)$ 的倍数；L2 再加 $\gcd(a',b')=g$
**窗口**：$|p|,|q|\le B=3$（常数，**不随不平衡程度变化**）
**分支测度**：$\mathcal C(s)=\#\{\text{合法移动}\}$；**动力学**：选使 $\mathcal C(\text{后代})$ 最大的合法邻居（平局按 $|p|+|q|,p,q$ 定序，确定且规范）

---

## 2. ⚠️ 审计判据修正（本轮发现；唐先生指定的第一道审计**空转**）
$$\boxed{\text{判据}\ \mathcal C_n\notin\sigma(|a-b|,ab,c)\ \text{按原样表述是【空】的}}$$
**理由**：$c=a+b$ ⟹ $(|a-b|,c)$ **决定无序状态** $\{a,b\}$ ⟹ 任何状态的对称函数都"被它们决定" ⟹ 该判据无法被任何状态违反。
$$\boxed{\text{修正为【方向性审计】：由 }\mathcal C\text{ 诱导的方向是否与 }|a-b|\text{-梯度方向一致？}}$$
**实算结果**：A1 命中数 = 0（与上述空转一致，**不构成反证**）；A2 有 40 个反例证明 $\mathcal C$ 不是 $(g,c)$ 的函数（窗口边界截断）；A3：$\mathrm{corr}(|a-b|,\mathcal C)=-0.0731$（**弱**，略负）、$\mathrm{corr}(g,\mathcal C)=-0.6618$（**强负**）⟹ 真正依赖是 $g$，不是 $|a-b|$。

---

## 3. ⭐⭐ 结构性理由（近证明）
$$\text{合法性 L1 + 窗口 }B\ \Longrightarrow\ \mathcal C=\Big(2\Big\lfloor\tfrac{B}{g}\Big\rfloor+1\Big)^2\ \text{对 }g\ \text{单调递减}$$
$c\ge4$ 时平衡态 $a=b=c/2$ 有 $g=c/2\ge2$，故
$$\mathcal C(\text{balance})=\Big(2\big\lfloor\tfrac{B}{c/2}\big\rfloor+1\Big)^2<\mathcal C(\text{primitive},g=1)$$
$$\boxed{\text{⟹ 分支最大化动力学【永不】选择平衡态 }(c\ge4)}$$
**实例（$c=20,B=3$）**：$g=1\Rightarrow\mathcal C=28$；$g=2\Rightarrow6$；$g\ge4\Rightarrow1$；平衡 $g=10\Rightarrow\mathcal C=1$

---

## 4. 实测行为
| 变体 | reach $a=b$ | mean $R$: 初 → 末 |
|---|---|---|
| L1/C1 | **0.0324** | 0.4106 → 0.4763 |
| L1/C2 | **0.0324** | 0.4106 → **0.5638** |
| L2/C1 | 0.0324 | 0.4106 → 0.4763 |
| L2/C2 | 0.0324 | 0.4106 → 0.5638 |
| **参考 R0_grad**（读 $|a-b|$） | **0.5185 = CEILING** | → 0.9706 |

**轨道实例**：$(1,19)$ 3 步 $\to(7,20)$ 进入**短周期**；$(7,13)\to(7,10)$；$(2,28)\to(6,28)$
$$\boxed{\text{动力学确实离开强合成态（mean }R\uparrow\text{），但在 primitive 区【停滞并进入短周期】}}$$
而 primitive 区**包含最大不平衡态** $(1,c-1)$，其 $\mathcal C=28$ = 最大值。

---

## 5. 裁决
$$\boxed{\text{未来分支方向与 AM-GM 等号流形是【结构性反】对齐，而非仅去相关}}$$
$$\boxed{\text{分支对 }g\ \text{单调递减，而平衡【最大化】}g\ \Longrightarrow\ [\text{算术未来最丰富者}] 与 [\text{等号流形}] 位于两端}$$
```
算术未来最丰富 = 最大不平衡的 primitive 态 (1,c-1)：C=28（最大）
等号流形       = 算术自由度最小者（g=c/2 最大）：C=1（最小）
```
$$\boxed{\text{⟹ primitive arithmetic future complexity }\not\Rightarrow\text{ balance}}$$
**且本轮给出了【为什么】自然的"未来丰富度"泛函无法提供 alignment**：
因为它对 $g$ 单调，而平衡恰是 $g$ 的极大点——**两者被同一个 $g$ 反向支配**。

---

## 6. ⚠️ 本轮自我修正（第三次，记录在案）
初稿 verdict 有两处与数据不符：① 把"A1 命中 0"写成"$\mathcal C$ 不是 $|a-b|$ 的函数"（后者未被数据支持）；
② 把 $\mathrm{corr}(|a-b|,\mathcal C)$ 的符号写成正（实为 $-0.0731$）。**均已修正**。
**教训（收敛为一条方法纪律）**：
$$\boxed{\textbf{Gate V（空转检查）}:\ \text{任何审计判据在运行前，必须先给出一个【能使其失败】的状态}}$$
否则该判据可能是空转的（本轮即为此例）。**建议作为数学纪律登记**（与 RCI-1/RCI-2 同级，但不入 NO-GO 地图）。

---

## 7. 诚实边界
```
· §0 规格（升级为 future-branching 方向场、C_n 定义、第一道审计、失败含义、future constraint geometry 转向）—— 唐先生本轮
· §1 移动空间精确推导、机器实现、§2 审计判据空转的发现与修正、§3 结构性理由、§4 实测、§5 裁决、
  §6 自我修正与 Gate V 提议 —— 小灵本轮
· 等级：【精确】= 移动空间 $\mathbb Z^2$ 的推导（$\Delta a+\Delta b=\Delta c$ 的格解）；
  【近证明】= $\mathcal C=(2\lfloor B/g\rfloor+1)^2$ 对 $g$ 单调递减（对 L1 合法性 + 窗口，边界截断除外）；
  【实测】= 全部 reach/corr/轨道数字（$B=3$，$c\le30$，780 初态，$K\le25$）
· ⚠️ "分支最大化永不选平衡态"成立范围：$c\ge4$ 且 L1/L2 + 窗口 $B$；对更大 $B$ 或其它合法性【未验证】
· ⚠️ "反对齐"为【结构性结论】；其"近证明"部分依赖 $\mathcal C$ 只依赖 $g$ 这一事实（边界截断下不精确，见 A2）
· §6 的 Gate V 为【方法纪律提议】，未形式化
· 未使用 ζ / Mellin / 零点 / 函数方程；未使用 Λ；无统计拟合（确定性格点枚举）
```

## 8. 提交链
```
7bbadbf ABD-1 第一轮 → 本篇（ABD-1′ 第一轮）
```
