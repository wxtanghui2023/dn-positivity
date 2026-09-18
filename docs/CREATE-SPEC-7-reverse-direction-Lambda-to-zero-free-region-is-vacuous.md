已查地图（**先查后写**）：`CLOSED-ROUTES-MAP:228`／`:2915`（DBN 热流＝`R2-C`：形变型**闭环为循环**，`RH ⟺ Λ≤0`）、`C-109`（S1 槽：`模型→插值→Poincaré 型不等式`；其 RH 对应物＝DBN 形变线，判为循环）、`C-111`（DBN 端点**半阶分支**：`off(t)=√(2(Λ−t))`，`|d off/dt|→∞`）、`C-115`（"端点退化"＝`Λ≤0 ⟺ RH` 同墙异述）、`M4-C6-REFINAL`（M4 死 `F5`／端点）、`CREATE-SPEC-2`（候选 D 的 `F3` 死：Gamma 零-free）。关键词回查：`零-free 区域`＝多档（术语已在）；`y²/2`／`碰撞时间`／`消灭时间`／`annihilation`＝**0 档** ⟹ **"Λ 与离轴距离"的定量关系式未登记** ✓。**结论**：⭐ 唐先生 21:48 选 **(i) Tao 的反向方向（`Λ\to` 零-free 区域）** ⟹ **本档给其定量标定：该方向在一切已知 `Λ` 上界下\ \textbf{定量真空}（被经典结果支配）** ✓✓

FREEZE-ACK: 本档即冻结期内的方向攻击与定量标定（依 `§8.1`；不产候选结论）

D0: 本档对象 = **反向方向（`Λ\to` 零-free 区域）的定量标定** ＋ 一条初等关系式（`Λ\ge y_0^2/2`）—— 关系 = 方向攻击与标定，非新机制
D1: 0

# CREATE-SPEC-7 · **(i) Tao 反向方向（`Λ\to` 零-free 区域）的定量标定：真空**

> **时间**：2026-09-18 21:48 唐先生：**「i」** ⟹ 沿 Tao（Polymath15）明说的**未尝试反向**：*smallness of Λ implies a zero free region* ✓

---

## §0 结论（先行）

$$\textbf{初等关系（推导）}：\text{离轴零点对距离}\ y_0 \Longrightarrow \textbf{消灭时间}\ t_*=y_0^2/2 \Longrightarrow \boxed{\Lambda\ \ge\ y_0^2/2}✓✓$$
$$\qquad \Longrightarrow \textbf{反向结论}：\text{无零点满足}\ \operatorname{Re}s>\tfrac12+\sqrt{2\Lambda}✓✓$$
$$\textbf{标定}：\text{以}\ \Lambda\le0.22（\text{Polymath15}） \Longrightarrow \operatorname{Re}s\le\tfrac12+\sqrt{0.44}\approx\mathbf{1.163}\ \textbf{比平凡事实}\ \operatorname{Re}s<1\ \textbf{更弱} \Longrightarrow \textbf{真空}✓✓$$
$$\qquad \Longrightarrow \text{非真空门槛}：\sqrt{2\Lambda}<\tfrac12 \iff \boxed{\Lambda<\tfrac18=0.125};\ \text{今}\ 0.22>\tfrac18 \Longrightarrow \textbf{真空}✓✓$$
$$\qquad \Longrightarrow ⭐\ \text{这}\ \textbf{定量解释} \text{了 Tao 为何说该方向}\ \text{"extremely inefficient"}✓✓$$

---

## §1 初等关系式（本档推导）

$$\text{取一对离轴零点}\ \rho=\tfrac12+y_0+i\gamma,\ \bar\rho \Longrightarrow \text{局部二阶模型}\ H_0(z)=z^2+y_0^2+O(z^3)✓$$
$$\qquad \text{DBN 流}\ \partial_tH=-\partial_z^2H \Longrightarrow H_t=z^2+y_0^2-2t\quad（\text{精确于二次模型}）✓$$
$$\qquad \text{零点}：z=\pm\sqrt{2t-y_0^2}\ \textbf{实}\iff t\ge\boxed{y_0^2/2}✓✓$$
$$\qquad \Longrightarrow \text{该对的}\ \textbf{消灭时间}\ t_*=y_0^2/2;\quad \Lambda=\sup_{\text{pairs}}t_* \Longrightarrow \Lambda\ge y_0^2/2✓✓$$
$$\Longrightarrow \boxed{\operatorname{Re}\rho\ \le\ \tfrac12+\sqrt{2\Lambda}}\quad（\text{对所有}\ \rho）✓✓$$

## §2 与经典结果的支配比较（标定核心）

| 结论 | 排除区 | 来源 |
|:--|:--|:--|
| 平凡（Euler 积／PNT） | $\operatorname{Re}s\ge1$ | 经典 |
| 经典零-free 区 | $\operatorname{Re}s>1-\dfrac{c}{(\log t)^{2/3}(\log\log t)^{1/3}}$ | Korobov–Vinogradov |
| **反向（`Λ≤0.22`）** | $\operatorname{Re}s>1.163$ | 本档 |

