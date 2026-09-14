# E163 · ⭐⭐⭐⭐ **D1-A/B/C 可逆归位审计**（先审计 ✓，不做深入计算 ✓）
### **结果：A 归位 ✓｜C 归位 ✓｜⭐ B 【未完全归位 ✓ —— 唯一存活者 ✗】**

> 委托 ✓ 唐先生 13:32（**组件 2 → D1；只允许 D1-A/B/C；每候选【先做可逆归位审计 ✓】再做计算 ✓**）
> 前置 ✓ `docs/TEMPLATE-object-pinning.md`（组件 2 ✓，已建 ✓）
> 判据 ✓ 您的 G1–G4 ✓：**若两三步内可恢复 ⟹ 标 REPACKAGED ⟹ 停 ✗**
> 纪律 ✓ 未用 RH ✓；未跑 Lean ✓；**本档零新计算 ✓**（仅归位审计 ✓）

---

## §0 三候选裁决（✓ 先给 ✓）

$$\boxed{\textbf{D1-A}\ \text{零点配对和的精确有限化} \Longrightarrow \textbf{归位 ✓（显式公式 ✗）}}$$
$$\boxed{\textbf{D1-C}\ \text{相位/对称望远镜} \Longrightarrow \textbf{归位 ✓（辐角原理 ＋ Riemann–von Mangoldt 的 }S(T)\ \text{✗）}}$$
$$\boxed{\textbf{D1-B}\ \text{加法×乘法双侧闭合} \Longrightarrow ⚠️ \textbf{未完全归位 ✓ —— 唯一存活 ✓（附刚性警告 ✗）}}$$
$$\Longrightarrow\ ⭐\ \text{依您的预登记 ✓：三类【未】全归位 ⟹ }\textbf{"恒等式作为生成单元"【未被否定 ✓】}\ \text{（1／3 存活 ✓）}$$

## §1 D1-A：零点配对和的精确有限化 ⟹ **归位** ✗

$$\textbf{对象 ✓}：\Sigma_{\rho\in Z_N}F(\rho)\ \text{与【有限】Euler／素数数据之间的【精确有限】恒等式 ✗}$$
$$\textbf{可逆恢复路径 ✓（两步 ✓）}：$$
$$\qquad\text{步 1 ✓}：\text{任何把【零点侧】与【素数侧】耦合的恒等式 ✓，其【已知通道唯一】＝ 显式公式（}E158\ \S4\ \text{同一结论 ✓）}$$
$$\qquad\text{步 2 ✓}：\text{显式公式}\ \Sigma_\rho h(\rho)=\hat h(0)+(\text{archimedean})-\sum_n\frac{\Lambda(n)}{\sqrt n}\bigl(h(\log n)+h(-\log n)\bigr)\ \textbf{对容许 }h\ \text{【精确 ✓】}$$
$$\qquad\qquad\text{但它是 }\textbf{【全局】的 ✗}（\text{对 }Z_N\ \text{截断 ⟹ 尾部零点}\ \{\gamma>\gamma_N\}\ \text{贡献【非零 ✗】}）$$
$$\Longrightarrow\ \boxed{\textbf{REPACKAGED ✗（显式公式 ✓）}}\ \text{—— 精确障碍 ✓：}\textbf{有限 }N\ \text{的精确恒等式 ⟺ 尾部贡献可由有限素数精确表示 ✗，}\text{而该通道【只有显式公式 ✓，且它是全局的 ✗】}$$
$$\qquad\text{（}\textbf{注 ✓}：\text{若改用【围道积分／辐角原理】精确算尾项 ✓，} \Longrightarrow \text{又落入 D1-C 的归位 ✓）}$$

## §2 D1-C：相位/对称望远镜 ⟹ **归位** ✗

