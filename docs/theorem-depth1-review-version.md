# 定理（复核版）：运输曲率的深度-1 界

**建立**：2026-09-10 ｜ **替代**：`theorem-depth1-transport.md` §3（原版两行证明有漏洞，已被唐先生拦截）
**封存判据**：唐先生拍板 α（本支线按此定理收口）

---

## 0. 原版被拦截的漏洞（留档，不许删）

原版声称："$W$ 通过 $\operatorname{rad}(\cdot)$ 与整除性依赖 $S$ ⟹ $\omega_p$ 只依赖 $(a,b)\bmod p$"。

**漏洞**：由 $\operatorname{rad}(c)$ 的**整除性**只需 $c\bmod p$，**不能**推出
$\operatorname{rad}(c)\bmod p$ 由 $c\bmod p$ 决定。

反例（已数值验证）：$c=10,\ c'=25,\ p=3$，二者 $\equiv1\pmod3$，但
$$\operatorname{rad}(10)=10\equiv1,\qquad \operatorname{rad}(25)=5\equiv2 \pmod 3 .$$
⟹ 若权的某一步使用 $\operatorname{rad}(c)$ 的**模 $p$ 数值**，$K_p=1$ 的证明立即失效。
**原版陈述过强，作废。**

---

## 1. 定理（复核版，适用范围写死）

**假设**：四状态闭环 $S,\ S_A,\ S_M,\ S_{AM}$ 上的局部曲率已化简为
$$\omega_p(S)=\sum_{j=1}^{r}c_j\,\mathbf 1_{p\mid \ell_j(a,b)} ,$$
其中 $c_j$ 与 $a,b$ 无关，每个
$$\ell_j(a,b)=u_j a+v_j b\qquad(u_j,v_j\in\mathbb Z)$$
是**整系数线性式**。

**结论**：
$$\boxed{\ \omega_p(S)\ \text{仅依赖}\ (a\bmod p,\ b\bmod p)\ }\quad\Longrightarrow\quad \boxed{\ K_p=1\ }$$

**证明（两行）**：

1. 对每个整系数线性式：$\;p\mid\ell_j(a,b)\iff \ell_j(a\bmod p,\ b\bmod p)\equiv0\pmod p$。
   故每个整除指示、以及其有限线性组合 $\omega_p$，均只依赖 $(a,b)\bmod p$。∎

2. **对本支线实际使用的权，化简其四状态差分**（这是"验证"而非"假设"）：
   由 $v_p(\operatorname{rad}(n))=\mathbf 1_{p\mid n}$ 与
   $S_{AM}=\operatorname{rad}(b{+}c)\cdot(b,c,b{+}c)$、$S_M=\operatorname{rad}(c)\cdot(a,b,c)$ 得
   $$\boxed{\ \omega_p^{(\text{pow})}=\alpha\big[3v_p(\operatorname{rad}(b{+}c))-3v_p(\operatorname{rad}(c))\big]
   =3\alpha\big(\mathbf 1_{p\mid b+c}-\mathbf 1_{p\mid c}\big)\ }$$
   即 $v_p$ 的高阶项**精确抵消**，只剩整除指示，落回第 1 行形式。
   radical 型同样落回该形式（见 §2 数值）。∎

**证毕。**

---

## 2. 数值复核（本轮亲算，非转述）

```
(A) 反例验证（唐先生的拦截）：rad(c) mod p 不是 c mod p 的函数
    c=10, c'=25, p=3: 同余成立，但 rad 分别 ≡1, ≡2  ⟹ 反例成立 ✓

(B) 实际 ω_p^rad 的值表（a 外层, b 内层）
    p=3: [0,0,0,0,2,−2,0,−2,2]
    p=5: [0,0,0,0,0,0,0,2,0,−2,0,0,0,−2,2,0,2,−2,0,0,0,−2,0,2,0]

(C) span 检验（精确有理高斯消元）
    p=3: rank(候选)=5, rank(候选+目标)=5  ⟹ 在 span{1,1_{ℓ≡0}} 内 ✓  (5 维 ⊂ 9 维)
    p=5: rank(候选)=7, rank(候选+目标)=7  ⟹ 在 span 内 ✓            (7 维 ⊂ 25 维)

(D) 手验两格（p=3）
    (1,1): S+0; SA(3✓)−1; SM+0; SAM(3,6,9全✓)+3        ⟹ ω=+2 ✓
    (1,2): S+1; SA−1; SM(3,6,9)−3; SAM(15✓)+1           ⟹ ω=−2 ✓

(E) 幂型 telescoping：p=2,3,5 各 22500 样本，反例 0（含混合权）
(F) min_depth (N=500): K_p = 1 对 p∈{2,3,5,7}（radical 型与幂型均如此）
    对照：数据自身 p-深度 D_p 最大为 8(p=2), 5(p=3), 3(p=5), 3(p=7)
```
脚本：`scripts/verify_span_minimal.py`、`scripts/verify_telescoping.py`、`scripts/C2a_depth.py`

---

## 3. 复核边界（必须随定理一起引用）

本定理**不声称**：
1. $\operatorname{rad}(n)\bmod p$ 由 $n\bmod p$ 决定（**该命题为假**，见 §0）。
2. 任意非线性 $v_p$ 权、或任意依赖 $\operatorname{rad}(n)$ **数值**的运输都满足 $K_p=1$。

它只声称：**实际曲率经四状态差分后能化为有限个 $\mathbf 1_{p\mid\ell(a,b)}$ 的情形，$K_p=1$。**

---

## 4. 结果（按唐先生要求收紧后的措辞）

$$\boxed{\textbf{实际 radical/乘积型运输曲率是 depth-1，因而不携带 }p\textbf{-adic 跨尺度记忆。}}$$

**不要**写成更强的"任何 radical-type transport curvature 都是 depth-1"——那超出证明。

**本支线按 α 收口。** 关闭证书 = 观测到的 $K_p=1$ **＋** 到 mod-$p$ 线性整除数据的**精确归约**。
