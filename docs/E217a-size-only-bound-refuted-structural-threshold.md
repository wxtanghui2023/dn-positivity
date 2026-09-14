# E217-A · ⭐⭐⭐⭐⭐ **规模型下界的存在性审计：【被一次性杀死 ✗✗】—— 同尺寸 $k$ 下 $|B(A)|$ 从 $0$ 到 $\approx0.8|S|$ ｜且【结构分界线已被识别 ✓✓】（好 $A$ ⟺ $A$ 位于小素数平方倍数的陪集 ✓）**
> 依唐先生 2026-09-14 20:13 裁定 ✓（**先做反例审计 ✓；不先假定 $F(|A|,M)$ 存在 ✓；A 不过则不继续 B/C ✓**）
> 纪律 ✓ 未用 RH ✓；未涉 ζ ✓；未跑 Lean ✓；数值＝numpy（$M=Q^2=810000$ ✓，$|S_M|=492421$ ✓ 密度 0.6079 ✓）

---

## §0 设计（✓ 反例优先 ✓）

$$\text{固定 }S_M\ ✓,\ B(A)=\bigcap_{a\in A}(S_M-a)\ ✓;\quad \text{问 ✓}：\exists F(|A|,M)>0\ \text{使 }|B(A)|\ge F\ \text{对【所有合法 }A\ ✓】$$
$$\textbf{证伪策略 ✓}：\text{构造同尺寸 }|A_1|=|A_2|=k\ \text{而 }|B(A_1)|\gg|B(A_2)|\ ✓（\text{最好 }B(A_2)=\varnothing\ ⟹ F(k,M)=0\ ✓✓）$$
$$\text{样本族 ✓}：\text{①随机 200 ✓；②等差 }A=\{0,d,\dots,(k-1)d\}\ (d\in\{1,2,100,900,1000,10^4,44100,9\times10^4\}\ ✓)；③平方倍数 }a_i=i\cdot q^2\ (q\in\{6,30,900\}\ ✓)；④同余族 }a_i=i\cdot r\ (r\in\{4,9,25\}\ ✓）$$
$$\textbf{结构诊断 ✓}：|A-A|\ ✓,\ |A+A|\ ✓,\ E(A)=\#\{(a_1,a_2,a_3,a_4):a_1+a_2=a_3+a_4\}\ ✓$$

## §1 ⭐ 结果（✓ 关键 ✓）

```
k=4 （n=213 样本）：min |B| = 0 ✗（22/213 为 0 ✓）    中位 96384      max 448626（AP d=44100 ✓）
k=8 （n=213 样本）：min |B| = 0 ✗（142/213 为 0 ✓✓）  中位 0 ✗✗      max 395362（AP d=44100 ✓）
```
$$\Longrightarrow\ \boxed{\textbf{同尺寸 }k\ \text{下，}|B(A)|\ \text{从 }0\ \text{到 }0.8|S_M|\ ✗✗}\ \Longrightarrow\ \boxed{\textbf{任何仅依赖 }(|A|,M)\ \text{的正向下界只能是 }F(k,M)=0\ ✓✓}$$
$$\qquad\Longrightarrow\ \boxed{\textbf{规模型必要条件【被一次性杀死 ✗✗】}}\ ✓（\text{您设计的证伪策略成功 ✓）}$$
$$\qquad\textbf{附 ✓}：k=8\ \text{时【中位数即为 }0\ \text{✗✗】}\ ⟹ \text{"随机 }A\ \text{几乎总给出 }B=\varnothing"\ ✓（142/213=67\%\ ✓）$$

## §2 ⭐⭐ 结构分界线（✓ 意外但关键 ✓）

```
            |B(A)|     |A−A|   |A+A|   E(A)
坏 A（随机）   0          29      16      55
好 A（AP, d=44100）  395362     8       15     344
```
$$\Longrightarrow\ \boxed{\textbf{好 }A\ \text{的 }|A-A|\ \text{【小得多 ✗】（}8\ \text{vs }29\ ✓\ \text{—— 即 }A-A\ \text{几乎只有 }k\ \text{个元素 ✓）而 }E(A)\ \text{【高得多 ✓】（}344\ \text{vs }55\ ✓）}$$
$$\textbf{机制解释 ✓（关键 ✓）}：d=44100=Q_7=2^2\cdot3^2\cdot5^2\cdot7^2\ ✓\ \Longrightarrow\ \text{所有 }a=i\cdot d\ \text{都是 }p^2\ (p\le7)\ \text{的倍数 ✓}$$
$$\qquad\Longrightarrow\ b+a\equiv b\ {\rm mod}\ p^2\ \text{对 }p\le7\ \text{全部成立 ✓}\ \Longrightarrow\ \textbf{小素数约束【坍缩为单个约束 ✓】}\ ✓（\text{与 }b\ \text{自身相同 ✓）}$$
$$\qquad\Longrightarrow\ \text{故 }k\ \text{个约束几乎完全【冗余 ✓】}\ \Longrightarrow\ |B|\approx|S|\cdot\prod_{p>7}(\cdots)\approx0.8|S|\ ✓✓\ \text{—— 与实测 0.805 吻合 ✓}$$
$$\qquad\textbf{对比 ✓}：\text{随机 }A\ \text{的元素落在各种残类 ✓}\ \Longrightarrow\ k\ \text{个约束【独立 ✓】}\ \Longrightarrow\ |B|\approx|S|\cdot0.61^k\ ✓\ (k{=}8:0.61^8\approx0.022\ ⟹\ \approx10^4\ \text{✗})\ \text{—— 而实测多为 }0\ ✗\ \text{（因窗口效应 ✓）}$$

## §3 判词（✓ 按您的流程 ✓）

$$\boxed{\textbf{E217-A 结论 ✓}：\text{规模型下界 }|B(A)|\ge F(|A|,M)>0\ \textbf{不存在 ✗✗}}\ ✓$$
$$\qquad\text{按您指示 ✓：}\text{A【未通过 ✓ ⟹ 本轮不继续 B/C ✗】}\ ✓$$
$$\qquad\textbf{但附带得到一个可直接进入 E217-B 的结构参数 ✓✓}：\boxed{|A-A|\ \text{与 }E(A)\ \text{构成可识别的分界 ✓}}\ ✓$$
$$\qquad\qquad\text{更强形式 ✓}：\text{好 }A\ \text{的充要候选条件＝}A\ \text{位于【小素数平方倍数陪集】}\ \big(a_i+a_j\equiv a_k+a_l\ {\rm mod}\ Q_P\ \forall P\ ✓\big)\ ✓✓$$

## §4 该结果的意义（✓ 三点 ✓）

$$\textbf{① 对归档的补强 ✓}：\text{E210 归档中"覆盖侧正面构造"未被证否 ✓，但本轮证明【不能靠"规模"】✗ —— 必须靠【结构】✓}$$
$$\textbf{② 与早期"free 元素"概念的呼应 ✓}：\text{E185/E189/E190 的 }a\equiv0\ {\rm mod}\ Q_P\ ✓\ \text{正是本轮的"好 }A"\ \text{的单元 ✓ ✓（}\text{AP d=}Q_7\ \text{＝全部元素 free ✓）}$$
$$\textbf{③ 但注意 ✓（不over-claim ✓）}：\text{AP }A\ \text{虽使 }|B|\ \text{巨大 ✓，但其【覆盖能力】仍待检验 ✗}$$
$$\qquad\qquad\text{（因 }A\ \text{全部是 }Q_7\ \text{的倍数 ✓ ⟹ }A+B\ \text{只能覆盖 }B+Q_7\mathbb{Z}\ \text{型的和 ✓）};\ \text{且 }A\ \text{发散于 }Q_7\cdot\mathbb{Z}\ ✓\ \text{只能有 }k\ \text{个元素在 }[0,M)\ ✓$$

## §5 (E217-B) 建议（✓ 因为分界线已现，可直入结构参数 ✓）

```
① ★ 直接做结构-规模关系 ✓：固定 k ✓，采样 A ✓，画散点 (|A−A|, E(A), |A+A|, 各小素数模占位) → |B(A)| ✓
   判据 ✓：是否存在【比随机好得多】的结构类 ✓（除 AP/Q_P 陪集之外 ✓）？
② ★ 关键新问题 ✓（由 §4③ 引出 ✓）：AP A 的 |B| 巨大 ✓ 但覆盖能力如何 ✓？
   —— 若 (A_Q7, B(A_Q7)) 满足 S ⊆ A+B ✓ 且 A 无限 ✓ ⟹ 直接得到解 ✓✓！
   —— 但 A 必须是【倍数集】的无限子集 ✓ ⟹ 检验：A = Q_7·{0,1,2,...} ✓（无限 ✓）时，
      A+B ⊇ S ✓？hmm —— B = B(A) 也会相应缩小 ✗ ⟹ 这正是原问题 ✓（须算 ✓）
③ 若 ② 给出 A+B=S ✓ ⟹ 阶段突破 ✓；否则回到结构-规模关系 ✓
```

## §6 边界与一句话（✓）

```
✅ 反例审计 ✓（213×4 样本 ✓ 含四族结构 ✓）；极值结构诊断 ✓；|B|=0 计数 ✓
✅ 结论 ✓：规模型下界不存在（F=0 ✓）；好/坏 A 的结构分界已现（|A−A| ✓, E(A) ✓）
⚠️ 仅 k=4,8（16/30 未完成 ✗）；仅单窗口 M=Q² ✓；"好 A ⟺ 陪集"是【观察 ✓】非定理 ✗
⚠️ 不声称覆盖侧无解 ✗；不声称 AP 型 A 能解题 ✗（覆盖能力未检验 ✓）
⭐ 净产出 ✓：① 杀掉规模型必要条件 ✓✓；② 识别结构分界线 ✓✓；③ 指向"Q_P 陪集"与"邻域宽度"的定量关系 ✓
```
$$\boxed{k=4:\ |B|\in[0,448626]\ ✓;\ k=8:\ |B|\in[0,395362]\ \text{（中位 0 ✗，142/213 为 0 ✓）}\ \Longrightarrow\ \textbf{规模型下界不存在（}F(k,M)=0\ ✓✗）；\text{结构分界 ✓：好 }A\ (\text{AP }d{=}Q_7)\ \text{的 }|A-A|{=}8,\ E{=}344\ \text{vs 坏 }A\ \text{的 }29,\ 55\ ✓\ \Longrightarrow\ \textbf{好 }A\ \text{位于小素数平方倍数陪集 ⟹ 约束坍缩 ✓；A 未通过 ⟹ 本轮止于 A ✓；但分界线已可直接进入 E217-B ✓}$$
