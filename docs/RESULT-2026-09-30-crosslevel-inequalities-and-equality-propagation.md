# RESULT-2026-09-30 — **(乙) 跨层一致性**：两条**可证**跨层不等式（两码零违反 ✓✓）＋ **(甲) 之钥：等式条件逐层传播** ✓✓

> 空间 B｜非 C 号｜唐先生 16:59「先乙，再甲」｜**不主张任何新值**（V290）
> 时间：2026-09-30 18:2x

**已查地图** ✓：`RESULT-2026-09-30-per-y-inequality-slack-distribution`／`tight-per-y-pattern-inequality`（不等式本体）
D0: 本档对象 = **该不等式族之跨层（$m\to m{+}1$）结构**（新 ✓，档案无同名）
D1: 0（产出 = **两条可证跨层不等式 ＋ 一条等式传播律 ＋ 一条(甲)之具体靶** ⚠️✓）

---

## §0 **先撤销我的错误推导** ✗（纪律 ✓）

$$\text{我\ \textbf{曾\ \textbf{误推}}}:\ \delta^{(m+1)}=\delta^{(m)}_0+\delta^{(m)}_1+(s_0{+}s_1)+(c_0{+}c_1) ✗\ ——\ \text{实测\ \textbf{92/256 违反}} ⟹ \textbf{\text{当场撤销}} ✓$$
$$\text{真关系（重推 ✓）}:\ \delta^{(2)}_{y_2}=\delta^{(1)}_{(0,y_2)}+\delta^{(1)}_{(1,y_2)}+(s_0{+}s_1)+(u'-u_0-u_1)\quad\text{其中 }u'\le u_0{+}u_1,\ u_0{+}u_1\le u'+ (s_0{+}s_1)\ ✓$$
$$\qquad(u_b:=|U^{(1)}_{(b,y_2)}|,\ u':=|U^{(2)}_{y_2}|;\ \text{证}: U^{(1)}_{(b,y_2)}=A_b\cup B_b,\ u'=|A_0|{+}|A_1|,\ |B_b|=s_{1-b}\ ⟹\ |A_b|\le|A_b\cup B_b|\le|A_b|{+}s_{1-b}\ ✓)$$

## §1 **两条可证跨层不等式（实测零违反 ✓✓）**

$$\boxed{\textbf{(i) 超加性}:\ \delta^{(2)}_{y_2}\ \ge\ \delta^{(1)}_{(0,y_2)}+\delta^{(1)}_{(1,y_2)}} ✓\quad \text{（120-码 0/256；62-码 0/128）}$$
$$\boxed{\textbf{(ii) 上界}:\ \delta^{(2)}_{y_2}\ \le\ \delta^{(1)}_{(0,y_2)}+\delta^{(1)}_{(1,y_2)}+(s_0{+}s_1)} ✓\quad \text{（同前，零违反）}$$

## §2 **(甲) 之钥：等式条件逐层传播** ✓✓

$$\delta^{(2)}_{y_2}=0\ \Longrightarrow\ \delta^{(1)}_{(0,y_2)}=\delta^{(1)}_{(1,y_2)}=0\ \ \textbf{\text{且}}\ \ u_0{+}u_1-u'=s_0{+}s_1\ (\text{极端情形}) ✓✓$$
$$\therefore\ \textbf{\text{高阶取等强制低阶取等}} ⟹ \text{等式条件沿层级\ \textbf{向下传播}};\ \text{又}\ \delta^{(1)}_b=0\ \text{自身即刚性构型（球族两两不交＋严格补集} ✓)$$
$$\Longrightarrow\ \textbf{(甲) 之具体靶}:\ \text{证“}\exists m_0,y:\ \delta^{(m_0)}_y=0\ \text{之刚性构型无法满足\ \textbf{全层传播}}”\ \text{或证“全等情形}\ (\forall m,y:\delta=0)\ \text{不可能”} ⚠️$$

## §3 **全等情形之算术条件（诚实 ⚠️）**

$$\forall m,y:\ \delta^{(m)}_y=0\ \Longrightarrow\ \sum_\sigma|N_1[L_\sigma]|=2^n-(m+1)M\ \text{对一切 }m\ \text{成立} \Longrightarrow\ (m{+}1)M\le2^n\ \forall m\ \text{相关层级} ✓$$
$$\qquad M{=}106,n{=}10:\ (m{+}1)\cdot106\le1024\Longrightarrow m\le8\ ✓\ \text{（\textbf{算术上可能}} ⚠️）$$
$$\therefore\ \text{“全等情形不可能”\ \textbf{不能}由算术直接得出} ✗;\ \text{须用\ \textbf{局部刚性＋传播} 之组合} ⚠️\ ——\ \text{即\ (甲) 之真正内容 ✓}$$

## §5 【技术词回查】（`scripts/tech_word_check.sh` 逐字输出 ✓）

```
技术词 跨层不等式  命中文件数=2    :: P10X4-2026-09-26-decoupling-and-four-one-line-lemmas.md ＋ 本档
技术词 等式传播     命中文件数=1    :: 本档
```

$$\textbf{分类（三项如实 ✓）}:\ \text{(1) }\textbf{本档新增}：\text{“等式传播”} ✓;\quad \text{(2) }\textbf{档案已有（引用，不列为提出）}：\text{“跨层不等式”命中 }P10X4\text{-2026-09-26（空间 A 之 decoupling 线）} ⟹ \text{本档**不**主张该词之新性} ✗;\quad \text{(3) }\textbf{通用词（不计）}：\text{“跨层／传播”裸词}$$
$$\text{空间 A/B 分离（AMEND-27）}:\ \text{“跨层不等式”之既有命中属空间 A（decoupling 线），对象不同，} ⟹ \text{标为**跨空间同名（不计）**} ✓$$


## §4 边界与纪律

$$\textbf{(D1)}\ \text{无 P1} ✗;\ \textbf{(D2)}\ \text{误推已撤销（92/256 违反为据 ✓）};\ \textbf{(D3)}\ \text{未主张新值／未取禁用原文／未碰 RH} ✓$$

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=FINGERPRINT-CITED R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
