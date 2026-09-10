# 乙′：S9 严格化（引理）+ 甲：D2 interaction-data 预筛

**日期**：2026-09-10 15:16+ ｜ 依据：唐先生乙′→甲 ｜ 预算：纸面（无代码）

---

# 第一部分：S9 严格化

## 1. 原 S9 的两支箭头（第二支不成立）
```
原表述：J-反协变 + 仅由两支 reach 决定 ⟹ θ 必为 reach 差函数 ⟹ 零点 = 重合点 ⟹ N43
```
* **箭头①（成立）**：$J(a,b)=(b,a)$ + $\theta(b,a)=-\theta(a,b)$ ⟹ $\theta(a,a)=-\theta(a,a)$ ⟹ $\theta(a,a)=0$
* **箭头②（❌ 不成立）**：$\theta(a,b)=0\Longrightarrow a=b$ **不自动成立**

**反例形式（小灵验算）**：$\theta(a,b)=(a-b)\,g(a+b)$
```
反对称 ✓（交换翻转 (a−b)，g(a+b) 不变）
但零集 = {a=b} ∪ {g(a+b)=0} ⟹ **严格大于对角线** ✓ 证实唐先生的修正
```

## 2. ⭐ S9 严格版（正式登记为引理）

$$\boxed{\textbf{S9}\ \text{(Reach-only anti-covariance obstruction)}}$$
设内部变量 $\theta=\Theta(r_1,r_2)$，$r_1,r_2$ 是**仅有的两个** scale reaches，且 $\Theta(r_2,r_1)=-\Theta(r_1,r_2)$。
则在交换 $J:(r_1,r_2)\mapsto(r_2,r_1)$ 下必有
$$\boxed{\Theta(r,r)=0}$$
**证明**：$\Theta(r,r)=-\Theta(r,r)\Longrightarrow2\Theta(r,r)=0\Longrightarrow\Theta(r,r)=0\qquad\blacksquare$
**推论**：
$$\boxed{\text{reach-only 反协变 }\theta\ \Longrightarrow\ r_1=r_2\ \text{【必属】其 fixed locus}}$$
取 $(r_1,r_2)=(H,X/H)$ 得 $H=\tfrac XH\Longrightarrow H=\sqrt X$：
$$\boxed{\text{若 }\sqrt X\text{ 的 fixed point 【只】由 reach-only }\theta\text{ 产生，则它【不可能】满足 I3/I4 的"独立 internal fixed law"要求}}$$
**⚠️ 严格边界（必须写明）**：**不**声称"零点集只有 $H=\sqrt X$"——只声称**对角线被包含**。

## 3. ⭐ 为何严格版对"逃生"更致命
```
可能的逃生："我不用 θ=a−b，我找一个很复杂的反对称函数"
⟹ 无论多复杂，只要 θ=Θ(a,b) 且 Θ(b,a)=−Θ(a,b)，就恒有 Θ(a,a)=0
⟹ **复杂化 θ 不能把 fixed-point 机制从两-reach 对角线上解耦**
⟹ 这是真正的结构门（不只是本轮一个观察）
```

---

# 第二部分：θ 的数据源分类（取代数学对象分类）

| 类 | 数据源 | 状态 |
|---|---|---|
| **D0** | reach data：$\theta=\Theta(r_1,r_2)$ | **由 S9 排除** |
| **D1** | label/class data（素标号、character、剩余类、互反符号…） | 上轮实验证明**天然无 scale reach** ⟹ $\approx$ **Sym(ℙ) 支** |
| **D2** | **interaction data**：$\theta=\Theta(\mathcal C_1,\mathcal C_2)$，$\mathcal C_i$ 为两通道的**内部算术状态**（非长度、非标签） | **唯一剩下的** |

**D2 六门（唐先生）**：
```
D2-1 存在两个内部算术状态 u,v（不是两个尺度）
D2-2 交换不是简单 u↔v，而是 native transformation J(u,v)=(v♯,u♯)
D2-3 存在真正的二通道交互量 θ=Θ(u,v)，一般有 Θ(v♯,u♯)≠Θ(u,v)
D2-4 但 J²=1
D2-5 fixed 方程 Θ(u,v)=Θ(v♯,u♯) 产生独立的算术约束
D2-6 该约束同时绑定 H↔X/H
```
**⭐ 唐先生 §7 的关键新增门（B2 暴露的问题）**：
$$\boxed{\theta\ \text{must be }J\text{-sensitive, not merely }J\text{-invariant}}$$
$$\text{若}\ \theta(u,v)=\theta(Ju,Jv)\ \text{则}\ \theta=\theta'\ \text{恒成立}\ \Longrightarrow\ \text{排除}$$
$$\text{又不得只是反对称（}\theta'=-\theta\text{）否则 fixed condition 直接退化成}\ \theta=0\ \Longrightarrow\ \text{回到 S9}$$
$$\boxed{\text{真正的困难区域}:\quad\theta'\neq\theta,\qquad\theta'\neq-\theta,\qquad J^2\theta=\theta}$$

---

# 第三部分：𝕀_cross 正式目标

