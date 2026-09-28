# AUDIT-2026-09-29b — **自证两不等式（含已验证恒等式）＋ $\theta$ 门槛表（$\theta_0{=}6\Rightarrow107$）＋ 缺口仍存**

> **性质**：**自证推导（含实测核验）**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-29 08:3x ✓
> **唐先生令（逐字）**：「自行推导不等式」✓

**已查地图**：接续 `AUDIT-29a`（可实现机制上确界）／`af`（Haas 2008 Thm 52/54）✓

D0: 本档对象 ＝ **档案已有**（deep holes $A$／$Z$／excess——无新数学对象 ✓）
D1: 0（产出＝**一条新恒等式（已验证）＋ 两条自证不等式 ＋ 门槛表** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✓✓ 自证恒等式（实测吻合）}:\ \sum_{x\in A}E(B(x,1))=121M-4(N_1{+}N_2)-11264}$$
$$\boxed{\text{② ✓ 由 van Wee 链得\ \textbf{新上界}（档案所指"缺件"）}:\ N_1{+}N_2\ \le\ (122M-11288)/4}$$
$$\boxed{\text{③ ✗ 缺口仍存}:\ M{=}106\ \text{时}\ 117\le N_1{+}N_2\le411}$$
$$\boxed{\text{④ ★ }\theta\ \text{门槛}:\ \theta_0{=}6\Rightarrow107;\ \text{但 120-code 实测 }\theta{=}8.31\ \Longrightarrow\ \text{该精化上限}\approx104\ ✗}$$

## §1 ① 自证恒等式（**本档核心，已实测吻合 ✓✓**）

$$\text{记 }A=\{x:d(x,C)=1\}\ (\text{deep holes}),\quad E(z)=\mu(z)-1,\quad B(x,1)\ \text{为半径-1 球}$$
$$\text{关键事实（已核）}:\ E(B(x,1))=2\bigl(A_1(x)+A_2(x)\bigr)-11\ \Longrightarrow\ \textbf{恒为奇数}\ \Longrightarrow\ \ge1\ (\varepsilon{=}1)$$
$$\text{求和}:\ \sum_{x\in A}A_1(x)=10M-2N_1,\qquad \sum_{x\in A}A_2(x)=45M-2N_2,\qquad |A|=1024-M\ (\text{等号})$$
$$\therefore\ \boxed{\sum_{x\in A}E(B(x,1))=121M-4(N_1{+}N_2)-11264}\ ✓✓$$
$$\textbf{实测核验（120-code）}:\ 121\cdot120-4\cdot199-11264=14520-796-11264=\mathbf{2460};\ \text{直算亦}\ \mathbf{2460}\ ✓✓$$

## §2 ② 由 van Wee 链得 $N_1{+}N_2$ 之**上界**（**档案所指"缺件"之类型 ✓**）

$$\text{van Wee 链}:\ \varepsilon|A|\ \le\ \sum_{x\in A}E(B(x,1))\qquad(\varepsilon{=}1)$$
$$\text{代 §1 恒等式}:\ 1024-M\ \le\ 121M-4(N_1{+}N_2)-11264\ \Longrightarrow\ \boxed{4(N_1{+}N_2)\ \le\ 122M-11288}\ ✓$$
$$\text{（}M{=}106:\ N_1{+}N_2\le411;\quad M{=}120:\ \le838\ \text{—— 实测 }199\ \text{远小于上界}）$$
$$\text{即}\ \boxed{\text{本档自证出档案所述之"}\textbf{上界}\text{"（}\sum E(z)|A\cap B(z,1)|\ \text{型量可反向控制 }N_1{+}N_2\text{）}}✓$$

## §3 ③ 缺口仍存（**诚实 ✗**）

$$\text{下界（Cauchy--Schwarz，}M{=}106\text{）}:\ 2(N_1{+}N_2)=\sum_x\binom{\mu(x)}2\ \ge\ \frac{(11M)^2/1024-11M}{2}\ \Longrightarrow\ N_1{+}N_2\ \ge\ 117$$
$$\therefore\ M{=}106:\qquad \boxed{117\ \le\ N_1{+}N_2\ \le\ 411}\qquad(\text{缺口显著，未闭合}) ✗$$
$$\text{欲闭合需}:\ \text{上界}\le116,\ \text{即}\ 122M-11288\le464\ (M{=}106)\ \Longrightarrow\ 1644\le464\ \textbf{假} ✗$$

## §4 ★ ④ $\theta$ 精化与门槛表（**$\theta_0{=}6$ 恰给 107 ✓，但不可达**）

$$\text{van Wee 之实质}:\ |A|\ \le\ \theta\,E_{\rm tot},\qquad \theta:=\frac{\sum_{z\in Z}E(z)|A\cap B(z,1)|}{E_{\rm tot}}\qquad(\text{Lemma 51 给逐点 }|A\cap B(z,1)|\le n-R=9)$$
$$\therefore\ M\ \ge\ \frac{1024(1+\theta_0)}{1+11\theta_0}\qquad(\theta_0\ \text{为普适上界})$$
| $\theta_0$ | $M\ge$ | $\lceil\cdot\rceil$ |
|---|---|---|
| $9$ | $102.4000$ | $\mathbf{103}$（＝van Wee） |
| $8$ | $103.5506$ | $104$ |
| $7$ | $105.0256$ | $106$ |
| $\mathbf{6}$ | $\mathbf{106.9851}$ | $\mathbf{107}$ ★ |
| $5$ | $109.7143$ | $110$ |
| $4$ | $113.7778$ | $114$ |

$$\textbf{但实测（120-code）}:\ \theta=2460/296=\mathbf{8.3108}\ \Longrightarrow\ \text{任何普适 }\theta_0\ge8.31\ \Longrightarrow\ \text{该路线之极限}\ \approx\boxed{104}\ ✗$$
$$\therefore\ \boxed{\text{$\theta$ 精化\ \textbf{不能}达 107（}\because\ \text{120-code 本身 }\theta{=}8.31>\theta_0)}}$$

## §5 附带核验（**✓**）

$$\varepsilon\ \text{不可提升到 }3:\ E(B(x,1))\ \text{为奇数且 min}{=}1\ (\text{分布 }\{1{:}338,3{:}417,5{:}106,7{:}29,9{:}8,11{:}6\})$$
$$\qquad \text{若 }\varepsilon{=}3\Rightarrow 3(1024-M)\le9E\Rightarrow M\ge120.47\Rightarrow121>120\ \textbf{矛盾}\ \Longrightarrow\ \varepsilon{=}1\ \text{为真上限}\ ✓$$

## §6 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "自证恒等式" "N1N2上界" "theta门槛"
技术词 自证恒等式   命中文件数=0    ::
技术词 N1N2上界   命中文件数=0    ::
技术词 theta门槛   命中文件数=0    ::
```

## §7 边界（硬 ✓）

- **自证 ＋ 120-code 全量实测核验** ✓；**不占 C 号** ✓；**不作方向性决策** ✗；不跨空间 ✓
- 外部内容**未受信任** ⚠️；**不主张** $106$ 已排除 ✗（V290）；**不主张** $\theta_0\le8$ 可证 ✗
