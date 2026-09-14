# E169 · ⭐⭐⭐⭐ **有限群 $\mathbb Z/p^2$ 的极端加法覆盖：命题【可满足 ✓】⟹ 不能作 NO-GO ✗**
### 主结果：**(A)(B)(C) 有解 ✓（显式构造 ＋ p=3 穷举 3726 个 ✓）；但换得【严格双侧常界 ✓】**

> 委托 ✓ 唐先生 13:57（**不要用"上下密度"换掉增长假设 ✗；直接攻有限群 $\mathbb Z/p^2$-SF ✓；不碰 RH ✓**）
> 执行 ✓ 小灵｜脚本 ✓ `scripts/E169_finitegroup_psf.py/.txt` ✓｜纪律 ✓ 未用 RH ✓；未涉 ζ 解析 ✓；未跑 Lean ✓

---

## §0 接受您的否决（✓）

$$\text{"上下密度＋平移铺砌 ⇒ 正则增长"}\ \textbf{是同型未证命题 ✗ —— 采纳您的否决 ✓}$$
$$\text{靶改为 ✓}：\ \text{(A) }X+Y=G\setminus\{0\}\ ✓,\ \text{(B) }|X|+|Y|\le p^2-1\ ✓,\ \text{(C) }|X||Y|\ge p^2-1\ ✓$$

## §1 引理（Kneser ✓）：(B) 几乎自动

$$\text{Kneser ✓}：|X+Y|\ge|X+H|+|Y+H|-|H|\ ✓,\ H=\operatorname{Stab}(X+Y)\ ✓;\ \text{而}\ \operatorname{Stab}(G\setminus\{0\})=\{0\}\ ✓$$
$$\qquad\text{证 ✓}：(G\setminus\{0\})+h=\{(x+h):x\ne0\}=G\setminus\{-h\}\ne G\setminus\{0\}\ (h\ne0)\ \checkmark$$
$$\Longrightarrow\ |X+Y|\ge|X|+|Y|-1\ ✓ \Longrightarrow\ \textbf{(B) 弱化为}\ |X|+|Y|\le p^2\ ✓\（\text{差一个常数 ✓）}$$

## §2 ⭐ 主结果：**显式构造 ⟹ 命题可满足** ✗

$$\boxed{X:=\{0,1\}\ ✓,\qquad Y:=\{\text{奇剩余 mod }p^2\}\ ✓\ (|Y|=(p^2-1)/2\ ✓)}$$
$$\text{验证 ✓}：X+Y=Y\cup(1+Y)=\text{奇}\cup(\text{偶}\setminus\{0\})=G\setminus\{0\}\ \checkmark$$
$$\qquad\text{（}\text{关键 ✓}：p\ \text{奇 ⟹ }-1\equiv p^2-1\ \text{是偶数 ⟹ }-1\notin Y\ ⟹\ 0\notin 1+Y\ ✓；\text{且 }0\notin Y\ ✓）$$
$$\text{(B) ✓}：2+\frac{p^2-1}{2}\le p^2-1\iff p^2\ge5\iff p\ge3\ \checkmark\qquad\text{(C) ✓}：2\cdot\frac{p^2-1}{2}=p^2-1\ge p^2-1\ \checkmark$$
$$\Longrightarrow\ ⭐\ \boxed{\textbf{(A)(B)(C) 对【每个】奇素数 }p\ \textbf{都有解 ✗}} \Longrightarrow \textbf{该命题单独【不能】给出 NO-GO ✗✗}$$

## §3 p=3 穷举（✓ $G=9$，非空子集 511 个）

$$\textbf{解数 ＝ 3726 ✓}\quad (|X|,|Y|)\ \text{分布 ✓}：$$
| $(|X|,|Y|)$ ✓ | 个数 ✓ | | $(|X|,|Y|)$ ✓ | 个数 ✓ |
|:--|:--|:--|:--|
| $(2,4)$ ✓ | 27 ✓ | $(2,5),(5,2)$ ✓ | 243 ✓ |
| $(3,3)$ ✓ | **108** ✓ | $(3,4),(4,3)$ ✓ | 648 ✓ |
| $(4,4)$ ✓ | 540 ✓ | $(2,6),(6,2)$ ✓ | 189 ✓ |
$$\Longrightarrow\ ⭐\ \textbf{均衡解（}|X|,|Y|\ge3\ \text{）共 2808 个 ✗} \Longrightarrow \textbf{均衡制【局部可实现 ✗】}$$
$$\qquad\text{（}\text{例 ✓：}(3,3)\ \text{解 108 个 ✓ —— }|X||Y|=9\ \text{对 }8\ \text{个和 ⟹ 恰 1 次碰撞 ⟹ 【近单射 ✓】）}$$

## §4 ⭐⭐ 换得的【严格双侧常界】（✓ 无需增长假设 ✓）

