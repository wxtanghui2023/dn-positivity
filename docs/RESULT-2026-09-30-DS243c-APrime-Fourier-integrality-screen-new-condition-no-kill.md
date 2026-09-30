# RESULT-2026-09-30-DS243c — (a′) Fourier/整性筛：得**新必要条件 $\sum m^2=601$** ✓，但**无硬杀** ✗ ⟹ 按 STOP 进 (a)

> 空间 B｜非 C 号｜唐先生 12:50「选 (a′)→(a)；STOP 条件：只有推出某 fiber/差谱**不存在**才记 P1」｜**不主张任何新值**（V290）
> 时间：2026-09-30 13:1x

**已查地图**：承 `DS243`／`DS243b`（乘子约化、$\{36,40,45\}$）
D0: 本档对象 = **档案已有**（$\mathbb Z_9^2$-fiber 结构）之 **Fourier 筛**（新数学对象：无 ✗）
D1: 0（产出 = **一条新必要条件 ＋ 一条等价性判定 ＋ 一条非杀判定** ⚠️✓）

---

## §0 记号与约束（**方向计数已按 DS243b 重新核实** ✓）

$$H=\mathbb Z_9^2\ (\text{阶}81);\ C_0,C_1,C_2=G/H\ (\mathbb Z_3);\ R_i=D\cap C_i,\ r_i\in\{36,40,45\};\ \sum_i r_i=121$$
$$a_i(h):=|\{x\in R_i:\ x+h\in R_i\}|\quad(h\in H);\qquad b_{ij}(h):=|\{x\in R_i:\ x+h\in R_j\}|\ (i\ne j)$$
$$\textbf{硬约束（已核方向）}:\quad \forall\,0\ne h\in H:\quad \sum_i a_i(h)=60\ ✓\quad(\text{须 }d,d'\text{ 同在 }C_i)$$

## §1 Fourier 侧：**与总量条件等价**（诚实结论 ⚠️）

$$\text{Parseval}:\ \sum_{\chi\in\hat H}|\widehat{1_{R_i}}(\chi)|^2=|H|r_i=81r_i;\qquad a_i=\text{自相关}\Longrightarrow \hat a_i(\chi)=|\widehat{1_{R_i}}(\chi)|^2\ge0$$
$$\Longrightarrow\ \sum_i \hat a_i(\chi)=\sum_h\Big(\sum_i a_i(h)\Big)\chi(h)=121\cdot\chi(0)+60\!\!\sum_{h\ne0}\!\chi(h)=\boxed{61}\quad(\text{每个非平凡 }\chi)$$
$$\text{而 }\sum_{\chi\ne1}\sum_i\hat a_i(\chi)=80\cdot61=4880=81\cdot121-4921\ ✓\ (\text{自洽})$$
$$\therefore\ \textbf{该条件与“}\sum_i a_i(h)=60\text{”\textbf{逐字等价}（Fourier 可逆）} \Longrightarrow \text{单看它\ \textbf{不带来新信息}} ✗;$$
$$\qquad\textbf{新信息只在“每个 }\hat a_i\ \text{必须是真指示函数之模方”这一\ \textbf{可实现性} 上} ✓$$

## §2 **新必要条件**（阶-3 字符 ⟹ 更细分布约束）✓

$$\text{阶-3 字符 }\chi\ \text{在 }3H=\{3x\}\cong\mathbb Z_3^2\ \text{之 9 个陪集上常值};\ \text{令 }m_{i,j}=|R_i\cap(\text{第 }j\text{ 个陪集})|,\ \sum_j m_{i,j}=r_i,\ m\le9$$
$$\hat a_i(\chi)=r_i^2-3(AB+BC+CA)_i\quad(A,B,C=\text{该平行类三块之和})$$
$$\text{每平行类}:\ \sum_i(AB+BC+CA)_i=\frac{4921-61}{3}=1620\ \ (\text{4 个平行类})$$
$$\textbf{本档新恒等式（200 随机例核验 ✓✓）}:\quad \sum_{c=1}^{4}(AB+BC+CA)_c=\frac32\big(r^2-\sum_j m_j^2\big)$$
$$\Longrightarrow\ \sum_c\sum_i(\cdots)=6480=\frac32\sum_i\Big(r_i^2-\sum_j m_{i,j}^2\Big)\ \Longrightarrow\ \boxed{\sum_{i,j}m_{i,j}^2=4921-4320=\mathbf{601}}$$
$$\textbf{这是\ \textbf{新} 必要条件} ✓\ (\text{涉及比 }\{r_i\}\ \text{更细之数据 }m;\ \text{不依赖 61-乘子})$$

## §3 可行性判定（**不杀** ✗）

$$\sum_j m^2\ \text{最小值（均匀）}:\ 36{:}144,\ 40{:}180,\ 45{:}225\ \Longrightarrow\ 549;\qquad \text{最大}:\ 324,\ 340,\ 405\ \Longrightarrow\ 1069$$
$$549\ \le\ \mathbf{601}\ \le\ 1069\ \Longrightarrow\ \textbf{可行（无矛盾）} ✗\quad(\text{但 601 是\ \textbf{紧约束}，可进强搜索})$$
$$\text{另核：模 3 同余 }\hat a_i\equiv r_i^2\ (\mathrm{mod}\ 3)\ \Longrightarrow\ \sum_i r_i^2\equiv61\equiv1\ (\mathrm{mod}\ 3)\ ✓;\ \ \sum_i(AB+BC+CA)_i=1620\equiv0\ (\mathrm{mod}\ 3)\ ✓\ \text{自洽}$$

## §4 **判定（回应 STOP 条件）**

$$\boxed{\text{Fourier/整性筛\ \textbf{未}推出任何 fiber 或差谱不存在} ✗ \Longrightarrow \textbf{不记 P1};\ \text{全部只作\ \textbf{搜索约束}}}$$
$$\text{收益（可审计）}: \textbf{(i)}\ \sum m^2=601\ \text{（新）};\ \textbf{(ii)}\ \text{平行类层面 }1620/类\ \text{（新）};\ \textbf{(iii)}\ \text{确认总量条件与 Fourier 侧等价（防重复包装 ✓）}$$

## §5 纪律（照唐先生指示 ✓）

$$\textbf{(D1)}\ \text{v3 仅 "feasibility signal only"}\ ✓;\quad \textbf{(D2)}\ \text{61-乘子假设\ \textbf{仍待核}} ⚠️,\ \text{仅作计算约束};\quad \textbf{(D3)}\ \text{无新数学对象／未取文献原文／未碰 RH}\ ✓$$
$$\textbf{(D4) 自查}:\ \text{曾误判 }\hat a_i\ \text{必为整数（实为\ \textbf{实代数整数}，不必有理）} ⟹ \text{当场修正} ✓$$

## §6 去向：**(a) 立即执行** ✓

$$\text{强搜索之硬约束} = \boxed{\{r_i\}=\{36,40,45\}\ (\text{逐陪集})}\ +\ \boxed{\sigma\text{-不变（99 轨道）}}\ +\ \boxed{\sum m^2=601\ (\text{二级})} +\ \boxed{K\ \text{阶 }9\ \text{之 378 解（三级，不一次塞入）}}$$

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=NA R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
