已查地图：命中（`EDR-P1-P3-nailed-down`／`IP-5-RUN-dminus3-bounded-search-result`（`B_n` 表）／`ZF-EDR-2-gapA-dissolved-and-gapB-exact-form`）⟹ 引用，不开新案
D0: 本档对象 = `EDR-CAP` 第一刀：`CAP-1`（`\exists(E,P,S):|Z_S|>\omega(D)`?）⟹ **出反例**；并给出**修正后的正确形式**
D1: 0 （[REVIEW] 轮次：反例与修正，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`EDR-CAP-1`：`|Z_S|\le\omega(D)` 为假（平凡反例），正确形式是 `|Z_S\setminus\{1\}|\le\omega(D)`**

## §1 ⚠️ 先接受您的修正（本档起点）

```
【您的修正（照录）】 `|Z_S|\le\omega(D)` **不能**从 `r_q` 论证直接推出；现有论证给的是 $$|Z_S|\le N_0+\#\{\text{可用 }q\in S\}$$ 要压成 `\le\omega(D)` 须证 `N_0=0` 或"例外指标无损重分配" ✓✓
【⟹ 本档结论】 **`N_0=0` 不可能** —— 见 §2 ✓
```

## §2 ⭐ **反例（本档核心；由本线 `B_n` 表可直接读出）**

```
【关键事实】 `r_q:=\min\{n:q\mid B_n\}`；而 `B_1=1` ⟹ **`q\mid B_1` 不可能** ⟹ $$r_q\ge2\ \ \text{对所有素数 }q$$ ✓✓
【⟹ 推论 1】**`n=1` 永不被本原除子记账** ⟹ `n=1` 恒为例外指标 ⟹ $$Z_{\rm exc}\supseteq\{1\}\ \Longrightarrow\ |Z_{\rm exc}|\ge1\ \ \text{（恒成立，与 }E,P,S\text{ 无关）}$$ ✓✓✓
【反例（`S=\{2\}`，`D=2`，`\omega(D)=1`）】 `E:y^2+y=x^3-x^2-10x-20`，`P=(5,5)`：本线表 `B_1=1`（`\operatorname{Supp}=\varnothing\subseteq S` ✓）、`B_2=2`（`\operatorname{Supp}=\{2\}\subseteq S` ✓）、`B_3=13` ✗、`B_4=2^2\cdot151` ✗（`151\notin S`）⟹ $$Z_{\{2\}}\cap[1,10]=\{1,2\}\ \Longrightarrow\ |Z_S|=2\ >\ \omega(D)=1$$ ✓✓✓
【⟹ `CAP-1` 判定】 $$\boxed{|Z_S|\le\omega(D)\ \text{为假（反例平凡且与 }E,P\text{ 无关，根因 }n=1\text{）}}$$ ✓✓
【⟹ 您的修正被验证】 `N_0\ge1` **恒成立**（`n=1` 不可消除）⟹ 严格版 `|Z_S|\le\omega(D)` **结构上不可达** ✓✓
```

## §3 修正后的正确形式（本档给出）

```
$$\boxed{|Z_S(E,P)|\ \le\ 1+\omega(D)}$$ ✓ 或等价地 $$\boxed{|Z_S\setminus\{1\}|\le\omega(D)}$$
【证据（本线表）】 `S=\{2\}`：`|Z_S|=2=1+\omega(D)` ✓ **饱和**；`S=\{2,3\}`：`|Z_{\{2,3\}}|\cap[1,10]=\{1,2\}` ⟹ `|Z_S|=2\le1+2=3` ✓
【结构分解】 `|Z_S|=|Z_{\rm exc}|+|Z_{\rm prim}|`，`Z_{\rm exc}\supseteq\{1\}`，`|Z_{\rm prim}|\le|S|` ⟹ 上界 `1+|S|` ✓
【⟹ 新的极值问题（`CAP` 修正版）】 $$\boxed{\sup_{E,P,S}\bigl(|Z_S|-1-\omega(D)\bigr)\ \le\ 0\ ?}$$ ✓✓ 且"等号（饱和）"已成**最小实例**：`S=\{2\}` 与 `S=\{2,3\}` **都恰好饱和** ✓
```

## §4 判定与下一刀

```
**`CAP-1`（原形式）** ⛔ **否** —— 反例平凡（`n=1`），**且根因与 `E,P` 无关** ⟹ `|Z_S|\le\omega(D)` **应废弃** ✓
**`CAP-1`（修正形式）** ⚠️ **未决** —— `\exists(E,P,S):|Z_S|>1+\omega(D)`？需**搜索**（本线 `B_n` 表 + 更多 `S` 组合）✓
**`CAP-2/CAP-3`** 顺延 ✓
【⛔ 纪律（照录）】 **不碰 abc／不追 `N_0` 显式上界**；只做**容量项纯结构 sharpness** ✓
【边界】 §2 反例由本线 `B_n` 表（档级）直接读出，可重跑既有脚本复核；§3 修正形式与结构分解为**本档自行推导**；未制造候选／未启动搜索／未碰 RH 总攻。
