# FINGERPRINT-2026-09-30 — **BÖW-107 方法指纹**（自 Kéri 论文第 9 章逐字定位 ✓）：**逐坐标构造＋同构约化之计算机分类**；书面全文在 **Kaski–Östergård 2006 §7.2**

> 空间 B｜非 C 号｜唐先生 16:32「先做 BÖW-mechanism fingerprint，不要猜程序」｜**不主张任何新值**（V290）
> 时间：2026-09-30 17:0x

**已查地图** ✓：`ASSETS-REGISTRY` C-429（subspace distribution ＋ conditional LP，P0 已在档）／C-541（WITHAAS）／L3012（**未做者＝`Layer 2+`：子空间耦合＋incidence＋整数可行**）／L1554（**支撑层＝未被 excess／congruence 吃掉之自由度**）
D0: 本档对象 = **档案已有**（Kéri 第 9 章／参考文献）中之**方法指纹抽取**（新数学对象：无 ✗）
D1: 0（产出 = **一条方法指纹 ＋ 两条阶梯之信息类型判定 ＋ 一个可验证实现里程碑** ⚠️✓）

---

## §0 **Step A：方法指纹（Kéri 第 9 章逐字 ✓）**

$$\text{章名（逐字译）}:\ \text{“9. fejezet — }\textbf{\text{算法与计算机程序：用于混合 térlefedő 码之分类}}\text{”}\ ✓$$
$$\text{核心机理（逐字译）}:\ \text{“将属于结果集之码}\ \textbf{\text{逐坐标地构造}}\ \text{（koordinátánként építjük fel）}\ \text{……其结果集若为}\ \textbf{\text{空}}\ ⟹\ \boxed{K(t,b;R)>M}\ ✓✓\ \text{（即以空结果集\ \textbf{证明下界}）}”$$
$$\text{谱系（逐字译）}:\ \text{二元简化版由 }[16],[22]\ \text{提出};\ \text{后由 }\mathbf{[103]\ \text{Blass--Litsyn 1998}}\ \text{与}\ \mathbf{[121]\ \text{Östergård--Blass 2001}}\ \text{推进（}\textbf{\text{仍仅二元，且为\ \textbf{下界} 而非分类}}\text{）};$$
$$\qquad\boxed{\text{“该方法的\ \textbf{混合码} 变体之应用，}\textbf{\text{首次由 }[130]\ \text{报道}}\text{，但它}\textbf{\text{只极简略地概述方法}}\text{”}}\ ✓✓\ (\text{逐字: „csak nagyon röviden vázolja”})$$
$$\qquad\text{完整写法}:\ \textbf{[138]\ Kaski--Östergård, \textit{Classification Algorithms for Codes and Designs}, Springer 2006, §7.2}\ ✓;\quad \text{二元变体进一步发展于 }[155]\ (\text{Kéri--Östergård})\ ✓$$

**⇒ 指纹 = 以"逐坐标构造 ＋ 同构（inequivalent）约化 ＋ 部分覆盖剪枝"穷举搜索；空集 ⟹ 下界。** ✓

## §1 **Step B：n=9 之 +5 与 n=10 之 +2 是\ \textbf{同一信息类型}** ✓✓

$$\text{n=9}:\ 52\to54\to55\ [82]\to56\ [112]\to57\ [103]\to\mathbf{62\ [121]}\quad(\mathbf{+5})$$
$$\text{n=10}:\ 94\to96\ [18]\to97\ [46]\to103\ [52]\to105\ [67]\to\mathbf{107\ [130]}\quad(\mathbf{+2})$$
$$\text{而 }[121]\ \text{与 }[130]\ \text{在 §0 之谱系中}\ \textbf{\text{同属一族}}（\text{逐坐标构造；}[121]\ \text{为二元版、}[130]\ \text{为混合版}）\ ✓✓$$
$$\therefore\ \boxed{\text{两步所增之信息类型\ \textbf{相同}：皆为"计算机穷举／分类"型，而非解析局部不等式}}\ ✓✓$$
$$\text{⇒ }\textbf{\text{107 不是需要"发明新机制"的解析引理；而是一个\ \textbf{可复现的计算型结果}}}\ ✓\ \text{（推翻"22 年前算力有限 ⟹ 必为简短手算"）} ✗$$

