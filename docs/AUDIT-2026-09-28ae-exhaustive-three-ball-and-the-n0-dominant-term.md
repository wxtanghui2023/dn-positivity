# AUDIT-2026-09-28ae — **穷举定谳：交大小$\in\{0,1\}$（"3 中心"否）＋ $n_0$ 为主项（$(5)/(F)$ 假之根因）**

> **性质**：**审计（穷举实测）**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-28 22:27 ✓
> **唐先生令**：严纠上一轮断言 ✓

**已查地图**：接续 `AUDIT-ad`（$T{=}\triangle(G_2)$）／`AUDIT-ac`（三矩）／`EXCESS-2026-09-25`（三球交表）✓

D0: 本档对象 ＝ **档案已有**（三球交／$n_0,n_1,n_2$／$G_2$——`EXCESS-2026-09-25` 已载交表 ✓）
D1: 0（产出＝**穷举定谳 ＋ 新量 $n_0$ 定位 ＋ 三处纠正** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✗ 唐先生本轮之"纠错"}\ \textbf{本身有误}:\ \text{交大小\ \textbf{只取 }0\ \text{或 }1};\ \text{Type I 亦为 }1\ \text{中心（非 }3\text{）}}$$
$$\boxed{\text{② ✓ 原断言成立且\ \textbf{双重确认}}:\ T=138=41+97=\triangle(G_2(C))}$$
$$\boxed{\text{③ ✗ }(5)/(F)\ \text{之根因} ＝ \text{漏掉}\ n_0;\ \text{实测}\ \Sigma n_0=220\ \text{（\textbf{主项}）}}$$

## §1 ① 穷举定谳：三球交大小 $\in\{0,1\}$（**穷举全部 $\binom{120}3$ ✓✓**）

$$\text{非零之距离型\ \textbf{仅两类}}:\ (1,1,2)\Rightarrow\text{交 }1\ (\textbf{41 次});\qquad (2,2,2)\Rightarrow\text{交 }1\ (\textbf{97 次})$$
$$\text{其余全部距离型}\Rightarrow\text{交 }0;\qquad \textbf{交大小取值集合} = \{0,\ 1\}\ \Longrightarrow\ \text{无 }\ 3\ \text{者}\ ✗✗$$
$$\text{逐例验证}:\ \{0,e_1,e_2\}\Rightarrow\text{共同 }1\text{-中心} = \{0\}\ (\text{数}=\mathbf 1);\qquad \{e_1,e_2,e_4\}\Rightarrow\{0\}\ (\text{数}=\mathbf 1)$$
$$\text{理由}:\ \text{若 }x{=}e_i\ \text{为共同中心}\Rightarrow d(e_i,e_j)=2>1\ ✗;\ \text{故 }e_i,e_j\ \textbf{不是}共同中心$$
$$\therefore\ \boxed{\text{唐先生原断言（共同中心\ \textbf{唯一}）\ \textbf{正确}};\ \text{本轮之"3 中心"纠正}\ \textbf{撤销}}\ ⚠️✓$$

## §2 ② 三角形接口之双重确认（**✓✓**）

$$\triangle(G_2(C))=41+97=\mathbf{138}=T=\sum_x\binom{a(x)}3\ \Longrightarrow\ \boxed{T=\triangle(G_2(C))}\ \text{（两法独立一致）}✓✓$$
$$\text{且}\ \Sigma_x\delta^3=E+6\triangle(G_2)\ \text{恒等成立}\ ✓$$

## §3 ③ $(5)/(F)$ 之根因：漏 $n_0$（**本档关键诊断 ✓✓**）

$$\text{唐先生之分解}:\ d_2(c)=n_1(c)+n_2(c)\ \textbf{漏了}\ n_0(c)\ ✗$$
$$\textbf{正确定义}:\ n_j(c):=\#\{y\in C\cap S_2(c):\ m(y)=j\},\ j\in\{0,1,2\};\qquad d_2=n_0+n_1+n_2$$
$$\textbf{实测（120 码求和）}:\quad \Sigma n_0=\mathbf{220},\qquad \Sigma n_1=74,\qquad \Sigma n_2=\Sigma q=4$$
$$\qquad \Sigma(n_0{+}n_1{+}n_2)=298=2N_2\ ✓\ \text{（自洽 ✓）}$$
$$\text{故}\ n_1+2n_2\le9s\ \text{成立（违反 }\mathbf 0\text{）};\qquad\text{但}\ d_2+q=n_0+n_1+2n_2\ \textbf{≰}\ 9s\ ✗$$
$$\therefore\ \boxed{\text{唐先生 (5)/(F) 为假，根因 ＝ 漏 }\mathbf{n_0};\ \text{且 }n_0\ \text{为\ \textbf{主项}（220 / 298）}}\ ✓✓$$
$$\text{读数}:\ \text{距离 2 之码字对中，绝大多数（220/298）\ \textbf{不}被共同的距离 1 码字"桥接"}}$$

## §4 旁及纠正：$A_2$ vs $N_1{+}N_2$（**✓**）

$$\text{唐先生 22:23 谓}\ \Sigma_x\binom{\mu(x)}2=2A_2\ \text{并得}\ A_2\ge71\ ✗$$
$$\text{实测}:\ |B_1(c)\cap B_1(c')|=2\ \text{对}\ d{=}1\ \textbf{与}\ d{=}2\ \text{皆成立};\ d\ge3\ \text{为 }0$$
$$\therefore\ \Sigma_x\binom{\mu(x)}2=2(N_1+N_2)\ \text{（\textbf{非} }2A_2\text{）}\ \Longrightarrow\ M{=}106\ \text{之下界为}\ \boxed{N_1+N_2\ \ge\ 71}\ ✓$$

## §5 本轮可存活之资产（**清点 ✓**）

$$\checkmark\ T=\triangle(G_2(C))\ \text{（双重确认）};\qquad \checkmark\ \Sigma\delta^3=E+6\triangle(G_2);\qquad \checkmark\ \text{交大小}\in\{0,1\}\ \text{（穷举）}$$
$$\checkmark\ n_1+2n_2\le9s\ \text{（真，0 违反）};\qquad \checkmark\ \Sigma n_0=220\ \text{（新量化：多数距离-2 对\ \textbf{无桥接}）};\qquad \checkmark\ N_1+N_2\ge71$$
$$\checkmark\ E\ \text{表（}M{=}106\Rightarrow142,\ 107\Rightarrow153\text{）};\qquad \checkmark\ \text{史链}\ 105{=}\text{Zhang},\ 107{=}\text{BÖW}\ ✓$$

## §6 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "三球交穷举" "n0主导项" "纠错反被纠"
技术词 三球交穷举   命中文件数=0    ::
技术词 n0主导项    命中文件数=0    ::
技术词 纠错反被纠   命中文件数=0    ::
```

## §7 边界（硬 ✓）

- **穷举实测**（$\binom{120}3$ 全量）＋ 档案交叉 ✓；**不占 C 号** ✓；**不作方向性决策** ✗；不跨空间 ✓
- 外部内容**未受信任** ⚠️；**不编造** Zhang／BÖW 公式 ✗；**不主张** $E\ge153$ 可得 ✗（V290）
