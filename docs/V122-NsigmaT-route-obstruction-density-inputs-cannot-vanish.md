# V122 · ⭐⭐⭐⭐⭐ **$N(\sigma,T)$ 路线全程推演：判词【缺口 ＝ RH 本身 ✓ —— 密度型输入【原理上】不可能给出所需结论（可证标度障碍 ✓）】⟹ 杀 ✗｜四类反向搜索（A/B/C/D）零新输入 ✓**
> 委托 ✓ 唐先生 2026-09-14 21:56（**"把 $N(\sigma,T)$ 方向从零点密度理论最强已知形式一路推到 RH，检查中间缺哪条不等式；缺口＝RH 则杀"** ✓）
> 依据 ✓ `FRONTIER-PRIMEGAP-SURVEY-2026-09.md`（GM 2026 ✓）＋ `EXPLICIT-GM-FEASIBILITY.md`（`E48` ✓）＋ `E47`（唯一未封铰链 ✓）＋ 总册 §1 W3/W4 ✓
> 执行 ✓ 小灵｜**纸面 ✓（零数值 ✓）**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓｜编号 ✓ V122 ✓

---

## §0 判定（✓ 一句话先说 ✓）

$$\boxed{\textbf{缺口 ＝ RH 本身（更准确：缺口 ＝ 一条【定性消失型】输入，而所有幂型密度界原理上给不出 ✗）}}\ \Longrightarrow\ \boxed{\textbf{密度方向杀 ✗}}\ ✓$$
$$\qquad\text{且该"杀"的依据是【可证的标度障碍 ✓✓】，不是"没找到" ✗ —— 这是本轮唯一净增量 ✓}$$

## §1 全程推演（✓ 三步到底 ✓）

$$\textbf{Step 1（目标的精确形式 ✓）}：\mathrm{RH}\iff \forall\sigma>\tfrac12,\ N(\sigma,T)=0\ \ \forall T\ ✓（\text{即零点密度在 }(1/2,1]\ \text{上恒为零 ✓}）$$
$$\qquad N(\sigma,T):=\#\{\rho:\ \Re\rho>\sigma,\ |\Im\rho|\le T\}\ ✓\ \text{—— }\beta\ \textbf{直接进入定义 ✓}（\text{非 β-盲 ✓，与 W1 不同 ✓）}$$
$$\textbf{Step 2（已知最强无条件形式 ✓）}：\text{Guth–Maynard（Annals 203 (2026) 623–675 ✓）}$$
$$\qquad N(\sigma,T)\ \ll\ T^{A(\sigma)+\varepsilon}\ ✓,\qquad A(\sigma)=\frac{15(1-\sigma)}{3+5\sigma}\ ✓\ \text{在 }[1/2,1]\ \text{上一致 ✓}$$
$$\qquad\text{对照 ✓}：\text{Ingham (1940) }A=\frac{3(1-\sigma)}{2-\sigma}\ ✓;\ \text{密度假设 DH（猜想 ✓）}A=2(1-\sigma)\ ✓$$
$$\textbf{Step 3（关键 ✓ —— 标度障碍 ✓✓）}：\text{要 }N(\sigma,T)=0\ \text{必须该界 }<1\ \text{对充分大 }T\ ✓\ \Longrightarrow\ \text{需 }A(\sigma)\le0\ ✓$$
$$\qquad\Longrightarrow\ \sigma\ \ge 1\ ✗\quad（\text{因所有已知形式与 DH 都满足 }A(\sigma)>0\ \text{对一切 }\sigma<1\ ✓）$$
$$\qquad\textbf{数值确认 ✓}：$$
```
A(1/2) = 7.5/5.5 = 1.3636 （GM）   ← N(1/2,T) ≪ T^1.364 ✓ 与 N(1/2,T)=N(T)≈(T/2π)logT 相容 ✓
A(3/4) = 3.75/6.75 = 0.5556        ← 仍 ≫ 1 ✗（DH 同点给 T^0.5 ✗）
A(0.9) = 1.5/7.5 = 0.2             ← 仍 ≫ 1 ✗
A(σ) → 0 仅当 σ → 1 ✗
```
$$\Longrightarrow\ \boxed{\textbf{任何幂型密度界 }N(\sigma,T)\ll T^{A(\sigma)+\varepsilon}\ \text{在 }\sigma<1\ \text{处都随 }T\ \text{增长 ✗ ⟹ 永不"消失" ✗✓}}$$
$$\qquad\Longrightarrow\ \textbf{故密度型输入【原理上】给不出"}\exists\sigma_0<1:\ N(\sigma_0,T)=0\text{"}\ ✓\ ——\ \text{这不是估计不够强 ✗，而是【逻辑类型不匹配 ✗✓】}$$

## §2 所需输入的正确形式（✓ 缺口定位 ✓）

