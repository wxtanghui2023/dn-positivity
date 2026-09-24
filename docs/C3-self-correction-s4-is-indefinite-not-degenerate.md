已查地图：命中（`C3-s4-is-the-definiteness-boundary`（**本档更正其 §2 假设**）／`C3-d1992-table-and-s4-audit-point`）⟹ 引用，不开新案
D0: 本档对象 = **自纠**：`s=4` **不是** Hermitian 临界退化点（`H_4` 为 **indefinite**，`\ker H_4=\{0\}`）⟹ "零空间攻击线"**CLOSED** ＋ 精化缺口链
D1: 0 （[REVIEW] 轮次：自纠与定界，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **自纠：`s=4` 是 indefinite，不是退化边界**

## §1 ⛔ 假设作废（本档自纠）

```
【上档（`4d367c0`）假设】 `s=2` PD → `s=3` PSD → **`s=4` 临界退化** → `s>4` indefinite ⟹ 零空间 → 高阶约束 ✓（**该假设已作废**）
【实测结论（唐先生一手计算，**档级**）】 $$\boxed{s=2:\ \text{PD},\quad s=3:\ \text{PSD},\quad s=4:\ \textbf{indefinite},\quad s>4:\ \text{indefinite}}$$ ✓✓ ⟹ **`s=4` 无零余量边界** ✓✓
```

## §2 数据（逐字）

```
**【系数（`p.109` 式 `(44)` 对应）】** $$c_{12}=c_{34}=c_{31}=e^{2\pi i/s},\qquad c_{23}=c_{24}=c_{41}=e^{-2\pi i/s}$$ ✓
**【代入 `s=4`（`c_4=i`）】** $$H_4=\begin{pmatrix}1&i&-i&i\\-i&1&-i&-i\\i&i&1&i\\-i&i&-i&1\end{pmatrix}$$ ✓
**【特征值（精确）】** $$-\sqrt2,\quad 2-\sqrt2,\quad \sqrt2,\quad 2+\sqrt2$$ ✓✓
**【⟹ 签名与核】** $$\operatorname{signature}(H_4)=(3,1,0),\qquad \ker H_4=\{0\},\qquad \det H_4=-4\neq0$$ ✓✓
```

## §3 本档所做的一致性自检（不越"不再在 `h(s=4)` 上计算"之令）

```
$$①\ \operatorname{tr}(H_4)=4\quad\overset{?}{=}\quad(-\sqrt2)+(2-\sqrt2)+\sqrt2+(2+\sqrt2)=4\ \checkmark$$ ✓
$$②\ \operatorname{tr}(H_4^2)=\sum_{i,j}|h_{ij}|^2=4\cdot1+12\cdot1=16\quad\overset{?}{=}\quad2+(2-\sqrt2)^2+2+(2+\sqrt2)^2=16\ \checkmark$$ ✓✓
【结论】**报告数据自洽**（`tr` 与 `tr(H^2)` 两独立检验均通过）；**本档未做完整特征值复算**（遵您"不要继续在 `h(s=4)` 上计算"）✓
```

## §4 ⛔ 后果：零空间攻击线 CLOSED

```
$$\boxed{\text{"固定维 Hermitian 临界退化}\to\text{零空间}\to\text{高阶约束"}\ \text{该线 CLOSED}}$$ ✓✓
【理由】 $$\ker H_4=\{0\},\quad n_-(H_4)=1$$ ⟹ **无零空间可挖，亦非 PSD** ✓
```

## §5 ⭐ 精化后的缺口链（照录）

```
$$\boxed{\begin{array}{c}P_4\ \text{universal}\\\downarrow\\ H_4\ \text{indefinite}\\\downarrow\\ \textbf{不能推出}\ P_4\ \text{infinite}\\\downarrow\\ 2010\ \text{有 finite quotient }(|G|=7680)\\\downarrow\\ \textbf{仍不能推出}\ P_4\ \text{finite}\end{array}}$$ ✓✓
【⟹ 新出现的精确子问题（仅登记，不计算）】 **"为何 `H` indefinite 不能推出 `P_s` infinite，而 `s\ge6` 却被证明 infinite？"** —— 答案应在 **`h` 与 `P_s` 的层次关系**（`h` 作用于 `\mathcal M(P_s)` 而非 `P_s`）⟹ **这正是 `§11E` 应说明的层次纪律** ✓✓
```

## §6 状态表与下一步

```
$$\begin{array}{c|c}
s=4\ \text{为 Hermitian PSD/零空间临界点}&\textbf{\times CLOSED}\ (\text{本案自纠})\\
H_4&\text{indefinite}\\
\operatorname{signature}(H_4)&(3,1,0)\\
\det H_4&-4\\
P_4\ \text{universal 是否 finite}&\textbf{仍需 }2002/\text{后续文献门审计}\\
2010\ \text{finite quotient}&\text{已知，不能解决 universal 层}\\
\end{array}$$ ✓
【门 1（决定性，不变）】**`2002\ §11E/§11H` 对 `P_4` 的最终处理** ⟹ 若已严格证 `P_4` infinite ⟹ **该点直接关闭**；若未 ⟹ **再判是否有别于 Hermitian-null 的新攻击接口** ✓✓
【⛔ 纪律】 **不在 `h(s=4)` 上继续计算**；**不计算、不实现**；`C2` 暂停 ✓
【边界】 §1–§2 为**您一手抽取/计算（档级）**；§3 为**本档一致性自检（算术级）**；§4–§6 为**本档判定**；未制造候选／未启动搜索／未碰 RH。

## §7 【技术词回查】（补录）
```
技术词 indefinite       命中文件数=18   :: ./V186-inertia-mechanism-audit-endpoint-degenerates-to-positivity.md ./E7-A3-2-bandwidth-check.md ./C3-self-correction-s4-is-indefinite-not-degenerate.md 
```
