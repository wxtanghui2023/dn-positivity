# AUDIT-2026-09-29i — **一手证据：van Lint--van Wee Thm 5 在 $R{=}1$ **就是** van Wee Thm 16；$(0,10,1)$ 给 **103**；$M{=}106$ 余量 **360** ⟹ 不可能到 107**

> **性质**：**一手文献取证 ＋ 逐位核验**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-29 10:2x ✓
> **唐先生令**：「取一下混合码广义界」✓（且唐先生已自行核算，本档**逐位复核**）

**已查地图**：接续 `AUDIT-29a`（可实现机制上确界 103）／`29f`（复现账）✓

D0: 本档对象 ＝ **档案已有**（mixed bound／excess 分层——无新数学对象 ✓）
D1: 0（产出＝**一手取证 ＋ 等价链确认 ＋ 余量否证** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✓✓ 免费一手全文到手}:\ \text{van Wee 1991 博士论文}\ (220\ \text{页}\ /\ 8{,}278{,}815\ \text{B}\ /\ \text{有文本层})}$$
$$\boxed{\text{② ✓✓ 逐字}:\ "\text{Theorem 16 is generalized for all covering radii }R\ (\text{see }[19,\text{Theorem 5}])"\ \Longrightarrow\ \textbf{Thm 5 在 }R{=}1\ \textbf{即 Thm 16}}$$
$$\boxed{\text{③ ✓✓ }(t,b,R)=(0,10,1)\Rightarrow\ \text{条件 }9E\ge1024-M\Rightarrow M\ge102.4\Rightarrow\boxed{103}\ ——\textbf{不是 107}}$$
$$\boxed{\text{④ ★ }M{=}106:\ \text{余量}=1278-918=\mathbf{360}\ \Longrightarrow\ \textbf{逼不出一个单位}}✗$$

## §1 ① 一手来源（**✓✓**）

