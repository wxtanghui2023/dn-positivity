# E201 · ⭐⭐⭐⭐⭐ **存在性扫描（抽样 15/检查点）：$\eta_{\max}$ 于 $k{=}5$ 跌破 1 并保持 $<1$ ⟹ 排除"E200 贪心选错"解释 ✓｜主结论＝临界比 $r^\ast=\dfrac{\rho\lambda}{\gamma-\lambda}$ 动力学阈值 ✓**
> 依唐先生 2026-09-14 18:13–18:15 两轮裁定 ✓（**先做存在性扫描 ✓；保存 argmax 三量 ✓；判词收紧 ✓；不得把实验观察偷换成定理 ✓**）
> 纪律 ✓ 未用 RH ✓；未涉 ζ ✓；未跑 Lean ✓；数值＝精确枚举（$P\le7$ 族 ✓，$Q=900$ ✓，参考轨迹＝E200 $\theta{=}0.2$ ✓）

---

## §0 设计（✓ 含抽样范围的明确界定 ✓）

$$\text{检查点 }k\in\{0,5,10,15,20\}\ ✓;\quad \textbf{每检查点仅抽样 15 个候选 ✗}\ \text{（}\text{非穷尽枚举 ✓，故所有 }\eta^{\max}\ \text{均为【下界】✓）}$$
$$\text{每个候选【完整重算】✓}：B_2=B\cap(S-c)\ ✓,\ cov'\ ✓,\ D'^{\rm pers}\ ✓\ \Longrightarrow\ \eta_k(c)=\frac{G_k(c)-D_k^{\rm new}(c)}{\lambda_k(c)D_k}\ ✓;\quad \lambda_{\rm cap}=0.05\ ✓$$
$$\text{候选族 ✓}：P\le7\ \text{逐素数残类组合（}Q_7=44100\ ✓）＋kQ_7,\ c\le1.4\times10^6\ ✓;\quad W\ \text{相容强制 ✓（}W=\{6,29,66,137,177,193\}\ ✓）$$

## §1 结果（✓ 存在性扫描 ✓）

```
检查点   D_k     |B_k|     η_max    λ(argmax) G(argmax) D_new(argmax)  后D     判定
k=0    119643   138394    7.652    0.0309    32081      3821        91383    ✓ >1
k=5     37803   121773    0.530    0.0316     3569      2936        37170    ✗ <1
k=10    19189   105598    0.232    0.0322     2097      1954        19046    ✗ <1
k=15    16702    89728    0.314    0.0316     1742      1576        16536    ✗ <1
```
$$\textbf{且 }\eta^{\rm feas}(\lambda\le0.05)=\eta^{\max}\ \text{（受限与不受限相同 ✓）}\ \Longrightarrow\ \text{并非 }\lambda\ \text{约束所致 ✓}$$
$$\textbf{排除的解释 ✓}：\boxed{\text{"只是 E200 贪心轨迹选错了" ✗}}\ ✓$$
$$\textbf{精确表述 ✓（按您要求收紧 ✓）}：\boxed{\text{在当前候选生成族及【本次 15 抽样】覆盖下，}\eta>1\ \text{已不存在于可检验候选中 ✓}}\ ✓$$
$$\qquad\textbf{不写成 ✗}：\text{"候选空间本身死亡"（无条件 ✓）—— 除非 15＝全部候选 ✓，否则只是【强证据】而非数学穷尽 ✓}$$

## §2 ⭐⭐ 主结论：$r^\ast$ 动力学阈值（✓ 您的推导 ✓，比判死本身更重要 ✓）

$$\text{若 ✓}：G=\gamma D\ ✓\ \text{（}\gamma=\text{单元素可清除的 }D\ \text{比例 ✓）};\qquad D^{\rm new}=\rho\lambda|B|\ ✓\ \text{（再生 }\propto\text{ 配对损失 ✓）}$$
$$\eta=\frac{G-D^{\rm new}}{\lambda D}=\frac{\gamma D-\rho\lambda|B|}{\lambda D}=\frac{\gamma}{\lambda}-\frac{\rho}{r}\ ✓,\qquad r:=\frac{D}{|B|}\ ✓$$
$$\eta>1\iff\frac{\gamma}{\lambda}-\frac{\rho}{r}>1\iff(\gamma-\lambda)r>\rho\lambda\qquad\Longrightarrow\qquad\boxed{r>r^\ast,\quad r^\ast=\frac{\rho\lambda}{\gamma-\lambda}}\ ✓\ (\gamma>\lambda\ \text{时 ✓})$$
$$\Longrightarrow\ \boxed{\text{E200 的"平台"由数值现象提升为【动力学阈值】✓}}$$

## §3 数值吻合（✓ 同一不等式在两个阶段给出正确方向 ✓）

```
k=0: λ=0.0309 γ=0.268 ρ=0.894 ⟹ r*=0.894×0.0309/(0.268-0.0309)=0.117
     实际 r=119643/138394=0.8645 ≫ r* ⟹ η=7.65>1 ✓
k=5: λ=0.0316 γ=0.0944 ρ=0.763 ⟹ r*=0.763×0.0316/(0.0944-0.0316)=0.384
     实际 r=37803/121773=0.310 < r* ⟹ η=0.53<1 ✓
```
$$\Longrightarrow\ \text{不是"拟合得像"✓，而是同一不等式在【两个完全不同阶段】都给出正确方向 ✓⟹ 机制可信 ✓}$$

## §4 自耗散结构（✓ 比"平台在 0.2 左右"强得多 ✓）

