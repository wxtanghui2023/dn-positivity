已查地图：命中（`C3-step5-candidates-and-its-structural-ceiling`／`C3-nontriviality-resolved-by-dart-counting`）⟹ 引用，不开新案
D0: 本档对象 = **`⑤` 收口为 FAIL** ＋ **永久剔除伪引理 `uvu=vu`** ＋ ⭐**`Bridge-C-1:[a,b^2c]=1`（本档代数验证）** ＋ `T_R=[b,c^{-1}]` ＋ presentation 压缩
D1: 0 （[REVIEW] 轮次：关系推导与验证，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`Bridge-C-1` 验证 ＋ `⑤` 收口**

## §1 `⑤` 收口（照录）

```
六个候选 `x_1,\ldots,x_6`（`T_LT_R` 幂与交错）**均未**得到 $$x\in\Gamma_{012}\cap\Gamma_{123},\ x\notin\Gamma_{12}$$ ✓
$$\boxed{⑤:\ \text{HAND-CANDIDATE FAMILY FAILED TO PRODUCE G4}}$$ ✓ ⟹ **不得升级为 CLOSED** ✓
**【永久剔除】** 伪引理 $$uvu=vu\ (\text{对合 }u,v)\ \textbf{永久移除}$$ ✓✓（`S_3` 反例；错因＝把蕴含方向当恒等式）✓；**A–E 保留** ✓
```

## §2 ⭐⭐ `Bridge-C-1`：`[a,b^2c]=1`（本档逐步代数验证）

```
**【步 1（`A`）】** `(ab)^2=1\Longrightarrow ab=b^{-1}a^{-1}\ \xrightarrow{\text{左乘 }b}\ \boxed{bab=a^{-1}}$$ ✓（纯代数，无需计算）
**【步 2（`B`）】** `(abc)^2=1\Longrightarrow abc=c^{-1}b^{-1}a^{-1}\ \xrightarrow{\text{左乘 }bc}\ bcabc=a^{-1}\ \xrightarrow{(bc)^2=1}\ \boxed{(bc)a(bc)=a^{-1}}$$ ✓
**【步 3（比较 `A`,`B`）】** $$bab=(bc)a(bc)$$ ✓
**【步 4】** 左乘 `b`：$$ab=b^2c\,a\,bc$$ ✓；右乘 `bc`（并 `(bc)^2=1`）：$$a b^2 c=b^2 c\,a$$ ✓✓
$$\boxed{[a,\ b^2c]=1}$$ ✓✓✓ —— **验证通过（仅用 `(ab)^2=(bc)^2=1` 与 `bab=a^{-1}`）** ✓✓
```

## §3 ⭐ `T_R=[b,c^{-1}]`（本档验证）

```
$$T_R=b^2c^{-1}=b^2c^2\ \xrightarrow{\,bc=c^{-1}b^{-1}\,}\ b\,(c^{-1}b^{-1})\,c=bc^{-1}b^{-1}c=[b,c^{-1}]$$ ✓✓（约定 `[x,y]=xyx^{-1}y^{-1}`）✓
```

## §4 presentation 压缩（照录）

```
$$\boxed{a^3=b^6=c^3=1,\quad (ab)^2=(bc)^2=(abc)^2=1,\quad (b^2a^{-1})^2=1,\quad (b^2c^{-1})^3=1}$$ ✓
```

## §5 ⭐ 桥关系的意义（照录）

```
原本 `\Gamma_{012}=\langle a,b\rangle` 与 `\Gamma_{123}=\langle b,c\rangle` **只通过 `b` 接触**；`Bridge-C-1` 给出 $$a\ \longleftrightarrow\ b^2c\ (\in\Gamma_{123})$$ 的**直接耦合** ⟹ **首次得到"左侧生成元与右侧非平凡元素直接交换"** ✓✓
【⟹ 这比继续算 `x_1,\ldots,x_6` 有价值】 ✓
```

## §6 下一刀（照录，待执行）

```
**【局部问题】** 在 `[a,b^2c]=1`、`T_R=b^2c^{-1}`、`T_R^3=1` 下，寻找 `a` 与 `T_R` 的**有限阶耦合** ✓
**【逐个算】** $$aT_Ra^{-1},\quad aT_R^2a^{-1},\quad T_RaT_R^{-1},\quad T_R^2aT_R^{-2}$$ ✓
**【判据】** 若能压成 `b^k`、或**只含 `b,c` 的字**／**只含 `a,b` 的字** ⟹ 一旦同一元素既有 `ab`-表示又有 `bc`-表示 ⟹ **真正的 intersection candidate** ✓✓
**【目标形态】** $$x\in\Gamma_{012}\cap\Gamma_{123}\ \text{且}\ x\notin\Gamma_{12}$$ ✓
【⛔ 纪律】 **暂不解禁 `B`**（不用 Todd–Coxeter／不做低长度枚举）✓；**未得证书时只写"未产生证书"** ✓
【⛔ 边界】 §2–§3 为**本档代数验证**（可手验）；§4–§6 为**照录**；`U_{2,3}` 仍 **OPEN**；未制造候选／未启动搜索／未碰 RH。

## §7 【技术词回查】（补录）
```
技术词 commutator       命中文件数=27   :: ./rct-four-layer-final.md ./O3-mechanism-audit-and-ontology.md ./theorem-status-audit.md 
技术词 bridge relation  命中文件数=0    :: 
```
