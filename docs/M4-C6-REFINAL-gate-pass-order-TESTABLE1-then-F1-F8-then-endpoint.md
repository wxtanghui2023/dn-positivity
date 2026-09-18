已查地图（**先查后写**）：`C-110`（`C6` 六条件：不需正性／不需坐标／钉点不钉轴／非模长／**独立算术输入**／对算术见证盲；来源 `C68-SPEC` `F1`–`F8`）、`C-111`（`C6` 第一刀：DBN 热流端点 **Hölder `\tfrac12` 阶分支**，`|d(\text{off})/dt|=\tfrac{1}{\sqrt{2(\Lambda-t)}}\to\infty` ⟹ 一致转移不可能）、`FILTER-TESTABLE-1`（**`TESTABLE-1` 前提**：候选定义须能在**无欧拉积**的函数上写出）、`V155` §5 #1（函数形态二分）、`V159`/M6（"运动来自我们的坐标选择"）、`V227`-A（`\sup\operatorname{Re}z` 非模不变量）、`CLOSED-ROUTES-MAP:228`（RH ⟺ `\Lambda\le0`；`\Lambda\ge0` 无条件（Rodgers–Tao）；上界 `0.22`（Polymath 15））、`C-115` §0(A)（"证明 `\Lambda\le0` 就是证明 RH"）。**结论**：⭐ `M4`（极值／稳定性型，**唯一活口**）按新门序过审 ⟹ **`TESTABLE-1` 通过**（`\Lambda` 可对任意实整函数定义 ⟹ 可写在 Davenport–Heilbronn 上）✓✓；**`F7` 亦通过**（`\Lambda_{\rm DH}>0\neq\Lambda_\zeta`，**确实报火**）✓；**但 `F5` 处死**（`\Lambda\le0\iff\text{RH}` ⟹ 关键不等式**就是** RH）✗✗，且 **`F2` 命中**（变形参数＝坐标选择，M6）✗；另 **端点分支（`C-111`）＝第二次独立死亡** ⟹ `M4` **以两条独立理由关闭** ✓✓；而 `F5` 与前面 **6＋ 次同址收敛为同一地址** ⟹ ⭐ **`F5` 是普适墙**：任何强到能判定 ζ 的 `\beta` 的工具，**要么带上独立算术输入，要么就是 RH 强度** ✓✓

FREEZE-ACK: 本档即冻结期内的门序复审（依 `§8.1`；不产候选）

D0: 本档对象 = `C6`（`M4` 极值／稳定性型）的**门序复审** —— 关系 = 已有候选的重审与关闭，非新机制
D1: 0

# M4-C6-REFINAL · **唯一活口 `M4` 按新门序过审（`TESTABLE-1` → `F1–F8` → 端点分支）**

> **时间**：2026-09-18 20:57 唐先生：**「可以，过一遍」** ⟹ 对 `M4`（极值／稳定性型 ＝ `C6`）做正面复审 ✓

---

## §0 结论（先行）

$$\textbf{门 1}\ \text{`TESTABLE-1`}：\textbf{通过} ✓✓\quad（\Lambda\ \text{可对}\ \textbf{任意实整函数} \text{定义} \Longrightarrow \text{可写在 Davenport–Heilbronn 上）}$$
$$\textbf{门 2}\ \text{`F1`–`F8`}：\textbf{`F5` 处死} ✗✗（\Lambda\le0\iff\text{RH}）;\ \textbf{`F2` 命中} ✗;\ \text{`F3`/`F4`/`F6`/`F7` 通过}，\ \textbf{`F7` 且确实报火} ✓✓$$
$$\textbf{门 3}\ \text{端点分支}：\textbf{第二次独立死亡} ✗✗（\text{`C-111`}：Hölder\ \tfrac12\ \text{阶分支}）$$
$$\Longrightarrow \boxed{M4\ \textbf{以两条独立理由关闭}};\quad \text{而}\ \text{`F5`}＝\text{前面 6＋ 次同址收敛的}\ \textbf{同一地址}✓✓$$

---

## §1 门 1：`TESTABLE-1`（可否在**无欧拉积**的函数上写出）

