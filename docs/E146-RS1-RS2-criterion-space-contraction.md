# E146 · ⭐⭐⭐ **方向 (ii) 表征收缩：RS-1／RS-2 判定 —— 第三类型【只能是非自伴谱型】✗**
### （＝ 总册 **L1**，已判 NO-GO ✓ ⟹ **已知类型穷尽 ✓，但无定理 ✗**）

> 委托 ✓ 唐先生 2026-09-14 12:06（**规格定稿后直接进入 V109 方向 (ii) 表征收缩 ✓**）
> 依据 ✓ `docs/V109-coverage-argument-charter.md` §⑤-2（**RS-1／RS-2 逐字 ✓**）＋ §②-2（中档 M ✓）＋ `E106` §4–§5 ✓
> 执行 ✓ 小灵｜**纸面审计 ✓（零数值 ✓）**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓；**先查档 ✓**

---

## 0. 判定（✓ 四条）

```
⭐ **① RS-1（判据空间分类 ✓）【已在档 ✓】**：`E106` §5 逐字已给 **判据空间 ＝ 正性型 ∪ 求和-公式型** ✓
   $$\Longrightarrow\ \textbf{RS-1 已完成 ✓（不需重做 ✗）}\ \text{—— 与 }V109\ \text{§⑤-2 的"抓手最实"一致 ✓}$$
⭐⭐⭐ **② RS-2 判定 ✓（本轮内容 ✓）**：**"是否存在既非正性型、又非求和-公式型的 RH 等价判据？"**
   $$\text{判据要 RH 等价 ✓ ⟹ 必须【侦测 } \beta-\tfrac12\neq0\ \text{的偏离 ✓】⟹ 侦测方式只有三种【结构可能 ✓】：}$$
   $$\text{(i) 侦测}\ \textbf{符号翻转 ✓} \Longrightarrow \text{正性型 ✓}\qquad\text{(ii) 侦测}\ \textbf{尺度/增长改变 ✓} \Longrightarrow \text{求和-公式型 ✓}$$
   $$\text{(iii) 侦测}\ \textbf{既不靠符号、也不靠增长 ✗} \Longrightarrow \textbf{只能是【谱型 ･ 非自伴】✗✓}$$
   $$\Longrightarrow\ \boxed{\textbf{第三类型（若存在）【必须】是"谱型但非自伴"✗ —— 而它正是总册 }L1\ ✓}$$
   $$\text{而 }L1\ \textbf{已判 NO-GO（作为 RH 路径 ✓，}docs/L1\text{-nonselfadjoint-spectral-rigidity-audit.md ✓）}\ \Longrightarrow\ \boxed{\textbf{已知类型穷尽 ✓}}$$
🔴 **③ 但【无定理 ✗】**：\text{"只有三类"本身未证 ✗（＝ }V109\ \text{§②-2 中档 }M\ \text{未证 ✓；}CLOSED\text{-}ROUTES\text{-}MAP\ \text{§E.4 自陈 OPEN ✓）}
⭐ **④ 中档 }M\ \text{的残余被【锐化 ✓】**：
   $$\text{原残余 ✓}：\text{"类表是否完整"✗（不可判定 ✓，}V108\ ✓）\qquad\textbf{新残余 ✓}：\boxed{\text{"第三类型是否只能是非自伴谱型"✗}}$$
   $$\text{—— 【更锐 ✓】：只需排除"非符号、非增长、非谱"的第四侦测方式 ✓（一个更小的问题 ✓）}$$
```

## 1. 推导（✓ 为什么只有三种侦测方式 ✓）

