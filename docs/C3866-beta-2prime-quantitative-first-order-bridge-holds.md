已查地图（**先查后写**）：`C-3865`（**β-2 首轮 VOID：LP 符号错** ✓✓）、`C-3864`（**β-1′：`t^*_{\mathrm{full}} = 0`；control `t^* = +1`；KKT 基准** ✓✓）。回查见 §5 ✓

D0: 本档对象 = **C-380-66：B1-β-2′（符号修正版）—— 定量一阶 odd→even 桥常数**（唐先生 2026-09-21 22:40 发令）
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（七条 ✓✓）

$$\textbf{① 修正后的 LP}✓✓：\ \min_{h,c}c✓\ \text{s.t.}\ \boxed{v_{13}h \le -1}✓,\ \boxed{v_{19}h \le -1}✓,\ \boxed{Wh - c\mathbf 1 \le 0}✓✓$$

$$\qquad \text{（}\textbf{符号纪律}✓✓：行}\ [v_{13},0]\ \text{配}\ b = -1✓\ \text{（不是}\ [-v_{13},0]\ \text{配}\ +1✗）\ ——\ \text{这正是}\ C\text{-}3865\ \text{的错处}✓✓$$

$$\textbf{② 两个 primal 版本同时跑（唐先生①）}✓✓$$

$$\qquad \textbf{无界版}✓：\text{status} = 0\ \text{（有限最优}✓） \Longrightarrow \boxed{c_{\mathrm{full}}^{\mathrm{unb}} = 0.500808953629}✓✓$$

$$\qquad \textbf{压缩版}（\|h\|_\infty \le 1✓）：\boxed{c_{\mathrm{full}}^{\mathrm{box}} = 0.500808953629}✓✓ \Longrightarrow \textbf{两版一致}✓✓$$

$$\qquad \qquad \text{原因}✓：\text{最优}\ h\ \text{的}\ \|h\|_\infty = 0.04896 \ll 1✓ \Longrightarrow \textbf{box 未 binding}✓✓$$

$$\textbf{③ 与}\ C\text{-}3864\ \textbf{的交叉校验（强 sanity）}✓✓$$

$$\qquad \text{先验推论}✓✓：t^*_{\mathrm{full}} = 0⟹\textbf{不存在六项皆负的方向}✓✓ \Longrightarrow \boxed{c_{\mathrm{full}} \ge 0\ \textbf{必成立}}✓✓$$

$$\qquad \text{实测}✓✓：c_{\mathrm{full}} = +0.500809 \ge 0✓ \Longrightarrow \boxed{\text{交叉校验 OK}}✓✓\ \text{（若}\ < 0\ \text{则必是实现的错}✓）$$

$$\qquad 40\ \text{dps}✓✓：a_{13} = \mathbf{-1.0}✓,\ a_{19} = \mathbf{-1.0}✓（归一化饱和✓）；\ \max_q(b_q - c) = 8.46\times10^{-16}✓✓$$

$$\textbf{④ 对偶证书（唐先生③）}✓✓$$

$$\qquad \text{标准形式的 marginals 带负号}⚠️✓ \Longrightarrow \textbf{纯符号约定问题}✓（本档已改正✓）：$$

$$\qquad \boxed{\nu_{13} = +0.452590 \ge 0}✓,\qquad \boxed{\nu_{19} = +0.048219 \ge 0}✓,\qquad \boxed{\mu = (0.4196,\ 0.4957,\ 0.0210,\ 0.0637) \ge 0}✓✓$$

$$\qquad \boxed{\sum_q\mu_q = 1}✓✓,\qquad \boxed{c_{\mathrm{full}} = \nu_{13} + \nu_{19} = 0.500809}✓✓\ \text{（与 primal 吻合到求解器精度}✓）$$

$$\qquad ⚠️ \textbf{待加固}✓：|\ c_{\mathrm{primal}} - c_{\mathrm{dual}}\ |\ \text{的}\ \textbf{高精度 gap}（\text{现为求解器精度} \sim10^{-9}✓）\ \text{须下一刀用}\ 40\ \text{dps 重算}✓$$

$$\textbf{⑤ odd-only control（唐先生④）}✓✓：\text{删去四条}\ b_q\ \text{行} \Longrightarrow \text{LP status} = 3\ \text{（unbounded）}✓✓$$

