已查地图：命中（`AMEND-14`）⟹ 本档为其**校准测试**（零新数学），不开新案
D0: 本档对象 = **闸门双向校准**：对 `5` 个**已证可行的前沿成果**（旧闸门应全部误杀）＋ `2` 个**逐字已覆盖的重述型目标**（应全部拦下）做回归
D1: 1（首次对闸门做实证校准）
[RESEARCH]

# **校准测试：旧闸门 vs 前沿成果**

## §1 样本（全部为已发表/已证可行的 `dent`）

```
$$\begin{array}{c|c|c}
\#&\text{成果}&\text{性质}\\
\hline
F1&\ell_2(10,2)\le50\ (\text{原纪录 }51)&\text{具体构造 + 双验证}\\
F2&\text{Sidon 二阶项 }F(N)\le N^{1/2+0.94301}\ (\text{原 }0.9435)&\text{指数改进}\\
F3&\text{union-closed 常数 }0.38305\ (\text{已认证})&\text{认证常数}\\
F4&\text{Caccetta–Häggkvist }k{=}3:\ c=0.34640>0.3388&F_4\ \text{证书}\\
F5&\text{Cohn–Elkies 精确 }R=3627599/500000=7.255198&\text{精确值}\\
\end{array}$$ ✓✓（皆为"对象经典、方法标准、领域活跃"型）
```

## §2 ⛔ 旧闸门回归（`G1`–`G5` ＋ 原 `AMEND-9`）

```
$$F1:\ G3\ \text{要"新量"}\ \Longrightarrow\ \text{"更好的构造"}\ \textbf{非新量}\ \Longrightarrow\ REJECT;\quad L1\text{–}L4:\ \text{covering codes 标准且活跃}\ \Longrightarrow\ REJECT$$ ✗
$$F2:\ \text{"指数改进"非新对象}\ \Longrightarrow\ REJECT;\quad \text{Sidon 是成熟对象}\ \Longrightarrow\ REJECT$$ ✗
$$F3:\ \text{"认证一个常数"非新量}\ \Longrightarrow\ REJECT;\quad \text{union-closed 活跃}\ \Longrightarrow\ REJECT$$ ✗
$$F4:\ \text{"证书"非新量}\ \Longrightarrow\ REJECT;\quad \text{CH 猜想活跃}\ \Longrightarrow\ REJECT$$ ✗
$$F5:\ \text{"精确值"非新对象}\ \Longrightarrow\ REJECT;\quad \text{sphere packing 文献成熟}\ \Longrightarrow\ REJECT$$ ✗
$$\Longrightarrow\ \boxed{\text{旧闸门 }5/5\ \textbf{误杀}}$$ ✓✓✓（**这就是唐先生 16:41 的反证：若按旧闸门，GPT/Claude 同样一个课题都找不到**）
```

## §3 ✅ 新闸门回归（`AMEND-12` §2 ＋ `AMEND-14` §3–§4）

```
$$F1:\ \texttt{A1}\ \text{具体断言（50 列码存在）};\ \texttt{A2}\ \text{枚举/ILP + 独立验证};\ \texttt{A3}\ \text{失败 = residue}\ \Longrightarrow\ \boxed{\textbf{放行}}$$ ✓
$$F2\text{–}F5:\ \text{同理（均有具体断言＋检验法＋失败形态）}\ \Longrightarrow\ \boxed{\textbf{放行 }5/5}$$ ✓✓✓
$$\textbf{（且杀伤门槛已收紧）}:\ \text{不得以"领域活跃／方法标准／对象经典"为由拒绝};\ REJECT\ \text{须附逐字覆盖声明}$$ ✓
```

## §4 ✅ 反向回归（防"闸门空转"：须仍能拦下**真重述型**目标）

```
$$R1:\ \text{"在 Lean 中证明 Sylvester 惯性定律"}\ \Longrightarrow\ \text{Mathlib 已逐字含（}QuadraticForm.\text{equivalent\_...\_weighted\_sum\_squared，自述为 Sylvester's law of inertia）}\ \Longrightarrow\ \boxed{\textbf{拦下}}$$ ✓✓
$$R2:\ \text{"把指数 3 的 }\lambda=(Q-8+A)/9\ \text{作为目标推导"}\ \Longrightarrow\ \text{经典三次分圆数公式逐字覆盖}\ \Longrightarrow\ \boxed{\textbf{拦下}}$$ ✓✓
$$\Longrightarrow\ \boxed{\text{新闸门双向合格}:\ \text{放行 }5/5\ \text{真 }dent\ +\ \text{拦下 }2/2\ \text{真重述}}$$ ✓✓✓
```

## §5 判词

```
$$\boxed{\text{旧闸门（}5/5\ \text{误杀）＝误校};\qquad \text{新闸门（}5/5\ \text{放行 ＋ }2/2\ \text{拦下）＝合格}}$$ ✓✓✓
$$\textbf{对唐先生 16:41 反证的直接回答}:\ \text{不合适};\ \text{旧闸门确会令 GPT/Claude 一无所得};\ \text{已修正为"可攻击性准入 ＋ 逐字覆盖才可拒 ＋ 校准绊线"}$$ ✓✓
【⛔ 纪律】 本档零新数学；`U_{2,3}` 暂停；**不回 RH** ✓
【边界】 §1 的成果数据引自本项目早期档案（对 `F1`–`F5` 的"行为"描述为**档级**，未逐条回原文复核）⚠️

## §附 【技术词回查】（补录）
```
技术词 calibration      命中文件数=21   :: ./MAG1-magnitude-calibrated-and-forced-abscissa.md ./P5-Y3-SOURCE-CARD-and-AMEND9-gate-REJECT.md ./PAPERA-v2-structure.md 
技术词 attackability    命中文件数=1    :: ./RESEARCH-CONSTITUTION.md 
```
