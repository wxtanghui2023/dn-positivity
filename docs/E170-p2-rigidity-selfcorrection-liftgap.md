# E170 · ⭐⭐⭐⭐ **p=2 刚性验证 ＋ 自我更正 E169 ＋ "局部⟹全局"缺口的精确化**
### 结论：**您对 ✓；密度/CRT/筛法三条攻击【皆 NO-GO ✓】；而我的 E169 "显式构造"【是错的 ✗】—— 错点恰是跨素数机制所在 ✓**

> 委托 ✓ 唐先生 14:02（**先推到底，不把"密度＋模 $p^2$"当天生杀手 ✗；p=2 退化为薄因子二选一 ✓；攻"局部因子分解的相容性"✗**）
> 执行 ✓ 小灵｜脚本 ✓ `scripts/E170_p2_rigidity_and_oddimage.py/.txt` ✓｜纪律 ✓ 未用 RH ✓；未涉 ζ 解析 ✓；未跑 Lean ✓

---

## §0 接受您的判定（✓）＋ 加一条结构性理由

$$\text{"平方自由密度不是跨素数障碍" ✓ —— 采纳 ✓；}\textbf{结构性理由 ✓}：|S_M|=M\prod_{p\mid M}(1-p^{-2})\ \textbf{是完全乘性 ✓}；$$
$$\qquad\text{且【乘积集自动提升 ✓】：}A_M=\prod_pA_p,\ B_M=\prod_pB_p\ \Longrightarrow\ A_M+B_M=\prod_p(A_p+B_p)\ \checkmark$$
$$\Longrightarrow\ \text{(A)(B)(C) 的【乘积型解】永远可提升 ⟹ 有限阶段【永不】产生障碍 ✗}$$

## §1 p=2（mod 4）：**穷举验证 ✓ 您的二分正确 ✓**

