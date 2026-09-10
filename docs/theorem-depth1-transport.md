# 定理：运输曲率的深度-1 界（可复核版）

**建立**：2026-09-10 ｜ 模型：算术运输曲率 v1/v2 ｜ 判定：本支线按此定理收口

---

## 0. 模型与记号的严格定义

状态：$S=(a,b,c)$，$a,b\ge1$，$c=a+b$（正整数三元组，满足加法关系）。

运输（均保 $a+b=c$）：

$$T_A(a,b,c)=(b,\;c,\;b+c),\qquad T_M(S)=u(S)\cdot S,\quad u(S)=\operatorname{rad}(c)$$

四状态记作

$$S,\quad S_A:=T_A S,\quad S_M:=T_M S,\quad S_{AM}:=T_M T_A S$$

曲率（对权 $W>0$）：

$$\Omega(S)=\log\frac{W(S_{AM})\,W(S)}{W(S_A)\,W(S_M)}$$

权的对数素数展开（唯一分解定理的直接后果，**对任何正整数权自动成立**）：

$$\log W(S)=\sum_p w_p(S)\log p,\qquad w_p(S)\in\mathbb Z$$

局部缺陷：$\;\omega_p(S):=w_p(S_{AM})+w_p(S)-w_p(S_A)-w_p(S_M)$，于是

$$\boxed{\ \Omega(S)=\sum_p \omega_p(S)\log p\ }\qquad\text{（精确，非渐近）}$$

**注意**：此分解恒真，故不具判别力。判别力在**深度**（见下）。

---

## 1. 权的允许类（这是定理的适用范围，必须写死）

$$\boxed{\ W(S)=\prod_{n\in\{a,b,c,\;u a,ub,uc,\;u_2 b,u_2 c,u_2(b+c)\}} n^{\alpha_n}\operatorname{rad}(n)^{\beta_n}\ ,\qquad \alpha_n,\beta_n\in\mathbb Q\ }$$

即：**四状态分量上的单项式型 × radical 幂型权**。
（$u=\operatorname{rad}(c)$，$u_2=\operatorname{rad}(b+c)$。）

## 2. 深度定义（C2-a）

$$\boxed{\ K_p(S):=\min\{K:\ \omega_p(S)\ \text{由}\ (a\bmod p^{K},\;b\bmod p^{K})\ \text{唯一决定}\}\ }$$

---

## 3. 定理

> **定理（深度-1 界）**
> 对第 1 节允许类中的任何权 $W$，任何素数 $p$，任何状态 $S$：
> $$\omega_p(S)\ \text{仅依赖}\ (a\bmod p,\;b\bmod p)$$
> 因而
> $$\boxed{\,K_p(S)=1\quad\forall p,\ \forall S\,}$$
> 推论：$\Omega(S)$ 不含任何**跨尺度记忆**（深度有统一上界且 $=1$）。

### 证明（两行）

**第一步（整除性降为 mod-$p$ 条件）。**
每个状态的分量都是如下形式之一：整系数线性式 $\ell(a,b)\in\{a,b,a+b,a+2b,b+c\}$，或它与 $\operatorname{rad}(c)$/$\operatorname{rad}(b+c)$ 的乘积。而
$$p\mid\textstyle\prod_i \ell_i(a,b)\iff \exists i:\ p\mid\ell_i(a,b)\iff \exists i:\ \ell_i(a\bmod p,\;b\bmod p)\equiv0\pmod p .$$
故所有整除指示（即所有 $\beta_n$ 项与 $w_p$ 中的指示部分）只依赖 $(a,b)\bmod p$。∎

**第二步（$v_p$ 部分在四状态间成对抵消）。**
对 $n\in\{a,b,c\}$ 的幂型部分贡献 $\alpha\sum_{n}v_p(n)$，由
$$\textstyle\sum_{\text{comp}\in S_{AM}}v_p=\underbrace{3v_p(u_2)+v_p(b)+v_p(c)+v_p(b+c)}_{\text{注意 }S_A=(b,c,b+c)},\qquad
\sum_{\text{comp}\in S_{M}}v_p=3v_p(u)+v_p(a)+v_p(b)+v_p(c),$$
以及 $v_p(\operatorname{rad}(m))=\mathbf 1_{p\mid m}$，得
$$\boxed{\ \omega_p^{(\alpha)}=\alpha\Big[3v_p(u_2)-3v_p(u)\Big]=3\alpha\big(\mathbf 1_{p\mid b+c}-\mathbf 1_{p\mid c}\big)\ }$$
即 $v_p$ 的高阶信息**完全抵消**，只剩整除指示。合并第一步即得 $\omega_p$ 只依赖 $(a,b)\bmod p$。∎

**证毕。**

---

## 4. 数值验证（复核用）

```
C2-a：min_depth（N=500），p ∈ {2,3,5,7}
  p   radical型 K_p   幂型(abc) K_p    数据自身深度 D_p(max)
  2        1              1                  8
  3        1              1                  5
  5        1              1                  3
  7        1              1                  3

逐条核对：radical 型 (a mod p, b mod p) 类数 / 多值类
  p=2: 4 类 / 0        p=5: 25 类 / 0
  p=3: 9 类 / 0        p=7: 49 类 / 0
（多值类 = 0 即 K_p=1）
```
**对照栏最关键**：数据自身携带 $p$-深度达 8（$p=2$），而曲率 $K_p=1$
⟹ **曲率把整个结构投影到了 depth-1 扇区**。

脚本：`scripts/C2a_depth.py`

---

## 5. 结果

$$\boxed{\textbf{radical-type transport curvature is depth-bounded (}K_p=1\textbf{), hence no cross-scale memory.}}$$

本支线按此定理**收口**。

## 6. 定理的诚实边界（复核时必须看这一节）

1. 定理仅覆盖第 1 节的**单项式×radical 幂型权**。任何**非线性于 $v_p$** 的权
   （如 $v_p^2$、$\log v_p$）**不在覆盖范围内**，因为此时
   ① $v_p$ 不再成对抵消，② $\log W=\sum w_p\log p$ 的整数系数展开失效。
2. 故"升级到含 $v_p$ 深度的权"**是一次真正的模型重置**（曲率与分解两个定义都要改），
   不是本定理的推论。
3. 本定理是**负面但有界**的结果：它证明了该模型类不含跨尺度记忆，
   并未证明"跨尺度记忆不可能存在"。