$$\boxed{\mathfrak I_{\rm cross}:\ \text{cross-channel internal interaction class}}$$
寻找 $(u_H,v_{X/H})$ 与 canonical 交互可观测量 $\theta=\Theta(u_H,v_{X/H})$，使
$$J:(u_H,v_{X/H})\mapsto(u'_{X/H},v'_H),\qquad J^2=1$$
$$\Theta(u_H,v_{X/H})\neq\Theta(u'_{X/H},v'_H)\ \text{一般成立}\qquad\text{但}\qquad\Theta(u_H,v_{X/H})=\Theta(u'_{X/H},v'_H)$$
具有**非平凡的算术解集**，且**该解集不是 $H=X/H$**

---

# 第四部分：小灵执行 —— D2 预筛（三项新结果）

## 4.1 ⭐⭐ 新门 S10：**线性性排除**
```
设 θ 取值于向量空间，J 线性作用且 J²=1 ⟹ θ 分解为 J-偶部 ⊕ J-奇部
⟹ 在每一部上 θ'=±θ ⟹ 恰好落入 D2 已排除的两种情形（θ'=θ 或 θ'=−θ）
```
$$\boxed{\textbf{S10}:\ \text{线性可观测量自动被 D2-3/S9 排除}\ \Longrightarrow\ \textbf{D2 需要【非线性】可观测量}}$$
（或取值于非线性空间，如两个非线性不变量的比）
**⭐ 推论**：非线性恰是所需资源 ⟹ **非线性资源的原生清单**：
```
① 乘积/复合：非线性 ✓ 但属 Sym(ℙ)/divisor 侧 ⟹ 已关闭
② carry：非线性 ✓ 但已关闭（RH-carry 层三重死因）
③ 幂映射/迭代：非线性 ✓ 但 HG-3/HG-4 已在 CRT+canonicity 下关闭
⟹ 残余：既非标号侧、又非 reach 侧的原生非线性资源 —— 【目前未命名/无候选】
```

## 4.2 ⭐⭐ 新门 S11：**swap 机制预筛**（D2 的前置件：无 native swap 则无 D2 对象）
| # | swap 机制 | 死因 |
|---|---|---|
| SW1 | 结构对偶/变换（乘法 ↔ 加法，Mellin/Fourier） | **违反禁止项**（Mellin/Fourier） |
| SW2 | 函数方程型 $s\leftrightarrow1-s$ | 已关闭（FE 路线） |
| SW3 | 群上求逆/共轭 | 落 S9 / inverse 族 |
| SW4 | Galois/系数域共轭 | **标号侧**（D1） |
| SW5 | 范畴 adjunction 的 unit/counit | **coboundary**（Integrability–Null Pincer 腿 i） |
| **SW6** | **真正不同类型的对合** | **形式开放，但【无候选】** |

$$\boxed{\text{任何 D2 候选必须提供一种 SW6 型对合 ⟹ 目前无实例}}$$

## 4.3 D2 预筛结论
$$\boxed{\textbf{D2}\ \text{本轮未找到 canonical instance}}$$
```
残余的精确形式（本轮的最终残余）：
   一个【SW6 型 native 对合】+ 【非线性、J-敏感但非 ±】的交互可观测量，
   其数据源【既非 reach 亦非标号】，且 fixed 解集【独立于 H=X/H】
```

## 4.4 终止条件核对（唐先生设定的规则）
```
唐先生规则：「如果 D2 在经过 S9、I2、I3、I4、I5 后仍找不到 canonical instance，再进入丙」
本轮：S9 已严格化并作为前置过滤器使用；S10/S11 已投入；
      D2 的**前置件（native swap）**本身已枚举到 SW6（无候选）
⟹ 【终止条件的前提】表面已满足
⚠️ 但诚实标注：D2 只跑了【一轮预筛】，且 SW6 仅"形式开放"而非"已证为空"
⟹ 建议进入丙，但【决定权在唐先生】；若不进入，则须为 SW6 给出【新的生成原则】而非新名字
```

## 4.5 状态
$$\boxed{R_{A\text{-}ind}=\text{inactive},\qquad R_{B4}=\text{inactive},\qquad R_{\rm int\text{-}sym}=\textbf{active}\ \text{但空间已压缩为 }\mathfrak I_{\rm cross}}$$
**S 门累计**：S1–S11（S6/S7/S8 通用；**S9 为 filter 级**；S10/S11 本轮新增）
**继续遵守**：暂不碰 $\Lambda$（顺序：internal interaction → nontrivial self-dual fixed locus → second-order object → 才问 Λ 耦合）

## 5. 诚实边界
```
· S9 的修正（第二箭头不成立）+ 反例形式 (a−b)g(a+b) 为唐先生指出，小灵验算确认
· S9 严格版的证明为【初等、严格】；其推论"对角线必属 fixed locus"随之严格
· D0/D1/D2 分类、D2-1..6、§7 的 J-sensitive 要求、𝕀_cross 定义为唐先生本轮
· S10（线性性排除）为小灵的【严格初等推理】（J 线性且 J²=1 ⟹ ±1 分解），
  其"因此需要非线性"的推论依赖"可观测量取值于向量空间"这一前提 ⟹ 若取值于非线性空间则不适用（已注明）
· S11 的 SW1–SW5 死因各自对应既有登记/+禁止项；SW6"形式开放"= 未证明为空
· 4.4 的终止条件核对为【程序性建议】，决定权在唐先生
· 未写代码、未做数值；未引入 ζ 零点或谱算子；全文未使用 Λ
```

## 6. 提交链
```
424d2fa R-INT-SYM-PRE1 → 本篇（S9 严格化 + D2 预筛）
```
