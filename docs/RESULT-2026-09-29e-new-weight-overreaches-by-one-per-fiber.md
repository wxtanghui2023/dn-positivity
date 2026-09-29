# RESULT-e（2026-09-29）—— **新权重 $r(r+1)/2$ 过强（差 $1$/fiber 恰为承重项）；旧式 $\frac{(r-1)(r+2)}2$ 站立**

> **性质**：**问题特化续（自测）**——**不占 C 号** ✓；**不作路线裁定** ✗；空间 B ✓
> **时间**：2026-09-29 19:25 ✓

**已查地图**：`RESULT-d`（旧式 $50/50$）／`RESULT-c`（两来源恒等式）✓

D0: 本档对象 ＝ **档案已有**（凸性／纤维—经典 ✓）
D1: 0（产出＝**一处过强之否证 ＋ 凸性获证 ＋ 规模数据** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✗ 新式 }w=r+\tbinom r2=\frac{r(r+1)}2\ \text{仅 }26/60\ (\text{过强})}$$
$$\boxed{\text{② ✓✓ 旧式 }\frac{(r-1)(r+2)}2\ \text{仍 }60/60\ ——\ \text{二者恰差 }1/\text{fiber};\ \textbf{"}-1\text{" 承重}}$$
$$\boxed{\text{③ ✓✓ 凸性公式 }60/60\ (\text{唐先生之 }\ell\binom{\lfloor R/\ell\rfloor}2+(R\bmod\ell)\lfloor R/\ell\rfloor\ \text{型})}$$
$$\boxed{\text{④ 规模（}a{=}53）：|P|{=}27,|Q|{=}26,|L|{=}243,R{=}I(Q,L){=}67,\ \sum w_{\text{旧}}{=}50,\ F{-}F(P){=}79>71✓}$$

## §1 三版本实测（✓ 对照）

| 权重 | $60$ 样本成立 |
|---|---|
| $r+\tbinom r2=\frac{r(r+1)}2$ | $\mathbf{26/60}$ ✗ |
| $\frac{(r-1)(r+2)}2$ | $\mathbf{60/60}$ ✓✓ |
| $r$（线性） | $60/60$ ✓ |

$$\frac{r(r+1)}2-\frac{(r-1)(r+2)}2=1\quad\forall r\ \Longrightarrow\ \text{新式 ＝ 旧式 }+1/\text{fiber}\ ✗$$

## §2 含义（✓）

$$\boxed{\text{单 fiber 预算是 }\frac{(r-1)(r+2)}2\ (r\ge1),\ \text{不可简化为 }\frac{r(r+1)}2}$$
$$\text{（"}-1\text{"来自配对/计数中某处之一次性损耗;\ \textbf{其来源未查明}）}⚠️$$
$$\therefore\ \text{下一步若要用凸性，须采用旧式，}\textbf{不得}用新式$$

## §3 凸性（✓✓ 获证）

$$\sum_{x\in L}\tbinom{r_x}2\ \ge\ \ell\tbinom{\lfloor R/\ell\rfloor}2+(R\bmod\ell)\lfloor R/\ell\rfloor\qquad(R{=}\sum r_x,\ \ell{=}|L|)$$
$$\text{实测 }60/60\ \text{成立}\ ✓;\quad \text{粗版}\ \sum\tbinom r2\ge\frac{R^2}{2\ell}-\frac R2\ \text{亦可用}✓$$

## §4 规模数据（✓）

$$a{=}53\ \text{之 }62\text{-码子集}:\ |P|{=}27,\ |Q|{=}26,\ |L|{=}243,\ R{=}67,\ \sum w_{\text{旧}}{=}50$$
$$F(A)-F(P)=79\ >\ 9a-406=71\ ✓\qquad(F\ \text{超出纤维上限，非紧})$$

## §5 下一目标（不变）

$$\boxed{\text{求 }R=I(Q,N_1^*(P))\ \text{之统一下界};\ \text{再经凸性 }\Rightarrow\ \text{净 }F}$$
$$\text{（唐先生之建议方向：控制 }R\ \text{而非逐 fiber）}✓$$

## §6 边界（硬 ✓）

- **三版本实测 ＋ 凸性实测** ✓；**不占 C 号** ✓
- **不主张** $107$ 可达/不可达 ✗（V290）；**"}-1\text{"之来源未明**（如实标注）⚠️