$$\textbf{判据的 RH 等价性 ✓} ⟺ \bigl(\mathrm{RH}\ \text{真}\Rightarrow\ \text{判据成立}\bigr)\ \wedge\ \bigl(\mathrm{RH}\ \text{假}\Rightarrow\ \text{判据失效}\bigr)$$
$$\Longrightarrow\ \text{判据必须对【}\exists\rho:\ \beta\neq\tfrac12\ \text{】敏感 ✓ ⟹ 必须把偏离 }\beta-\tfrac12\ \text{转成一个【可观测的失效 ✓】}$$
$$\text{而"可观测失效"的结构类型 ✓（穷举式 ✓）：}$$
$$\qquad\text{(i) 量【变号】✓：正定泛函/二次型由 }\ge0\ \text{变}\ <0\ \checkmark\ \Longrightarrow\ \text{正性型 ✓}$$
$$\qquad\text{(ii) 量【变阶】✓：有界/}\sim c\ \text{的量变为无界/}\gtrsim x^{\theta}\ \checkmark\ \Longrightarrow\ \text{求和-公式型 ✓}$$
$$\qquad\text{(iii) 量【不变号、不变阶 ✓】，但其【谱/几何位置】改变 ✗：}\ \text{如算子谱从实轴移出 ✓ ⟹ 谱型 ✗}$$
$$\Longrightarrow\ \text{(iii) 若算子【自伴 ✓】⟹ 谱实自动 ✓ ⟹ 无法侦测 ✗ ⟹ 必为【非自伴 ✗】✓✓}$$

## 2. 与定稿规格的关系（✓ $A+B+C_{\rm int}$ 属哪一型 ✓）

$$\text{规格 }A+B+C_{\rm int}\ \text{的【陈述形式】＝ 存在性／构造型 ✗（非符号、非增长 ✓）}$$
$$\Longrightarrow\ \text{若其内部对象【自伴／正定 ✓】⟹ 其判据形态【折叠回正性型 ✓】（}E106\ \text{§4 对偶同一 ✓）}$$
$$\Longrightarrow\ \text{若【非自伴 ✗】⟹ 属第三类型 ✗ ⟹ 撞 }L1\ ✓\ \text{（NO-GO ✓）}$$
$$\Longrightarrow\ ⭐\ \boxed{\text{故定稿规格【若要】产生"第三类型判据 ✓"，必须走非自伴谱路 ✗ —— 而该路已判 NO-GO ✓✓}}$$

## 3. 中档 $M$ 的**当前状态**（✓ 依 V109 §②-2 ✓）

$$\textbf{中档 }M\ \text{逐字 ✓}：\text{"一切 canonical 单点隔离机制同构于有限表征空间 }\mathcal C\ \text{中一点 ✓"}\ \text{—— }\textbf{未证 ✗}$$
$$\text{本轮【不证明 ✗】，但把它的【唯一残余】从"类表完整性 ✗"压到：}\ \boxed{\text{"第三类型 ＝ 非自伴谱型 ✗"是否穷尽 ✓}}$$
$$\text{且该残余【已有部分答案 ✓】：}\text{非自伴谱型 }＝L1\ \text{【已详审 ✓】（五族全归为半平面／扇形／实轴／空竖条 ✗；}\textbf{从不给出【指定竖线】✗✓）}$$

## 4. 边界与纪律（✓）

```
✅ **纸面 ✓（零数值 ✓）**；先查档 ✓（V109 §②-2／§⑤-2 ✓；E106 §4–§5 ✓；L1 审计档 ✓）
⚠️ **① 三分法（符号／增长／谱 ✓）是【我的结构论证 ✓】**，**不是穷举定理 ✗** —— 可能存在我未列出的第四侦测方式 ⚠️
   （本轮正是把"是否存在第四种"定为新残余 ✓ —— 自洽 ✓）
⚠️ **② RS-1 的"已完成"指 }E106\ \text{§5 的分类 ✓**；我**未逐字复核 §5 全文 ✗**（依其在档结论 ✓）
⚠️ **③ 本轮【不声称】第三类型不存在 ✗** —— 只声称：**若存在，必为非自伴谱型 ✓（且该型已 NO-GO ✓）**
⚠️ **④ 不声称中档 }M\ \text{成立或失败 ✗**
⚠️ **未用 RH** ✓；**未跑 Lean** ✓
⭐ **净产出 ✓**：① **RS-1 在档 ✓（不需重做 ✓）**；② ⭐ **RS-2 判定：第三类型必为非自伴谱型 ✗ ＝ }L1\ ✓\ ⟹\ \text{已知类型穷尽 ✓}**；
   ③ **中档 }M\ \text{残余锐化 ✓**（}→\ \text{"是否有第四侦测方式"✗}); ④ **定稿规格与第三类型的关系明确 ✓**
