已查地图（**先查后写**）：`C-3856`（**B1 首刀：两候选非极小；`0.876069` 仅为上界** ✓✓）、`C-3855`（**A：内部信号** ✓✓）、`C-3854`（**靶与硬门槛** ✓✓）、`C-380-13`（**线性对偶封口** ✓✓）。回查见 §4 ✓

D0: 本档对象 = **C-380-57：B1-α 首刀 —— KKT 候选定向求解（单 active 奇频形式）＋ 次微分诊断**（唐先生 2026-09-21 22:13 发令）
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（七条 ✓✓）

$$\textbf{① 档位}✓✓：\text{只做}\ \textbf{KKT 候选定位}✓✓；\ \textbf{不做}二阶证明}✗✓；\ \text{数值只用于}\ \textbf{发现分支}✓✓$$

$$\qquad \text{量词顺序严守}✓✓：\ \gamma^{(13)} = \min_{\sigma}\min_{x \in E_{\mathrm{even}}}\max_{0 \le r \le 12}\big|F_{2r+1}^{(\sigma)}(x)\big|✓✓$$

$$\qquad ⚠️ \textbf{账本更正（唐先生）}✓✓：\ \boxed{\gamma^{(13)} \le 0.876069\ \text{（上界）}}✓✓,\ \textbf{不是} \text{"}\approx 0.876\text{"}✗✓\ \text{（真值未定}✓）$$

$$\textbf{② 本刀所用 KKT 形式}✓✓：\text{固定}\ (\sigma, r^*)✓\ \text{与 active 偶频集}\ \mathcal A✓ \Longrightarrow \text{方阵系统}✓✓：$$

$$\qquad \boxed{\ \pm\nabla F_{2r^*+1}^{(\sigma)} + \sum_{r \in \mathcal A}\lambda_r\nabla F_{2r} = 0\ (5\ \text{式})✓,\qquad F_{2r} = \tfrac12\ (r \in \mathcal A)✓,\qquad \lambda_r \ge 0\ }✓✓$$

$$\qquad \text{规模}✓：\mathcal A\ \text{池} = \{[3],[4],[9],[3,4],[3,9],[4,9],[3,4,9],[4,9,12],[3,4,9,12]\}✓（\textbf{含唐先生指出的}\ \{3,4,9\}✓）$$

$$\qquad \qquad \times\ 16\ \sigma\ \times\ 13\ r^*\ \times\ \pm\ \text{号}\ \times\ 3\ \text{起点} \Longrightarrow \textbf{3744 场景}✓✓$$

$$\textbf{③ ⚠️ 结果：}\textbf{0 个 surviving KKT 候选}✗✓（\text{全部被后置条件筛掉或被 Newton 拒绝}✓）$$

$$\qquad \text{后置检查}✓✓（\textbf{按唐先生要求，残差近零不算 KKT}✓）：\text{残差} \le 10^{-9}✓；\lambda \ge 0✓；\ F_{2r} \le \tfrac12\ (r \notin \mathcal A)✓；\ r^* = \arg\max_r|F_{2r+1}|✓；\ \sigma = \arg\min_\sigma\max_r|F_{2r+1}|✓✓$$

$$\qquad \text{边界过滤}✓：\phi_j \in [10^{-3},\ \tfrac{\pi}{2}-10^{-3}]✓（\text{排除}\ x_j = 0／1\ \text{边界}✓）$$

$$\textbf{④ ⭐ 诊断（本刀的核心产出）}✓✓：\text{"0 候选"}\ \textbf{不}等于"不存在 KKT 点"✗✓；\ \text{两种解释}✓✓：$$

$$\qquad \textbf{(a) }\mathcal A\ \text{池过小}✓：\text{真 active 集可能不在池中}✓（\text{但覆盖了候选 1 的近 binding 组合}\{3,4,9\}✓）$$

$$\qquad \textbf{(b) ⭐ 目标非光滑}✓✓：\text{目标是}\ \max_r\ \text{（且外层对}\ \sigma\ \text{取}\ \min）✓ \Longrightarrow \text{在极小点处}\ \textbf{通常有多个并列活跃的奇频／多个并列的}\ \sigma✓✓$$

$$\qquad \qquad \Longrightarrow \text{正确的 KKT 是}\ \textbf{次微分（凸组合）形式}✓✓：$$