## §2 **Step C：对应到我们的对象（可计算）**

$$\text{取 }k\ \text{维子空间族 }\mathcal U_k:\ N_U=|C\cap U|;\ \text{局部变量 }x_{U,j}=\#\{U:|C\cap U|=j\}\ ✓$$
$$\text{一阶（会退化为已知量）}:\ \sum_j j\,x_{U,j}=\sum_U|C\cap U|=\sum_{c}\#\{U\ni c\}\ ✓;\quad \text{二阶（\textbf{才开始见排列}）}:\ \sum_j\binom j2x_{U,j}=\sum_{\{c,c'\}}\#\{U:c,c'\in U\}\ ✓$$
$$\textbf{坐标子空间族特例（最锋利 ✓）}:\ U_S=\mathrm{span}(e_i:i\in S)\ \Longrightarrow\ |C\cap U_S|=\#\{c:\operatorname{supp}(c)\subseteq S\}\ ✓\ ——\ \textbf{支撑层量}，档案 L1554 已确认为\ \textbf{未被 }T\text{-Walsh／excess 吃掉之自由度}\ ✓✓$$
$$\text{二阶矩}:\ \sum_{|S|=k}\binom{N_S}{2}=\sum_{\{c,c'\}}\binom{10-|\operatorname{supp}(c\cup c')|}{k-|\operatorname{supp}(c\cup c')|}\ ⟹\ \textbf{依赖 }(\text{重量,距离})\ \text{联合型}\ \supset\ \text{距离分布}\ ✓$$

## §3 **可验证里程碑（我建议之第一步 ✓）**

$$\boxed{\text{先复现 }[121]\ \text{之 }n{=}9\ \text{结果（57}\to\text{62}）\ ——\ \text{以验证我方"逐坐标构造＋同构约化"实现正确}} ✓✓$$
$$\text{然后推广至 }n{=}10,\ M{=}106\ \text{之}\ \textbf{\text{空集判据}}\ ⟹\ K(10,1)\ge107\ ✓$$
$$\textbf{未决（诚实 ⚠️）}:\ [130]\ \text{如何在 }M{=}106\ \text{（106 词码）下避免朴素爆炸？}\ \textbf{\text{假设}}:\ \text{经由\ \textbf{归约到小 }M\ \text{的混合 }(t,b;R)\ \text{情形}\ \text{再穷举}\ (\text{与档案"BÖW 混合框架"一致 }) ⚠️\ ——\ \text{待验 ✓}$$

## §5 【技术词回查】（`scripts/tech_word_check.sh` 逐字输出 ✓）

```
技术词 逐坐标构造     命中文件数=1    :: ./FINGERPRINT-2026-09-30-BOW-107-method-fingerprint-from-Keri-chapter-9.md
技术词 方法指纹     命中文件数=1    :: ./FINGERPRINT-2026-09-30-BOW-107-method-fingerprint-from-Keri-chapter-9.md
技术词 空集判据     命中文件数=0    :: 
```

$$\textbf{分类}:\ \text{三词之命中均\ \textbf{仅本档自身}（或 0）} \Longrightarrow \textbf{本档新增} ✓;\quad \text{“空集判据”为 0 ⟹ 全新命名 ✓}$$
$$\text{空间 A/B 分离（AMEND-27）}:\ \text{无跨空间同名} ✓;\quad \text{通用词（不计）}:\ \text{“指纹”／“判据”裸词} ✓$$


## §4 边界与纪律

$$\textbf{(D1)}\ \text{无 P1} ✗;\ \textbf{(D2)}\ \text{未持有 }[130],[121],[138]\ \text{全文（不得冒充）}\ ✓;\ \textbf{(D3)}\ \text{未取禁用原文／未主张新值／未碰 RH} ✓$$

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=FINGERPRINT-CITED R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