$$\textbf{对象 ✓}：\Sigma_{k=1}^N\Delta\phi_k=\phi_N-\phi_0\ ✓\ \text{且右端【可由算术对象独立计算 ✗】}（\text{您已预设：若 }\phi_N-\phi_0=\arg\Xi\ \text{⟹ 归位 ✗）}$$
$$\textbf{可逆恢复路径 ✓（一步 ✓）}：$$
$$\qquad\Sigma_k\Delta\arg\Xi=\textbf{辐角原理 ✗}\ \Longrightarrow\ \text{零点计数 }N(T)\ ✓\ ——\ \text{而"独立由算术算得的总辐角"}\textbf{恰是 }S(T)=\frac1\pi\arg\zeta(\tfrac12+iT)\ \text{✗}$$
$$\qquad\Longrightarrow\ \text{Riemann–von Mangoldt ✓}：N(T)=\frac{T}{2\pi}\log\frac{T}{2\pi e}+\frac78+S(T)\ ✓\（\text{经典 ✓）}$$
$$\Longrightarrow\ \boxed{\textbf{REPACKAGED ✗（辐角原理 ＋ R–vM 的 }S(T)\ ✓）}\ \text{—— }\textbf{且它与 }E155/E156\ \text{（"证明 }S(T)=o(\log T)\ \text{无改进 ✓"）}\ \textbf{同型 ✓}$$
$$\qquad\text{（}\text{故 }{\bf D1-C}\ \text{的右端"算术可算"}\textbf{【必然】经 }S(T)\ \text{✗ ⟹ 无逃逸 ✓）}$$

## §3 ⭐ D1-B：加法×乘法双侧闭合 ⟹ **未完全归位** ✓（唯一存活 ✓）

$$\textbf{目标形状 ✓}：\ \Sigma_{m+n=N}A(m)B(n)\ \longleftrightarrow\ \prod_{p^\nu\parallel N}F(p,\nu)\ ✓\ \text{（}\textbf{Cauchy 卷积 ✗} \leftrightarrow \textbf{乘性 ✗）}$$
$$\textbf{已检索的已知族 ✓（逐条对照 ✓）}：$$
| 已知族 ✓ | 形状 ✓ | 是否命中您的目标 ✗ |
|:--|:--|:--|
| **Gauss** $\Sigma_{d\mid n}\varphi(d)=n$ ✓ | **【除数】卷积 ✗** | ❌ **不命中** ✗ |（\text{且右侧 }n\ \text{是"加法线性"✓，非包络 ✓） |
| **Jordan totient** $\Sigma_{d\mid n}J_k(d)=n^k$ ✓ | 【除数】卷积 ✗ | ❌ 不命中 ✗ |
| **Ramanujan 和** $c_q(n)=\Sigma_{(a,q)=1}e^{2\pi ian/q}$ ✓ | **加法（指数）↔ 乘法（模数 ✓）** ⭐ | ⚠️ **最接近 ✓ 但它是【单变量和 ✗】，非【卷积 ✗】** |
| **Dirichlet 卷积 ↔ Euler 积** ✓ | **【Dirichlet】卷积 ✗** | ❌ 不命中 ✗（形状不同 ✓） |
| **完全乘性 ⟹ 由素数幂决定** ✓ | 刚性 ✓ | ⚠️ **是【限制 ✓】而非【实例 ✗】** |
$$\Longrightarrow\ ⭐\ \textbf{检索结论 ✓}：\text{已知族【全部落在两种形状】✗：}\textbf{【除数卷积】✓ 或 【Dirichlet 卷积】✓}；$$
$$\qquad\text{而您指定的【}\textbf{Cauchy（加法）卷积 ↔ 乘性}\text{】形状 ⟹ \textbf{在已检索范围内【未见已知定理 ✓】}}$$
$$\textbf{但必须写死的刚性警告 ✗}：\text{乘性 ⟹ }\textbf{值由素数幂 }f(p^\nu)\ \text{【完全决定 ✗】} \Longrightarrow \text{要求：}\textbf{Cauchy 卷积在【互素拆分下可因子化 ✗】}$$
$$\qquad\Longrightarrow\ \text{这是一个【强且非平凡 ✓】的条件 —— }\textbf{但它【未】被已知族覆盖 ✓，也【未】被立即否定 ✗}$$
$$\Longrightarrow\ \boxed{\textbf{判定 ✓：未完全归位 ✓（无 2–3 步可逆恢复 ✗）⟹ 【存活 ✓】}}\ \text{（依您的 G3 ✓）}$$
$$\qquad\text{⚠️ }\textbf{但不等于可开工 ✗}：\text{须先过 }\textbf{G1（精确 ✓）／G2（新耦合 ✓）／G4（产生新可算量 ✗）}\ \text{与【组件 2 对象固定 ✓】}$$

## §4 本轮净结论（✓ 依您的预登记 ✓）

$$\text{您预登记 ✓："若三类【全】归位 ⟹ '恒等式作为生成单元'不足以产生新结构 ✗ ⟹ 转攻 C5 ✗"}$$
$$\Longrightarrow\ ⭐\ \textbf{实际结果 ✓：}2/3\ \text{归位 ✓，}\textbf{1/3 存活 ✓} \Longrightarrow \textbf{预登记的另一支触发 ✓}：\ \boxed{\text{D1-B 进入下一轮【G1–G4 检验 ✓】}}$$
$$\text{且本轮的**方法收益 ✓**：}\textbf{审计在【零新计算】下完成 ✓}，}\text{并【区分】出唯一存活者 ✓ —— }\textbf{这正是您要的"先审计后计算" ✓✓}$$

