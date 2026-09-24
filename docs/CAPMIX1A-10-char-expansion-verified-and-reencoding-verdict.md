已查地图：命中（`CAPMIX1A-9-degenerate-points-algebraic-closure`）⟹ 执行其 §6 之步骤②，不开新案
D0: 本档对象 = **`\lambda_{\rm raw}` 精确角色展开**（(2)/(5)/(6) 已验证）＋ ⛔**两处自纠**（① 定义写错已按您更正；② `\mathcal J_H` 压缩式有**未算净边界项**）＋ ⭐**判定：角色路线回落到同类 incidence 计数 ⟹ 重编码**
D1: 1 （延续新自由度；本档给出"Jacobi 闭式是否只是重编码"的**实测判定**）
[RESEARCH]

# **`CAP-MIX-1A(10)`：角色展开验证 ＋ 重编码判定**

## §1 ⛔ 自纠一（照您钉死）

```
**【我上档的错误】** 写成 $$\lambda_{\rm raw}=\#\{x\in G:\ x+1\in G\}$$ **仅在 `-1\in G`（`d` 偶）时等价** ✗
**【正确原始定义（本档全程采用）】** $$\boxed{\lambda_{\rm raw}=\#\{x\in G:\ -1-x\in G\}}$$ ✓
【原因】`-1-x\in-G` 与 `-1-x\in G` 仅在 `-1\in G` 时相同；`d` 奇时 `-G\ne G` ✓
```

## §2 ⭐ 您的精确闭式（本档数值验证通过）

```
$$\lambda_{\rm raw}=\frac1{m^2}\Big[\,q-2-3A_H+\mathcal J_H\,\Big],\qquad A_H=\sum_{\chi\in H^\times}\chi(-1)$$
$$\mathcal J_H=\sum_{\chi,\psi\in H^\times,\ \chi\psi\ne\varepsilon}\chi(-1)\psi(-1)J(\chi,\psi)$$
**【`A_H` 的两分支（照您 §8）】** $$A_H=\begin{cases}m-1,&-1\in G\ (d\ \text{偶})\\ -1,&-1\notin G\ (d\ \text{奇})\end{cases}$$ ✓
$$\Longrightarrow\ \boxed{\lambda_{\rm raw}=\frac{q-3m+1+\mathcal J_H}{m^2}\ (d\ \text{偶});\qquad \lambda_{\rm raw}=\frac{q+1+\mathcal J_H}{m^2}\ (d\ \text{奇})}$$ ✓✓
**【实测】** `branch_ok=204 / branch_bad=0` ✓ —— **⚠️ 但须诚实标注：此检查在形式上与 `\mathcal J_H` 的定义互为重述（非独立检验）** ✓
**【变量替换 (7) 复核】** $$\mathcal J_H=\sum_{\eta\in H^\times}\eta(-1)\,S_\eta,\qquad S_\eta=\sum_{\chi\in H^\times,\chi\ne\eta}J(\chi,\eta\chi^{-1}),\qquad \text{符号因子 }=\eta(-1)\ \text{（照您 §13）}$$ ✓✓（**验算通过**）
```

## §3 ⭐⭐ `S_\eta` 算到底：**它落回一个同类 incidence 计数**

```
**【把内层和交换回有限域（照您 §14 的路线）】**
$$S_\eta=\sum_{t\ne1}\eta(1-t)\sum_{\chi\in H^\times,\chi\ne\eta}\chi\!\left(\frac{t}{1-t}\right),\qquad \sum_{\chi\in H^\times,\chi\ne\eta}\chi(z)=m\cdot1_G(z)-1-\eta(z)$$ ✓
$$\Longrightarrow\ S_\eta=m\cdot\!\!\sum_{z\in G,\ z\ne-1}\!\!\eta\!\left(\frac1{1+z}\right)\ +\ (\text{常数项})$$ ✓（**其中常数项 = 我在 §4 未能算净的边界项**）
**【再外层对 `\eta` 求和】** $$\mathcal J_H\ \leadsto\ m^2\,N^\ast-m\cdot|G\setminus\{-1\}|+A_H,\qquad \boxed{N^\ast=\#\{z\in G:\ z\ne-1,\ -1/(1+z)\in G\}}$$ ✓✓
**【⟹ 关键观察（本档核心）】** `N^\ast` 与 `\lambda_{\rm raw}` **同为"平移/反演型 incidence 计数"**，且**实测抽样中 `N^\ast=\lambda_{\rm raw}`**：
$$(3,9,4):\ \lambda=1,N^\ast=1;\quad (3,27,13):\ 7,7;\quad (3,81,8):\ 7,7;\quad (3,81,4):\ 1,1;\quad (3,81,10):\ 1,1$$ ✓✓
$$\Longrightarrow\ \boxed{\text{角色/Jacobi 路线\textbf{回落到同一类计数}}\ \Longrightarrow\ \textbf{重编码，而非 }O(m)\ \text{闭式}}$$ ✓✓✓（**正是您要我"要么算穿、要么判死"的那一项：此处判"化不掉"**）
```

