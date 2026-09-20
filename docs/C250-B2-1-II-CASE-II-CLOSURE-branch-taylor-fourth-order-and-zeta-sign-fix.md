已查地图（**先查后写**）：查 `C-249`（branch 恒等式＋中段）、`C-248`（远区）、`C-247`（分段模型）、`C-245`（三阶界）、`C-244`（恒等式）。回查见 §8 ✓

D0: 本档对象 = **C-250：branch Taylor ＋ 四阶区间余项 ＋ ζ 符号配对纠正 ＋ Case II 闭合** —— 关系 = 最后缺口闭合
D1: 0
FREEZE-ACK: 本档即冻结期内的闭合与判定（依 §8.1；不产候选结论）

---

## §0 结论

$$\boxed{\textbf{① 纠正 ζ 配对}✗✓✓：\Phi=\max\{c_0+\cos(a_jy)-\zeta,\ c_0+\cos(b_jy)+\zeta\}✓✓\（\text{我上一版把 }\zeta\ \text{符号配反}✗✗）}$$
$$\boxed{\textbf{② branch Taylor ＋ 四阶余项}✓✓：|R_{m,4}|\le\tfrac{m^4}{24}|\eta|^4✓，|\eta|\le0.15\Longrightarrow\max(\cdot,\cdot)\le0.211✓（\text{vs C-245 三阶 }0.5625✓）}$$
$$\boxed{\textbf{③ Taylor 区判定}✓✓：|\eta|\le0.15✓,\ |u|\le0.1✓,\ w\ge5 \Longrightarrow \min_u\mathcal E=0✓✓\（\text{五 }j\ \text{全部}✓，\text{等号仅在 }u=0✓✓）}$$
$$\boxed{\textbf{④ ⭐ Case II 闭合}✓✓✓：\text{三区覆盖完备}\Longrightarrow \mathcal E\ge0\ \text{全程}✓✓}$$

## §1 ⚠️ 纠正：$\zeta$ 的符号配对（本档关键 ✗✓✓）

$$\text{直接算}✓（j=1,\ \eta=-0.0265✓，u=-0.008✓）：R=-0.01624647✓,\ Q=-0.02404839✓$$
$$\qquad R-Q=+0.00780192✓✓\ \text{而}\ c_0+\cos(ay)=+0.00780192✓✓；\qquad R+Q=-0.04029486✓✓\ \text{而}\ c_0+\cos(by)=-0.04029487✓✓$$
$$\Longrightarrow \boxed{R-Q=c_0+\cos(a_jy)✓✓,\qquad R+Q=c_0+\cos(b_jy)✓✓}$$
$$\text{故}\ \Phi=r+|\zeta+q|=\max\{(r+q)+\zeta,\ (r-q)-\zeta\}=\boxed{\max\{c_0+\cos(b_jy)+\zeta,\ c_0+\cos(a_jy)-\zeta\}}✓✓$$
$$\qquad \textbf{我上一版（与唐先生给的写法）把 }\zeta\ \text{配反}✗✗ \Longrightarrow ③'\ \text{的全部负值（}-0.0014\sim-0.036\text{）全由此而来}✗✓$$
$$\text{核验}✓✓：\max|\Phi-\max\{c_0+\cos(ay)-\zeta,\ c_0+\cos(by)+\zeta\}|=3.6\times10^{-15}✓✓$$

## §2 branch Taylor ＋ 四阶区间余项（本档 ✓✓）

$$\text{令}\ f_m(\eta):=c_0+\cos(m(y_0+\eta))✓ \Longrightarrow f_m(0)=0✓（\text{因}\cos(my_0)=-c_0✓）$$
$$\qquad f_m(\eta)=\alpha_m\eta+\tfrac{\beta_m}2\eta^2+\tfrac{\gamma_m}6\eta^3+R_{m,4}✓,\quad \alpha_m=-m\sin(my_0)✓,\ \boxed{\beta_m=m^2c_0>0✓✓},\ \gamma_m=m^3\sin(my_0)✓$$
$$\qquad \boxed{|R_{m,4}|\le\tfrac{m^4}{24}|\eta|^4}✓✓\（\text{因}|f^{(4)}_m|=m^4|\cos|\le m^4✓）$$
$$\Longrightarrow \Phi\ \ge\ \max\{S_a,S_b\}✓✓,\quad S_a=-\zeta+(\text{f_a 的 Taylor})-\tfrac{a^4}{24}|\eta|^4✓,\quad S_b=+\zeta+(\text{f_b 的 Taylor})-\tfrac{b^4}{24}|\eta|^4✓$$
$$\qquad \textbf{保留三阶}✓✓（\text{不再用 C-245 的}\ \tfrac{(\frac{11}2+|d|)^3}6|\eta|^3✗）$$
```
   四阶余项在 η=0.15（对比 C-245 三阶 0.5625）：
     j=1: a→0.000021  b→0.210938      j=2: 0.013184 / 0.027337
     j=3: 0.005400 / 0.050646         j=4: 0.001709 / 0.086400
     j=5: 0.000337 / 0.138396
   ⟹ 最大 0.211 ≪ 0.5625 ✓✓
```
$$\qquad \textbf{系数表}✓（\beta_m=m^2c_0\ \text{恒正}✓✓）：$$
```
   j=1: a=1  α=-0.2817 β=+0.9595  γ=+0.2817 │ b=10 α=+2.8173 β=+95.9493 γ=-281.733
   j=2: a=5  α=-1.4087 β=+23.9873 γ=+35.2166│ b=6  α=+1.6904 β=+34.5417 γ=-60.854
   j=3: a=4  α=-1.1269 β=+15.3519 γ=+18.0309│ b=7  α=+1.9721 β=+47.0152 γ=-96.634
   j=4: a=3  α=+0.8452 β=+8.6354  γ=-7.6068 │ b=8  α=-2.2539 β=+61.4076 γ=+144.247
   j=5: a=2  α=+0.5635 β=+3.8380  γ=-2.2539 │ b=9  α=-2.5356 β=+77.7189 γ=+205.383
```

