已查地图：已跑 scripts/prework_map_check.sh 全局同余 双计数 球交 距离-2 图 ⟹ 逐字核 `FAILSET-2026-09-26-...` §2（"$d(c,c')\le2$ 时 $|B_1(c)\cap B_1(c')|=2$ ✓（真）" ✓）、`SCOL-2026-09-26-...`、`DEL6/del6` 摘要（二阶 LP：$A_1\le49$ ✓）；本档 = **(a) 全局整数/同余障碍可达性审计 ⟹ 四层全部坍缩（第 15 次同向收敛 ✓）**。
D0: 本档对象 = 119 的全局整数/同余障碍可达性（G-I..G-IV）
D1: 2（**先纠正球交数前提 ✗→✓**；**模 2 平凡性引理 ✓（新，可留档 ✓）**；**四层坍缩 ⟹ 该形状封口 ✓**）

# (a) 全局整数/同余障碍可达性审计（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(HA-1 ⚠️前提纠正（必须先做 ✓）)}\ \text{球交数应为}\ \boxed{|B_1(c)\cap B_1(c')|=\begin{cases}2&d(c,c')\in\{1,2\}\\0&d\ge3\end{cases}}\ ✓\（\text{档案 }FAILSET\ §2\ \text{逐字核实 ✓）—— \textbf{不是}"}1\ \text{若 }d{=}2\text{"}\ ✗}$$
$$\qquad\textbf{后果 ✓}:\ \boxed{\sum_x\binom{b(x)}2=2(A_1+A_2)}\ ✓\ \text{—— 故"}\{d{=}2\}\ \text{对数"}\ \textbf{不}等于 }\sum_x\binom{b(x)}2\ ✗;\ \text{正确对象}=\boxed{P:=A_1+A_2=\tfrac12\sum_x\binom{b(x)}2}\ ✓✓$$
$$\boxed{\textbf{(HB-1 ⭐模 2 平凡性引理（本档新 ✓，值得留档）)}\ \text{对每个字符 }\chi\ (\text{权 }w):\ \widehat b(\chi)=\bigl(11-2w(\chi)\bigr)\widehat C(\chi)\ ✓\ \text{（因 }\sum_{x\in B_1(c)}(-1)^{\chi x}=(-1)^{\chi c}(11-2w)\ ✓）}$$
$$\qquad\Longrightarrow\ \text{全部乘子 }11-2w\in\{11,9,7,5,3,\mathbf 1,-1,-3,\ldots\}\ \textbf{皆为奇数 ⟹ 在 }\bmod 2\ \text{下全可逆 ⟹ 模 2 不产生任何新信息 ✗✓}$$
$$\qquad\text{（核对 ✓）}:\ \widehat b(\chi)\equiv\sum_x b(x)=1309\equiv1,\ \widehat C(\chi)\equiv M=119\equiv1\ (\bmod 2)\ \text{—— 两侧一致 ⟹ 无约束 ✗}$$
$$\boxed{\textbf{(HC-1 🔴G-I/G-III/G-IV 全部坍缩（profile 恒等式 ✓）)}\ \sum_x b=11M=1309\ ✓;\ \sum_x\binom{b}2=2P\ ✓;\ \sum_x\binom{b}3=T\ ✓;\ \sum_x b(b-1)=2\sum_x\binom b2\ ✓}$$
$$\qquad\text{—— 四者\textbf{皆由 profile }(N_k)\ \text{唯一决定} ✓;\ \text{而 profile 的全部已知约束}=\{\sum N_k{=}1024,\ \sum kN_k{=}1309,\ N_1\ge M\ (\text{minimality ✓})\}\ ✓ \Longrightarrow\textbf{ 无新同余 ✗}$$
$$\qquad\text{G-III 判定 ✓}:\ \text{"}P\bmod m\text{" 由 profile 决定 ✓；距离-2 图未在可检形状下产生独立同余 ✗（档案已用标准工具：Delsarte 二阶 LP 得 }Q{=}1\ \text{下 }A_1\le49\ ✓\text{—— 那是\textbf{线性}路线 ✓、非同余 ✗）}$$
$$\qquad\text{G-IV 判定 ✓}:\ T\ \text{同为 profile 决定 ✓；其"}\sum_{\rm triples}|\cap B_1|\text{"读法给出的是\textbf{耦合等式}（profile ↔ 坐标结构 ✓）而非同余 ✗};\ |\cap B_1|\in\{0,1,3\}\ \text{型（2 维张成→3 ✓、3 维张成→1 ✓、更大→0 ✓）}$$
$$
$$
```

---

## §1 四层逐条（**✓**）

```
$$\textbf{G-I（基本双计数）: 坍缩 ✗}\ ——\ \text{全部自然量为 profile 恒等式 ✓（见 HC-1 ✓）}$$
$$\textbf{G-II（模 2／模 4 覆盖方程）: 坍缩 ✗，但得一条干净引理 ✓}\ ——\ \text{模 2：由 (HB-1) 平凡 ✓；模 4：}\widehat b(\chi)\equiv(11-2w)\widehat C(\chi)\ (\bmod 4)\ \text{为\textbf{关系式}（两侧皆由码决定 ✓）而非障碍 ✗，除非引入独立输入 ⚠️}$$
$$\textbf{G-III（二次交整数性）: 坍缩 ✗}\ ——\ P=\tfrac12\sum_x\binom{b}2\ \text{profile 决定 ✓};\ \text{距离-2 图的"全局同余"在可检形状下未见独立约束 ✗}$$
$$\textbf{G-IV（三重交）: 坍缩为耦合等式 ✗}\ ——\ T=\sum_x\binom{b}3\ \text{profile 决定 ✓};\ \text{三球交大小依赖坐标关系 ✓（故 }T\ \text{把 profile 与坐标结构\textbf{耦合} ✓）—— 耦合 ⟹ 可能是新入口 ⚠️，但\textbf{不是同余} ✗✓}$$
$$
$$
```

---

## §2 STOP 判定（**✓ 按唐先生 gate B**）

```
$$\boxed{\textbf{判定} = \textbf{B. 恒等式坍缩} \Longrightarrow \textbf{第 15 次同向收敛}\ ✓}\ \text{—— 全局整数/同余形状（在 G-I..G-IV 全部自然候选下）\textbf{正式封口} ✓}$$
$$\textbf{诚实边界（纪律 ✓）}:\ \text{本档\textbf{未}证明"不存在同余障碍" ✗};\ \text{只证：四层自然候选全部坍缩 ✓（"未发现 ≠ 不存在" ✓）}$$
$$\textbf{唯一可留档资产 ✓}:\ \text{(HB-1) 模 2 平凡性引理（乘子全奇 ⟹ 模 2 无信息 ✓）—— 可用于快速否决未来"模 2 型"候选 ✓}$$
$$\textbf{状态 ✓}:\ \boxed{K(10,1)=119\ \text{保持 UNKNOWN};\ \text{局部形状（已封 ✗）＋ 全局同余形状（本档封 ✓）}}$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：球交数前提纠正、模 2 平凡性引理（乘子全奇）、G-I..G-IV 四层坍缩判定、$T$ 的 profile↔坐标耦合等式
- **档案已有（引用，不列为提出）**：FAILSET-2026-09-26（球交数 ✓）、SCOL-2026-09-26、PROPAGATION-2026-09-26、Delsarte 二阶 LP（$A_1\le49$）


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 模 2 平凡性  命中文件数=1    :: ./CONGRUENCE-119-2026-09-27-global-integer-audit-collapse.md 
技术词 坍缩判定     命中文件数=1    :: ./CONGRUENCE-119-2026-09-27-global-integer-audit-collapse.md
```
- **本档新增**：球交数前提纠正、模 2 平凡性引理（乘子全奇）、G-I..G-IV 四层坍缩判定、$T$ 的 profile↔坐标耦合等式（见上方命中数；0 命中者为自造语／内部标签 ✓）