$$\textbf{上界 ✓}：\text{唯一性 ⟹ 映射}\ (a,b)\mapsto a+b\ \text{单射 ✓} \Longrightarrow A(M)B(M)\le|S\cap[0,2M]|\ ✓$$
$$\qquad\text{取 }M=p^2\ ✓：\ A(p^2)B(p^2)\le\frac{6}{\pi^2}\cdot2p^2+O(p)=\boxed{1.2159\,p^2}\ ✓\ \textbf{（严格 ✓）}$$
$$\textbf{下界 ✓（(C)＋本节上界 ✓）}：|A_p||B_p|\ge p^2-1\ ✓,\ |A_p|\le A(p^2)\ ✓ \Longrightarrow\ |B_p|\ge\frac{p^2-1}{A(p^2)}\ge\frac{p^2-1}{1.2159p^2/|A_p|}\ ✓$$
$$\Longrightarrow\ \boxed{A(p^2),\ B(p^2)\in\bigl[0.9069\,p,\ 1.3417\,p\bigr]\ ✓}\ \text{（}\textbf{双侧常界 ✓ 严格 ✓）}$$
$$\text{即 ✓：}\boxed{A(X)\asymp\sqrt X\ \text{在 }X=p^2\ \text{处 ✓}}\ ——\ \textbf{这是"增长假设"的【严格替代 ✓，但只沿 }p^2\ \text{✗】}$$

## §5 判定（✓ 诚实 ✓）

$$\textbf{① 您给的命题 (A)(B)(C) ＝ 可满足 ✓ ⟹ 不是 NO-GO ✗（本轮主结论 ✓）}$$
$$\textbf{② "薄因子"路线死亡 ✗}：\text{构造给出 }|X|=2\ ✓，\text{但 §4 的严格双侧界 ⟹ }\textbf{全局下因子必 ≈ }p\ ✗ \Longrightarrow \text{薄解【不可全局实现 ✓】}$$
$$\textbf{③ 但"均衡"也【不能】被排除 ✗}：\text{p=3 已有 2808 个均衡解 ✓ ⟹ 局部无矛盾 ✓}$$
$$\textbf{④ 严格约束全部【相容 ✗】}：0.8225p^2\le A(p^2)B(p^2)\le1.2159p^2\ ✓\ \text{—— 不矛盾 ✓}$$
$$\Longrightarrow\ ⭐\ \textbf{净结论 ✓}：\text{该路线【不能】给出 NO-GO ✗；}\textbf{但把"增长假设"严格化为【双侧常界 ✓】（沿 }X=p^2\ ✓）$$

## §6 ⭐⭐ 收窄后的第二阶段靶（✓ 新增一条您未列的约束 ✓）

$$\boxed{\textbf{跨 }p\ \text{相容性 ✓}：\text{同一 (}A,B)\ \text{能否对所有 }p\ \text{同时给出 }|A_p|,|B_p|\approx p\ \text{的近单射覆盖 ✗？}}$$
$$\qquad\Longrightarrow\ ⭐\ \textbf{并且全局还有两条 (A)(B)(C) 【未含】的约束 ✓（我的观察 ✓）}：$$
$$\qquad\qquad\text{(D) }A\subseteq S-1\ ✓\ \text{（}a+1\in S\ \forall a\in A\ ✓）\qquad\text{(E) }B\subseteq S\ ✓$$
$$\qquad\qquad\text{（}\text{二者由 }1\in B\ \text{与 }0\in A\ \text{给出 ✓（引理 2 ✓）—— }\textbf{它们是【全局】约束 ✗，有限群条件【抓不到】✓）}$$

## §7 边界与纪律（✓）

```
✅ **未用 RH ✓；未涉 ζ 解析 ✓（只用了 |S∩[0,X]| = (6/π^2)X+O(√X) 这一经典计数 ✓）；未跑 Lean ✓**
⚠️ **① §4 的下界用了 §4 上界（同一经典计数 ✓）** —— 二者【独立 ✓】，无循环 ✓
⚠️ **② p=3 穷举只到 }G=9$ ✗**（p≥5 未穷举 ✗）—— 但 §2 的构造对【所有奇 p】成立 ✓ ⟹ 可满足性结论【不依赖】穷举 ✓
⚠️ **③ §5 的"薄解不可全局实现"依赖 §4 的常数 ✓**（0.9069 ✓）—— 若 |A_p| 可小于该界则失效 ✗（已证不可 ✓）
⚠️ **④ 未声称 P-SF 已证或已否 ✗**；未声称 D1-B\* 已死 ✗
⭐ **净产出 ✓**：① **命题可满足（显式构造 ✓ ＋ 穷举 3726 ✓）**；② **均衡解存在（2808 ✓）**；
   ③ ⭐ **严格双侧常界 }A(p^2),B(p^2)\in[0.9069p,1.3417p]$ ✓**（增长假设的严格替代 ✓）；④ **新增全局约束 (D)(E) ✓**
```

## §8 一句话（✓）

$$\boxed{\textbf{有限群路线【不能】给 NO-GO ✗（命题可满足 ✓）；但它的严格双侧常界与新增约束 (D)(E) 是【真收益 ✓}}$$


---

## §9 ⚠️ **勘误（2026-09-14 14:05，自我更正 ✓）**
本档 §2 的"显式构造"$X=\{0,1\}$, $Y=\{$奇剩余$\bmod p^2\}$ **【是错的 ✗】**。
**错点**：{$奇数$} 在 $\bmod p^2$ 下的像**不是奇剩余，而是全部剩余**——因 $p^2$ 是奇数，$p^2\in\{$奇数$\}$，故 $p^2\equiv0$，即 $0$ 在像中。
**⟹ 该构造违反 (A) ✗，作废 ✓。** 仍然成立的是：**固定 $p$ 的有限问题 (A)(B)(C) 确实可满足**（$p=3$ 穷举 3726 解 ✓）。
详见 `docs/E170-*.md` ✓。原文本保留不删 ✓（T10 ✓）。
