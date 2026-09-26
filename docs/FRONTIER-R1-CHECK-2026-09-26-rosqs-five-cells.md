已查地图：已跑 scripts/prework_map_check.sh RoSQS Steiner 四元系 rotational ⟹ **未覆盖**（本线首次触及 ✓；`FRONTIER-R1-2026-09-26` 已立 ✓）；**已查**：`CLOSED-ROUTES-MAP`（无 RoSQS 条目 ✓）、`ASSETS-REGISTRY`（A23-D4 模板可复用 ✓）。
D0: 本档对象 = RoSQS(v) 五格（56/70/82/86/98）的现状、指纹与 P0–P2（检索对象）
D1: 0（产出为逐格 frontier check、指纹与工作单；**未跑搜索** ✓）

# FRONTIER-R1-CHECK-2026-09-26 · RoSQS 五格逐格核查

## §0 结论（先给）

```
$$\boxed{\textbf{(X-1 状态)}\ \text{RoSQS 开放表权威来源＝Ji--Zhu 2002 (JCD 10, 433--443) \textbf{Table I}}\ ✓;\ \text{原列 7 值}\ (46,56,70,82,86,92,98)$$
$$\qquad\text{KKW 2025/2026 (arXiv:2509.23483, DCC 94:157) \textbf{构造了 46 与 92}}\ ✓\ \Longrightarrow\ \textbf{现存 5 格}:\ \mathbf{56,70,82,86,98}\ ✓✓$$
$$\boxed{\textbf{(X-2 核查)}\ \text{firecrawl 检索（2026-09-26）\textbf{未见}任何其它文献触及这 5 格}\ ✓;\ \text{唯一近期成果即 KKW 的 46/92}\ ✓}$$
$$\boxed{\textbf{(X-3 指纹)}\ \text{每格证书＝\textbf{基块表}（}Z_{v-1}\ \text{轨道代表，约 }150\text{--}400\ \text{块}\ ✓）—— \textbf{紧凑、可独立核验}（A23-D4 模板 ✓✓）}$$
$$\boxed{\textbf{(X-4 风险 ⚠️)}\ \text{KKW 已用"扩张群法"尝试同族参数且未成}\ ✗;\ \text{构造性数学工具（乘积构造）属 Ji--Zhu 领域}\ ⚠️\ \Longrightarrow\ \text{需\textbf{差异化}（见 §4）}}$$
$$
$$
```

---

## §1 (X-1)(X-2) 逐格现状表（本档核查 ✓）

```
$$\begin{array}{c|c|c|c|c}
v & v\bmod 6 & \text{SQS}(v)\ \text{容许?} & \text{RoSQS}(v)\ \text{状态} & \text{来源}\\
\hline
46 & 4 & ✓ & \textbf{已构造}（KKW 2025 Thm 2.1 ✓） & [25]+KKW\\
56 & 2 & ✓ & \textbf{开放} ✓ & [25] Table I\\
70 & 4 & ✓ & \textbf{开放} ✓ & [25] Table I\\
82 & 4 & ✓ & \textbf{开放} ✓ & [25] Table I\\
86 & 2 & ✓ & \textbf{开放} ✓ & [25] Table I\\
92 & 2 & ✓ & \textbf{已构造}（KKW 2025 Thm 2.2 ✓） & [25]+KKW\\
98 & 2 & ✓ & \textbf{开放} ✓ & [25] Table I
\end{array}$$
$$\textbf{定义}:\ \text{RoSQS}(v)=\text{SQS}(v)\ \text{带一个 }v-1\ \text{阶循环自同构（含唯一不动点 }\infty\text{）}\ ✓$$
$$\textbf{数据可达性}:\ \text{KKW 论文 [29] 公开 46/92 的基块}\ ✓;\ \text{作者站 }\texttt{steiner3.html}\ \text{给 }v\le50\ \text{的 GAP 可读库（不含 56+}\ ⚠️\text{）}\ ✓$$
$$
$$
```

---

## §2 (X-3) 对象指纹（每格 ✓）

