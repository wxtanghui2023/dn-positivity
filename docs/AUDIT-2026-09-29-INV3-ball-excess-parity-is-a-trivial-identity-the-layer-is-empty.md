# AUDIT-2026-09-29-INV3 — 第 3 轮：**"球 excess parity" 是恒等式的直接推论**（该层**零信息**）；深层同余**不存在**

> 空间 B｜非 C 号｜唐先生 23:34「继续」｜**不主张任何新值**（V290）

**已查地图**：`AUDIT-29i/j/l/m`（parity 三次同型）／`AUDIT-28q`（可调参数表）／本会话 `INV2`
D0: 本档对象 = **档案已有**（球 excess／Habsieger 同余）之**恒等式化审计**（新数学对象：无 ✗）
D1: 0（产出 = **一条新恒等式 ＋ 一条"层为空"判定 ＋ 一处自查** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① 新恒等式（1024/1024 全验 ✓✓）}:\ \delta_{N[v]}\ =\ 11\cdot\mathbf1_{v\in C}\ +\ 2a_1(v)\ +\ 2a_2(v)\ -\ 11}$$
$$\qquad\Longrightarrow\ \text{其 parity（}v\notin C\Rightarrow\text{奇};\ v\in C\Rightarrow\text{偶}\text{）\ \textbf{自动成立}}$$
$$\boxed{\text{② 故档案所记"球 excess parity（904/904、120/120）"＝此恒等式之\ \textbf{平凡推论} ⟹ \textbf{零信息}}\ ⚠️}$$
$$\boxed{\text{③ 深层同余（mod 4/8）\ \textbf{不存在}：}\delta\ \text{与}\ (a_1{+}a_2)\ \text{在各模数下\ \textbf{取遍全部余类}} ⟹ \text{该层\ \textbf{为空}}\ ✗}$$

## §1 恒等式（推导 ＋ 全验）

$$ \delta_{N[v]}=\sum_{y\in N[v]}\bigl(\mu(y)-1\bigr)=\Bigl(\sum_{c\in C}\bigl|N[c]\cap N[v]\bigr|\Bigr)-11$$
$$\text{而}\ \bigl|N[c]\cap N[v]\bigr|=\begin{cases}11 & d(c,v)=0\\ 2 & d(c,v)=1,2\\ 0 & d(c,v)\ge3\end{cases}\ \Longrightarrow\ \delta_{N[v]}=11\mathbf1_{v\in C}+2a_1(v)+2a_2(v)-11\quad(a_j:=\#\{c:d(c,v)=j\})$$
**实测**：120-码 全 1024 点 **不符者 = 0** ✓✓

$$\therefore\ \text{parity 之"发现"（`29j`/`29l` 逐条实测 904/904、120/120）\ \textbf{无需任何结构}：}2a\ \text{为偶、}11\ \text{为奇}\ \checkmark$$

## §2 深层同余之搜索（**实跑，否**）

| 对象 | mod 2 | mod 4 | mod 8 |
|---|---|---|---|
| $\delta_{N[v]}$（$v\in C$） | $\{0{:}120\}$ | $\{0{:}72,\ 2{:}48\}$ | $\{0{:}50,2{:}23,4{:}22,6{:}25\}$ |
| $\delta_{N[v]}$（$v\notin C$） | $\{1{:}904\}$ | $\{1{:}452,\ 3{:}452\}$ | $\{1{:}346,3{:}423,5{:}106,7{:}29\}$ |
| $a_1{+}a_2$（$v\notin C$） | $\{0{:}452,1{:}452\}$ | $\{0{:}106,1{:}29,2{:}346,3{:}423\}$ | — |

$$\boxed{\text{除 mod 2（恒等式推论）外，\textbf{无任何同余律}} \Longrightarrow \text{Habsieger 之同余\ \textbf{不在此处}}（至少不在此对象上）}\ ✗$$

## §3 ⚠️ 自查

$$\text{我核验式曾写"}\Sigma_{v\notin C}a_1\ \text{应}=10M=1200\text{"} \Longrightarrow \textbf{错误}:\ \text{正确}=\ 10M-2A_1=1100\ \checkmark\ (\text{实跑 1100 ✓，数据无误，仅核验式写错})$$

## §4 第 3 轮判定与去向

$$\text{第 3 轮}:\ \textbf{未找到丢失之细节};\ \text{但\ \textbf{排除}了"球 excess parity／深层同余"这一支} ⟹ \text{细节不在此}$$
$$\text{下一候选（唯一未探之形）}:\ \text{Habsieger 摘要逐字是"covering condition\ \textbf{as a system of linear inequalities}\ ＋ excesses\ \text{之同余}"}$$
$$\qquad\Longrightarrow\ \text{同余之载体可能是\ \textbf{多个 excess 变量之联立系统}（含跨距离类约束），而非单点 }\delta$$
$$\qquad (\text{且 }AUDIT\text{-}29e\ \text{已证：单条线性 }\le105.2223 \Longrightarrow \text{其力量必来自\ \textbf{整性/同余}那一半}) ⚠️$$

## §5 边界（硬 ✓）

- **不主张**任何新值；本档为**审计**（含一处自查）✓
- 未取论文原文（R16–17）✓

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=NA R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
