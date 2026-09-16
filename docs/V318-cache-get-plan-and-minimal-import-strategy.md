# V318 · **olean 问题：联网解法 ＋ 按需加载策略**（唐先生 14:26 两条指令）

## 指令一：不要加载 Mathlib 全部（内存不够）⟹ 按需使用

$$\text{① }\textbf{构建层面}：\texttt{lake exe cache get}\ \text{仅}\ \textbf{下载预编译 olean}，\textbf{不编译 Mathlib} ⟹ \textbf{内存友好}（\text{无编译器峰值}）✓✓$$
$$\text{② }\textbf{Lean 文件层面}：\text{只 import 必需模块（避免}\ \texttt{import Mathlib}\ \text{整体）}：$$
$$\qquad \text{本次}\ \texttt{V316\_kernel\_bound.lean}\ \text{仅 3 个 import}：$$
$$\qquad \qquad \texttt{Mathlib.MeasureTheory.Integral.IntervalIntegral};\quad \texttt{Mathlib.MeasureTheory.Integral.Bochner.Basic};\quad \texttt{Mathlib.Analysis.SpecialFunctions.Pow.Real} ✓$$
$$\qquad ⚠️\ \text{可进一步减：}\texttt{Pow.Real}\ \text{本块（}\texttt{kernel\_mass}\text{）似不需要 ⟹ 落库时可删} ⚠️✓$$
$$\text{③ }\textbf{策略（落库时）}：\text{逐块编译}\ \to\ \text{仅保留被用到的 import};\ \text{避免}\ \texttt{lake build}\ \text{整库} ✓✓$$

## 指令二：olean 问题联网搜索 ⟹ 标准解法已确认

$$\text{查得标准解（ArchWiki／Lean 官方／Zulip 档案一致）}：\boxed{\texttt{lake exe cache get}} ✓✓✓$$
$$\qquad \text{作用}：\text{从 Mathlib 缓存服务器下载}\ \textbf{预编译 olean};\ \text{必要时}\ \texttt{lake exe cache get!}\（\text{强制重取}）✓$$
$$\qquad \text{前置条件}：\text{olean 须与}\ \texttt{lean-toolchain}\ \textbf{同版本} ⟹ \text{本项目}\ \texttt{v4.33.0}\ \text{与 mathlib4 的 toolchain 须匹配（ArchWiki 原文明确）}⚠️✓$$
$$\qquad \text{已知失败模式（Zulip）}：\text{缓存"看似最新"但实际缺文件（}\text{本次症状吻合：}\texttt{IntervalIntegral.olean}\ \text{单独缺失}）⟹ \text{解法}\ \texttt{cache get!}\ \text{或}\ \text{删}\ \texttt{.lake}\ \text{重取} ✓$$

## 实测状态（本轮）

$$\text{已启动}：\texttt{cd}\ \sim\texttt{/lean-repro/zeta23-local \&\& lake exe cache get}（\texttt{timeout 900}，后台）✓$$
$$\qquad \text{轮询 30\,s}\ \to\ \text{无输出};\ \text{再查}\ 25\,s\ \to\ \boxed{\texttt{IntervalIntegral.olean}\ \textbf{尚未出现}};\ \texttt{.lake/build}\ \text{仍}\ 13\,\mathrm{G} ✓$$
$$\qquad ⟹ \text{状态}：\textbf{进行中（未完成）};\ \text{可能正在编译}\ \texttt{cache}\ \text{工具本身或下载中} ⚠️✓$$
$$\qquad ⚠️\ \text{已知风险}：\texttt{cache}\ \text{工具需先编译（依赖 Mathlib）⟹ 可能先撞同一个 olean 缺口}（\text{先有鸡还是先有蛋}）⚠️✓$$

## 判词 ＋ 下一步

```
① **联网解法确认**：lake exe cache get（下载预编译 olean，不编译 ⟹ 内存友好）✓✓
② **按需加载**：构建层用 cache（免编译）；文件层只 import 必需模块（本次 3 个，可减到 2）✓✓
③ ⚠️ 实测未完成（IntervalIntegral.olean 尚未出现）；cache 工具自身编译可能撞同一缺口 ⚠️
④ 未用 RH ✓；零数值 ✓
```

```
下一步（按优先级）
 (α) 继续等 cache get；若完成 ⟹ 重跑 lake env lean V316_kernel_bound.lean（期望：kernel_mass 编译）✓
 (β) 若 cache 工具自身编译失败（撞同一缺口）⟹ 退路：**定点编译该模块**：
        lake build Mathlib.MeasureTheory.Integral.IntervalIntegral
      （输出最小、内存按需）✓
 (γ) 若网络不通 ⟹ 启用 ghfast.top 镜像或换用项目内已有积分接口重写 kernel_mass（但项目自身 olean 也缺）⚠️
 (δ) **同时**：把 V316_kernel_bound.lean 的 import 精简到最小（删 Pow.Real 若不需要）✓
```