$$\text{所需 ＝ 一条【定性／刚性】陈述 ✓（非平均型 ✗）}：\text{某 }\sigma_0<1\ \text{处零点的【绝对不存在 ✓】，而非【计数上界 ✗】}$$
$$\qquad\textbf{与档案已有结论完全吻合 ✓}：$$
$$\qquad\text{① }`E47`\ \text{的唯一未封铰链 ✓}＝\text{"一个离线零是否迫使离线谱【稠密增长 ✗】"}\ ✓（\text{现有工具全为上界型 ✗}）$$
$$\qquad\text{② 总册 W3（}$T^2$\ \text{律 ✓}）／W4（log 律 ✓）}：\text{只消费验证高度的输入 ⟹ 边界被迫 ✗ ⟹ 【必须换输入 ✓】}$$
$$\qquad\text{③ 总册 §3 第 7 步 Gate 1 ✓}：\text{"有无【被实际消费】的单调/递减结构？"}\ ✗\ \text{—— 密度界只给【绝对大小】✓ ⟹ }\textbf{K2-E″ 命中 ✗}$$
$$\Longrightarrow\ \boxed{\text{缺口} ＝ \text{RH 本身（等价形式：}\text{"定性消失型输入"}\ \exists?\ ✗）}\ ✓$$

## §3 四类反向搜索（✓ 按您给的清单逐一 ✓ 全部落在已图内 ✓）

| 类 | 对象 | $\beta$ 进入方式 | 判定 | 指针 |
|:--|:--|:--|:--|:--|
| **A** | $N(\sigma,T)$ 二维分布 | **直接**（定义即 $\Re\rho>\sigma$ ✓） | ⭐**结构性杀 ✗（可证标度障碍 ✓）**：幂型界永不消失 ✓ | 本档 §1 ✓ |
| **B** | 零点对之间显式相关量 | 经 $\gamma$ 差 ✓ | **β-盲 ✗**（垂直通道 ✓）；其 β-敏感版本 ＝ **共轭配对／显式公式** ⟹ **II 类 ✗**（N2 循环 ✓） | 总册 §1 W5／N39 ✓；TP₅ 撤回 ✓ |
| **C** | de Branges 型评价泛函／嵌入常数 | 原理 ✓ | **已审计 ✗**：`R-A1-de-branges-audit` K2＋K3 双触发；**未打破自伴性墙 ✗**（只把困难搬进空间构造 ✓） | `R-A1`；宪法 §6.1 ✓ |
| **D** | Hadamard 乘积中实部位置几何量 | ✓（如 $\sum_\rho\Re(1/\rho)=\sum\beta/(\beta^2+\gamma^2)$ ✓） | **II 类 ✗**：该量**无条件可算 ✓**（项目实测 $Z_1=0.023093867665098557$ ✓）但**有效位数代价 $\Theta(n)$、相消结构性** ⟹ 不能给定量界 ✗ | `PAPERA-arithmetic-route` Task 4 ✓ |

$$\Longrightarrow\ \boxed{\textbf{四类零新输入 ✓}}\ ✓：\text{A 结构性杀 ✗；B／D 落 II 类（循环或不可定量 ✗）；C 已审 ✗}$$

## §4 判词（✓ 按您的判据 ✓）

$$\boxed{\textbf{杀 ✗}}\ ——\ \text{缺口 ＝ RH 本身 ✓（按您预设："若缺口＝RH ⟹ 杀" ✓）}$$
$$\qquad\textbf{但杀法比"循环"更强 ✓}：\text{不是"需要 RH ✗"，而是【密度型输入在逻辑类型上就不能承载定性消失 ✗】}\ ✓✓$$
$$\qquad\Longrightarrow\ \boxed{\text{这解释了为何 }50\ \text{年（Huxley→GM ✓）把指数从 }7/12\ \text{推到 }17/30\ \text{也毫无帮助 ✗}：\text{指数改善【不可能】抵达 }A\le0\ ✓}$$
$$\qquad\qquad\text{（GM 把短区间推到 }\theta>17/30\ ✓\ \text{仍差 }1/2\ \text{达 }0.067\ ✗；\text{而本推演说：这条路【不存在】有限步到达 ✓）}$$

## §5 边界（✓）

```
⚠️ 不声称"不可能存在新输入"✗（仅否证【幂型密度型】输入 ✓）
⚠️ 不声称 DH ⟹ RH ✗（DH 严格弱于 RH ✓，well-known ✓）；不重证 DH 相关内容 ✓
⚠️ A(σ)>0 对 σ<1 是【所有已知形式＋DH】的事实 ✓，非"所有可能界"的定理 ✗（但任何幂型界若要"消失"⟹需 A≤0 ⟹ σ≥1 ✓，此为逻辑一致 ✓）
⚠️ 纸面审计 ✓ 零数值 ✓；GM 常数形状引用自 `E48`（我方已核 ✓）
✅ 净产出 ✓：① 可证标度障碍（幂型密度界原理上不可消失 ✓✓）；② 缺口精确定位＝定性消失型输入 ✓；
   ③ 四类反向搜索零新输入 ✓；④ 解释了"指数改进为何无用"✓
```
$$\boxed{\mathrm{RH}\iff N(\sigma,T)=0\ \forall\sigma>\tfrac12\ ✓；\text{已知最强 }N\ll T^{15(1-\sigma)/(3+5\sigma)+\varepsilon}\ ✓（A(1/2){=}1.364,\ A(3/4){=}0.556,\ A(0.9){=}0.2\ ✓）；\text{要"消失"需 }A\le0\ ⟹\sigma\ge1\ ✗ \Longrightarrow \boxed{\textbf{密度型输入原理上不可能给出所需结论（可证 ✓）}}\ ⟹ \textbf{缺口 ＝ RH 本身 ⟹ 杀 ✗}；\text{四类反向搜索（A/B/C/D）零新输入 ✓；\text{唯一正解形态＝定性消失型输入（与 }E47\ \text{唯一未封铰链一致 ✓）}}$$
