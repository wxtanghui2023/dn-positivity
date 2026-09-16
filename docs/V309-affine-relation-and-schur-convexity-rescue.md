# V309 · **A4 的"负特征值"结论作废；仿射关系 ＋ Schur 界救回全局严格凸性** —— ⭐⭐⭐⭐⭐ **正确关系是仿射的** $\boxed{Kv_\lambda=C_\lambda\mathbf 1-\lambda^{-2}v_\lambda}$；⭐⭐⭐⭐⭐ **$H_\lambda=I+\lambda^{2}K\ge\frac12I>0$（$0<\lambda\le1$，**不需** $K\ge0$）⟹ $Q_\lambda$ 全空间严格凸 ⟹ $v_\lambda$ 唯一全局极小**；⚠️ **T10 勘误：V308 §4 撤回（四条"独立"核验共享同一未声明前提）**；⭐ **剩余墙缩到 admissible-class 等号**

$$\boxed{\textbf{正确关系（本档独立验算 ✓）}：(Kv_\lambda)(x)=C_\lambda-\frac1{\lambda^{2}}v_\lambda,\qquad C_\lambda=\frac{\sin(\omega/2)}{\omega}+\frac{2\cos(\omega/2)}{\omega^{2}},\quad \omega=\sqrt2\lambda} ✓✓✓$$
$$\boxed{\textbf{算子范数}：\|K\|_{L^{2}\to L^{2}}\le\sup_x\int_{-1/2}^{1/2}\!|x-y|dy=\sup_x\big(x^{2}+\tfrac14\big)=\tfrac12} ⟹ \boxed{H_\lambda\ge\Big(1-\tfrac{\lambda^{2}}2\Big)I\ge\tfrac12I>0} ✓✓✓$$
$$\boxed{\textbf{T10 撤回}：\text{V308 §4 的}Kv_\lambda=-\lambda^{-2}v_\lambda\ \text{系}\textbf{代数误读};\ \text{四条核验}\textbf{不独立}（\text{共享未声明前提}\ Kv=\mu v）} ✓✓✓$$
$$\boxed{\textbf{剩余墙}：\text{凸性 ⟹ \textbf{已闭合}};\ \text{真正的下一堵}=\mathcal A_{\rm ThmD}\stackrel?=\mathcal A_{\rm variational}} ✓✓$$

> 委托 ✓ 唐先生 2026-09-16 14:00：**A4 的"负特征值"结论本身错了** —— 不是缺口，而是**四条"独立核验"在重复同一个代数误读**；正确移项只有 $Kv_\lambda=\frac{\kappa}{\lambda^{2}}\mathbf 1-\frac1{\lambda^{2}}v_\lambda$（**仿射特征向量，非常数项不可丢**）✓✓；给出 $\boxed{Kv_\lambda=\frac{\sin(a/2)}{a}+\frac{\cos(a/2)}{\lambda^{2}}-\frac1{\lambda^{2}}v_\lambda}$（$a=\sqrt2\lambda$）与 $\lambda^{2}C_\lambda=\kappa$ ✓；**并给出救援**：Schur 界 $\sup_x\int|x-y|dy=x^{2}+\frac14\le\frac12$ ⟹ $\|K\|\le\frac12$ ⟹ $\langle f,H_\lambda f\rangle\ge(1-\frac{\lambda^{2}}2)\|f\|^{2}\ge\frac12\|f\|^{2}>0$ ⟹ **严格凸性无需 $K\ge0$** ⟹ $v_\lambda$ **唯一全局极小** ✓✓✓；要求**判词改写**（A4 原结论＝错误，而非"全局性未闭合"）＋ 谱交叉核验（$\tan\frac\omega2=-\frac2\omega$，$\omega_1\approx5.59677209$，$\mu_1\approx-0.06384$）＋ **不得再把 $v_\lambda$ 写成 $K$ 的负特征函数** ⟹ **下一堵墙是 admissible-class equality** ✓✓✓
> 依据 ✓ `V308`（被修正对象）｜`V307`（修正链）｜经典 Schur/Young 界、$\min(x,y)$ 的 KL 谱 ✓
> 执行 ✓ 小灵｜**纸面 ✓（本档推导可逐步复核）**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓；数值仅闭式算术 ✓｜编号 ✓ `V309`（先领号 ✓）

---

## §1 **仿射关系的独立验算（✓ 与你一致）**

