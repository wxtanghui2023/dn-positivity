已查地图：已跑 scripts/prework_map_check.sh Type A 坐标类 §V ⟹ 执行自 `P3ALPHA-2026-09-27-...`（✓）＋ 唐先生 13:31（先开甲 ✓）；本档 = **P3-甲 = STOP（含 Type A/B/C 与 (d',s) 的对照升级 ✓）**。
D0: 本档对象 = §V Type A 坐标类是否给出新的 q 层结构
D1: 2（**STOP 判定 ✓（含证明）**；**(d',s) 对 Type A/B/C 的细化对照 ✓**）

# P3-甲：Type A 坐标类审计（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(BS-1 P3-甲 = STOP ✓)}\ \text{Type A}\ \textbf{不}给出任何新的 }q\text{ 层结构}\ ✓\ \text{—— 理由\textbf{不是"文献没写"，而是一个\textbf{证明} ✓}:}}$$
$$\qquad\text{论文 Theorem 17 证明逐字}:\ \textit{"since there are }\textbf{no two codewords in }\mathcal C\textbf{ at distance 2 apart}\textit{"}\ ✓\ \Longrightarrow\ \boxed{A_2=0\ \text{对 Type A}}\ ✓$$
$$\qquad\Longrightarrow\ \text{我方 }q_v\ \text{按定义以距离 2 对为计数对象 ⟹ }q\equiv\mathbf 0\ \Longrightarrow\ \text{"Type A}\Longrightarrow q_v\in\{0,\lambda\}\text{"\ }\textbf{平凡成立但空洞}（\lambda=0\ ✓）$$
$$\qquad\Longrightarrow\ \text{按唐先生 gate}:\ \textbf{只有概念相似、无新数学蕴含} \Longrightarrow \textbf{STOP} ✓\ \text{（\textbf{不记为新结果}} ✓)$$
$$\boxed{\textbf{(BS-2 §V 的对象是\textbf{另一个}统计量 ✓)}\ §V:\ \textit{"the number of codeword pairs }\{c,c'\}\text{ that differ }\textbf{only on any given coordinate}\text{ is the same for all coordinates"}\ ✓\ \text{——这是\textbf{伙伴对}(partner pairs)\text{的坐标剖面} ✓}$$
$$\qquad\text{Type A 时伙伴对＝距离 1 对 ✓ ⟹ §V 量 ＝ }a_v\ \text{（距离-1 方向计数 ✓）}\ne q_v\ \text{（距离-2 跨界计数 ✓）};\ \text{且其剖面\textbf{刚性} ✓（Lemma 37 逐字：一对坐标不一致、两对部分一致、其余全一致 ✓）}$$
$$\boxed{\textbf{(BS-3 ⭐对照升级 ✓)}\ \text{我方 }(d',s\in\mathrm{Im}f)\ \text{分类\textbf{细化}论文的 Type A/B/C 三分 ✓✓}:}$$
$$\qquad\mathrm{Type\ A}=\{(0,\top)\}\ (A_2{=}0\ ✓);\quad \mathrm{Type\ B}=\{(d',\bot):d'\le3\}\ (A_1{=}0\ ✓);\quad \mathrm{Type\ C}=\{(d',\top):d'\ge1\}\ \text{（}A_2\in\{1024,1536,1792,1920\}\ ✓\text{）}$$
$$
$$
```

---

## §1 取证（**✓ 逐字**）

```
$$\text{(i) Type A 定义（}§\mathrm I\text{ ✓）}:\ \textit{"Type A codes, in which the codewords in every pair }\{c,c'\}\text{ are at distance 1 apart"}\ ✓$$
$$\text{(ii) Type A 刻画（Theorem 17 ✓）}:\ \text{零化 Type A NP1CC}\iff\text{extended 零化完美码}\ \cup\ \text{同长 extended 完美码的\textbf{奇平移}}\ ✓$$
$$\qquad\text{证明关键句（逐字 ✓）}:\ \textit{"since there are no two codewords in }\mathcal C\textbf{ at distance 2 apart}\text{, it follows that the sub-code of even-weight (respectively, odd-weight) codewords has minimum distance (at least) 4"}\ ✓\ \Longrightarrow\ A_2=0\ \text{（\textbf{文献独立确认我方等号链推论}} ✓✓)$$
$$\text{(iii) }§V\text{ 对象（逐字 ✓）}:\ \text{见 BS-2};\ \text{其刚性由 Lemma 37 证明给出}:\ \textit{"one coordinate on which the partners in each pair disagree; two coordinates on which there is agreement in some of the pairs; and }2^r-2\text{ coordinates on which the partners in each pair agree"}\ ✓$$
$$
$$
```

---

## §2 为何不存在"同源局部结构"（**✓ 三条独立理由**）

```
$$\text{(R1) }q\ \text{在 Type A \textbf{恒零}}（A_2{=}0\ ✓）\ \text{——无内容可量子化} ✗$$
$$\text{(R2) }§V\ \text{的量是 }a_v\ \text{型（伙伴对＝距离 1 ✓），\textbf{不是 }q_v\ \text{型}（跨界距离 2 ✓）；两者\textbf{索引方式亦不同}（单坐标 vs 半层方向 ✓）}$$
$$\text{(R3) }§V\ \text{研究的是"全坐标相等"的\textbf{对称性子类}（一个 }a_v\ \text{常值条件 ✓），\textbf{不是}量子化律（}q_v\in\{0,\lambda\}\ \text{的\textbf{两值结构} ✓）；且论文 Type A 的实际剖面\textbf{刚性}（Lemma 37 ✓）而非自由分拆 ✗}$$
$$\qquad\Longrightarrow\ \text{无蕴含链 Type A}\Rightarrow q\ \text{层新结构} \Longrightarrow \textbf{STOP} ✓$$
$$
$$
```

---

## §3 对照升级（**⭐ 本档真正的增量 ✓**）

```
$$\begin{array}{c|c|c|c}
\text{论文类型} & \text{我方 }(d',s) & A_2 & \text{论文可见性}\\
\hline
\mathrm{Type\ A} & (0,\top) & 0 & \text{Theorem 4 一种重分布 ✓}\\
\mathrm{Type\ B} & (d',\bot),\ d'=0..3 & 2048 & \text{Theorem 4 另一种重分布 ✓}\\
\mathrm{Type\ C} & (d',\top),\ d'=1..4 & 1024/1536/1792/1920 & \textbf{论文只说"共享 A 或 B 的重分布" ✓ ⟹ 看不见 4 个子类} ✗\\
\end{array}$$
$$\Longrightarrow\ \boxed{\text{我们的 }(d',s)\ \text{分类在 Type C 上给出\textbf{论文不可见的 4 级细化}}（A_2\ \text{各不相同 ✓✓）};\ \text{与 A-P3ALPHA-1（}B\not\Rightarrow q\text{）一致 ✓✓}$$
$$\qquad\text{诚实标注 ✓}:\ \text{该细化是\textbf{我方定理的推论}（非文献结果 ✓）；本档只做\textbf{对照定位}，\textbf{不声称}论文蕴含它 ✗，也不声称新定理（已在 A-ALIGNTHM-1 内 ✓）}$$
$$
$$
```

---

## §4 边界与下一步（**✓**）

```
- §1 为逐字取证 ✓；§2 为 STOP 论证 ✓；§3 为对照升级 ✓（非新结果，属定位 ✓）
- \textbf{未}计算 ✓；\textbf{未}枚举 ✓；\textbf{未}扩张目标 ✓（遵唐先生 ✓）；类型 C 的 4 子类是否"论文不可见"仅就\textbf{重量分布层}而言 ✓（距离分布层未逐项对照 ⚠️）
- \textbf{119}：完全不碰 ✓
$$\text{下一步（按唐先生顺序 ✓）}:\ \textbf{P3-}\beta\ \text{（分类剪枝 ✓）—— 现在可用 }(d',s)\ \text{作剪枝不变量 ✓}$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：P3-甲 STOP 判定、Type A 恒零论证、(d',s) 对 A/B/C 的细化对照
- **档案已有（引用，不列为提出）**：A-ALIGNTHM-1、A-P3ALPHA-1、Type A/B/C、$A_2$、$q_v$、$J$


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 STOP 判定      命中文件数=2    :: ./T3MIN1-2026-09-26-minimal-three-point-psd-attack.md ./P3JIA-2026-09-27-typeA-coordinate-audit-STOP.md 
技术词 (d',s) 对照    命中文件数=0    ::
```
- **本档新增**：P3-甲 STOP 判定、Type A 恒零论证、$(d',s)$ 对 A/B/C 的细化对照（见上方命中数；0 命中者为自造语／内部标签 ✓）