$$\text{约束 ✓}：A_2\subseteq S-1=\{0,1,2\}\ ✓,\ B_2\subseteq S=\{1,2,3\}\ ✓\（\text{由 (D)(E) 缩 ✓）$$
$$\textbf{穷举结果 ✓：解数 ＝ 2 ✓}\qquad \boxed{(A_2,B_2)=(\{0\},\{1,2,3\})\quad\text{或}\quad(\{0,1,2\},\{1\})}$$
$$\Longrightarrow\ \boxed{\textbf{全局二分支 ✓}：\text{要么 }A\subseteq4\mathbb Z\ ✓,\ \text{要么 }B\subseteq4\mathbb Z+1\ ✓}\（\text{整个集合的剩余类约束 ✓）}$$
$$\qquad\text{（}\text{您 §4 的警告 ✓ 照录 ✓}：A\subseteq4\mathbb Z\ \text{与 }A(X)\asymp\sqrt X\ \textbf{完全相容 ✗}（A=\{4n^2\}\ ✓）\Longrightarrow \textbf{p=2 单独不是 NO-GO ✗）$$

## §2 ⚠️ **自我更正：E169 的"显式构造"是错的** ✗（✓ 本轮最重要一条 ✓）

$$\text{我 E169 写 ✓}：X=\{0,1\}\ ✓,\ Y=\{\text{奇剩余 mod }p^2\}\ ✓ \Longrightarrow X+Y=G\setminus\{0\}\ ✓$$
$$\textbf{错在 ✓}：\textbf{"奇数的像 mod }p^2\text{" 不是"奇剩余"✗，而是【全部剩余 ✗】}：$$
$$\qquad p^2\ \text{是奇数 ✓} \Longrightarrow p^2\in\{\text{奇数}\}\ ✓ \Longrightarrow p^2\equiv0\ (\mathrm{mod}\ p^2)\ \Longrightarrow\ \boxed{0\in Y\ ✓} \Longrightarrow Y=G\ \Longrightarrow\ 0\in X+Y\ ✗$$
$$\text{数值 ✓}：p=3,5,7\ \text{的奇数像均为【全部剩余】✓（脚本 ✓）} \Longrightarrow \textbf{该"构造"违反 (A) ✗，作废 ✓}$$
$$\text{（}\textbf{仍然成立的部分 ✓}：\text{【固定 }p\ \text{的有限问题】(A)(B)(C) 【确实可满足 ✓】—— }p=3\ \text{穷举 3726 解 ✓（含 (3,3) 解 108 个 ✓）—— }\text{错的只是我那个"跨所有 }p\ \text{的族"✗）}$$

## §3 ⭐⭐ **"局部 ⟹ 全局"缺口的精确化**（✓ 由 §2 的错点直接给出 ✓）

$$\text{错点 ✓ 提示了真正的机制 ✓}：\textbf{集合的"局部意图"不是它的模像 ✗}：$$
$$\qquad\boxed{\text{"}B_p\ \text{避开 }0\text{"} \iff \textbf{不存在 }b\in B\ \text{使}\ p^2\mid b\ ✓} \iff \textbf{(E)}\ B\subseteq S\ ✓$$
$$\Longrightarrow\ ⭐\ \textbf{(D)(E) 的"全局性"由此得到精确表述 ✓}：\text{它们约束的是【实际集合】✗，不是有限多个剩余 ✓}$$
$$\qquad\text{故 ✓：}\textbf{局部条件（每个 }p\ \text{单独 ✓ 可满足 ✗）＋ 乘积提升（自动 ✓）}\ \textbf{【都】不能替代 (D)(E) ✗}$$
$$\qquad\text{而 (D)(E) 一旦写成"}\forall p:\ B\ \text{不含 }p^2\ \text{的倍数"✗}\ ✓，\textbf{它就【等价于】原问题 ✓}（B\subseteq S ✓）⟹ \textbf{无新信息 ✗}$$
$$\text{（}\textbf{这正是您 §11 说的"逆极限" ✓}：\text{相容族 }\mathcal T_p\ \text{存在 ✓，但【同一 }B\text{】实现它 ⟺ (E) ✓ ⟺ 原命题 ✗）}$$

## §4 筛法审计（✓ 我也试了 CRT/筛法路线 ✗）

$$\text{CRT 筛 ✓}：A(X)\le X\prod_{p\le y}(|A_p|/p^2)+O(M)\ ✓,\quad M=\prod_{p\le y}p^2=e^{2\theta(y)}\ ✓$$
$$\qquad\text{若取 }M\asymp X\ \text{则误差 }O(X)\ \textbf{吞掉主项 ✗（经典困境 ✓）}$$
$$\qquad\text{用筛法基本引理 ✓（}y=X^{1/u}\text{）则误差小 ✓，但此时积只到 }p\le X^{1/u}\ ⟹\ \textbf{所得不等式【相容 ✗】}$$
$$\Longrightarrow\ \textbf{筛法路线【不产生矛盾 ✗】}；\text{与您的判定一致 ✓}$$

## §5 判定表（✓ 更新您的表 ✓）

| 攻击 ✓ | 结果 ✓ |
|:--|:--|
| **D/E 单独 ✓** | **不矛盾 ✗** |
| **squarefree 密度 ✓** | **不矛盾 ✗**（完全乘性 ✓；乘积提升 ✓） |
| **单个 }p^2$ ✓** | **不矛盾 ✗**（p=3：3726 解 ✓） |
| **}4p^2$ CRT 密度 ✓** | **不矛盾 ✗**（您 ✓） |
| **}p=2$ ✓** | ⭐ **强刚性 ✓（2 解 ✓，全局二分支 ✓）—— 但不足以杀 ✗** |
| **}p=2$ + 奇素数 ✓** | **尚未矛盾 ✗** |
| **多素数 CRT ✓** | **仍未矛盾 ✗**（乘积集自动提升 ✓） |
| **筛法 ✓** | **相容 ✗** |
| **同一 }(A,B)$ 的跨 }p$ 提升 ✓** | ⭐ **等价于 (E) ✓ ⟹ 等价于原问题 ✗（无新信息 ✓）** |

$$\Longrightarrow\ \boxed{\textbf{D/E 路线的"原始密度攻击"已 NO-GO ✓；而"跨 }p\text{ 提升"}\textbf{【等价】于原命题 ✗}}$$

## §6 边界与纪律（✓）

```
✅ **未用 RH ✓；未涉 ζ 解析 ✓；只用了 |S∩[0,X]| 的经典计数 ✓；未跑 Lean ✓**；**先查档 ✓**
⚠️ **① §2 是【自我更正 ✓】** —— E169 的"显式构造"作废 ✗，原档保留不删 ✓（T10 ✓），已加勘误 ✓
⚠️ **② §3 的"(D)(E) ⟺ 原命题"是我的判定 ✓** —— 逻辑：B_p 避 0 ⟺ B 无 p^2 倍数 ✓（一字 ✓）
⚠️ **③ §4 的筛法审计是【方向性 ✓】** —— 未写出完整严格版 ✗
⚠️ **④ 未声称 P-SF 已证/已否 ✗**；未声称 D1-B\* 已死 ✗
⭐ **净产出 ✓**：① **p=2 二分验证 ✓ ＋ 全局二分支 ✓**；② ⚠️ **自我更正 E169 ✗（错点 ＝ 局部意图 ≠ 模像 ✓）**；
   ③ ⭐ **"(D)(E) ⟺ 原命题"（跨 }p$ 提升无新信息 ✗）**；④ **筛法路线 NO-GO ✓**
```

## §7 一句话（✓）

$$\boxed{\text{您的判定全部成立 ✓；我的 E169 构造作废 ✗；}\textbf{而"跨 }p\text{ 提升"经查【等价于原命题 ✗】—— 局部路线到此为止 ✓}}$$
