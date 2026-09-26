已查地图：已跑 scripts/prework_map_check.sh K(10,1) Fourier 卷积 excess divisibility ⟹ 与既有 `HQ1`（Haas 层式，Fourier/excess 同族 ✓）＋ `L2AUDIT`（Gijswijt–Polak SDP ✓）比对；本档为**换坐标系路线审计**（唐先生 2026-09-26 21:29 稿 ✓）；含计算核验 ✓。
D0: 本档对象 = $b=1_C*1_{B_1}$ 的 Fourier 反卷积与 $\delta$ 的谱约束（既有对象，**换语言** ✓）
D1: 0（产出为四步验真：框架确认 ＋ 两处自动化 ＋ 无能量缺口 ＋ Booleanity 定位）

# FOURIER-2026-09-26 · 卷积/谱反演路线审计

## §0 结论（先给）

```
$$\boxed{\textbf{(F-1 确认)}\ \text{框架\textbf{正确}:\ }w(u)=11-2|u|\in\{\pm1,\pm3,\pm5,\pm7,\pm9,11\}\ \text{无零点}\ \Longrightarrow\ T=1_{B_1}*\ \textbf{可逆};\ \widehat\delta(u)=w(u)\widehat{1_C}(u)\ (u\ne0)\ ✓✓}$$
$$\boxed{\textbf{(F-2 判定)}\ \text{你列的“divisibility ＋ 奇性”两条\textbf{自动成立}}:\ w(u)\mid\widehat\delta(u)\ \text{是}\ \widehat\delta=w\widehat{1_C}\ \text{的改写}\ ✗;\ \widehat\delta\ \text{奇}\Longleftarrow|\widehat{1_C}|\ \text{奇}\Longleftarrow|C|\ \text{为奇数}\ ✗✗}$$
$$\boxed{\textbf{(F-3 判定)}\ \text{两条能量式正确但\textbf{互相蕴含}}（\widehat\delta^2=w^2\widehat{1_C}^2）\ \Longrightarrow\ \text{实质只含 profile}\ \sum_x\delta(x)^2=287\ \text{的信息}\ ⚠️}$$
$$\boxed{\textbf{(F-4 判定)}\ \text{shell 系统\textbf{无严格能量缺口}}:\ \text{必要同余＋两个总量}\ \Longrightarrow\ \text{已构造显式可行解}\ \mathbf{h'_5=11852,\ h'_4=1482}\ \checkmark\ \Longrightarrow\ \text{按你的规则\textbf{进入 Booleanity}}\ ✗✓}$$
$$\boxed{\textbf{(F-5 定位)}\ \text{剩余全部内容＝Booleanity}\ 1_C=T^{-1}(1+\delta)\in\{0,1\}^{1024}\ ✓\ \text{—— 但它\textbf{等价于原问题}（非松弛）};\ \text{即\textbf{换坐标}，非\textbf{换难度}}}$$
$$
$$
```

---

## §1 (F-1) 框架逐项确认（含数值核验 ✓）

```
$$\textbf{球的谱}:\ \widehat{1_{B_1}}(u)=1+\sum_i(-1)^{u\cdot e_i}=1+(10-2|u|)=11-2|u|\ ✓$$
$$\textbf{取值}:\ |u|=0..10\Longrightarrow 11,9,7,5,3,1,-1,-3,-5,-7,-9\ \text{——\textbf{无零点}}\ ✓✓\ (\text{因 }11\ \text{奇、}2|u|\ \text{偶})$$
$$\textbf{反卷积}:\ \widehat\delta(u)=w(u)\widehat{1_C}(u)\ (u\ne0)\ ✓;\ \widehat\delta(0)=285\ ✓;\ \widehat{1_C}(0)=119\ ✓$$
$$\qquad\textbf{数值核验（本档 ✓）}:\ 随机码\ \times\ \text{随机字符}\ 150\ \text{次},\ \text{违背}\ \mathbf 0\ ✓✓$$
$$\qquad\textbf{注意}:\ u=0\ \text{处需 }b\ \text{的常数项（}\widehat b(0)=\widehat\delta(0)+1024=1309\ ✓），公式形式与 }u\ne0\ \text{不同 ✓（唐稿未区分 ⚠️）}$$
$$
$$
```

