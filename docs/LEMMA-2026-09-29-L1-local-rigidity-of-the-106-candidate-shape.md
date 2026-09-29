# LEMMA-2026-09-29-L1 — 106-候选形状的局部刚性：每个中点 ≥3 个"内部"距-2 码字

> 空间 B｜非 C 号｜S1′③ 首轮（唐先生令：先复现 107）｜**不主张 107**（V290）
> 依赖：`AUDIT-2026-09-29zg` §2 之形状（$M{=}106$、处处 $\mu\le2$、49 相邻匹配对 ＋ 22 距-2 对 ＋ 8 孤立词）
> 时间：2026-09-29 22:3x

**已查地图**：承 `ERRATUM-n1`／`ROUTE-…-107-ladder`（F1–F9）／`AUDIT-zg`
D0: 本档对象 = **档案已有**（$\mu$-场／$a_y$／距-2 对之双中点）之**局部化**（新数学对象：无 ✗）
D1: 0（产出 = 一条**条件引理** ⚠️✓）

---

## §0 引理（条件：处处 $\mu\le2$）

$$\textbf{L1}:\quad \text{设 }\{u',v'\}\ \text{为距-2 对},\ m\ \text{为其一中点}\ (m\notin C,\ \mu(m){=}2).\ \text{令}\ J_m:=[10]\setminus\{a,b\}\ \text{为除两对端方向外之 8 个方向}$$
$$\boxed{\text{则}\ m\ \text{的 8 个"自由点"}\ m\oplus e_j\ (j\in J_m)\ \text{中},\ \textbf{至少 6 个}\ \text{由\ \textbf{距 }m\ \text{恰为 2 且两支方向皆在}\ J_m\ \text{之码字}\ \text{覆盖}}$$
$$\Longrightarrow\ \text{每个中点至少对应}\ \mathbf 3\ \text{个此类"内部"码字}\ \Longrightarrow\ \Sigma_{\text{中点}}\ \ge\ 44\times3=\mathbf{132}\ \text{个（中点, 内部码字）关联}$$

## §1 证明（三步，皆初等）

$$\textbf{(i) 距离限制}:\ \text{覆盖}\ m\oplus e_j\ \text{之码字}\ c\ \text{须}\ d(c,m)\le2;\ \text{而}\ d(c,m){=}1\Rightarrow c\ \text{亦覆盖}\ m\Rightarrow\mu(m)\ge3\ ✗$$
$$\qquad\therefore\ d(c,m)=\mathbf2,\ \text{即}\ c=m\oplus e_p\oplus e_q\ (p\ne q)$$

$$\textbf{(ii) 方向限制（上界 2）}:\ \text{若}\ p{=}a\ (\text{或}\ b)\ \Longrightarrow\ c=m\oplus e_a\oplus e_q\ \Longrightarrow\ d(c,u'){=}1\ \Longrightarrow\ c\ \text{与}\ u'\ \textbf{相邻}$$
$$\qquad\text{而}\ \mu(u')\le2\Rightarrow a_{u'}\le1\ \Longrightarrow\ u'\ \text{至多一个距-1 邻}\ \Longrightarrow\ \text{此情形对}\ u'\ \text{至多 1 次};\ \text{同理}\ v'$$
$$\qquad\text{且此类}\ c\ \text{恰覆盖}\ m\ \text{的}\ \mathbf 1\ \text{个自由点}\ (m\oplus e_q)\ \Longrightarrow\ \text{至多 2 个自由点靠"附着"码字}$$

$$\textbf{(iii) 内部}:\ \text{余下}\ \ge6\ \text{个自由点须由}\ p,q\in J_m\ \text{之码字覆盖；此类码字恰覆盖 2 个自由点}\ \Longrightarrow\ \ge3\ \text{个内部码字}\ \blacksquare$$

## §2 读数与现状

- **L1 是严格的**（条件仅"处处 $\mu\le2$"，即 `AUDIT-zg` §2 形状）
- **但尚未得矛盾** ⚠️：需再对 $\Sigma_c\#\{m:\ c\ \text{为}\ m\ \text{之内部码字}\}$ 给出**上界**（$c$ 距-2 之点至多 45 个 ⟹ 现只能给平凡界）
- **经验支持**：真实码远离该形状（120-码 $\mu_{\max}{=}5$、62-码 $\mu_{\max}{=}4$）⟹ 形状"不自然"，其不可实现性或来自全局覆盖几何 ⚠️

## §3 下一步（S1′③ 续）

- **(α)** 给"内部码字"计数加上**上界**：内部码字 $c=m\oplus e_p\oplus e_q$ 与 $m$ 之对端 $u',v'$ 距离 3 ⟹ 其"归属"受限于几何
- **(β)** 反向：设处处 $\mu\le2$ 不可能（即证 $\mu_{\max}\ge3$ 于 $M{=}106$），再迭代 $\mu_{\max}\ge4$ —— 这与 `ERRATUM-n1` 撤回的旧推论**名字相同、论证不同**，须严格区分 ⚠️✓
- **(γ)** 若 (α)(β) 皆不成，则须换层（$A_2$ 之几何上界／混合框架）

## §4 边界（硬 ✓）

- L1 为**条件**引理，不得当作"$M{=}106$ 不可能"之证据 ✗✓
- 未重攻 pair 层（R02）／未取论文原文（R16–17）✓；**不主张 105/106/107 中任何新值** ✗

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=NA R06=NA R07=NA R08=NA R09=NA R10=NA R11=NA R12=NA R13=NA R14=NA R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA

---

## §5 附带加强（✓ 由 `AUDIT-zg` 形状直接推出）

$$\text{在该形状下，非码字之 }\mu{=}2\ \text{点}\ \textbf{恰为}\ 44\ \text{个距-2 中点}\ (\text{其余非码字点}\ \mu{=}1)$$
$$\text{而自由点}\ m\oplus e_j\ \text{皆}\ \textbf{非码字}\ (\text{否则其覆盖 }m\Rightarrow\mu(m)\ge3 ✗)\ \Longrightarrow\ \mu(m\oplus e_j)=\mathbf1$$
$$\therefore\ \boxed{\text{每个自由点\ \textbf{私有}（唯一覆盖者）}} \Longrightarrow\ \text{其覆盖者\ \textbf{互不相同}};\ \text{8 个自由点之覆盖者集合}\ =\ \text{内部(2 个/词)}+\text{附着(1 个/词)}$$
$$\Longrightarrow\ \text{每中点之覆盖者数}\in[4,8],\ \text{内部词}\ge3\ \text{（与 L1 相容，且更强：\textbf{无重复})}\ ✓$$
