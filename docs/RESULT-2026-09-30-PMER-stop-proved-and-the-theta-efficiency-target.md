# RESULT-2026-09-30 — **PMER 之 STOP 可证明** ✓✓（profile 影子 $=F_k$）＋ **集合级签名表** ＋ **★ $\theta$-效率定量靶**（可证伪、非聚合）

> 空间 B｜非 C 号｜唐先生 20:00 令：机制级 STOP 与原问题 STOP 必须分开；下一刀转"local feasibility → global compatibility"｜**不主张任何新值**（V290）

**已查地图** ✓：`RESULT-2026-09-30-PMER-implemented-…`／`RESEARCH-2026-09-30-local-to-global-…`（§8–§11）／`STATE-2026-09-30-block-layer-decomposition…`／L1554（支撑层＝自由度）
D0: 本档对象 = **档案已有对象之\ \textbf{证明性} 刻画 ＋ 签名表 ＋ 新定量靶**（新定理 ✓）
D1: 0（产出 = **一条 STOP 之证明 ＋ 一张签名表 ＋ 一个可证伪靶** ⚠️✓）

---

## §0 **PMER：STOP（枚举机制）** —— 且此 STOP 可\ \textbf{证明} ✓✓

$$\textbf{精确全局条件（k{=}2，四块分层引理之逐 }\sigma\ \text{形式）}:\ \forall\sigma\in\mathbb F_2^2:\ \Delta_\sigma\ :=\ Q_8\setminus N_1[L_\sigma]\ \subseteq\ \bigcup_{\tau:\ d(\tau,\sigma)=1}L_\tau\ ✓$$
$$\qquad\text{实测（120-码）}:\ \textbf{\text{违反 0/4}} ✓✓\ \text{（即精确条件成立）};\quad \text{证}:\ \text{点 }(\sigma,y)\ \text{被}\ \text{本 fiber（}y\in N_1[L_\sigma]\text{）或邻 fiber 之\ \textbf{恰同后缀}（}y\in L_\tau,\ d(\tau,\sigma){=}1\text{）覆盖} ✓$$
$$\textbf{其 profile 影子（本档关键 }✓✓\text{）}:\ \text{由 }|\Delta_\sigma|=2^{nc}-|N_1[L_\sigma]|\ \text{与}\ |N_1[L_\sigma]|\le(nc{+}1)m_\sigma\ \text{得必要式}$$
$$\qquad\boxed{(nc{+}1)\,m_\sigma+\sum_{\tau\sim\sigma}m_\tau\ \ge\ 2^{nc}}\quad\text{——}\textbf{\text{恰为 }}F_k\text{ 本身}} ✓✓$$
$$\therefore\ \boxed{\text{精确条件之一切\ \textbf{逐 }\sigma\text{/成对 profile 影子}\ 皆等于 }F_k} ⟹ \textbf{\text{任何 profile 级目录（含 PMER 及其变体）\ \textbf{证明性} 地看不见兼容性内容}} ✓✓$$

## §1 **集合级签名表（新资产 ✓）（120-码，$k{=}2$，$|Q_8|{=}256$）**

| $\sigma$ | $\|L_\sigma\|$ | $\|N_1[L_\sigma]\|$ | $\|\Delta_\sigma\|$ | 精确式松弛 $\sum_{\tau\sim\sigma}\|L_\tau\|-\|\Delta_\sigma\|$ | $F_k$ 影子松弛 |
|---|---|---|---|---|---|
| 00 | 28 | 207 | 49 | **15** | 60 |
| 01 | 32 | 210 | 46 | **10** | 88 |
| 10 | 32 | 210 | 46 | **10** | 88 |
| 11 | 28 | 207 | 49 | **15** | 60 |

$$\therefore\ \textbf{\text{集合级签名比 profile 影子紧得多（松弛 10–15 vs 60–88）}} ✓\ ——\ \text{即：}\textbf{\text{兼容性之信息确实存在于集合级}} ✓$$

## §2 **★ $\theta$-效率靶（本档新，可证伪、非聚合 ✓✓）**

$$\text{精确条件}\ \Longrightarrow\ \text{必要式}:\ |N_1[L_\sigma]|\ \ge\ 2^{nc}-\sum_{\tau\sim\sigma}m_\tau\ ✓$$
$$\text{定义\ \textbf{效率}}:\ \theta(L):=\frac{|N_1[L]|}{(nc+1)|L|}\ \le\ 1\ \text{（球不交时为 1；重叠时 <1）};\quad \theta_\sigma:=\frac{|N_1[L_\sigma]|}{9\,m_\sigma}$$
$$M{=}106\ \text{（均衡 }m\approx26.5\text{）}:\ \text{需}\ |N_1[L_\sigma]|\ge256-53=203\ \Longrightarrow\ \boxed{\theta_\sigma\ \ge\ \frac{203}{9\cdot26.5}\approx0.867}\ ⚠️$$
$$\textbf{实测（120-码）}:\ \theta=\frac{207}{252}=0.821\ (\text{对 }|L|{=}28);\quad \frac{210}{288}=0.729\ (\text{对 }|L|{=}32)\ ⟹\ \textbf{\text{皆低于 }0.867} ✗✓$$
$$\therefore\ \boxed{\text{若证“任意 cover 之切片 }L\ \text{满足 }\theta(L)\le\sim0.86\text{”（或其与 }(|L|,M)\ \text{之权衡式）} ⟹ M\ge107}\ ✓✓$$
$$\textbf{此靶之优点}:\ \text{(i) \textbf{\text{非聚合}}（依赖切片之\ \textbf{形状}／聚类度，非仅 }|L|\text{）};\ \text{(ii) \textbf{\text{实测方向正确}}（0.73–0.82 vs 需 }0.867\text{）};\ \text{(iii) \textbf{\text{可证伪}}（反例＝高聚类切片）} ✓✓$$
$$\textbf{诚实}:\ \text{未证} ✗;\ \text{且一般切片可为球不交型（}\theta{=}1\text{，如最短距离 3 之码），故须\ \textbf{与规模条件联立}（那类切片需邻域 }m_\tau\ \text{极大），即真形式为\ \textbf{\text{权衡式}} ⚠️$$

## §4 【技术词回查】（`scripts/tech_word_check.sh` 逐字输出 ✓）

```
技术词 效率靶        命中文件数=1    :: 本档
技术词 签名表        命中文件数=1    :: 本档
```

$$\textbf{分类}:\ \textbf{本档新增}：\text{两词皆仅本档} ✓;\quad \textbf{档案已有（不列）}：无;\quad \textbf{通用词（不计）}：\text{“效率／签名”裸词} ✓$$
$$\text{空间 A/B 分离（AMEND-27）}:\ \text{无跨空间同名} ✓$$


## §3 边界与纪律

$$\textbf{(D1)}\ \text{无 P1} ✗;\ \textbf{(D2)}\ \text{影子的等价性为证明（非拟合）；实测 0/4、松弛表皆实测 ✓};\ \textbf{(D3)}\ \text{未主张新值／未取禁用原文／未碰 RH} ✓$$

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=FINGERPRINT-CITED R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