$$\qquad \Longrightarrow \boxed{c_{\mathrm{control}} = 0}✓✓\ \text{（}\textbf{由 LP 得出}✓，\ \textbf{非预填}✗✓：}\text{"no finite impedance"✓）$$

$$\textbf{⑥ ⭐ 判词（唐先生表格）}✓✓：\ c_{\mathrm{full}} > 0✓,\ c_{\mathrm{control}} = 0✓,\ \text{primal／dual CLOSED（差一项高精度 gap}⚠️\text{）} \Longrightarrow$$

$$\qquad \boxed{\text{定量一阶 odd} \to \text{even 桥}\ \textbf{成立}}✓✓\ \text{（局部）};\qquad \boxed{D(h) = \delta \Longrightarrow E(h) \ge 0.500809\,\delta}✓✓\ \text{（候选常数}✓）$$

$$\qquad \text{解读}✓✓：\textbf{任何}\ \text{把两条 active odd 分支同时压低}\ \delta\ \text{的方向}✓,\ \text{必然使}\ \textbf{至少一个}\ \text{active 偶频增加}\ \ge 0.5008\,\delta✓✓$$

$$\qquad \Longrightarrow\ \text{这是}\ C\text{-}3864\ \text{的 B3（定性）}\ \textbf{升级为定量}✓✓\ \text{—— 第一个}\ \textbf{可计算、可证书化的正常数}✓✓$$

$$\textbf{⑦ 纪律}✓✓：\text{本档}\ \textbf{不}碰}\ (\lambda,\omega)\ \text{比例审计}✗✓（遵唐先生令："先不要碰"✓）；\ \text{该审计}\ \text{登记为下一刀}✓$$

## §1 数值记录（数字驱动 ✓✓）

```
点：残差 1.6e-15（x = [0.80093022, 0.5611432, 0.70245716, 0.6261014, 0.86884389]）
(1) 无界版：status=0，c_full = 0.500808953629，h = [0.024405, 0.01462, -0.018416, 0.02306, 0.048962]
(2) 压缩版 |h|inf<=1：c_full = 0.500808953629（同值）；约束残差 <= 0 全部成立；box duals 全 0
    对偶（改正符号后）：nu13 = +0.452590, nu19 = +0.048219；mu = [0.4196, 0.4957, 0.0210, 0.0637]；sum(mu) = 1
    c_full = nu13 + nu19 = 0.500809（吻合到求解器精度）
    40 dps：a13 = -1.0, a19 = -1.0；max_q(b_q - c) = 8.46e-16
    交叉校验（t*=0 => c_full >= 0）：c_full = +5.008e-01 -> OK
(3) control（删 b 行）：status=3（unbounded）-> c_control = 0（无有限阻抗）
(4) (lambda,omega) 比较：按令未做
```
- 脚本 ✓：`scripts/c380_66_beta2prime.py`✓；输出 ✓：`scripts/out_c380_66_beta2p.txt`✓

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| 符号修正版 LP ✓ | **完成** ✓✓ |
| `c_{\mathrm{full}}`（无界／box） ✓ | **0.500808953629（两版一致）** ✓✓ |
| 与 `C-3864` 交叉校验 ✓ | **OK（`\ge 0`）** ✓✓ |
| primal／dual ✓ | **CLOSED（高精度 gap 待加固）** ⚠️✓ |
| `c_{\mathrm{control}}` ✓ | **0（LP 得出：unbounded）** ✓✓ |
| **判词** ✓ | **定量一阶桥成立（局部）** ✓✓ |
| `(\lambda,\omega)` 比例审计 ✓ | **未做（遵令，下一刀）** ✗✓ |
| 全局 `V_\sigma` 证书 ✓ | **未** ✗✓ |

## §3 边界（不得声称 ✗✓）

- **不**声称全局最优／`V_\sigma` 的真值 ✓
- **不**声称该桥已连接到 arithmetic bridge（尚未）✓
- **不**声称 `(\lambda,\omega)` 的比例关系（未审计）✓
- **不**把 `c_{\mathrm{control}} = 0` 解释为"偶频约束可删"（恰相反：它是唯一阻抗来源）✓

## §4 本档**不**做的事 ✓✓

$$\textbf{不}碰}\ (\lambda,\omega)✗；\ \textbf{不}改}\ V_\sigma\ \text{记号}✗；\ \textbf{不}开全局证书工程}✗✓$$

## §5 【技术词回查】输出（**先跑后写** ✓）

```
技术词 定量一阶桥  命中文件数=0    :: 
技术词 对偶符号约定 命中文件数=0    :: 
技术词 阻抗常数     命中文件数=0    ::
```

## §6 下一步（须唐先生发令 ✓）

$$\textbf{① 高精度 gap}✓✓：40\ \text{dps 重算}\ c_{\mathrm{primal}} - (\nu_{13} + \nu_{19})✓\ \text{并给位数}✓$$
$$\textbf{② }(\lambda,\omega)\ \textbf{比例审计}✓（\text{现才允许}✓）：\text{检验}\ \mu \stackrel{?}{=} \lambda/\textstyle\sum\lambda✓\ \text{与}\ \nu \stackrel{?}{=} \text{比例}\ \omega✓✓\ \text{（若成立} \Longrightarrow \textbf{KKT 几何} \Rightarrow \textbf{定量 Farkas 分离}✓✓）$$
$$\textbf{③ 尺度敏感度}✓：\text{box 半宽对}\ c_{\mathrm{full}}\ \text{的影响}✓（\text{本档未 binding}✓）；\ \text{以及}\ \delta\ \text{的二阶效应对桥的修正}✓$$