---

## §2 (F-2)(F-3) 两处“新约束”实为自动 ＋ 能量式互相蕴含

```
$$\textbf{(F-2a)}:\ \widehat\delta(u)=w(u)\widehat{1_C}(u)\ \text{即}=\ \text{“}w(u)\mid\widehat\delta(u)\text{”}\ \text{本身}\ ✓\ \text{——\textbf{恒等}，非新算术约束}\ ✗$$
$$\textbf{(F-2b)}:\ \widehat{1_C}(u)\equiv\sum_{c\in C}1=|C|=119\equiv1\ (\mathrm{mod}\ 2)\ \text{对\textbf{任意}奇基数码成立}\ ✓\ \Longrightarrow\ \widehat\delta\ \text{奇亦自动}\ ✗$$
$$\textbf{(F-3)}:\ \sum_{u\ne0}\widehat\delta^2=1024\cdot287-285^2=212663\ ✓;\ \sum_{u\ne0}\frac{\widehat\delta^2}{w^2}=1024\cdot119-119^2=107695\ ✓$$
$$\qquad\text{但}\ \widehat\delta^2=w^2\widehat{1_C}^2\ \text{逐项成立}\ \Longrightarrow\ \text{两式\textbf{等价}};\ \text{且由 profile}\ \sum\delta^2=287\ \text{已定}\ \Longrightarrow\ \textbf{不含新信息}\ ⚠️$$
$$
$$
```

---

## §3 (F-4) shell 系统：无严格能量缺口（显式可行解 ✓）

```
$$\textbf{记}\ G_k=\sum_{|u|=k}\widehat{1_C}(u)^2\ ✓;\quad \sum_{k}G_k=107695\ ✓;\quad \sum_kw_k^2G_k=212663\ ✓\ (w_k=11-2k)$$
$$\textbf{必要同余}:\ G_k\ \equiv\ \binom{10}{k}\ (\mathrm{mod}\ 8)\ \text{（奇平方}\equiv1\ \mathrm{mod}\ 8\ ✓）\ \Longrightarrow\ G_k=\binom{10}{k}+8h'_k,\ h'_k\ge0\ ✓$$
$$\Longrightarrow\ \sum_k h'_k=\frac{107695-1023}{8}=13334\ ✓;\quad \sum_kw_k^2h'_k=\frac{212663-11143}{8}=25190\ ✓$$
$$\qquad\text{（注意}\ \sum_{u\ne0}w^2=11264-121=11143\ ✓\ \text{—— }\text{含 }u=0\ \text{项会造假矛盾 ⚠️ 见 §5 自查）}$$
$$\textbf{显式可行解（本档 ✓）}:\ h'_5=11852,\ h'_4=1482\ \Longrightarrow\ \sum h'=13334\ ✓,\ \sum w^2h'=11852+1482\times9=25190\ ✓✓$$
$$\Longrightarrow\ \textbf{无严格能量缺口}\ ✗\ \Longrightarrow\ \text{按唐先生预设规则：进入 Booleanity（而非回到 }b\text{-capacity）}\ ✓$$
$$
$$
```

---

## §4 (F-5) 剩余内容＝Booleanity（等价于原问题 ✓）

```
$$\textbf{干净形式}:\ \text{找 }284\text{-子集 }S\ (\text{含 }z)\ \text{使}\quad 1_C=T^{-1}\big(1+1_S+1_z\big)\in\{0,1\}^{1024},\ |C|=119\ ✓$$
$$\qquad\text{（因 }Q=1\ \text{给出}\ \delta=1_S+1_z,\ |S|=284,\ z\in S\ ⟹\ \delta(z)=2\ ✓\ \text{恰为唯一 }b{=}3\ \text{点 ✓）}$$
$$\textbf{判定}:\ \text{该条件\textbf{既非松弛亦非充分}，与原覆盖问题\textbf{等价}}\ ⚠️\ \Longrightarrow\ \text{是\textbf{换语言}，不自动降低难度}\ ✓$$
$$\qquad\textbf{一处理论增益（可记 ✓）}:\ \text{Booleanity 蕴含 }f^2=f\ \text{型二次关系}\ \Longrightarrow\ \text{强于 Delsarte 的一阶正性族}\ ✓\ \text{（但求解仍等价于原问题 ⚠️）}$$
$$
$$
```