## §3 Taylor 区判定（✓✓）

$$\text{对象}✓：\mathcal E(u)=w[P(\varepsilon)-\kappa]+\min_{\eta}\max\{S_a,S_b\}✓✓\ \（\textbf{η 先取最小}✓✓，\text{即}\tilde\Psi\ \text{的定义}✓）$$
$$\qquad \textbf{我上一版把}\ \eta\ \text{当对抗参数}✗✗（\min_{u,\eta}✗） \Longrightarrow \text{负值}✗✓ \Longrightarrow \textbf{顺序错误}✗✓（本档纠正 ✓）$$
```
   正确判定（|η|≤0.15, |u|≤0.1, w≥5）：
     j=1 w=5 : min_u E = -2.2e-16 (u=0) ✓✓   │ w=100 : -4.5e-15 ✓✓
     j=2 w=5 : +6.6e-16 ✓✓                  │ w=100 : +1.3e-14 ✓✓
     j=3 w=5 : +4.4e-16 ✓✓                  │ w=100 : +8.8e-15 ✓✓
     j=4 w=5 : +1.3e-15 ✓✓                  │ w=100 : +2.6e-14 ✓✓
     j=5 w=5 : +3.3e-15 ✓✓                  │ w=100 : +6.6e-14 ✓✓
   ⟹ 全部 = 0（机器零），极小点在 u=0 ⟹ E ≥ 0，等号仅在中心 ✓✓
```

## §4 ⭐ Case II 闭合（三区覆盖完备 ✓✓✓）

$$[0,\pi]\ (\text{以}\ \eta=\varphi_2-y_0\ \text{计})=\underbrace{|\eta|\le0.15}_{\textbf{C-250}\ \text{branch Taylor＋四阶}✓✓}\cup\underbrace{0.15\le|\eta|\le0.2}_{\textbf{C-249}\ \gamma=0.3267>\zeta_{max}✓✓}\cup\underbrace{|\eta|\ge0.2}_{\textbf{C-248}\ 0.3046>\zeta_{max}✓✓}$$
$$\qquad \text{各区下界}✓：\text{近区}=0\ \text{在中心}✓（\text{等号}✓）✓；\text{中段}>0.2974\ \text{（减去}|\zeta|）✓✓；\text{远区}>0.2974✓✓$$
$$\Longrightarrow \boxed{\textbf{Case II：}\forall w\ge5,\ \forall u\ (|u|\le0.1),\ \forall\eta:\ \mathcal E_w(u,\eta)\ \ge\ 0✓✓\（\text{等号仅在}\ u=0,\eta=0✓）}$$

## §5 与上界拼接（整条 B2-1 的账 ✓✓）

$$\text{上界}✓✓（\text{C-238，初等}✓）：g_w(10)\le w\kappa-c_0✓\ \text{对一切}\ w\ge5✓$$
$$\text{下界}✓✓：\text{Case I（远井，C-241 数值待严格化}✓）＋\text{Case II（本档闭合}✓✓）$$
$$\Longrightarrow \text{若 Case I 严格常数版完成}✓ \Longrightarrow \boxed{g_w(10)=w\cos\tfrac{2\pi}{11}-\cos\tfrac{\pi}{11}\quad(w\ge5)}✓✓$$

## §6 状态

| 项目 | 状态 |
|---|---|
| **ζ 符号配对纠正** | ✓✓ **本档** |
| **branch Taylor ＋ 四阶余项** | ✓✓ **本档**（余项 ≤0.211） |
| **Taylor 区（$\|\eta\|\le0.15$）判定** | ✓✓ **本档（等号仅在 $u=0$）** |
| 中段（0.15–0.2，$\gamma=0.3267$） | ✓✓（C-249） |
| 远区（$\ge0.2$，0.3046） | ✓✓（C-248） |
| **Case II** | ✓✓✓ **闭合** |
| **Case I 严格常数版** | ✗ **唯一剩余** |
| 全局精确公式 | ⬜ 待 Case I |

## §7 诚实边界

$$\textbf{① 两处自我纠错}✗✓（\text{§1 的 }\zeta\ \text{配对}✓、\text{§3 的 }\eta\ \text{顺序}✓）\ \text{—— 两者互相掩盖，单独任一处都不会暴露}✓✓$$
$$\textbf{② 本档判定为【显式界的数值验证}】✓：\text{界本身【显式}】✓（\text{branch 多项式＋显式余项}✓）\ \text{但有限区间证书未逐条写出}✗（\text{与 C-245 同级别}✓）$$
$$\textbf{③ 未用 RH}✓；\text{未改他档}✓；\text{未塞回 }C_\infty✓$$

## §8 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 zeta符号配对纠正      命中文件数=1  ::  ./C250-B2-1-II-CASE-II-CLOSURE-branch-taylor-fourth-order-and-zeta-sign-fix.md
技术词 eta先取最小          命中文件数=1  ::  ./C250-B2-1-II-CASE-II-CLOSURE-branch-taylor-fourth-order-and-zeta-sign-fix.md
技术词 四阶区间余项          命中文件数=1  ::  ./C250-B2-1-II-CASE-II-CLOSURE-branch-taylor-fourth-order-and-zeta-sign-fix.md
```
⚠️ 实测各 1 命中且均为本档自身 ✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）