$$sources/\text{vanWee-1991-thesis-TUe-353803.pdf}\quad(8{,}278{,}815\ \text{B},\ 220\ \text{页},\ \%PDF{-}1.5)$$
$$\text{目录（逐字）}:\ \text{Paper 5 "Bounds on Packings and Coverings by Spheres in }q\text{-ary and Mixed Hamming Spaces"}\ (p.84);\ \text{Paper 6 "Generalized Bounds on Binary/Ternary Mixed Packing- and Covering Codes"}\ (p.101)$$
$$\text{（来源}\ \texttt{https://pure.tue.nl/ws/files/1995874/353803.pdf}\ ——\ \textbf{免费}✓;\ \text{ScienceDirect 反 403}\ ✗）$$

## §2 ② 等价链（**逐字 ✓✓**）

$$\textbf{论文引言逐字}:\ "\text{For }R>1\ \text{things become much more complicated. In a joint work with J.H. van Lint, Jr., }\textbf{Theorem 16 is generalized for all covering radii }R\ \text{(see }[19,\text{Theorem }5])"$$
$$\therefore\ \boxed{\text{van Lint--van Wee [19] Thm 5}\ \big|_{R=1}\ \equiv\ \text{van Wee Thm 16}\ \Longrightarrow\ \text{于 }(t,b)=(0,10)\ \text{给 }102.4\Rightarrow103}✓✓$$
$$\textbf{Theorem 16 逐字（论文 p.97）}:\quad |C|\ \ge\ \frac{(2t+b)3^t2^b}{(2t+b)(1+2t+b)-b}\ (b\ \text{偶});\qquad |C|>\frac{(2t+b)3^t2^b}{(2t+b)(1+2t+b)-2t}\ (b\ \text{奇})$$
$$\text{（}(t,b)=(0,10):\ \frac{10\cdot1024}{110-10}=102.4\ \Rightarrow\ 103\ ✓）$$

## §3 ③ 机制逐字（**✓，与唐先生推导一致**）

$$\textbf{Theorem 5 之判定条件（逐字）}:\quad (2t+b-R)\,P(M)\ \ge\ Q(M),\qquad P(M):=MV(t,b,R)-3^t2^b$$
$$Q(M):=L+\sum_{j=1}^{j^*-1}(j-1)L_j+(j^*-1)\Bigl(\sum_{j=1}^{R}L_j-P(M)\Bigr)$$
$$\textbf{LEMMA 6（逐字）}:\ "\text{If for given }t,b,R,\ M\ \text{satisfies }(10),\ \text{then so does }M+1"\ \Longrightarrow\ M_0\ \text{由\ \textbf{二分}}可得$$
$$\text{于 }(0,10,1):\ \tau_0=1,\tau_1=0\ (\text{两类});\ j^*=1\Longrightarrow Q=L=1024-M\ (\text{逐字相符})$$
$$\therefore\ 9\,E\ \ge\ 1024-M\ \Longrightarrow\ 100M\ge10240\ \Longrightarrow\ M\ \ge\ 102.4\ \Longrightarrow\ \boxed{103}✓✓$$

| $M$ | $E{=}11M{-}1024$ | $L{=}1024{-}M$ | $9E$ | 判定（余量） |
|---|---|---|---|---|
| $102$ | $98$ | $922$ | $882$ | **排除** $(-40)$ |
| $103$ | $109$ | $921$ | $981$ | 允许 $(+60)$ |
| $\mathbf{106}$ | $142$ | $918$ | $1278$ | 允许 $(\mathbf{+360})$ |

$$\text{（唐先生之 }882<922\ \text{与 }981\ge921\ \text{两处\ \textbf{逐位相符}}✓✓）$$

## §4 ★ ④ 对唐先生 §7 之问题的回答（**诚实 ✗**）

$$\text{问}:\ "\text{在 }M{=}106\ \text{时，哪里还有 1 个额外单位可以被迫丢掉}"$$
$$\textbf{答}:\ \boxed{\text{该框架在 }M{=}106\ \text{之余量为 }360\ (\text{需 }1278\ \text{才够，而条件只需 }918)} \Longrightarrow\ \textbf{逼不出任何单位}}$$
$$\therefore\ \text{须使\ \textbf{同一个 }9\ \text{因子}从 }9\ \text{提升到 }\ge12.7\ (\text{即 }12.72\cdot142\ge918\ \text{才勉强卡住})\ \text{或引入\ \textbf{独立新量}}$$
$$\text{而本会话已证}:\ \text{可实现算术族（含 }\theta\ \text{精化）上确界}\approx103{-}104;\ \text{level-3 SDP}=105.2223\Rightarrow106$$

## §5 分层账（**定稿 ✓✓**）

| 层 | 机制 | $n{=}10$ 之界 | 本会话状态 |
|---|---|---|---|
| sphere covering | 球计数 | $94$ | ✓ 可复现 |
| **mixed generalized bound** | van Wee Thm 16 / van Lint--van Wee Thm 5 | $\mathbf{103}$ | **✓✓ 本档一手确认** |
| Habsieger parity / excess | 局部同余 | 同层（$\varepsilon{=}1$） | ✓ 实测全中 |
| Wu--Chen surfeit | 二法算 $\zeta$ ＋ mod-3 | **$n{=}10$ 不适用** | ✗ 已排除 |
| **目标** | — | $\mathbf{107}$ | **未达** |

$$\therefore\ \boxed{\text{mixed 广义界线对 }n{=}10\ \textbf{封闭且只给 }103};\ \text{107\ \textbf{不在}该框架内}}✓✓$$

## §6 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "混合广义界定位" "Theorem16即Thm5" "余量360"
技术词 混合广义界定位    命中文件数=0    ::
技术词 Theorem16即Thm5   命中文件数=0    ::
技术词 余量360        命中文件数=0    ::
```

## §7 边界（硬 ✓）

- **免费一手文献（TU/e 论文）＋ 逐字引证 ＋ 逐位核算** ✓；**不占 C 号** ✓；**不作方向性决策** ✗
- 外部内容**未受信任** ⚠️；**不主张** $107$ 不可达 ✗（V290）；**不主张** Thm 5 之外无更强版本 ✗
- 已归档：`sources/vanWee-1991-thesis-TUe-353803.pdf` ＋ `sources/vanWee-thesis-Paper6-mixed-bounds-EXTRACT.txt`