## §4 ⛔ 自纠二（`\mathcal J_H` 的压缩式有未算净边界项）

```
**【我推的压缩式】** $$\mathcal J_H\overset{?}{=}m^2N^\ast-m\,|G\setminus\{-1\}|+A_H$$ 
**【实测】** $$J_{\rm match}=14,\qquad J_{\rm mismatch}=190$$ ✗
**【偏差形态】** 偏差仅为 `\pm1` 或 `\pm(m-1)` ⟹ **边界项未算净**（候选来源：`z=-1` 排除项、`t=1` 的 `1-t=0`、`\eta(1)=1` 的 `\Sigma_{t\ne1}\eta(t)` 修正、以及 `z=0` 处的 `\chi(0)=0` 约定）✓
$$\Longrightarrow\ \textbf{须逐项重算 §3 的常数项（未完成）}$$ ⚠️
**【但不影响判定】** 偏差属**常数/`m` 级**，而 `N^\ast=\lambda_{\rm raw}` 的**类型同一性**已由抽样确立 ⟹ §3 的**重编码判定独立于该常数项** ✓✓
```

## §5 结论

```
$$(i)\ \textbf{退化修正 CLOSED};\qquad (ii)\ \textbf{精确角色展开 (2)/(5)/(6) 形式上正确（验证+重述）};\qquad (iii)\ \textbf{压缩判定}=\textbf{重编码}$$ ✓✓
$$\Longrightarrow\ \boxed{\text{“Jacobi 闭式 ⇒ 廉价 cap 证书” 判死}:\ \mathcal J_H\ \text{与 }\lambda_{\rm raw}\ \text{互相编码，无算法增益}}$$ ✓✓
$$\text{仍有价值的残留}:\ \text{if }\ N^\ast=\lambda_{\rm raw}\ \text{是\textbf{恒等式}},\ \text{则得到一个漂亮的\textbf{对合恒等式}}:\ -1-x\leftrightarrow-\tfrac1{1+x}\ (2\text{-次分式变换})$$ ✓
```

## §6 下一步

```
**(1)** 逐项重算 §3 常数项（**未完成**），并检验 `N^\ast=\lambda_{\rm raw}` 是否为**恒等式**（若是 ⟹ 分式变换下的对合不变量）✓✓
**(2)** 若 (1) 确认为恒等式 ⟹ 记录为**结构定理素材**（不是算法）；**不再在角色路线上求 `O(m)`** ✓
**(3)** 之后：`CAP-MIX-1B` char 2 四项版（**唯一未开的分支**）✓
【⛔ 纪律】 统一口径；计算仅本实验；`U_{2,3}` 暂停 ✓
【数据】 `out/capmix1N_charExpansion.txt`（204 行）；脚本 `scripts/capmix1N_charExpansion.py` ✓
【边界】 §2 的验证含**重述成分**（已标注）；§4 的边界项**未算净**（已登记）⚠️

## §附 【技术词回查】（补录）
```
技术词 Jacobi sum       命中文件数=2    :: ./CROSS-0-additive-multiplicative-cross-invariant-MAP-CHECK.md ./CAPMIX1A-9-degenerate-points-algebraic-closure.md 
技术词 involution       命中文件数=42   :: ./V106-L3-Q3-independent-sqrt-positivity-audit.md ./V175-level-theorem-local-factor-rigidity-bare-reflection.md ./p44-round2-mechanism-classes.md 
```
