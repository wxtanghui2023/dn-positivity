# V316-B 预检：仿射恒等式的**常数归一化**（写 Lean 前必须先钉死）

## 纸面推导（$K(x,y)=|x-y|$ 于 $[-\tfrac12,\tfrac12]$，$v_\lambda(s)=\cos(a s)$，$a=\sqrt2\lambda$）

$$\textcircled{1}\ (Kv)''=2v\ \text{（标准：}\ |\cdot|\ \text{核的二阶导）}\ \Longrightarrow\ Kv=-\frac{2}{a^{2}}v+\alpha x+\beta,\quad \frac{2}{a^{2}}=\frac1{\lambda^{2}}$$
$$\textcircled{2}\ \text{偶性}：Kv\ \text{偶（}|\cdot|\ \text{对称、}\cos\ \text{偶）}\ \Longrightarrow\ \alpha=0\ \Longrightarrow\ \boxed{Kv_\lambda=\beta\cdot\mathbf 1-\lambda^{-2}v_\lambda}$$
$$\textcircled{3}\ \text{端点（一阶）}：(Kv)'(\tfrac12)=\int_{-1/2}^{1/2}v=2\sin(a/2)/a;\quad (Kv)'=-\lambda^{-2}v'=\lambda^{-2}a\sin(a/2)$$
$$\qquad \Longrightarrow\ \lambda^{-2}a=\frac2a\iff a^{2}=2\lambda^{2}\ \checkmark\ \text{（自洽，}\beta\ \text{不可定）}$$
$$\textcircled{4}\ \text{取值}：(Kv)(\tfrac12)=\int_{-1/2}^{1/2}(\tfrac12-y)\cos(ay)dy=\sin(a/2)/a\ \text{（奇部为零）}$$
$$\qquad \Longrightarrow\ \beta=\frac{\sin(a/2)}{a}+\frac{\cos(a/2)}{\lambda^{2}}\quad(\vartheta:=a/2=\lambda/\sqrt2)$$

## ⚠️ 关键发现：$C_\lambda$ 的**两种不同归一化**（必须区分，否则 A4 式错位）

$$\textbf{(i) 仿射截距}\ \beta=\frac{\sin\vartheta}{\sqrt2\,\lambda}+\frac{\cos\vartheta}{\lambda^{2}};\qquad
\textbf{(ii) E–L 常数}\ \lambda^{2}\beta=\boxed{\cos\vartheta+\vartheta\sin\vartheta}$$
$$\Longrightarrow\ \text{E–L 形式：}\ \boxed{(I+\lambda^{2}K)v_\lambda=\lambda^{2}\beta\cdot\mathbf 1=(\cos\vartheta+\vartheta\sin\vartheta)\cdot\mathbf 1}$$
$$\text{而源码}\ c^{*}_\lambda=\frac{\sqrt2\sin\vartheta}{\cos\vartheta+\vartheta\sin\vartheta}\ \Longrightarrow\ \boxed{\lambda^{2}\beta=\frac{\sqrt2\sin\vartheta}{c^{*}_\lambda}}$$
$$\textbf{注意}：\lambda^{2}\beta=\cos\vartheta+\vartheta\sin\vartheta\ \textbf{恰是}\ c^{*}\ \text{的分母}\ \checkmark\ \text{（源码}\ \texttt{cStar}\ \text{用 division-safe 形式，分母即此项）}$$

## 结论（待唐先生确认后落 Lean）

$$\text{建议 Lean 中直接定义}\ \boxed{\texttt{vStarELconst}\ \lambda:=\cos(\theta\lambda)+\theta\lambda\cdot\sin(\theta\lambda)}\ (\theta=\lambda/\sqrt2)$$
$$\qquad \text{于是两条定理形状为：}$$
$$\qquad \texttt{KvStar\_affine}:\quad Kv_\lambda=\lambda^{-2}\big(\texttt{vStarELconst}\ \lambda\cdot\mathbf 1-v_\lambda\big)$$
$$\qquad \texttt{vStar\_EL}:\quad v_\lambda+\lambda^{2}Kv_\lambda=\texttt{vStarELconst}\ \lambda\cdot\mathbf 1$$
$$\textbf{严禁}：\ Kv_\lambda=\mu v_\lambda\ \text{形式的特征值陈述（A4 错位）};\ \text{两个积分常数}\ \alpha,\beta\ \textbf{必须在 Lean 中实际消掉}$$

## 分层（按唐先生定的顺序）
```
vStar_EL_second_deriv   : (Kv_λ)'' = 2 v_λ        （F'' = 2v）
vStar_EL_boundary       : (Kv)'(±1/2) = ∓∫v_λ    （端点/归一化）
KvStar_affine           : Kv_λ = β·1 − λ⁻²v_λ     （消 α=0、定 β）  ← 核心
vStar_EL_constant       : v_λ + λ²Kv_λ = λ²β·1
```