## §5 边界与纪律（✓）

```
✅ **零新计算 ✓**；未用 RH ✓；未跑 Lean ✓；**每候选先归位审计 ✓**
⚠️ **① D1-A/C 的归位依据为【经典结果 ✓】**（显式公式 ✓；R–vM ✓）—— 我**未逐字抄原文 ✗**（依组件 2 规则 1 ✗，**下一轮若真要引用须补 ✓**）
⚠️ **② D1-B 的"未见已知定理 ✓"是【检索性结论 ✗】** —— 范围限本项目档内 ＋ 我的既有知识 ✓（**未做文献检索 ✗**）⟹ **"未见"≠"不存在"✓**
⚠️ **③ 本档【不声称】D1-B 会成功 ✗** —— 仅声称其在【可逆归位审计】下【存活 ✓】
⚠️ **④ 组件 2 模板已建 ✓**（`docs/TEMPLATE-object-pinning.md` ✓）—— 含四项表 ＋ 硬闸 ＋ 三条规则 ＋ 反面样板（E63/E64／E88/E93/E96／E117／E120 ✓）
⭐ **净产出 ✓**：① **组件 2 模板 ✓**；② **D1-A 归位 ✓（显式公式；尾项不可有限化 ✗）**；③ **D1-C 归位 ✓（辐角原理／}S(T)$ ✓）**；
   ④ ⭐ **D1-B 存活 ✓（Cauchy 卷积↔乘性【未见已知族 ✓】）**；⑤ **方法验证 ✓：零计算审计即可筛选 ✓**
```

## §6 下一轮唯一动作（✓ 待您许可 ✓）

$$\text{对 }\textbf{D1-B}\ \text{做 }\textbf{G1–G4 ＋ 对象固定（组件 2）}✗：$$
$$\qquad\text{① G1 精确性 ✓：}\text{给出 }\mathcal I\equiv0\ \text{的【有限步可验】形式 ✗（或证明不存在 ✓）}$$
$$\qquad\text{② G2 新耦合 ✓：}\text{确认它【真的】耦合加性与乘性 ✓（而非 Dirichlet 型换皮 ✗）}$$
$$\qquad\text{③ G4 新量 ✓：}\text{诱导出此前没有的量 }J_N\ \text{与精确关系 }J_N=H_N\ ✗$$
$$\qquad\text{④ 组件 2 ✓：}\text{若需引用任何已知结果 ✓，先填 }(\mathcal O,\mathcal D,\mathcal H,\mathcal C)\ \text{四项 ＋ 逐字 ✓}$$
