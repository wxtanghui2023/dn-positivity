# A23-D4 Certificate Package

**题目**：2969-word incumbent `a23.6.10.2969H` 在删除深度 ≤ 4 下的局部最优性
（finite, deterministic, solver-free certificate）

---

## 1. 定理

> **Theorem (A23-D4).**
> 设 $C_0$ 为归档的 2969-word $(23,6,10)$ 常权码（文件 `a23.6.10.2969H.txt`）。
> 则不存在 $(D,S)$ 满足
> $$D\subseteq C_0,\quad |D|\le 4,\quad S\ \text{为重量-10 二进制词集},$$
> 使得 $(C_0\setminus D)\cup S$ 仍是合法 $(23,6,10)$ 码（两两距离 $\ge6$）、非重码，且
> $$|S|>|D|.$$
> 等价地：$C_0$ 是 **4-deletion local optimum**。

**范围声明（必须保留）**

- 本定理**不是** $A(23,6,10)$ 的上下界结果 ✗（2970 < 2979 < 2981，他方已构造 2979/2981）
- 本定理**限于** $|D|\le4$ ✓；$|D|\ge5$ 未触及
- 本定理**补上论文**（arXiv:2607.19550）明确标注为 *unresolved open problem* 的 depth-4 情形 ✓

---

## 2. 关键机制

对候选 $s$（重量-10，$s\notin C_0$）定义 **blocker 集**
$$B(s)=\{c\in C_0:\ |s\cap c|\ge 8\}.$$

由 $(23,6,10)$ 条件，$d(s,c)\ge6\iff|s\cap c|\le 7$，故
$$s\ \text{与}\ C_0\setminus D\ \text{相容}\iff B(s)\subseteq D.$$

因此一次删除 $D$、新增 $S$ 的交换合法，当且仅当
$$S\subseteq S(D):=\{s:|s|=10,\ s\notin C_0,\ B(s)\subseteq D\}$$
且 $S$ 内两两 $|s\cap s'|\le7$。

于是
$$\text{depth-}4\ \text{正交换存在}\iff \exists D,\ |D|=4:\ \alpha(H_D)\ge5$$
其中 $H_D$ 的顶点为 $S(D)$、边为 $|s\cap s'|\ge8$。

**结论**：全部 $|S(D)|\ge5$ 的 $D$ 上 $\alpha(H_D)\le4$ ⟹ 不存在正交换。

---

## 3. 文件清单

| 文件 | 角色 | 状态 |
|---|---|---|
| `a23.6.10.2969H.txt` | **输入**：公开码表 `aeb.win.tue.nl/codes/cwc/d6/a23.6.10.2969H`（`$BASE=16`，2969 行） | ✓ |
| `a23_d4_state_table.tsv` | **certificate 核心**：14,671 行 = 全部 $|S(D)|\ge5$ 的 $D$，列为 `c1 c2 c3 c4 \| n1 n2 n3 n4 \| |S(D)| \| alpha` | ✓ |
| `verify_d4.py` | **独立校验器**（V1–V4；不 import step6；不读任何前次中间对象） | ✓ |
| `a23_d4_verification_summary.txt` | 机器可读校验输出 ＋ 双 SHA-256 指纹 | ✓ |
| `a23_d4_verification_log.txt` | 校验器完整运行日志 | ✓ |
| `step6.py` | **主枚举器**（族 A∪B∪C'∪D 四族穷尽） | ✓ 有效 |
| `step7_patch.py` | **完备性补丁**（三元组 $SD(T)\ge5$ 情形） | ✓ 有效 |
| `step2n.py` / `step5.py` | 中间阶段（blocker census 验证 / 早期部分枚举） | ✓ 参考 |
| `step2.py` / `step3.py` / `step4.py` / `step4b.py` | **已废弃**：含语法错误或口径错误（族 C 条件写错） | ✗ 仅供留痕 |

---

## 4. 校验接口（V1–V4）

```
V1  C0 integrity : |C0|=2969, wt=10, d_min=6, 互异
V2  blocker cert : 生成式算法（C0 侧枚举 |s∩c|=8 与 |s∩c|=9 关联）
                   → N0=0, N1=70, N2=1178, N3=6503, N4=22496
                   → N≤2=1248, N≤3=7751, N≤4=30247
V3  alpha verifier: 对 certificate 每行独立重算 S(D)，并用 2^{|S(D)|} ≤ 64 子集穷举求 α
V4  summary      : 机器可读输出 + SHA-256 指纹
```

**独立性措施**（相对主枚举器）

1. blocker 关联用**生成式**算法（从 $C_0$ 侧生成关系，10,807,160 条），与主枚举器的"扫候选 × 全 $C_0$"算法不同；
2. popcount 用 CPython `int.bit_count()`（原生），不用主枚举器的 numpy 字节查表；
3. $\alpha$ 用 $2^{|S|}$ 子集穷举，**不调用任何 solver / 优化器 / 图库**；
4. 不 import `step6.py`，不读取任何前次程序的中间对象。

---

## 5. 运行

```bash
# 依赖: Python 3.10+ (int.bit_count), 标准库即可
python3 verify_d4.py          # 约 2-3 分钟
```

**复现要求**：工作目录须包含 `a23.6.10.2969H.txt` 与 `a23_d4_state_table.tsv`；脚本内 `BASE` 常量需指向该目录。

---

## 6. 指纹（2026-09-26）

```
sha256(C0)          = f2cc5595ae9e788b1e706b2bc1dfa97d9f16f3fa43c0a4a0f453aaf4e3ed09cd
sha256(state-table) = 7de3407d6ee5658816e5d3d19cb02dbf0b1056199709e18d24f4a07dbbe0e8b4
```

**校验结论**

```
surviving_D_states = 14671
max_S_size = 6
max_alpha = 4
alpha: 1→13, 2→746, 3→6787, 4→7125
DEPTH4_LOCAL_OPTIMUM = TRUE
```

---

## 7. 未闭合 / 未主张

- $|D|\ge5$：未触及 ✗
- $A(23,6,10)$ 的全局上下界：未主张 ✗
- 把"14,671 状态枚举"压缩成有限禁形（结构定理化）：**未做**（台阶 2）
- 推广到 $A(n,6,w)$ 的一般机制：**未开始**（台阶 3）

---

## 8. 留痕：两处自身错误（供审计）

1. **枚举覆盖缺口**：早期版本族 C 条件写作 `if A[0] in B`（只覆盖共享元素的 2-组），漏掉**不相交** $2+2$；
   修正后新增覆盖 **664,922** 个 $D$（族 C'）。⟹ 最终 enumeration 不是"跑完即信"，而是经过明确的 coverage correction。
2. **独立校验器首版 bug**：生成式算法只生成 $|s\cap c|=8$ 的关联，**漏掉 $|s\cap c|=9$**，
   导致 $N_1$ 报 757（真值 70）✗；补上 9-交集生成后全部 PASS ✓。
   （主枚举器的 blocker 定义始终正确——它与论文三项基准 1248/7751/30247 逐数字对齐。）
