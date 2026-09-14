# E192 · ⭐⭐⭐⭐ **$P{=}5$ 长跑（嵌套 ＋ persistent-dead 正确口径）：未达判活标准 ✗｜E191 的乐观是 transient 假象 ✗｜唯一正面：residue 复用长期可行 ✓**
> 依唐先生 2026-09-14 16:45 裁定 ✓（**四条硬判据 ✓；不以"比例下降"为判活 ✓；persistent 与 transient 必须拆分 ✓；保持嵌套 $A_k\subset A_{k+1}$、$B_k\supset B_{k+1}$ ✓**）
> 纪律 ✓ 未用 RH ✓；未涉 ζ ✓；未跑 Lean ✓；数值＝精确枚举（$P{=}5$，Lim$=810000$ ✓）

---

## §0 实现要点（✓ 四条判据如何落地 ✓）

$$\textbf{① 嵌套 ✓}：A_k\subset A_{k+1}\ ✓（只增 ✓）；B_{k+1}=B_k\cap\{b:b+c\in S\}\ ✓（\textbf{只缩 ✓，旧 }B\ \text{不重优化 ✓）}$$
$$\textbf{② persistent-dead 的正确判据 ✓（本轮新增 ✓）}：n\ \text{可被 free 层覆盖}\iff \exists i\ge1:\ n-iQ\in B_k\ ✓$$
$$\qquad\iff \text{同一类 }n\bmod Q\ \text{中存在 }B_k\ \text{元素}<n\ ✓\ \Longrightarrow\ \boxed{\text{只需比较各类最小元 ⟹ }O(1)\ \text{判定 ✓}}\ ✓$$
$$\qquad\textbf{故 }D_k^{\rm pers}=\{n\notin A_k+B_k:\ \min(B_k\cap(n\bmod Q))\ge n\}\ ✓;\quad \text{transient}=\text{uncovered}\setminus\text{persistent}\ ✓$$
$$\textbf{③ 残类复用 ✓}：\text{候选限制为 }c\equiv r\bmod Q\ (r\in A_k\bmod Q)\ ✓\ \text{加层 }kQ\ ✓\ \Longrightarrow\ \text{低素数损伤}=0\ ✓（E191 策略 ✓）$$
$$\textbf{④ 监控量 ✓}：(u_k,\ |B_k|/|B_0|,\ R_{k,2},R_{k,3},R_{k,5},\ \eta_k)\ ✓,\ \eta_k=\frac{G_k/|D^{\rm pers}_{k-1}|}{L_k/|B_{k-1}|}\ ✓$$

## §1 结果（✓ 跑满 8 步后停滞 ✗）

$$\text{起始 ✓}：|B_0|=138394\ ✓,\ \text{uncovered}=122739\ ✓,\ \textbf{persistent-dead}=119643\ ✓\ (u_0=1)\ ✓$$
```
 步   +c     净消灭 G   persistent-dead(u)    |B|/|B₀|    η      R2 R3 R5
 1   901     14810     108602 (0.908)        0.947     2.337    2  4  5
 2  1808      6281     106006 (0.886)        0.896     1.067    2  4  5
 3   904      4956     106956 (0.894)        0.847     0.861    2  4  5
 4  1801      5631     105627 (0.883)        0.800     0.953    2  4  5
 5  1804      1810     111225 (0.930)        0.756     0.307    2  4  5
 6   908      1295     118442 (0.990)        0.713     0.205    2  4  5
 7  1836      1225     119693 (1.000)        0.672     0.181    2  4  5
 8   936       269     128216 (1.072)        0.633     0.039    2  4  5
 9    —    【无正收益候选 ⟹ 停滞 ✗】
```
$$\text{末态 ✓}：|A|=13\ ✓,\ A\bmod Q\ \text{残类数}=5\ ✓,\ |B|/|B_0|=0.633\ ✓,\ \textbf{persistent-dead}=128216\ (>119643\ ✗)$$

## §2 判词（✓ 四条判据逐条裁决 ✓）