---

## §5 自查（本档三次脚本 bug ⚠️，均已修 ✓）

```
$$\textbf{(S-1)}:\ \text{球交验证未排除 }x=y\ ⟹\ \text{误报 157 违例 ✗（已修 ✓，见 }\texttt{DELSARTE}\ \S1\text{）}$$
$$\textbf{(S-2)}:\ \text{本档 }\widehat b\ \text{实现漏重数（写成"每 }x\ \text{记一次"）⟹\ 首次核验 False ✗（已修 ✓，150 次 0 违背 ✓）}$$
$$\textbf{(S-3)}:\ \text{本次一度把}\ \sum_{\text{all }u}w^2=11264\ \text{当作}\ \sum_{u\ne0}w^2\ ⟹\ \text{得 }201399\equiv7\ (\mathrm{mod}\ 8)\ \text{的\textbf{假矛盾} ✗✗（已修 ✓：真值 }201520=8\times25190\ ✓）}$$
$$\qquad\Longrightarrow\ \textbf{纪律}:\ \text{凡“出现矛盾”必先自审实现（本线累计 20+ 次应验 ✓）}$$
$$
$$
```

---

## §6 判定与建议（诚实 ✓）

```
$$\textbf{本路线}:\ \text{框架正确 ✓、语言干净 ✓；但四步手工推导中\textbf{一至三步无新约束}（自动/可行）✗，第四步＝原问题 ⚠️}$$
$$\textbf{同族预警}:\ \text{excess＋同余＋Fourier 正是\textbf{经典}方法（Van Wee 1988；Haas 2013 ＝ 唐稿文献 [1]）};\ \text{本线 }\texttt{HQ1}\ \text{已试其层式族并\textbf{退化为恒等式}\ ✗ ⟹ 先验收益低 ⚠️}$$
$$\textbf{建议}:\ \text{(a) 若坚持此语言，唯一未试的具体口＝Booleanity 的\textbf{二次关系}（强于 Delsarte ✓）——但求解等价原问题，需新算法 ⚠️；}$$
$$\qquad\text{(b) ⭐ 更符合“换坐标系”原则的落点＝已开的 }\texttt{FRONTIER-R1}\ \text{线（Steiner 设计格／RoSQS 五格 ✓）：那里语言\textbf{不同类}（设计＋群作用）且每格为\textbf{有限可证书}问题 ✓✓}$$
$$
$$
```

---

## §7 边界（诚实标注）

- §1 为**严格推导 ＋ 150 次数值核验** ✓；§2、(F-2b) 的"自动性"判定为**本档结论** ✓
- §3 的可行解为**显式构造** ✓（仅说明**无缺口**，**不**说明真实码的存在性 ✗）
- §4 的"等价"为**本档判定** ✓；§6 的"先验低"为**判断**，非定理 ✓
- **未**排除 $Q=1$ ✗、**未**排除 119 ✗；**未**主张该语言无用 ✗（只主张其**短步已尽** ✓）

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 卷积反演框架确认 命中文件数=1    :: ./FOURIER-2026-09-26-convolution-reformulation-audit.md 
技术词 shell 无缺口判定 命中文件数=1    :: ./FOURIER-2026-09-26-convolution-reformulation-audit.md 
技术词 Booleanity 等价定位 命中文件数=1    :: ./FOURIER-2026-09-26-convolution-reformulation-audit.md
```
- **本档新增**：卷积反演框架确认、shell 无缺口判定、Booleanity 等价定位（见上方命中数）
- **档案已有（引用，不列为提出）**：Haas 层式（HQ1）、Delsarte 族、profile (740,283,1)、$\delta=1_S+1_z$