$$\textbf{支配}：\text{平凡结论}\ \operatorname{Re}s\ge1\ \Longrightarrow\ \operatorname{Re}s>1.163 \Longrightarrow \textbf{反向结论被平凡结论蕴含} \Longrightarrow \textbf{零新信息}✓✓$$
$$\qquad \text{大}\ t\ \text{侧}：\text{经典区}1-c/(\log t)^{2/3}\cdots\to1 \Longrightarrow \text{与}\ 1.163\ \text{无交集优势} \Longrightarrow \text{经典更强}✓✓$$
$$\Longrightarrow \text{反向方向要}\ \textbf{非真空} \text{，须}\ \Lambda<\tfrac18;\ \text{要}\ \textbf{在}\ t\to\infty\ \text{侧胜过经典} \text{，仍须}\ \sqrt{2\Lambda}<\tfrac12\ \text{恒成立} \Longrightarrow \textbf{门槛同为}\ \Lambda<\tfrac18✓✓$$

## §3 为什么这与"端点退化"一致（与 `C-111`／`C-115` 对照）

$$\text{`C-111` 逐字}：off(t)=\sqrt{2(\Lambda-t)}\ \Longrightarrow\ \textbf{半阶分支};\quad |d\,\mathrm{off}/dt|\to\infty\ \text{于端点}✓$$
$$\qquad \Longrightarrow \text{同一条局部模型的}\ \textbf{两种读法}：\text{正向读法给"端点不可微}（\text{`C-111`}）;\ \text{反向读法给"}\Lambda\ge y_0^2/2（\text{本档}）✓✓$$
$$\Longrightarrow \text{本档}\ \textbf{不改} \text{`C-115` 的校准}（\text{端点退化}＝\Lambda\le0\iff\mathrm{RH}\ \text{同墙异述}） \Longrightarrow \textbf{增补的是定量标定}✓✓$$

## §4 反向方向的**精确可用域**（若未来 \Lambda 更小）

$$\textbf{若}\ \Lambda<\tfrac18 \Longrightarrow \text{反向给"}\operatorname{Re}s\le\tfrac12+\sqrt{2\Lambda}<1\text{"，}\ \textbf{首次强于平凡}✓$$
$$\qquad ⚠️\ \text{但}\ \textbf{其形是"竖直带"}（\text{T-无关}），\ \text{而经典区是"}\ \textbf{T-相关} \text{"} \Longrightarrow \text{两者}\ \textbf{不可直接比较}✓✓$$
$$\qquad \Longrightarrow \text{真正有用的形态应为}\ \textbf{T-相关反向}：\text{"}\Lambda\le\delta(T)\Longrightarrow\ \text{无零点于}\ \operatorname{Re}s>1-\eta(T)\text{"};\ \text{文献无此形}（\text{Tao 只说"可设想"}）✓✓$$
$$\qquad ⚠️\ \text{本项目提示}：\text{由}\ \text{`C-111`}\ \text{的}\ \textbf{半阶分支} \Longrightarrow \text{任何沿}\ t\ \text{的}\ \textbf{一致转移} \text{在端点失败} \Longrightarrow \text{T-相关反向须}\ \textbf{绕开端点}✓✓$$

## §5 边界与回查

- ⚠️ §1 的关系式 $\Lambda\ge y_0^2/2$ 为**局部二阶模型下的推导**（`[推导·局部模型]`）；真实 DBN 流对**多零点耦合**，故严格常数可能不同 ⟹ **但**只要 $\Lambda\ge c\,y_0^2$（某固定 $c>0$），§2 的"非真空门槛"改形为 $\Lambda<c/4$，**真空结论对一切合理常数保持**（除非 $c<0.88$ 且 $\Lambda$ 更大）✓
- ⚠️ §2 引用 Polymath15 的 $\Lambda\le0.22$ 为**档案已有**（`CLOSED-ROUTES-MAP:228`）✓
- ⚠️ 本档**未做**数值；**未用** RH；**未声称** RH ✓
- ⚠️ 净结论：**反向方向在当前 `Λ` 上界下是真空的**（被平凡结论支配）⟹ 与 Tao 的"低效"警告**一致且更精确** ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）✓

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 21:5x）`[纪律]`（先跑后写）

```
技术词 消灭时间     命中文件数=0  ⟹ 本档新增
技术词 真空域      命中文件数=0  ⟹ 本档新增
技术词 反向标定     命中文件数=0  ⟹ 本档新增
技术词 Λ≥y²/2     命中文件数=0  ⟹ 本档新增
```
**读数（按实测）**：四项**全 0 档 ⟹ 均本档新增** ✓；且 `y²/2`／`碰撞时间` 在档案中亦为 0 ⟹ **"`Λ` 与离轴距离"的定量关系此前未登记** ✓