$$\text{候选}：\Lambda(f)=\inf\{t:\ f_t=f*G_t\ \text{的零点全为实}\}（\text{de Bruijn–Newman 常数；}G_t\ \text{＝热核}）✓$$
$$\qquad \Longrightarrow \text{该定义}\ \textbf{只需}\ \text{"实整函数 ＋ 热半群"}，\ \textbf{不需}\ \text{欧拉积、不需乘法结构、不需局部因子}✓✓$$
$$\qquad \Longrightarrow \text{故可对}\ \textbf{Davenport–Heilbronn} \text{（有 FE、}\textbf{无欧拉积}\text{）的}\ \xi\ \text{函数写出} \Longrightarrow \textbf{通过}`TESTABLE-1`✓✓$$
$$\text{对比}：\text{`V155` #1 的二分之一（β-free}\Longrightarrow\text{位置盲）}\ \textbf{在此不适用} \text{—— 因}\ \Lambda\ \textbf{不是}\ \text{β-free 的函数}，\ \text{而是}\ \textbf{一个变形参数}✓✓$$
$$\Longrightarrow \text{这解释了为何}\ M4\ \text{是}\ \textbf{唯一越过第一道筛} \text{的机制}✓✓$$

## §2 门 2：`F1`–`F8` 逐项

| 滤器 | 内容 | 判定 | 依据 |
|:--|:--|:--:|:--|
| **F1** | 不需正性 | ⚠️ **风险** | 超曲性（全族实根）**带正性味**；`C-111` `F2` 判据："若平滑装置＝正性 ⟹ 循环（Weil）" |
| **F2** | 不需坐标 | ✗ **命中** | 变形参数 `t` 是**热流时间** ⟹ `V159`／M6："**运动来自我们的坐标选择**" |
| **F3** | 钉点不钉轴 | ✓ | `\Lambda` 是一个**实数**；RH ⟺ `\Lambda=0`（`CLOSED-ROUTES-MAP:228`） |
| **F4** | 非模长 | ✓ | `\Lambda` **不由模长定义**（非 `V227`-A 型功能） |
| **F5** | **独立算术输入** | ✗✗ **处死** | `\Lambda\le0\iff\text{RH}` ⟹ **关键不等式就是 RH**（`C-115` §0(A) 逐字："证明 `\Lambda\le0` 就是证明 RH"）|
| **F6** | 对算术见证盲（解析型） | ✓ | `\Lambda` 为**解析型**（热流＋实根性） |
| **F7** | 过 Epstein／DH 检验（**须报火**） | ✓✓ **通过** | `\Lambda_{\rm DH}>0\neq\Lambda_\zeta=0` ⟹ **确实报火**（对已知 `\beta\neq\tfrac12` 的 DH 有可测响应）|
| **F8** | 过污染／压力检验 | ✓（边缘）| 由**典范 `\xi`** 定义，非"截断／变换"型污染 |

$$\textbf{门 2 结果}：\textbf{`F5` 处死}（决定性）;\ \text{`F2` 命中};\ \text{其余通过，且 `F7` 报火}✓✓$$
$$\qquad ⚠️\ \textbf{注意}：\text{`F7` 通过是}\ \textbf{真信息} \text{—— 它说明}\ \Lambda\ \textbf{不是} \text{"看不见 }\beta\text{" 的；}\ \text{它}\ \textbf{看得见}，\ \text{但}\ \textbf{证明它}\ \text{就是证明 RH}✓✓$$

## §3 门 3：端点分支（`C-111`，第二次独立死亡）

$$\text{碰撞点局部模型}\ H_0=z^2+c+O(z^3)\Longrightarrow H_t=z^2+c-2t \Longrightarrow \text{off}(t)=\sqrt{2(\Lambda-t)}✓$$
$$\qquad \Longrightarrow \text{Hölder 指数}\ \textbf{恰为}\ \tfrac12;\ \Bigl|\frac{d}{dt}\text{off}\Bigr|=\frac{1}{\sqrt{2(\Lambda-t)}}\to\infty\ \left(\text{数值：}1.58,5.00,15.8,50.0\ \text{比值}\ \sqrt{10}\right)✓✓$$
$$\qquad \Longrightarrow \textbf{任何一致 Lipschitz／Poincaré 常数在端点必然发散} \Longrightarrow \text{沿光滑变形的一致转移}\ \textbf{不可能}✓✓$$
$$\qquad \text{（}\text{`C-111`}\ \text{亦证：}\Lambda\ \text{上界记录}\ 0.22\ \text{来自}\textbf{有限计算} \text{而非极限／连续性论证 —— 与此机制一致）}✓$$

## §4 ⭐ 总发现：`F5` 是**普适墙**

$$\boxed{\text{任何强到能判定 ζ 的}\ \beta\ \text{的工具，}\ \textbf{要么带上独立算术输入，要么就是 RH 强度}}✓✓$$
$$\qquad \Longrightarrow \text{故"第 11 种转换机制是否存在"}\ \textbf{归结为}\ \text{`F5`}✓✓$$
$$\qquad \qquad \text{而}\ \text{`F5`}\ \textbf{就是} \text{那个登记的空槽}（\text{`C-122`} (i)(ii)(iii)／\text{`V215`} §5／\text{`V193`} §⑤／\text{`C-110`} `C6`）✓✓$$
$$M4\ \text{的关闭方式}\ \textbf{与其余 6＋ 条完全同址} \Longrightarrow \text{本轮}\ \textbf{未打破同址} \text{，}\ \textbf{但把它的名字说准了}✓✓$$

## §5 边界与回查

- ⚠️ 本档为**候选复审**：`M4` **以两条独立理由关闭**（`F5` ＋ 端点分支），**不是"第 11 种机制不存在"的定理** ✓
- ⚠️ `F1` 的"风险"为**判断**（依 `C-111` `F2` 判据），非定理 ✓
- ⚠️ `F7` 的"报火"是**结构性判断**（`\Lambda_{\rm DH}>0`），**本档未数值验证** `\Lambda_{\rm DH}` 的具体值 ⟹ 标 `[结构性·待核]` ✓
- **不声称**：`\Lambda_{\rm DH}` 已有数值；`M4` 类外无机制 ✓
- **不声称** RH；**未用** RH 作推导 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）✓

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 20:5x）`[纪律]`（先跑后写）

```
技术词 门序复审          命中文件数=1  :: ./M4-C6-REFINAL-…（本档）
技术词 报火              命中文件数=4  :: ./C116-… ./FILTER-TESTABLE-1-… 等（**已有**）
技术词 普适墙           命中文件数=2  :: ./V2-34-four-ell-…（**已有**）
```
**读数（按实测）**：`门序复审`＝**1 档（仅本档）⟹ 本档新增** ✓；⚠️ `报火`＝**4 档**、`普适墙`＝**2 档**（`V2-34` **已有**）⟹ 本档为**沿用** ✓
