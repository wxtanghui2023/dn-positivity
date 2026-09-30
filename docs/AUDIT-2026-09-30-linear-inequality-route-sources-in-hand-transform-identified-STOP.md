# AUDIT-2026-09-30 — 路线 A/B 文献核对：**两路线之来源皆在手** ✓✓；"linear inequality ⟹ 下界" 转换机器**已定位** ✓；按预注册判据 **A、B 皆 STOP** ✗

> 空间 B｜非 C 号｜唐先生 20:02 令（追 linear-inequality / mixed 转换机制）｜**不主张任何新值**（V290）

**已查地图** ✓：`RESULT-2026-09-30-sqr-census…`（STOP）／ASSETS-REGISTRY L1551–L1554（Habsieger 体系逐字＋A 型输出）／L1891（R2-1 DROP）／MASTER-FAILURE-MAP-107-LINE
D0: 本档对象 = **档案已有＋我方实有来源之定位与判定**（新数学对象：无 ✗）
D1: 0（产出 = **来源清单 ＋ 转换机器定位 ＋ 判据触发** ⚠️✓）

---

## §0 **来源（两路线皆在手 ✓✓）**

$$\text{(a) }\mathbf{Haas\ 2008}\ \text{（实有全文 ✓）}:\ \S3.4\ \text{Habsieger's improvement and the excess matrix};\ \S3.5\ \text{（Thm 26/32、excess matrix 主性质）};\ \S3.6\ \text{congruence set systems};\ \S3.7\ \text{the general excess bound improved}$$
$$\text{(b) }\mathbf{van\ Wee\ 1991\ thesis}\ \text{（实有 ✓ `vanWee-1991-thesis-TUe-353803.pdf`）}＋\mathbf{Paper\ 6}\ \text{（mixed bounds 全文 EXTRACT ✓ `vanWee-thesis-Paper6-mixed-bounds-EXTRACT.txt`）}$$
$$\qquad\text{Paper 6 逐字}:\ \text{“Theorem 16 generalizes Corollary 1a of [32]. It is always at least as good as the sphere covering bound.”};\ \text{“[19] ＝ van Lint jr., van Wee, }\textbf{\text{Generalized bounds on binary/ternary mixed packing and covering codes}}\text{, JCTA 57 (1991) 130–143” ✓}$$

## §1 **“线性不等式 ⟹ 下界” 转换机器（逐字定位 ✓）**

$$\textbf{Def 28（condition (}q\text{)）}:\ \exists\beta_0..\beta_{q-2}:\ \sum_{0\le i\le q-2}\beta_iE_i(x)+E_{q-1}(x)\equiv0\ (\mathrm{mod}\ q)\quad\forall x\in\mathbb F^n\ ✓$$
$$\textbf{Def 30（excess matrix）}:\ \text{设 }E_0=\dots=E_{p-2}=0;\ d_j\ (j\in A,\ |A|=E_{p-1})\ \text{遍历 }\mathbb Z\cap B(0,p-1)\ \text{按重数}\ E(d);\ D=(\text{行}=d_j)\in\mathbb Z^{E_{p-1}\times n};\ \text{列集 }B_1..B_n\subset A\ ✓$$
$$\textbf{Thm 31}:\ \text{condition (}q\text{)}\ \Longrightarrow\ \text{列集 }B_i\ \text{之强结构};\qquad \textbf{Thm 29（Habsieger）}:\ p\ge5\ \text{时}\ \boxed{E_{p-1}(x)\ \ge\ \mathbf{2p-1}}\ (\text{原 }p-1)\ \text{若满足 (}p{-}1\text{)、(}p{-}2\text{) ✓}$$
$$\therefore\ \textbf{\text{这正是您要的“先造线性不等式／同余条件，再转成 }K(n,R)\ \text{下界”之机器}} ✓✓$$

## §2 **当场核出之关键事实（本档新 ✓）**

$$\text{层和恒等式}:\ \sum_i\delta_i=11M-2^{10}=11M-1024\ ✓\ (\text{由层公式 (4) 之系数恒为 }11\text{ 得})\ ✓$$
$$\text{Lemma 2（}p=11\mid n{+}1\text{）}:\ \sum_{i<11}\delta_i\equiv10\ (\mathrm{mod}\ 11)\ ✓;\ \text{而 }11M-1024\equiv-1024\equiv-1\equiv10\ (\mathrm{mod}\ 11)\ \text{（}1024\equiv1\text{）} ✓$$
$$\Longrightarrow\ \textbf{\text{该同余对 }M\ \textbf{恒等相容、零约束}} ✗✓;\ \text{真正有牙者＝}q{=}p{-}1{=}10,\ q{=}p{-}2{=}9\ \text{之\ \textbf{深层 condition (}q\text{)}} ✓$$

## §3 **档案既有之判定（引用，不重复）**

$$\textbf{A 型输出（L1554 ✓）}:\ \{\delta_i\}\ \text{与}\ \{N_i\}\ \text{逐点互定} ⟹ \text{凡只用 }\{N_i\}/\{\delta_i\}\ \text{（层和、模 }p\ \text{同余、对 }x\ \text{聚合）之判据\ \textbf{完全由距离层决定}} ✓$$
$$\qquad\textbf{见证（P12-PASS）}:\ \text{三个最优 }(8,32)_1\ \text{码\ \textbf{距离分布相同} 而 }\sum_{i<j}q_{ij}^2=64/128/256 ⟹ \textbf{\text{距离层判据无法区分}} ⟹ \textbf{\text{坐标支撑层承载距离层之外的信息}} ✓✓$$
$$\qquad\Longrightarrow\ \text{van Wee／Habsieger／Zhang／Wu–Chen 之\ \textbf{全部量} 只依赖 }(N_i,\delta_i)\ \text{或其局部几何} ⟹ \textbf{\text{支撑层在其体系内结构性不可见}} ✓$$
$$\text{数值（L1551）}:\ \text{Habsieger（FPSAC95）已覆盖 }n\equiv2,4\bmod6 ⟹ n{=}10\ \text{给 }\ge104;\ \text{Zhang }\ge105\ ⟹ \textbf{\text{低于 107}} ✗$$

## §4 **判据核对（唐先生 20:02 预注册）**

$$\textbf{路线 A（HP 2000 转换）}:\ \text{转换机器\ \textbf{已定位} ✓（=§1）；但其内容＝}(N_i,\delta_i)\text{-only} ⟹ \text{喂入我方 }A_1,A_2,E,T_N\ \textbf{\text{只会压回 103–106 层}} ✗ \Longrightarrow \mathbf{STOP}\ ✗$$
$$\textbf{路线 B（van Lint–van Wee mixed）}:\ \text{其 general 式在 }(t,b){=}(0,10)\ \text{给}\ \frac{10\cdot1024}{110-10}=102.4\Rightarrow\mathbf{103}\ ✗\ (\text{档案已核 ✓});\ \text{其余 }(b,t)\ \text{为\ \textbf{混合空间} 之界（非 }K_2(10,1)\text{），且\ \textbf{无二元转移}} ✗ \Longrightarrow \mathbf{STOP}\ ✗$$
$$\textbf{唯一仍在之假说} ✓:\ \text{BÖW general }R{=}1\ \text{＝同族中一条\ \textbf{被加强} 之界，其 }(0,10)\ \text{取值}=107 ⚠️\ ——\ \text{重建需 [19]/[130] 正文（\textbf{不在手}} ✗)$$

## §6 【技术词回查】（`scripts/tech_word_check.sh` 逐字输出 ✓）

```
技术词 转换机器     命中文件数=1    :: 本档
技术词 来源在手     命中文件数=0    :: 
```

$$\textbf{分类}:\ \textbf{本档新增}：\text{“转换机器”仅本档（“来源在手”全档 0 命中）} ✓;\quad \textbf{档案已有}：\text{无};\quad \textbf{通用词（不计）}：\text{“路线／判据／机器”裸词} ✓$$
$$\text{空间 A/B 分离（AMEND-27）}:\ \text{无跨空间同名} ✓$$


## §5 边界与纪律

$$\textbf{(D1)}\ \text{无 P1} ✗;\ \textbf{(D2)}\ \text{判据预注册、未事后改};\ \textbf{(D3)}\ \text{未主张新值／未取禁用原文／未碰 RH} ✓$$

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=FINGERPRINT-CITED R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