$$\textbf{判据 ④（residue 状态稳定 ✓）}\ \boxed{\text{成立 ✓}}\ ✓：R_2=2,\ R_3=4,\ R_5=5\ \text{【全程恒定 ✓】}\ \Longrightarrow\ \textbf{残类复用长期可行 ✓（本轮唯一正面结论 ✓）}$$
$$\textbf{判据 ①（}\eta\ \text{有正下界 ✗）}\ \boxed{\text{不成立 ✗}}\ ✓：\eta：2.337\to1.067\to0.861\to0.953\to0.307\to0.205\to0.181\to\boxed{0.039}\ ✗\ \text{单调衰减到 0 ✓}$$
$$\qquad\Longrightarrow\ \textbf{前期的正收益是 transient ✗}\ ✓（正与 E190 同型 ✓）$$
$$\textbf{判据 ②（persistent-dead}\to0\ ✗）\ \boxed{\text{不成立 ✗}}\ ✓：108602\to\cdots\to128216\ ✗\ \text{【不降反升 ✓】（相对 }u_0=1\ \text{几乎没动 ✓，末期甚至超过 1 ✗）}$$
$$\textbf{判据 ③（}B_\infty\neq\varnothing\ ✓）\ \boxed{\text{未判 ✗}}\ ✓：|B|/|B_0|\ \text{仍 }0.633>0\ ✓\ \text{但基线持续缩 ✓}$$
$$\Longrightarrow\ \boxed{\textbf{四项未同时成立 ⟹ 按您的规则【不升级】为无限层延拓定理 ✗}}\ ✓$$

## §3 ⭐ 重要副产物：E191 的乐观必须打折 ✗（✓ 口径纠正 ✓）

$$\text{E191 用"未覆盖数"作监控量 ✓：}0.2495\to0.0894\ ✓\ \text{（看似成功 ✓）}$$
$$\text{但其中绝大部分是 }\textbf{transient}\ ✓：\text{free 层（}a=iQ\ ✓\text{）本来就能覆盖它们 ✓ ⟹ 不是 bootstrap 的功劳 ✗}$$
$$\Longrightarrow\ \boxed{\textbf{凡以"未覆盖数"为监控量的实验（E190/E191）都必须按 persistent 口径重读 ✗}}\ ✓\ \text{—— 您坚持的拆分是【必要】的 ✓✓}$$

## §4 (E193) 建议（✓ 三条，按优先级 ✓）

```
(a) ★ 放开候选族 ✓：允许 c 引入【新残类 mod 900】（支付低素数损伤 ✓），测 η 的长期行为 ✓
    —— 这直接检验您的 §7 判死条件："是否被迫进入更高 sieve-cost 的 (A mod 4, A mod 9) 状态"✗
    注意 ✓：本轮停滞发生在【残类复用族内】✗ ⟹ 停滞可能只是候选族太窄的假象 ✗，必须先排除 ✓
(b) 攻"persistent-dead 的下确界"✓：是否存在与尺度无关的 c>0 使 |D^pers| ≥ c·|S∩[Q,Q²)| ✓？
    若成立 ⟹ 层间障碍 ✓（比 E186/E189 都强 ✓）；若不成立 ⟹ 构造仍有戏 ✓
(c) 换 free 族 ✓：把"free"从 a≡0 mod Q_P 扩到 a≡0 mod 多个 Q' ✓（多层免费 ✓），检验 dead 集是否缩小 ✓
```

## §5 边界与一句话（✓）

```
✅ 四条判据全部落地 ✓；persistent-dead 的 O(1) 判据 ✓（同类最小元比较 ✓）
✅ 结果 ✓：η 单调衰减到 0.039 ✗、persistent-dead 不降反升 ✗ ⟹ 未达判活 ✗
✅ 唯一正面 ✓：R2/R3/R5 全程恒定 ⟹ 残类复用长期可行 ✓
⚠️ 候选族受限（仅 A mod 900 的 5 类 ✓）⟹ 停滞可能为族太窄的假象 ✗（必须由 (a) 排除 ✓）
⚠️ 仍不声称构造存在 ✗、不声称不可能 ✗
⭐ 净产出 ✓：① persistent/transient 拆分落地并**推翻了 E191 的乐观读数** ✗✓；② η 判据（衰减到 0 ✓）；
   ③ 残类复用长期可行 ✓；④ E193 的三条入口 ✓
```
$$\boxed{\text{按 persistent 正确口径：}\eta\to0.039\ ✗,\ \text{persistent-dead 不降反升 ✗ ⟹ 未达判活标准 ✗；E191 乐观＝transient 假象 ✗；唯一正面＝residue 复用长期可行 ✓；下一枪 (E193-a)：放开残类族以排除"族太窄"假象 ✗}}$$
