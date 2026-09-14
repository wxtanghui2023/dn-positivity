# (甲) **可发表中间产物 —— Spec（待唐先生确认 ✓）**

> 委托 ✓ 唐先生 2026-09-14 13:12（**甲乙并行 ✓**）｜依项目纪律 ✓：**Spec 确认 → 实现 → 验证** ✓
> 执行 ✓ 小灵｜**本档仅【Spec 与大纲 ✓】，不写正文 ✗**｜零计算 ✓；未用 RH ✓；未跑 Lean ✓

---

## §0 一句话定位（✓ 待您裁定 ✓）

$$\boxed{\text{一份【结构性障碍】报告 ✓：}\textbf{"N 条独立路线各自严格归约为同一缺失输入；且该缺失输入在两个已知证明中各自对应一个不可迁移要素"}✓}$$

## §1 拟题（✓ 三选一 ✓）

$$\textbf{(T1) }\text{Structural Obstructions in Approaches to the Riemann Hypothesis: Independent Routes, a Common Missing Input}✓$$
$$\textbf{(T2) }\text{What a Proof of the Riemann Hypothesis Would Have to Contain}✓\（\text{更强、更冒险 ✓）}$$
$$\textbf{(T3) }\text{Two-Layer Reduction for the Riemann Hypothesis: Realization versus Localization}✓\（\text{最数学化 ✓，围绕 }C_1+C_3\not\Rightarrow C_2\ ✓）$$

## §2 论文主张（✓ 核心 ✓ 与"不主张"并列 ✓）

$$\textbf{主张 ✓}：$$
$$\qquad\text{(i) }\textbf{规格 ✓}：\text{给出一个【可检验】的对 }char\ 0\ \text{证明的规格 }A+B+C_{\rm int}\ ✓（＋ }C_1/C_2/C_3\ \text{分层 ✓）}$$
$$\qquad\text{(ii) }\textbf{验证 ✓}：\text{该规格【捕获】两个已知证明 ✓（函数域 ✓／Selberg ✓），并各定位【一个】不可迁移要素 ✗（}E161\ ✓）$$
$$\qquad\text{(iii) }\textbf{归约引理集 ✓}：\text{一组【已证明】的严格引理（}E160\ §4.1\ \text{十项 ✓）}：}$$
$$\qquad\qquad\text{· 实现／定位【逻辑独立 ✓】（}C_1+C_3\not\Rightarrow C_2\ ✓）\quad\text{· 轴【内蕴 ✓】（}\operatorname{Fix}(\tau\sigma)=i\mathbb R\ ✓）$$
$$\qquad\qquad\text{· }i\mathbb R\ \textbf{非代数集 ✓}\quad\text{· 轴翻转【非自同构 ✓】}\quad\text{· 测度型 HP 算子【构造平凡但循环 ✓】}$$
$$\qquad\text{(iv) }\textbf{共同缺口 ✓}：N\ \text{条路线（谱／正性／transport／量词／生成 ✓）【各自】严格归约到【同一缺失输入 ✗】}$$
$$\textbf{不主张 ✗}：\text{① 不主张接近 RH ✓；② 不主张新机制 ✓；③ 不主张类表完备（＝工作假设 ✓）；④ 不主张任何已知路线"已死"✗}$$

## §3 大纲（✓ 七节 ✓）

```
§1 引言：为什么"障碍"值得写（三条：路线多／缺口同一／已知证明可对照 ✓）
§2 规格与分层：A+B+C_int ✓；C1/C2/C3 ✓；"实现 vs 定位"二分 ✓（E153 ✓）
§3 N 条路线及其严格归约（每条一段：对象 → 归约 → 落点 ✓）
§4 归约引理集（E160 §4.1 十项 ✓，逐项给证明或指针 ✓）
§5 验证：两个已知证明的规格核对 ✓（E161 ✓）＋ 不可迁移要素对照表 ✓
§6 缺失输入的唯一性（诚实边界 ✓）：工作假设 ＝ 显式公式唯一性 ✗；只声称【当前框架内】✓
§7 结论与开放问题（重开协议 ✓，E159 §5 ✓）
```

## §4 风险与对策（✓）

```
⚠️ **风险 A ✓**：审稿人会问"这不就是综述吗 ✗？" ⟹ **对策 ✓**：核心必须是【引理集 ＋ 验证表】✓，
   即 §4–§5 是**可核验的数学** ✓（而非文献综述 ✓）；§4 十项皆为【已证明 ✓】
⚠️ **风险 B ✓**：类表完备性未证 ✗ ⟹ **对策 ✓**：§6 明确写成【工作假设 ✓】，并给出【重开协议 ✓】（E159 §5 ✓）
⚠️ **风险 C ✓**：可能被认为"没有正面结果 ✗" ⟹ **对策 ✓**：主张 (ii)(iii) 本身就是正面内容 ✓
    （"一个能解释已知证明为何成立的规格"是**结构性定理** ✓）
```

## §5 待您裁定（✓ 三问 ✓）

$$\textbf{Q1 拟题 ✓}：\text{(T1) 稳健 ✓／(T2) 强 ✓／(T3) 数学化 ✓？}$$
$$\textbf{Q2 体裁 ✓}：\text{（a）arXiv 预印本 ＋ 结构化长文 ✓｜（b）短 note（只含引理集 ＋ 验证 ✓）｜（c）暂不写，先做 (乙) ✓？}$$
$$\textbf{Q3 §3 的"N"✓}：\text{列几条？建议【5–7 条】✓（谱／正性／transport／量词／生成 ／轴内蕴／zero-transfer ✓）}$$
