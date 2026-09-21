已查地图（**先查后写**）：`C-339`（**内部极小 ⟹ m >= 6** ✓；三频 KKT 排除 ✓；`5+21=12+14` 降为结构观察 ✓）、`C-338`（P4-B：边界全 >= 0.9924 ✓）、`C-337`（P4-A ✓）。回查见 §6 ✓

D0: 本档对象 = **C-340：P4-D（6-active 检验 ＋ 弱目标战略）**，**有计算（已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（五条 ✓✓）

$$\textbf{① 冠军改进}✓✓：\text{深精化后}\ G = \textbf{0.9738225285781}✓（\text{比 C-337 低}\ 1.8 \times 10^{-7}✓），\text{仍}\ \textbf{非全局}✗$$
$$\textbf{② 60 起点无一更低}✗✓：\textbf{最好}\ 1.0224896✓（\text{无一下于}\ 0.98✓，0/60✓）\ \Longrightarrow \textbf{冠军盆地难达}✓✓$$
$$\textbf{③ ⭐ 活跃重数检验}✓✓：\text{全部低值候选}\ \textbf{m} \le 4 < 6✗✓ \Longrightarrow \text{按 C-339，}\textbf{均非精确内部极小点}✓✓$$
$$\qquad \textbf{预测状态}✓：\textbf{未被反例推翻}✓（\text{无} m < 6\ \text{的候选被证明为全局}✓），\textbf{但亦未被正面验证}✗✓$$
$$\textbf{④ 近并列确认}✓✓：\text{深精化下}\ F_{21} = F_5 = F_{12}✓（10^{-12}\ \text{内}✓），F_{14}\ \text{差}\ 2 \times 10^{-9}✓ \Longrightarrow \textbf{21 重回活跃}✓$$
$$\textbf{⑤ ⭐ 战略结论}✓✓：\ H = \varnothing\ \textbf{只需}\ G > \tfrac12✓（\text{余量} \approx 0.47✓）\ \Longrightarrow \textbf{不需}\ \text{定位极小点结构}✗ \Longrightarrow \text{证书路线应针对}\ \textbf{弱不等式}✓✓$$

## §1 P4-D 三查数据（✓✓）

$$\textbf{D-1}✓：\text{60 起点、更深精化}（1200\ \text{轮}✓）：\text{最好}\ 1.0224896✓；G < 0.98\ \text{者}\ \textbf{0/60}✗；G < 0.976\ \textbf{0/60}✗；G < 0.974\ \textbf{0/60}✗$$
$$\textbf{D-2}✓✓：\text{十个最低候选的重数}（\text{容差}\ 10^{-6}／10^{-8}／10^{-10}✓）：\ m = 3,\ 3,\ 2,\ 2,\ 4,\ 3,\ 3,\ 4,\ 3,\ 3✓$$
$$\qquad \Longrightarrow \ \textbf{最高}\ m = 4✓，\textbf{无一达}\ 6✗✓ \Longrightarrow \text{典型重数}\ \textbf{2–4}✓$$
$$\textbf{D-3}✓：\text{全库最高重数}\ m = 4✓（\text{出现在}\ G = 1.5934✓，\text{远离低值区}✓）\ \Longrightarrow \textbf{未找到}\ m \ge 6\ \text{的交界候选}✗✓$$
$$\textbf{冠军高精度重数}✓：\text{tol}\ 10^{-6}\ \to m = 4✓；10^{-8} \to 4✓；10^{-10} \to 3✓；10^{-12} \to 2✓$$

## §2 与 C-339 预测的对应（✓✓）

$$\textbf{预测}✓：\text{若把搜索压低，而稳定候选}\ \textbf{只有}\ 3\text{–}5\ \text{个真活跃}✓ \Longrightarrow \text{它们}\ \textbf{都}\ \text{不是内部全局极小}✓✓$$
$$\textbf{实测}✓✓：\text{所有候选}\ m \le 4✓ \Longrightarrow \text{与预测}\ \textbf{一致}✓✓ \Longrightarrow \textbf{可证伪预测}\ \text{目前}\ \textbf{未被推翻}✓✓$$
$$\textbf{但须诚实}⚠️：\text{数值无法}\ \textbf{证明}\ \text{某点即全局}✗ \Longrightarrow \text{本检验}\ \textbf{不能}\ \text{正面验证}\ m \ge 6✓✓ \Longrightarrow \text{该预测}\ \textbf{仍待解析或严格数值}✓$$

