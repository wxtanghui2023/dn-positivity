# STATE-2026-09-30 — **块分层分解引理**（120-码精确验证 ✓）＋ **"转移"框架之自我更正** ✗（mixed 族已含 binary 情形 $(b,t){=}(10,0)$ ⟹ 无需转移，只需新的一般计数界）

> 空间 B｜非 C 号｜唐先生 16:48「继续」｜**不主张任何新值**（V290）
> 时间：2026-09-30 17:5x

**已查地图** ✓：`LOCALIZE-2026-09-30`（四重排除）／L3335（上界侧 substitution 已在档）／L3367（Haas 未引 BÖW）
D0: 本档对象 = **档案已有**（covering 条件 ＋ 块分解）之**结构性改写与验证**（新数学对象：见 §2 ⚠️）
D1: 0（产出 = **一条自我更正 ＋ 一条已验证引理 ＋ 一条松弛实测** ⚠️✓）

---

## §0 **档案核查（下界转移）**

$$\text{下界方向之转移原理：档案中\ \textbf{无}} ✗（唯上界侧 }substitution\ \text{在档：}\mathbb F_4\times\mathbb F_2^7\ \text{之 60 词混合码}\to\mathbb F_2^{10}\ \text{之 120-码 ✓）$$

## §1 ⚠️ **自我更正：我方"转移"框架部分错** ✗

$$\text{事实}:\ \text{混合族 }K_{2,3}(b,t;R)\ \textbf{\text{已含二元情形}}\ (b,t){=}(10,0)\ ✓\ (\text{即 }t{=}0)$$
$$\therefore\ \text{BÖW 之 general }R{=}1\ \text{界\ \textbf{在 }}(10,0)\ \text{处之取值，即\ \textbf{直接} 是二元界——}\text{不需要"转移原理"}} ✗✓$$
$$\Longrightarrow\ \text{正确目标}:\ \textbf{\text{一条新的一般（对 }(b,t)\text{）计数界}}\ \text{使 }f(10,0)\ge107\ ✓\ \text{（已知一般界在 }(10,0)\ \text{皆给 }102.4\ ✗）$$
$$\text{（\textbf{本更正撤销}前轮"下界转移"作为\ \textbf{独立目标} 之地位 ⚠️；转移\ \textbf{仍可} 作为\ \textbf{推导工具} ✓）}$$

## §2 **块分层分解引理（本档新；已在 120-码精确验证 ✓✓）**

$$\text{设 }C\subseteq\mathbb F_2^n,\ R{=}1;\ \text{块 }B\subseteq[n]\ (|B|{=}m);\ \text{记 }L_\sigma=\{w:(\sigma,w)\in C\}\subseteq\mathbb F_2^{[n]\setminus B}\ (\sigma\in\mathbb F_2^m)\ ✓$$
$$\qquad Y_\sigma=\bigcup_{\tau:\ d(\tau,\sigma)=1}L_\tau;\quad N_1[L]=\bigcup_{w\in L}(\{w\}\cup\{\text{1-翻转}\})\ ✓$$
$$\textbf{引理}:\ \forall\sigma:\ \boxed{N_1[L_\sigma]\ \cup\ Y_\sigma\ =\ \mathbb F_2^{\,n-m}}\ ✓✓\ \text{（等价于 covering 半径 }\le1\text{）}$$
$$\textbf{实测（120-码，}M{=}120\text{）}:\ m{=}2\ \text{（补维 8）}:\ \text{四 } \sigma\ \text{之并集皆}\ \mathbf{=256}\ \text{（slack}\ \mathbf 0\ ✓);\ m{=}3\ \text{（补维 7）}:\ \text{八 }\sigma\ \text{之并集皆}\ \mathbf{=128}\ \text{（slack}\ \mathbf 0\ ✓）}$$
$$\qquad\text{例（}m{=}2,\ \sigma{=}(0,0)\text{）}:\ |L|{=}28,\ |N_1[L]|{=}207,\ |Y|{=}63,\ \text{并}{=}256\ ✓\ (\text{注}\ 207{+}63{=}270>256\ ⟹\ \text{重叠 14}\ ✓)$$

## §3 **朴素计数形式有松弛** ✗

$$\text{体积式}:\ |L_\sigma|\,(n-m+1)+|Y_\sigma|\ \ge\ 2^{\,n-m}\ \text{（必要 ✓）};\quad \text{在 }120\text{-码 }m{=}2,\ \sigma{=}(0,0):\ 28{\cdot}9{=}252\ \ge\ 256-63{=}193\ ⟹\ \textbf{slack }59\ ✗$$
$$\therefore\ \boxed{\text{单块体积式\ \textbf{不足}} ✗\ \text{（"有效但不足"之又一例 ⚠️）};\ \text{真正紧的是\ \textbf{精确并集式}\ (✓)\ 与\ \textbf{亏损结构}\ (\text{哪些点被恰一次覆盖}) ✓}$$
$$\text{故可用之攻击面} =\ \textbf{\text{分层精确覆盖 ＋ 亏损（重数）结构}}\ \text{——即\ \textbf{支撑层/排列层} ✓✓（与 L1554 定位一致 ✓）}$$

## §5 【技术词回查】（`scripts/tech_word_check.sh` 逐字输出 ✓）

```
技术词 块分层     命中文件数=1    :: 本档
技术词 分层精确覆盖  命中文件数=1    :: 本档
```

$$\textbf{分类}:\ \text{两词仅本档命中} \Longrightarrow \textbf{本档新增} ✓;\quad \text{“块分层分解引理”为该对象首次命名 ✓}$$
$$\text{空间 A/B 分离（AMEND-27）}:\ \text{无跨空间同名} ✓$$


## §4 边界与纪律

$$\textbf{(D1)}\ \text{无 P1} ✗;\ \textbf{(D2)}\ \text{§1 自我更正已明示（不留错框架 ✓）};\ \textbf{(D3)}\ \text{未主张新值／未取禁用原文／未碰 RH} ✓$$

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=FINGERPRINT-CITED R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
