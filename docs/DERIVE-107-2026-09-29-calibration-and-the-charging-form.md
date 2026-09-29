# DERIVE-107（2026-09-29）—— **小 $n$ 校准 ＋ 目标的\ \textbf{充电形式}（系数 $6$）**

> **性质**：**纯推导（无引用）**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-29 12:5x ✓
> **唐先生令**：「自己推导，不要再想论文」✓

**已查地图**：`GATE-107-STATUS`（八族上限）／`29w`（cell 天花板）／`29x`（excess 逆趋势）✓

D0: 本档对象 ＝ **档案已有**（$K(n,1)$ 数值／$E$／$\mu$——无新数学对象 ✓）
D1: 0（产出＝**校准表 ＋ 目标之等价充电形式 ＋ 系数 $6$ 之定位** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✓ 校准（新）}:\ \text{不等式型机制在 }n{=}9\ \text{系统性短 }5{-}10\%;\ \text{且 SDP }\textbf{不支配}\ \text{van Wee}}$$
$$\boxed{\text{② ✓ 目标之\ \textbf{等价形式}}:\ K(10,1)\ge107\iff \boxed{6E+M\ge1024}\iff 67M\ge7168\ (E{=}11M{-}1024)}$$
$$\boxed{\text{③ ✓ 充电解释}:\ \iff \#\{\text{非码字}\}\le6\cdot\underbrace{\textstyle\sum_x(\mu(x)-1)}_{\text{excess 总量}}\ ——\ \text{即"每个非码字至多耗 }6\ \text{个 excess 单位"}}$$
$$\boxed{\text{④ ✗ 但已用之充电（深洞）只到 }9:\ \text{实测 }\frac{\sum_{x\in A}E(B(x,1))}{E}=8.31\Longrightarrow\ \text{该路线顶在 }9,\ \text{不足}}$$

## §1 ① 校准表（**✓ 新、有信息量**）

| $n$ | 真值 $K(n,1)$ | 球界 | van Wee $2^n/n$ | 真−球 | 真−vW |
|---|---|---|---|---|---|
| $4$ | $4$ | $4$ | $4.0$ | $0$ | $0.0$ |
| $5$ | $7$ | $6$ | $6.4$ | $1$ | $0.6$ |
| $6$ | $12$ | $10$ | $10.7$ | $2$ | $1.3$ |
| $7$ | $16$ | $\mathbf{16}$ | $18.3$ | $0$ | $-2.3$ |
| $8$ | $32$ | $29$ | $\mathbf{32.0}$ | $3$ | $0.0$ |
| $9$ | $62$ | $52$ | $56.9$ | $10$ | $\mathbf{5.1}$ |
| $10$ | $\ge107$ | $94$ | $103$ | $\ge13$ | $\ge4.6$ |

$$\textbf{读数}:\ \text{（i）}n{=}7\ \text{球界\ \textbf{紧}};\ n{=}8\ \text{van Wee\ \textbf{紧}}\Longrightarrow \text{各机制都\ \textbf{可能}紧}✓$$
$$\text{（ii）}n{=}9:\ \text{真值 }62;\ \text{球界 }52\ (-10);\ \text{van Wee }57\ (-5);\ \textbf{SDP-2025 }55.35\ (\text{比 van Wee \textbf{还差}})✓$$
$$\therefore\ \boxed{\text{SDP\ \textbf{不支配}\ 组合不等式}\Longrightarrow\ \text{组合型改进有空间}}✓$$
$$\text{（iii）}n{=}10:\ \text{从 }105.2223\ \text{到 }107\ \text{仅需 }+1.68\%\ ——\ \text{远小于 }n{=}9\ \text{处 }8\%\ \text{的缺口}\Longrightarrow \textbf{非无望}✓$$

## §2 ② 目标之等价形式（**✓ 精确**）

$$\text{设 }E=11M-1024\ (\text{恒等式})。\ \text{则}\ K(10,1)\ge107\iff M\ge106.99\iff$$
$$\boxed{6E+M\ \ge\ 1024}\iff \boxed{67M\ \ge\ 7168=7\cdot2^{10}}\iff 6(11M-1024)+M\ \ge\ 1024$$
$$\text{（数值}:\ M{=}106\Rightarrow 6\cdot142+106=958<1024\ ✗;\ M{=}107\Rightarrow 6\cdot153+107=1025\ge1024\ ✓）$$
$$\therefore\ \text{目标}＝\text{证}\ 6E+M\ge1024\ \text{对一切覆盖码}$$

## §3 ③ 充电解释（**✓ 可操作**）

$$\#\{\text{非码字}\}=1024-M;\qquad E=\sum_x(\mu(x)-1)=\text{覆盖之"多余量"}$$
$$6E+M\ge1024\iff 1024-M\le6E\iff \boxed{\text{每个非码字可被"记到"至多 }6\ \text{个 excess 单位上}}$$
$$\textbf{已用之充电（van Wee）}:\ 1024-M\le\sum_{x\in A}E(B(x,1))\le9E\ \Longrightarrow\ \text{系数 }9\ (\text{给 }102.4)✗\ \text{不足}$$
$$\text{实测（120-code）}:\ \sum_{x\in A}E(B(x,1))=2460,\ E=296\Longrightarrow \text{比值 }8.31\ ——\ \textbf{离 }9\ \text{很近}\Longrightarrow\ \text{此路榨干}✗$$
$$\therefore\ \boxed{\text{须一条\ \textbf{不同的}充电（非深洞球-excess），其系数 }6}$$

## §4 ④ 可核对之数值（**✓ 实测**）

| 码 | $M$ | $E$ | $\dfrac{1024-M}{E}$ | $\le6$? |
|---|---|---|---|---|
| 120-code | $120$ | $296$ | $3.05$ | ✓（裕度大） |
| greedy | $148$ | $604$ | $1.45$ | ✓ |
| greedy | $152$ | $648$ | $1.35$ | ✓ |
| **假设** $106$ | $106$ | $142$ | $\mathbf{6.46}$ | **✗** |

$$\therefore\ \text{该不等式对 }M\ge120\ \text{裕度很大，只在 }M{=}106\ \text{处失效}\Longrightarrow\ \textbf{证实它就是目标本身}✓$$

## §5 下一步（**纯推导，具体 ✓**）

$$\textbf{1.}\ \text{找一条与深洞球-excess \textbf{不同}的充电：候选载体}:\ \text{私有点之 owner 结构}\ /\ \text{距离-2 对之端点}\ /\ \text{二阶重叠之\textbf{加权}}$$
$$\textbf{2.}\ \text{判据}:\ \text{若该充电给系数 }c,\ \text{则推出 }M\ge\frac{1024(c+1)}{11c+1};\ c{=}6\Rightarrow107,\ c{=}9\Rightarrow103\ (\text{故须 }c\le6)$$
$$\textbf{3.}\ \text{已验证之边界}:\ \text{深洞路线 }c{=}9\ (\text{实测 }8.31,\ \text{紧})\Longrightarrow \text{必须换载体}✓$$

## §6 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "小n校准" "充电形式" "系数6"
技术词 小n校准    命中文件数=0    ::
技术词 充电形式    命中文件数=0    ::
技术词 系数6     命中文件数=0    ::
```

## §7 边界（硬 ✓）

- **数值全部实测／算术核对** ✓；**不占 C 号** ✓；**不作方向性决策** ✗
- **不主张**已得 107 ✗；**不主张**不可达 ✗（V290）
