# V159 · ⭐⭐⭐⭐⭐ **C6.6 → A1/A3 的等价性审计 —— ①撤回 V158(b) 的过度断言（"completeness ⟹ 必须用 $N_\zeta(T)$"被判为【非逻辑必然】✗✓，降为"计数路线 $\subset C$"）；②C6.6 压成【非解析、非循环谱双射 $\Lambda_M\cong Z_\zeta-\tfrac12$】；③本档给出并轨骨架：已知范式皆经 trace／显式公式／Mellin／Hadamard／Li-Weil ⟹ 有效内容 $\in$ Weil 泛函族 ⟹ 并入 A1/A3（[结构性] ⚠️）；④最终分叉被确立，§E.4 最后问题被**合法化**
> 委托 ✓ 唐先生 2026-09-15 10:42（**"③值得做，但不能直接按 V158 的 (b) 合并；这里有一个需要先纠正的逻辑点，否则会把'结构对应'错误地强制成'计数对应'"** ✓；并给出 §1–§3 全部核心论证 ✓）
> 查图 ✓ `V158`（(b) 待撤回；soundness／completeness 分解）｜`V157`（十条身份机制）｜`A1`（Li 系数／二次范围）｜`A3`（Weil 正性／比例天花板 0.682）｜`E106`（判据空间 ＝ 正性 ∪ 求和-公式 ⟹ 封闭）｜`E146/E147`（三分法）｜`V144`（层诊断）｜`V113/V114`（$T^2$ 律／预算交叉墙）
> 执行 ✓ 小灵（落档＋撤回＋边界标注＋**§4 并轨骨架为本档新增** ✓）｜**纸面 ✓（零数值 ✓）**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓｜编号 ✓ **V159**

---

## §0 判定（✓ 四条 ✓）

$$\boxed{\text{① }\textbf{撤回 }V158\text{(b)} ✗✓：\text{completeness}\not\Rightarrow\text{必须使用 }N_\zeta(T)\ \text{—— }\text{"RvM 是已知计数工具"}\neq\text{"所有 completeness 证明必经 RvM"}\ ✓✓;\ \text{降级为}\ \boxed{\text{计数路线}\subset C}}$$
$$\boxed{\text{② }C6.6\ \text{压成}\ ✓✓：\boxed{\text{非解析、非循环谱双射}\ \Lambda_M\xrightarrow{\ \sim\ }Z_\zeta-\tfrac12}}$$
$$\boxed{\text{③ 本档新增并轨骨架 ✓：已知证明范式皆经 trace／显式公式／Mellin／Hadamard／Li-Weil ⟹ 其}\textbf{有效内容}\in\textbf{Weil 泛函族} ⟹ \textbf{并入 A1/A3}（\text{[结构性]} ⚠️\ \text{非定理，需范式穷尽性}）}$$
$$\boxed{\text{④ 最终分叉确立} ✓✓;\ §E.4\ \text{最后问题}\textbf{被合法化} ✓✓：\boxed{\textbf{C6 是否真的构成第七种证明类，还是只是 A1/A3 的新表示？}}}$$

---

## §1 先判 $V158$(b) —— **撤回**（✓✓ 本档第一件事 ✓）

$$\text{命题}\ Z_\zeta-\tfrac12\subseteq\Lambda_M\ \textbf{不逻辑上必然要求先计算}\ N_\zeta(T)\ ✗✓$$
$$\qquad\text{例如完全可能存在}\ \textbf{结构定理}\ ✓：\Phi:\Lambda_M\xrightarrow{\ \sim\ }Z_\zeta-\tfrac12,\ \text{然后直接证}\ \zeta\bigl(\tfrac12+\Phi(\lambda)\bigr)=0\ \text{及反向存在性} ✓$$
$$\qquad\Longrightarrow\ \text{此证明可以是}\textbf{结构性双射证明}\text{，}\textbf{未必先使用}\ N_\zeta(T)=\tfrac{T}{2\pi}\log\tfrac{T}{2\pi e}+O(\log T)\ ✓✓$$
$$\Longrightarrow\ \boxed{\text{completeness}\not\Rightarrow\text{必须使用 }N_\zeta(T)}\ ✓✓\ \text{—— 故 }V158\text{(b)}\ \text{的"需 }N_\zeta(T)\text{，唯一途径是论证原理"}\textbf{应降级为结构性观察} ⚠️,\ \textbf{不得作定理} ✗$$
$$\qquad\boxed{\text{正确形式} ✓：\text{计数路线}\subset C\ \text{（而非 completeness}\subset C）}$$

---

## §2 ⭐ ③ 的正确做法：证明**范式并轨**，而不是证明必经 RvM（✓）