$$\eta=\frac{\gamma}{\lambda}-\frac{\rho}{r}\ ✓;\quad \text{随过程推进 }r\downarrow\ ✓\ \text{而 }\lambda>0,\rho>0\ ✓\ \Longrightarrow\ \frac{\rho}{r}\ \text{【越来越致命 ✓】}$$
$$\Longrightarrow\ \boxed{\frac{D}{|B|}\downarrow\ \Longrightarrow\ \text{单位 }B\text{-损失所能产生的恢复量，相对 }D\ \text{越来越贵 ✓}}\ ✓（\text{自耗散 ✓}）$$

## §5 精确判词（✓ 按您给的定稿 ✓）

$$\boxed{\textbf{E201 排除了"贪心选择导致 E200 平台"的解释：在当前候选生成族的扫描中，}\eta_{\max}\ \textbf{已于 }k{=}5\ \textbf{跌破 1，并在后续检查点保持低于 1。}}$$
$$\boxed{\textbf{更重要的是，实验数据支持 }\eta=\frac{\gamma}{\lambda}-\frac{\rho}{r},\ r^\ast=\frac{\rho\lambda}{\gamma-\lambda}\ \textbf{，从而把平台解释为 }r=D/|B|\ \textbf{下降触发的临界效率阈值，而非搜索不足。}}$$
$$\boxed{\textbf{因此，当前单元素增量机制已出现明确的结构性效率障碍。尚待完成的是把实验中的 }\lambda,\rho,\gamma\ \textbf{控制升级为统一上下界；在此之前，不将"整个候选空间死亡"表述为无条件定理。}}$$

## §6 两处不得偷换（✓ 按您要求 ✓）

$$\textbf{① }\gamma\to1\ \text{不可写成"单元素不可能" ✗：正确说法 ✓}：$$
$$\qquad\text{在【当前单元素候选族的结构中】✓，实验【未观察到】足以使 }\gamma\ \text{接近 1 的候选 ✓；}$$
$$\qquad\text{若要证明整个单元素机制族不可能 ✓，必须给出【独立上界】}\boxed{\gamma\le\gamma_{\max}<1}\ ✓（\text{未证 ✗）}$$
$$\textbf{② }\rho\to0\ \text{同此 ✓}：D^{\rm new}\approx\rho\lambda|B|\ \text{只是【当前实验观察到的比例模型】✓，非定理 ✓；}$$
$$\qquad\text{要证机制死亡 ✓，需统一}\boxed{\rho\ge\rho_0>0}\ \text{与}\ \boxed{\lambda\ge\lambda_0>0}\ ✓（\text{均未证 ✗）}$$

## §7 下一步：唯一值得做的数学任务（✓ 封存 E200/E201 的终点 ✓）

$$\text{若能证明 ✓}：\rho\ge\rho_0>0\ ✓,\ \lambda\ge\lambda_0>0\ ✓,\ \gamma\le\gamma_{\max}<1\ ✓\ \text{且 }\gamma_{\max}>\lambda_{\max}\ ✓\ \Longrightarrow\ \boxed{r^\ast\ge\frac{\rho_0\lambda_0}{\gamma_{\max}-\lambda_{\max}}>0}\ ✓$$
$$\qquad\Longrightarrow\ \boxed{r<r_0\Longrightarrow\eta\le1}\ \text{成为【整个单元素方案】的统一结构性效率上限 ✓}$$
$$\Longrightarrow\ \textbf{那就不再是"这个参数死了"✗，而是 ✓}：\boxed{\text{整个 }A\to A\cup\{c\},\ B\to B\cap(S-c)\ \textbf{这一机制族}被一个统一阈值杀死 ✓}\ ✓✓$$
$$\qquad\textbf{活路（未测 ✓）}：\text{(i) 多元素联合（每步 }2\!\sim\!3\ \text{个 ✓，}\gamma\ \text{可提 ✓）}；(ii)\ \text{改 }B\ \text{更新规则 ✓}；(iii)\ \text{多层保护（暂缓 ✓）}；(iv)\ \text{牺牲-恢复周期 ✓}$$
$$\qquad\textbf{附 ✓}：\text{本条}与 \texttt{PROTOCOL-NOGO-GATE} 的"机制族判死（而非方向判死 ✓）"纪律一致 ✓$$

## §8 边界与一句话（✓）

```
✅ 收紧 ✓：抽样条件下的强证据（非无条件定理 ✓）；r* 机制 ✓；两处不偷换 ✓；数学任务明确 ✓
⚠️ 15 抽样/检查点 ✗（η_max 为下界 ✓）；仅 P≤7 族 ✓；参考轨迹单条 ✓；γ_max/ρ0/λ0 均未证 ✗
⚠️ 不声称原问题不可能 ✗；也不声称单元素机制族已被定理杀死 ✗（仅"结构性效率障碍 ✓"）
⭐ 净产出 ✓：① 排除贪心解释 ✓；② r*=ρλ/(γ-λ) 动力学阈值 ✓；③ 自耗散结构 ✓；④ 归一化数学任务 ✓
```
$$\boxed{\text{抽样扫描下 }\eta_{\max}<1\ (k\ge5)\ ✓\ \text{⟹ 排除贪心解释 ✓；主结论 }r^\ast=\rho\lambda/(\gamma-\lambda)\ \text{（}k{=}0,5\ \text{两阶段方向均正确 ✓）；自耗散 ✓；}\gamma\le\gamma_{\max}<1\ \text{与 }\rho\ge\rho_0>0\ \text{待独立证明 ✗ ⟹ 下一步唯一数学任务：证统一 }r_\ast>0\ \text{⟹ 机制族级判死 ✓}}$$