```
$$\text{点集}\ \mathbb Z_{v-1}\cup\{\infty\}\ ✓;\ \text{群}\ \mathbb Z_{v-1}\ \text{平移（固定 }\infty\text{）}\ ✓$$
$$\text{块数}\ b=\frac{v(v-1)(v-2)}{24}\ ✓\ (v{=}56:\ 6930;\ v{=}98:\ 38024\ ✓)$$
$$\text{证书＝基块集（轨道代表）}:\ \text{数量}\ \lesssim\ \frac{v(v-2)}{24}+\frac{v-2}{2}=\frac{(v-2)(v+12)}{24}\ ✓\ (v{=}56:\ \approx153;\ v{=}98:\ \approx440\ ✓)$$
$$\qquad\text{（部分轨道因对称而更短 ⟹ 实际更少 ✓）}\ \Longrightarrow\ \textbf{证书为小型文本文件} ⟹ \text{可逐块核验＋SHA256 指纹}\ ✓✓$$
$$\text{验收条件（无需搜索即可判真伪 ✓）}:\ \text{① 每 3-子集恰被覆盖一次 ✓ ② 轨道封闭 ✓ ③ 块数}=b\ ✓$$
$$
$$
```

---

## §3 P0–P2 工作单（每格 ✓，**未执行**）

```
$$P0:\ \text{定义／等价}:\ \text{找基块集 }B_0\ \text{使}\ \mathbb Z_{v-1}\cdot B_0\ \text{恰覆盖全部 3-子集一次}\ ✓$$
$$P1\ \text{攻击入口（三择一 ✓）}:\ \text{(i) 精确覆盖搜索（群约化；\textbf{计算型} ⚠️）};\ \text{(ii) \textbf{乘积构造}（Ji--Zhu 型，把已知 RoSQS 相乘再补小值）};\ \text{(iii) 更大/更小指定群（KKW 扩张群法的变体）}$$
$$P2\ \text{构造形式}:\ \text{固定 }\infty\text{-块轨道（}\approx(v-2)/2\ \text{个 ✓）后，解 }\mathbb Z_{v-1}\ \text{不变 3-子集的多重度方程组}\ ✓$$
$$\textbf{禁止}:\ \text{开局即 SAT／大规模枚举}\ ✗\ (\text{AMEND-19／21 ✓})$$
$$
$$
```

---

## §4 差异化评估（诚实 ⚠️）

```
$$\textbf{我方优势}:\ \text{A23-D4 模板（群约化 → 搜索 → \textbf{独立 verifier} → 机器证书 ✓✓）；已有 }\texttt{pyguard}\ \text{资源纪律 ✓}$$
$$\textbf{风险 1}:\ \text{KKW 这篇作者是该领域最强组之一，且已对同族参数尝试扩张群法未成}\ ⚠️$$
$$\textbf{风险 2}:\ \text{构造性数学工具（乘积构造）属 Ji--Zhu (2002) 领域；纯"再跑搜索"可能只是重复}\ ⚠️$$
$$\Longrightarrow\ \textbf{建议路径}:\ \text{先过校准门 }\texttt{G-CAL}\ \text{（复现 KKW 公开的 RoSQS}(46)\ \text{基块，逐块核验 ✓）};\ \text{再用\textbf{两种独立方法}攻 }\mathbf{v=56}\ \text{（最小格 ✓）：精确覆盖（CP/SAT，群约化后规模可控 ⚠️）＋ 乘积构造试算 ✓}$$
$$
$$
```

---

## §5 下一步（需唐先生批 ✓）

```
$$\textbf{G-CAL（校准门 ✓）}:\ \text{下载 KKW 论文 [29] 链接的公开基块数据 ⟹ 独立 verifier 逐块核验 RoSQS}(46)\ \text{与 RoSQS}(92)\ ✓$$
$$\qquad\textbf{过门判据}:\ \text{① 3-子集覆盖恰一次 ✓ ② 轨道封闭 ✓ ③ 块数}=b\ ✓（三条件全过才可推进 56 ✓）$$
$$\textbf{需授权}:\ \text{允许下载该公开数据（纯本地核验，不外发 ✓）？}$$
$$
$$
```

---

## §6 边界（诚实标注）

- §1 状态依**文献直读**（arXiv v1 HTML ＋ Ji–Zhu 引用 ✓）；**未**独立复核 46/92 的构造 ✗（待 G-CAL ✓）
- §2 的基块数上界为**组合估算** ✓（对称缩短未计入 ✓）
- §3 仅工作单 ✓（**未执行**任何搜索 ✓）；§4 为**判断**，非定理 ✓
- **未**主张这 5 格"只能用计算"✗

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 RoSQS 五格核查表 命中文件数=1    :: ./FRONTIER-R1-CHECK-2026-09-26-rosqs-five-cells.md 
技术词 基块证书指纹 命中文件数=1    :: ./FRONTIER-R1-CHECK-2026-09-26-rosqs-five-cells.md
```
- **本档新增**：RoSQS 五格核查表、基块证书指纹（见上方命中数；0 命中者为自造语 ✓）
- **档案已有（引用，不列为提出）**：A23-D4 模板、AMEND-19/21、Ji–Zhu 2002、KKW 2025