$$\qquad \qquad \boxed{\ 0 \in \operatorname{conv}\Big\{\,\operatorname{sgn}(F_{2r+1}^{(\sigma)})\nabla F_{2r+1}^{(\sigma)}\ :\ (\sigma, r) \in \mathcal I\ \Big\} \ +\ \sum_{r \in \mathcal A}\lambda_r\nabla F_{2r}\ }✓✓$$

$$\qquad \qquad \qquad \text{（}\mathcal I\ \text{为并列活跃集}✓；等权情形}\ \omega_r \ge 0,\ \sum\omega = 1✓）$$

$$\qquad \Longrightarrow\ \text{本刀的单权重形式}\ (\omega = e_{r^*})✓ \text{只是一个特例}✓✓ \Longrightarrow \textbf{0 候选与"真 KKT 是并列型"}\ \textbf{相容}✓✓$$

$$\textbf{⑤ 结构含义（登记）}✓✓：\text{若真极值是}\ \textbf{并列型}✓（两个奇频／两个 σ 同时活跃）✓，\ \text{则}\ \textbf{机制的自然位置就在"交叉点"}✓✓$$

$$\qquad \text{这与}\ C\text{-}3856\ \text{的观察一致}✓：\text{候选 1 有}\ \textbf{三个偶频同时近 binding}✓✓ \Longrightarrow \text{极值几何是}\ \textbf{多重交叉}✓，\ \textbf{不是}单一约束现象}✗✓$$

$$\textbf{⑥ 边界}✓✓：\text{本刀}\ \textbf{不}声称"KKT 点不存在"✗✓；\ \textbf{不}声称}\ \gamma^{(13)}\ \text{的几何已确定}✗✓；\ \textbf{不}把 0 候选解释为否定结论}✗✓$$

$$\textbf{⑦ 账本（见 §2）}✓✓$$

## §1 数值记录（数字驱动 ✓✓）

```
场景数：3744（9 个 A × 16 σ × 13 r* × ±号 × 3 起点）
后置条件：残差 <= 1e-9 ; λ >= 0 ; 非活跃偶频 F_2r <= 1/2 ; r* = argmax|F_odd| ; σ = argmin_σ max|F_odd|
结果：surviving KKT 候选 = 0
对照：C-3856 两个候选点（g = 0.876069 / 0.9878）均被判"非局部极小"（一阶改善方向存在）
```
- 脚本 ✓：`scripts/c380_57_B1alpha_kkt.py`✓；输出 ✓：`scripts/out_c380_57_B1alpha.txt`✓

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| `\gamma^{(13)} \le 0.876069` ✓ | **上界（更正措辞）** ✓✓ |
| 单权重 KKT 候选（本刀形式） ✓ | **0 个** ✗✓ |
| 次微分 KKT ✓ | **未做（下一刀）** ✗✓ |
| 偶频多重近 binding ✓ | **是（{3,4,9}）** ✓✓ |
| 真极值几何 ✓ | **未定** ✓ |
| 二阶耦合判定 ✓ | **未做** ✗✓ |

## §3 边界（不得声称 ✗✓）

- **不**声称 KKT 点不存在 ✓
- **不**声称 `0.876069` 接近真值（只是上界）✓
- **不**用数值结果替代证明 ✓
- **不**把 `\lambda` 的符号检查当作充分性（须 ＋ 二阶必要条件）✓

## §4 【技术词回查】输出（**先跑后写** ✓）

```
技术词 次微分KKT     命中文件数=0    :: 
技术词 活跃集并列  命中文件数=0    :: 
技术词 凸组合权重  命中文件数=0    ::
```

## §5 下一步（须唐先生发令 ✓）

$$\textbf{B1-}\alpha\text{-2}✓：\ \textbf{次微分 KKT}✓✓：\text{改为凸组合权重}\ \omega_r \ge 0\ (\sum\omega = 1)✓ \text{并列活跃}✓；\ \text{并允许}\ \sigma\ \text{并列}✓；\ \text{方阵系统变为}\ (5 + |\mathcal I_\omega| + |\mathcal A|)\ \text{方程}✓✓$$
$$\textbf{B1-}\alpha\text{-3}✓：\ \textbf{扩大}\ \mathcal A\ \text{池}✓（\text{含全部}\ |\mathcal A| \le 3✓）\ \text{并放宽}\ \phi\ \text{边界过滤}✓✓（\text{允许}\ x_j \to 1✓）$$
$$\textbf{暂不做}✓：\ \text{二阶耦合判定}✗（\text{须先有 genuine KKT 点}✓）$$