$$\textbf{不要}\text{证明}\ C6.6\Rightarrow N_\zeta(T)\ ✗;\ \textbf{而证明}\ ✓：\boxed{C6.6\ =\ \text{一个新的 ζ-谱识别定理}}\ \text{然后检查它与 }A1/A3\ \text{的}\textbf{证明内容}\text{是否相同} ✓✓$$

$$\text{设}\ \Phi:\Lambda_M\to Z_\zeta-\tfrac12\ \text{是 C6.6 的内部双射} ✓;\ \text{soundness 给}\ \forall\lambda:\zeta\bigl(\tfrac12+\Phi(\lambda)\bigr)=0\ \text{(S)};\ \text{completeness 给}\ \forall\rho\ \exists\lambda:\Phi(\lambda)=\rho-\tfrac12\ \text{(C)}$$
$$\Longrightarrow\ \boxed{\Lambda_M\xrightarrow{\ \Phi\ }\cong Z_\zeta-\tfrac12}\ \tag{*}$$
$$\qquad\Longrightarrow\ \text{这本身}\textbf{已经是一个完整谱识别定理} ✓✓$$

### ⭐ 三层必须严格分开（✓ 唐先生逐字 ✓）

$$\textbf{层 1（逻辑蕴含）✓}：\text{若 C6.6 得完整零谱对应，则可推 RH}\ \textbf{只要}\ \Lambda_M\subset i\mathbb R\ ✓\ \Longrightarrow\ C6.6+\text{C6.5 purity}\Rightarrow\mathrm{RH}\ ✓$$
$$\qquad\text{但反向}\ \mathrm{RH}\Rightarrow C6.6\ \textbf{显然不成立} ✗\ \Longrightarrow\ \boxed{\text{C6.6 不是逻辑等价于 RH}}\ ✓✓$$
$$\textbf{层 2（证明载体）✓}：\text{若证明 (*) 的唯一有效工具是}\ \text{trace}\to\text{explicit formula}\to\text{Li/Weil positivity}\ ✓,\ \text{则}\ \boxed{C6.6\subseteq A1/A3}\ ✓\ \text{—— 但}\textbf{这仍需证明} ✗,\ \textbf{不能}\text{由"必须算 }N(T)\text{"推出} ✓✓$$
$$\textbf{层 3（真正的新情况）✓}：\text{若}\ A\to M\to\Lambda_M\xrightarrow{\Phi}\cong Z_\zeta-\tfrac12\ \text{而 }\Phi\ \text{的证明}\textbf{完全不使用}\ ✓：\text{explicit formula／}\xi\ \text{的论证原理／Mellin／L-function／Hadamard／Li-Weil positivity} \Longrightarrow \textbf{C6 才真正成为新类} ✓✓$$
$$\qquad\Longrightarrow\ \text{故}\textbf{目前不能宣布}\text{它已并入 }A1/A3\ ✗✓$$

---

## §3 ⭐ 本档新增：**并轨骨架**（✓ 证明"若载体属已知范式 ⟹ 并入 A1/A3" ✓）

$$\textbf{第一步（范式的统一入口）✓}：\text{已归档的 (*) 证明范式}\ \textbf{全部}\text{经以下之一} ✓：\text{(i) trace／显式公式};\ \text{(ii) }\xi\ \text{的论证原理（计数）};\ \text{(iii) Mellin};\ \text{(iv) L-函数（Euler 积＋FE）};\ \text{(v) Hadamard 分解};\ \text{(vi) Li/Weil positivity};\ \text{(vii) 定义型／}\det\text{（循环）};\ \text{(viii) selection} ✓$$
$$\textbf{第二步（关键归约 ✓）}：\text{其中 (i)–(vi) }\textbf{均作用于同一个对象}\ ✓：\ \text{Weil 泛函族}\ W(f)=\sum_\rho\hat f(\rho)-\bigl(\text{archimedean}\bigr)-\bigl(\text{prime terms}\bigr)\ ✓✓$$
$$\qquad\Longrightarrow\ \text{任何经 (i)–(vi) 的 (*) 证明，其}\textbf{有效内容}\text{必可写成对 }W(\cdot)\ \text{的}\textbf{正性／消失} \text{断言} ✓✓$$
$$\qquad\Longrightarrow\ \text{而}\ \boxed{W\ \text{的正性断言}\ \equiv\ A3\ \text{（Weil 正性）的对象}}\ ✓;\ \text{取 Li 检验族}\ f=f_n\ \text{即得}\ \boxed{\lambda_n\ \text{型断言}\ \equiv\ A1}\ ✓✓$$
$$\textbf{第三步（同墙结论 ✓）}：\text{故经 (i)–(vi) 的 C6.6 ⟹ 其内容 ∈ }A1/A3\ \text{族} ⟹ \text{须控制}\textbf{统一}的 Weil 泛函正性 ⟹ \text{已知无条件输入不足（}T^2\ \text{律／预算交叉／比例天花板 0.682）}\ ✓✓$$
$$\Longrightarrow\ \boxed{\text{若 C6 的谱双射载体属于}\textbf{已知证明范式}\text{，则并入 }A1/A3}\ ✓\ \text{—— 本档给出骨架 ✓，}\textbf{但为 [结构性] ⚠️}\ \text{（需"范式穷尽性"，同 }V157\ \text{边界）}$$
$$\qquad ⚠️\ \textbf{诚实边界 ✓}：\text{本档}\textbf{不}\text{证明范式穷尽} ✗;\ \text{亦}\textbf{不}\text{证明 (*) 必经 }W\ ✗\ \text{—— 只给出"若属已知范式则并轨"的骨架} ✓$$

