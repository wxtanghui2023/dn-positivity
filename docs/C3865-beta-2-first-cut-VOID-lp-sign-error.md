已查地图（**先查后写**）：`C-3864`（**β-1′：出口 B3（一阶形式）；`t^*_{\mathrm{full}} = 0`；control `t^* = +1`** ✓✓）、`C-3863`（**α-3 CLOSED；`\lambda,\omega` 基准** ✓✓）。回查见 §4 ✓

D0: 本档对象 = **C-380-65：B1-β-2a/b/c/d 首轮（LP 定量常数）—— VOID：约束符号错误（自检捕获）**（唐先生 2026-09-21 22:38 发令）
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（六条 ✓✓）

$$\textbf{① 档位}✓✓：\text{按}\ \beta\text{-2a/b/c/d}：\text{定义}\ D(h) = -\max\{a_{13}(h), a_{19}(h)\}✓,\ E(h) = \max_q[b_q(h)]_+✓✓；\ \text{单位 odd 下降 LP}✓；\ \text{独立 primal／dual 认证}✓；\ \text{odd-only control}✓；\ \text{最后才比}\ (\lambda,\omega)✓✓$$

$$\textbf{② ⚠️ 结果：}\textbf{VOID（约束符号错误，自检捕获）}✗✓$$

$$\qquad \text{实现错写}✗：\text{行}\ [-v_{13}, 0]\ \text{配}\ b = +1✓ \Longleftrightarrow \boxed{a_{13}(h) \ge -1}✗✗\ \text{（方向反}✓）$$

$$\qquad \text{应为}✓✓：a_{13}(h) \le -1 \Longleftrightarrow \text{行}\ [v_{13}, 0]✓\ \text{配}\ b = -1✓✓\ \text{（}a_{19}\ \text{同}✓）$$

$$\qquad \textbf{症状（矛盾即证据）}✓✓：\text{错版压缩 LP 给出}\ c = -14.8063885032 < 0✓\ \text{与}\ \text{四偶频皆降}✓;$$

$$\qquad \qquad \text{但}\ C\text{-}3864\ \text{已证}\ t^*_{\mathrm{full}} = 0⟹\textbf{不存在六项皆负的方向}✓✓ \Longrightarrow \textbf{两者不可同时成立}✓✓ \Longrightarrow \text{错版必假}✓✓$$

$$\qquad \Longrightarrow\ \textbf{该轮全部数字作废}✗✓\ \text{（不进任何账本}✗✓）$$

$$\textbf{③ 本轮}\textbf{不}产生判词}✗✓：c_{\mathrm{full}}／c_{\mathrm{control}}\ \text{均未定}✗✓；\ (\lambda,\omega)\ \text{比较}\ \textbf{未做}✗✓\ \text{（遵唐先生"最后才比"的顺序}✓✓）$$

$$\textbf{④ 副产出的有效观察}✓✓：\text{切平面／LP 路径本身}\ \textbf{可运行}✓；\ \text{且}\ \text{符号约定}\ \textbf{必须由}\ C\text{-}3864\ \text{的}\ t^* = 0\ \text{反向校验}✓✓$$

$$\qquad \Longrightarrow\ \text{登记为}\ \textbf{硬审计规则}✓✓：\boxed{\text{任何 LP 结果必须与已知的}\ t^*\ \text{结论互相校验}}✓✓$$

$$\textbf{⑤ 已知可用的锚点}✓✓：\ C\text{-}3864\ \text{的}\ \text{full\/control 对}\ (t^* = 0\ \text{vs}\ +1)✓；\ \text{KKT 基准}\ \lambda = (0.8379, 0.9897, 0.0419, 0.1273)✓,\ \omega = (0.9037, 0.0963)✓✓$$

$$\textbf{⑥ 账本（见 §2）}✓✓$$

## §1 数值记录（数字驱动 ✓✓；**全部 VOID** ✗）

```
（符号错误版本，仅作痕迹）
[UNBOUNDED-h] status=3 "The problem is unbounded"
[|h|inf<=1]  c = -14.8063885032, h = [1, 0.89613, 1, -0.260672, -1]
[|h|inf<=0.25] c = -3.7015971258
recession 检查：因 vstack 维度错误崩溃（5 vs 6）
```
- 脚本 ✓：`scripts/c380_65_beta2.py`（v1，崩溃）、`scripts/c380_65_beta2_v2.py`（v2，符号错）✓；输出 ✓：`scripts/out_c380_65_beta2.txt`✓

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| `D(h), E(h)` 定义 ✓ | **已写（未生效）** ⚠️✓ |
| 单位 odd 下降 LP ✓ | **实现有符号错 ⟹ VOID** ✗✓ |
| `c_{\mathrm{full}}` ✓ | **未定** ✗✓ |
| primal／dual 认证 ✓ | **未做** ✗✓ |
| odd-only control ✓ | **未做** ✗✓ |
| 与 `(\lambda,\omega)` 比较 ✓ | **未做（按顺序本应最后）** ✗✓ |

## §3 下一步（须唐先生发令 ✓）

$$\textbf{修正版}✓✓：\text{行}\ [v_{13}, 0]\ \text{配}\ b = -1✓；\ [v_{19},0]\ \text{配}\ b = -1✓；\ [W, -1]\ \text{配}\ b = 0✓✓$$
$$\qquad \text{并}\ \text{同时跑：}\textbf{压缩版}（|h|_\infty \le 1✓）\ \text{与}\ \textbf{无界版}✓ \Longrightarrow \text{判定}\ c_{\mathrm{full}}\ \text{是否有有限最优}✓✓$$
$$\qquad \text{再}\ \text{用}\ t^* = 0\ \text{交叉校验}✓✓（\text{硬规则}✓）;\ \text{随后 primal／dual ＋ control ＋ 最后比}\ (\lambda,\omega)✓✓$$

## §4 【技术词回查】输出（**先跑后写** ✓）

```
技术词 符号错误自检 命中文件数=0    :: 
技术词 紧化归一化  命中文件数=0    :: 
技术词 定量桥常数  命中文件数=0    ::
```