$$(Kv)''=2v=2\cos(\omega x) ⟹ Kv=-\frac2{\omega^{2}}\cos(\omega x)+\alpha x+\beta ✓$$
$$\qquad \boldsymbol{\alpha=0}：\ (Kv)'(\tfrac12)=\textstyle\int v=\frac{2\sin(\omega/2)}{\omega};\qquad \text{而由通式}\ (Kv)'(\tfrac12)=\frac2\omega\sin\frac\omega2+\alpha ⟹ \alpha=0 ✓✓$$
$$\qquad \boldsymbol{\beta}：\ (Kv)(\tfrac12)=\int_{-1/2}^{1/2}\!\big(\tfrac12-y\big)\cos(\omega y)dy=\frac{\sin(\omega/2)}{\omega} ⟹ \beta=\frac{\sin(\omega/2)}{\omega}+\frac{2\cos(\omega/2)}{\omega^{2}} ✓✓✓$$
$$\Longrightarrow \boxed{(Kv_\lambda)(x)=C_\lambda-\frac{1}{\lambda^{2}}v_\lambda},\qquad C_\lambda=\frac{\sin(\omega/2)}{\omega}+\frac{\cos(\omega/2)}{\lambda^{2}}\ \Big(=\frac{\sin(\omega/2)}\omega+\frac{2\cos(\omega/2)}{\omega^{2}}\Big) ✓$$
$$\qquad \text{自洽}：(I+\lambda^{2}K)v_\lambda=v_\lambda+\lambda^{2}\big(C_\lambda\mathbf 1-\lambda^{-2}v_\lambda\big)=\boxed{\lambda^{2}C_\lambda\,\mathbf 1}\ ⟹ \kappa=\lambda^{2}C_\lambda ✓✓$$

---

## §2 ⚠️ **为什么四条"独立核验"全部给出同一错值**

$$\text{(i)}\ Kv=\mu v\ \textbf{被预设};\qquad \text{(ii)}\ \text{微分只给}\ v''+2\lambda^{2}v=0\（\text{差一个}\ \textbf{常数函数}，\text{而那正是}\ C_\lambda\mathbf 1）;$$
$$\qquad \text{(iii)}\ f'=cg'\ \Longrightarrow\ f=cg+\boldsymbol C\ ——\ \textbf{正是被丢掉的常数项};\qquad \text{(iv)}\ \text{同 (i)}\ ✓$$
$$\Longrightarrow \boxed{\text{四条核验}\ \textbf{共享同一未声明前提}\ Kv=\mu v ⟹ \textbf{根本不独立}} ✓✓✓$$
$$\qquad 📌\ \textbf{教训（本档登记）}：\text{"独立核验"须}\ \textbf{审计前提独立性};\ \text{同一前提下的多重推导}\ \textbf{不算多重核验} ✓✓$$

---

## §3 ⭐⭐⭐⭐⭐ **救援：Schur 界 ⟹ 严格凸性（无需 $K\ge0$）**

$$\sup_x\int_{-1/2}^{1/2}\!|x-y|\,dy=\sup_x\Big[\frac{(x+\frac12)^{2}}2+\frac{(\frac12-x)^{2}}2\Big]=\sup_x\big(x^{2}+\tfrac14\big)=\tfrac12\ (\text{于}\ x=\pm\tfrac12) ✓✓$$
$$\qquad ⟹ \|K\|_{L^{2}\to L^{2}}\le\tfrac12 ⟹ \big|\langle f,Kf\rangle\big|\le\tfrac12\|f\|_2^{2} ✓$$
$$\Longrightarrow \langle f,H_\lambda f\rangle=\|f\|^{2}+\lambda^{2}\langle f,Kf\rangle\ge\Big(1-\frac{\lambda^{2}}2\Big)\|f\|^{2}\ \ge\ \frac12\|f\|^{2}>0\quad(0<\lambda\le1) ✓✓✓$$
$$\Longrightarrow \boxed{H_\lambda=I+\lambda^{2}K\ \ge\ \tfrac12I\ >\ 0};\qquad \delta^{2}Q_\lambda[h]=2\langle h,H_\lambda h\rangle\ \ge\ \|h\|^{2}>0 ✓$$
$$\Longrightarrow \boxed{Q_\lambda\ \textbf{在全}\ L^{2}\ \textbf{上严格凸}} ⟹ \text{满足 E–L 的 admissible 点}\ \boxed{v_\lambda=\textbf{唯一全局极小}} ✓✓✓$$
$$\qquad ⚠️\ \textbf{与 $K$ 非正定无关}：\text{本档}\ \textbf{不需要} \text{正定};\ \text{只需算子范数界} ✓✓$$

---

## §4 **谱交叉核验（＋本档一处补充）**