---

## §4 ⭐ 最终分叉与 §E.4 的合法化（✓✓）

$$\boxed{\text{若谱双射依赖 }\zeta\ \text{的解析结构}\ \Longrightarrow\ A1/A3/C\ \text{旧墙};\qquad \text{若存在独立结构性双射}\ \Longrightarrow\ \textbf{真正的新 C6}}$$
$$\qquad\Longrightarrow\ \text{这比 }V158\ \text{更严格 ✓，也}\textbf{避免}\text{把"没有找到其他证明"误写成"没有其他证明"} ✓✓\ \text{（与 }V136\ \text{勘误／}V144\ \text{"未找到"}\neq\text{"不存在"}\ \text{同型纪律} ✓）$$
$$\qquad\Longrightarrow\ \text{完成后，}§E.4\ \text{才能}\textbf{合法地}\text{问最后一个问题} ✓✓：\boxed{\textbf{C6 是否真的构成第七种证明类，还是只是 A1/A3 的新表示？}}$$

---

## §5 判词与下一步（✓）

$$\boxed{\textbf{V159 判词 ✓}：① 撤回 V158(b)（completeness}\not\Rightarrow N_\zeta(T)\text{）⟹ 降为"计数路线}\subset C\text{"} ✓✓;\ ② C6.6 ＝ 非解析非循环谱双射 ✓✓;\ ③ 三层严格分开（逻辑／载体／新情况）✓✓;\ ④ 并轨骨架（已知范式 ⟹ Weil 泛函族 ⟹ A1/A3）✓;\ ⑤ 最终分叉 ＋ §E.4 最后问题合法化 ✓✓}$$
$$\qquad\textbf{净收获 ✓（收口型）}：\text{③ 的目标被}\textbf{改成可做的形式} ✓\ \text{（证明范式并轨，而非证明必经 RvM）};\ \text{且}\boxed{\text{唯一开口＝\textbf{独立结构性双射}}} \text{被单独隔离} ✓✓$$
$$\qquad\textbf{下一步三选 ✓}：\text{① 攻击唯一开口：}\textbf{能否构造一个不用六大工具的结构性双射 }\Phi？\ \text{（这是真正的第七类候选位）};\ \text{② 把"已知范式穷尽性"形式化（把并轨骨架从 [结构性] 升为定理）};\ \text{③ 审 (i)–(vi)}\to W\ \text{归约中是否有 }\textbf{不经 }W\ \text{的例外} ✓$$
$$\text{`CLOSED-ROUTES-MAP` §F.5u 增补 ✓}：\text{撤回行 ＋ 谱双射行 ＋ 三层行 ＋ 并轨骨架行 ＋ 最终分叉行 ✓}$$

```
⚠️ §1 撤回为【逻辑必然性判定 ✓✓】（结构性双射证明是合法的存在形式）
⚠️ §2 三层为【唐先生逐字 ✓】；层 1 为【逻辑 ✓】；层 3 为【定义级 ✓】
⚠️ §3 并轨骨架为【结构性 ⚠️】非定理（需范式穷尽性；同 V157 边界纪律）
⚠️ §4 分叉为【结构性 ⚠️】；"合法化 §E.4 最后问题"为【制度级 ✓】
⚠️ 未用 RH ✓；未跑 Lean ✓；零数值 ✓
✅ 净产出：① 撤回 V158(b) 的过度断言 ✓✓；② C6.6 ＝ 非解析非循环谱双射 ✓✓；
   ③ 三层严格分开 ✓✓；④ 并轨骨架（已知范式 ⟹ Weil 泛函族 ⟹ A1/A3）✓；
   ⑤ 最终分叉 ＋ §E.4 最后问题合法化 ✓✓；⑥ 唯一开口 ＝ 独立结构性双射（被隔离）✓✓
```
