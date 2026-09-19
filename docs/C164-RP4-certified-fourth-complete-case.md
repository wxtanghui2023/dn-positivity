已查地图（**先查后写**）：`C-163`（`(\text{RP}_3)` 认证；证明架构表）、`C-162`（每箱精确下界；自适应细分）、`C-161`、`C-154`。关键词回查：`四情形`=1（`p27p33-fourfold-audit.md`，**通用词／已有用法，不计本档新增**）、`维数递推`=0（**新增**）、`初始网格代价`=0（**新增**）。
**本档任务（唐先生 2026-09-19 14:09 追问）**：**`M=4` 结果。**
**结论（先行）**：$$\textbf{(一)}\ ⭐⭐\ \boxed{(\text{RP}_4)\ \textbf{已认证}}：N_0=20\ \Rightarrow\ \text{评估}\ \mathbf{1{,}036{,}096}\ \text{箱、}\mathbf 0\ \text{未决、最小余量}\ \mathbf{0.000210}、\text{最大深度}\ 7、\mathbf{44.93\ s}✓✓$$
$$\qquad \Longrightarrow \textbf{第四个完整情形}：M=1（\text{引理 C}）、M=2（\text{`C-154`}）、M=3（\text{`C-163`}）、\mathbf{M=4}（\text{本档}）✓✓$$
$$\textbf{(二)}\ \text{证书参数哈希}：\mathrm{SHA256}[:16]=c5da38102e08b529\quad(\mathrm{SLACK}=10^{-12},\ \mathrm{TEST\_EPS}=10^{-9})✓$$
$$\textbf{(三)}\ \text{代价观察}：M=3\ (N_0=10)：17{,}440\ \text{箱}/0.78\ \text{s}；\ M=4\ (N_0=20)：1{,}036{,}096\ \text{箱}/44.9\ \text{s}✓$$
$$\qquad \text{总箱数} \approx \textbf{初始网格}\ N_0^M\ \text{的常数倍} \Longrightarrow \text{维数代价落回}\ N_0^M✓$$
$$\textbf{(四)}\ M=5\ \text{运行中}（N_0=8）\ ✓$$

FREEZE-ACK: 本档即冻结期内的证书运行（依 `§8.1`；不产候选结论）

D0: 本档对象 = **`(\text{RP}_4)` 保守证书（已认证）＋ 四情形表 ＋ 代价标度观察** —— 关系 = 认证与登记，非新机制
D1: 0

# C-164 · ⭐⭐ **`(RP_4)` 已认证 —— 第四个完整情形**

> **唐先生 2026-09-19 14:09**：`M=4` 结果？✓

---

## §1 `(RP_4)` 认证结果

$$\textbf{定理}\ (\text{RP}_4)：\forall\varphi\in[0,\pi]^4,\quad \max_{1\le k\le20}\ \sum_{j=1}^{4}\cos(k\varphi_j)\ \ge\ \frac12✓$$
$$\text{运行}（\texttt{scripts/rpM\_adaptive\_certificate.py}）：$$
$$\begin{array}{c|c|c|c|c|c}
M & N_0 & \text{评估箱数} & \text{未决} & \text{最小余量} & \text{用时}\\\hline
\mathbf 4 & 20 & \mathbf{1{,}036{,}096} & \mathbf 0 & 0.000210 & 44.93\ \text{s}\ ✓\\
\end{array}✓✓$$
$$\text{失败的一次尝试}（\text{记录在案}）：N_0=10\ \text{在}\ 400{,}001\ \text{箱处超预算、剩}\ 6{,}399\ \text{未决} \Longrightarrow \text{加大}\ N_0\ \text{即可}\ ✓$$

## §2 ⭐ 完整情形表（本档更新）

$$\begin{array}{c|l|l|c}
M & \text{工具} & \text{证书规模}\\\hline
1 & \text{引理 C（初等闭合式）} & —\ (\text{紧情形，证书不终止})\\
2 & \text{局部解析＋远场证书（`C-154`）} & \text{三段拼装}\\
3 & \text{自适应证书（`C-163`）} & 17{,}440\ \text{箱}/0.78\ \text{s}\\
\mathbf 4 & \mathbf{自适应证书（本档）} & \mathbf{1{,}036{,}096}\ \text{箱}/44.9\ \text{s}\\
\end{array}✓✓$$
$$\Longrightarrow \textbf{四个完整情形}，且~\ M\ge3\ \text{的情形}\ \textbf{统一} \text{由同一脚本认证}✓✓$$

## §3 代价标度（经验规律）

$$M=3：N_0=10 \Rightarrow 17{,}440\ \text{箱} \approx 17\times N_0^3\quad(0.78\ \text{s})✓$$
$$M=4：N_0=20 \Rightarrow 1{,}036{,}096\ \text{箱} \approx 6.5\times N_0^4\quad(44.9\ \text{s})✓$$
$$\Longrightarrow \text{总箱数} = \text{常数}\times N_0^M \Longrightarrow \textbf{维数代价}\ \text{落回}\ N_0^M\ \text{（初始网格主导）}✓$$
$$\qquad \text{常数很小}（\approx 6\text{–}17），\ \text{但指数仍不可免} \Longrightarrow M\ \text{上界由}\ N_0^M\ \text{与预算决定}✓$$

## §4 `M=5` 状态

$$N_0=8：\text{初始}\ 32{,}768\ \text{箱}；\ \text{预算}\ 400{,}000 \Longrightarrow \text{运行中}✓$$
$$\qquad \text{预期}：\text{若衰减率与}\ M=4\ \text{同量级，可能需更大预算（已标注）}✓$$

## §5 边界与回查

- ⚠️ 证书为**计算机辅助**；严格性依赖 (i) `C-163` §2 的三行论证；(ii) 保守化（`\mathrm{SLACK}`、`\mathrm{TEST\_EPS}`）✓
- ⚠️ **残留任务**（沿用 `C-163`）：把保守量换成**区间算术**，形式上闭合浮点缺口 ✓
- ⚠️ **不声称** `(\text{RP}_5)`（运行中）；**不声称**一般 `M` ✓
- ⚠️ **不声称**与 RH 相关 ✓
- **未用** RH；**未改**任何原档 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 14:1x）`[纪律]`（先跑后写）

```
技术词 四情形      命中文件数=1 :: ./p27p33-fourfold-audit.md   ⟹ 通用词／已有用法，【不计本档新增】
技术词 维数递推     命中文件数=0 ::  ⟹ 本档新增
技术词 初始网格代价  命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：`四情形`＝**复用**（另一语境，非本档新命名）；其余两项**本档新增** ✓