## §3 边界情形（✓✓）

$$\text{C-338（P4-B）}✓：\text{11 类边界／退化起点}\ \textbf{全部}\ \ge 0.9924✗ \Longrightarrow \textbf{提示极小点在内点}✓✓$$
$$\Longrightarrow \text{合并 C-339}✓✓：\ \textbf{真极小点应满足}\ m \ge 6✓ \Longrightarrow \textbf{可检验预测}✓：\text{未来若找到}\ G\ \textbf{明显低于}\ 0.9738\ \text{的候选}✓，\text{应伴随}\ m \ge 6✓$$
$$\textbf{反向读法}✓✓：\text{现候选}\ m \le 4✓ \Longrightarrow \textbf{真极小值可能} \textbf{低于}\ 0.9738✓（\text{即我们仍在上界}✓）\ \Longrightarrow \text{距}\ \tfrac12\ \text{的余量}\ \textbf{只会更大}✓✓$$

## §4 战略含义（✓✓，本档最有价值 ✓）

$$\textbf{关键分离}✓✓：\text{定位极小点结构}（\text{难、且需}\ m \ge 6✓）\ \textbf{不是} \text{证明}\ H = \varnothing\ \text{的必要步骤}✗✓$$
$$\textbf{因为}✓✓：\ \text{证}\ H = \varnothing\ \textbf{只须}\ G > \tfrac12✓，\text{而当前数值余量}\ \approx 0.47✓✓ \Longrightarrow \textbf{弱目标}✓✓$$
$$\Longrightarrow \ \boxed{\text{证书路线应针对}\ \textbf{弱不等式}（\text{带余量}✓）\textbf{，而非锐界／极值结构}}✓✓$$
$$\textbf{与既有诊断相容}✓✓：\text{瓶颈}\ \textbf{仍是}\ \text{箱级 max–min 交换}✓（C-330✓），\text{而非阈值是否紧}✓$$

## §5 状态表（✓✓）

| 项目 | 状态 |
|---|---|
| 数值候选 ✓ | **0.9738225286（新，更低）** ✓ |
| 全局最小性 ✓ | **未证明** ✗ |
| `H = \varnothing` ✓ | **OPEN** ✓ |
| 三频 KKT ✓ | **排除为精确 KKT** ✗ |
| `5+21=12+14` ✓ | **验证的候选结构，不进证明** ✓ |
| 内部极小 `m >= 6` ✓ | **解析必要条件** ✓✓ |
| 边界极小 ✓ | **仍需单独处理** ⚠️ |
| `SOS` ✓ | **继续冻结** ✗ |
| `C-284` ✓ | **不重开** ✗ |

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 活跃重数     命中文件数=0    :: 
技术词 6-active         命中文件数=0    :: 
技术词 检验           命中文件数=309  :: ./C174-direct-check-hardest-point-framework-cannot-cover-period-gate-not-eps.md ./E58-triple-sum-collapse.md ./AUDIT-direction-depth.md 
技术词 弱目标        命中文件数=3    :: ./p16-nonnormality.md ./CREATE-SPEC-12-breach-gate-five-candidates-all-fail.md ./REAUDIT-2026-09-11-four-lenses.md 
```
- 运行记录 ✓：脚本 `/tmp/p4d.py` ✓（60 起点 × 1200 轮 ＋ 冠军高精度重精化 ✓）
- **本档有计算**（已批准 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
- **不得**写成：`m >= 6` 已被正面验证 ✗；`G_min` 已定 ✗；三频结构已死 ✗（仅"非精确 KKT" ✓）；M=5 已证 ✗