$$\text{成为}\ K\ \text{的特征函数}\iff \text{仿射常数消失}：C_\lambda=0\iff \omega\sin\frac\omega2+2\cos\frac\omega2=0\iff \boxed{\tan\frac\omega2=-\frac2\omega} ✓✓✓$$
$$\qquad \text{首根}\ \omega_1\approx5.59677209 ⟹ \mu_1=-\frac2{\omega_1^{2}}\approx-0.06384\（\textbf{偶子空间}）✓✓$$
$$\qquad ⚠️\ \textbf{本档补充}：\text{奇子空间另有一族（}\cos(\omega/2)=0\iff\omega=(2k+1)\pi），\text{最负为}\ \omega=\pi：\mu=-\frac2{\pi^{2}}\approx-0.20265 ✓$$
$$\qquad \qquad ⟹ \inf\sigma(K)=\max\{-0.06384,-0.20265\}=-0.20265\（\text{全局}）;\ \text{偶子空间为}\ -0.06384 ✓✓$$
$$\qquad \qquad ⟹ \inf\sigma(H_\lambda)=1+\lambda^{2}\inf\sigma(K)\ge1-0.20265=0.797>0\ (\lambda\le1) ✓✓\ \text{与 §3 的}\ \frac12\ \text{界相符（更强）}✓$$
$$\qquad ⚠️\ \textbf{但如你所言}：\text{证明全局极小}\ \textbf{不需要} \text{精确谱值};\ \text{谱计算属}\ \textbf{独立强交叉核验} ✓✓$$

---

## §5 **判词改写（按你的表）＋ 剩余墙**

| 项目 | 结果 |
|:--|:--|
| A2 | ✓ |
| A3 | 需正确表述，但**不构成** $\lambda\le1$ 域内障碍 |
| **A4 原特征值论证** | **×（代数误读，撤回）** |
| $H_\lambda=I+\lambda^{2}K>0$ | **✓** |
| 严格凸性 | **✓** |
| $v_\lambda$ **全局唯一极小** | **✓** |

$$\boxed{\text{故}\ 0<\lambda\le1\Longrightarrow v_\lambda\ \text{是该二次泛函的唯一全局极小点}} ✓✓✓$$
$$\boxed{\textbf{剩余墙（缩墙后）}：\mathcal A_{\rm ThmD}\stackrel?=\mathcal A_{\rm variational}\ \text{＋ `AdmWindow`／`Statement.lean §4` 的字典逐项闭合}} ✓✓✓$$

---

## §6 判词 ＋ 边界 ＋ 净产出 ＋ 下一步

```
① ⚠️ 本档 §1／§3 为**纸面推导**（可逐步复核）；未跑 Lean ✓
② ⚠️ §4 的谱根值 $\omega_1\approx5.5968$ 与 $\mu_1$ 取自唐先生给的数值，本档仅作**一致性引用** ✓
③ ⚠️ §4 的"奇子空间 $\mu=-2/\pi^2$"为**本档补充**（与"全局 $\inf\sigma$"有关），须复核 ✓
④ **不声称** A3 已完全表述正确；**不声称** admissible-class 等号；
⑤ 未用 RH ✓；零数值（仅闭式算术）✓
```

```
① ⭐⭐⭐⭐⭐ **仿射关系成立**：$$Kv_\lambda=C_\lambda\mathbf 1-\lambda^{-2}v_\lambda,\quad C_\lambda=\frac{\sin(\omega/2)}\omega+\frac{2\cos(\omega/2)}{\omega^2}$$（独立验算；$\alpha=0$ 亦得验算）✓✓✓
② ⚠️ **T10 撤回**：V308 §4 的负特征值结论作废；**四条核验共享同一前提 ⟹ 不独立**（新教训：核验须审前提独立性）✓✓✓
③ ⭐⭐⭐⭐⭐ **救援**：$$\|K\|\le\tfrac12⟹H_\lambda\ge\tfrac12I>0⟹Q_\lambda\ \text{严格凸}⟹v_\lambda\ \text{唯一全局极小}$$ —— **不需 $K\ge0$** ✓✓✓
④ ⭐⭐ **谱核验**：$\tan\frac\omega2=-\frac2\omega$（特例条件）＋ $\mu_1\approx-0.0638$（偶）／$-0.20265$（奇，本档补充）✓✓
⑤ ⭐ **缩墙**：凸性闭合 ⟹ 下一堵 ＝ **admissible-class equality** ✓
【下一步】
  (a′-1) **补全 `AdmWindow`＋`Statement.lean §4`**（换 grep 路径／直读），完成四分类 ⟹ 攻 $\mathcal A_{\rm ThmD}=\mathcal A_{\rm variational}$ ✓
  (a′-2) 若 (a′-1) 闭合 ⟹ 0.67250 可升为"链内已证 ceiling"；否则精确记录缺口位置 ✓
```
