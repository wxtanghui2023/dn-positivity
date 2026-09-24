已查地图：命中（`M03-3b-power-sum-necessary-condition-extends-W`）⟹ `D2` 精确包含检验与判定，不开新案
D0: 本档对象 = **`D2` 精确集合包含检验**：`W_{\rm PS}` 映到 `Loewy Example 3.2` 的 `(a,b)` 坐标并逐点比较 ＋ ⭐**四项精确对应**（`LS=\Lambda(t)`；`W_3=t_*`；`JMP=`我方 Johnson 墙；`v=D_{\rm PS}`）＋ **判定：机制扩张 ✓／区域扩张 ✗** ＋ **地图修正副产品**（`R\setminus W\ne` 未知区）
D1: 1（首次把条带结果与 Loewy 2021 的区域做精确包含判定；产出 R∖W 与真未知区的分离）
[RESEARCH]

# **`D2` 判定：机制扩张，非区域扩张（附地图修正）**

## §1 坐标映射与原文（ELA 37, pp.1–13, 2021-01；已入档）

```
$$\textbf{原文}\ \Longrightarrow\ \texttt{sources/Loewy-2021-additional-notes-spectra-nonneg-symmetric-5x5.pdf}\ (13\ \text{页})$$ ✓
$$\text{本行族 }(1,t,t,-(q+\varepsilon),-(q+\varepsilon))\ \textbf{就是}\ \text{Example 3.2 的两参数族}\ (1,a,a,b,b):\ \boxed{a=t,\ b=-(q+\varepsilon),\ 1\ge a>0>b\ge-1}$$ ✓✓
$$s_1=S=1+2a+2b;\qquad y=\lambda_3-s_1=-1-a-2b\ge0\iff1+a+2b\le0\ (\textbf{MN 条件})$$ ✓✓
$$

## §2 ⭐ 四项精确对应（两套记号完全同构）

```
$$\textbf{(i)}\ \text{Loewy 的 }LS\ \text{曲线}\ 5+2b-7a=0\iff b=\frac{7a-5}{2}=-q(t)\ \Longrightarrow\ \boxed{LS\ \textbf{就是本行边界族 }\Lambda(t)}$$ ✓✓✓
$$\textbf{(ii)}\ \text{Loewy 的 }W_3=(0.479159\cdots,-0.822941\cdots)\ \textbf{恰为我方 }t_*=0.479159524723\ \text{点}$$ ✓✓✓（`LS∩JMP`）
$$\textbf{(iii)}\ \text{Loewy 的 }JMP\ \text{条件}\ u(a,b):=1+a^3+2b^3-(1+a+2b)^3\ \textbf{就是} 2026\ \text{前的 Johnson 墙}$$ ✓✓✓
$$\qquad \text{在本行族}: u(t,\varepsilon)=-\tfrac34\bigl[-8\varepsilon^3+100\varepsilon^2t-44\varepsilon^2-414\varepsilon t^2+372\varepsilon t-78\varepsilon+\boxed{567t^3-779t^2+337t-45}\bigr]$$
$$\qquad \Longrightarrow\ u(t,0)=-\tfrac34P(t),\ P(t)=567t^3-779t^2+337t-45\ \Longrightarrow\ \textbf{JMP 与 }LS\ \text{恰交于 }t=t_*$$ ✓✓✓（与 (ii) 自洽）
$$\textbf{(iv)}\ \text{Loewy 的 }v(a,b):=s_3-s_1^3-6s_1y(s_1+y)=6(a^3-b^3+2a^2b+a^2-2b^2-b)\ \textbf{就是本行 }D_{\rm PS}$$ ✓✓✓
$$\qquad \text{在本行族}: v(t,\varepsilon)=-\tfrac34(-2\varepsilon+9t-3)(4\varepsilon^2-24t\varepsilon+16\varepsilon+31t^2-46t+15)\ \textbf{逐字一致}$$ ✓✓✓
$$\qquad \text{且原文已证}\ \frac{\partial v}{\partial b}>0\ \text{in }D \Longrightarrow v<0\iff \text{位于 }LO\ \text{曲线之下}$$ ✓✓
```

## §3 `W_PS` 的分裂（按 `u` 的符号）

```
$$W_{\rm PS}=\{\varepsilon\in(\varepsilon_2(t),0)\}\ (\text{条带上半});\quad u\ \text{在 }\varepsilon\ \text{上\textbf{递减}}\ \Longrightarrow\ \exists\ \varepsilon_{\rm JMP}(t)\in(\varepsilon_2(t),0)\ \text{使 }u=0$$ ✓✓
$$\Longrightarrow\ \boxed{W_{\rm PS}=\underbrace{\{\varepsilon\in(\varepsilon_2,\varepsilon_{\rm JMP})\}}_{\textbf{Loewy }v\ \textbf{排除}\ (v<0,\ u>0)} \ \cup\ \underbrace{\{\varepsilon\in(\varepsilon_{\rm JMP},0)\}}_{\textbf{JMP }u\ \textbf{排除}\ (u<0)}}$$ ✓✓✓
$$\text{逐点核验（示例）}:\ t=0.45:\ \varepsilon=-0.01\Rightarrow v=-0.422<0,\ u=-0.386<0\ (\text{JMP});\quad \varepsilon=-0.1226\Rightarrow v=0,\ u=+0.062;$$
$$\qquad t=0.48:\ \varepsilon=-0.0141\Rightarrow v=0,\ u=+0.066;\quad \varepsilon=-0.01\Rightarrow v=-0.018<0,\ u=+0.050>0\ (\textbf{Loewy }v)$$ ✓✓
$$\Longrightarrow\ \boxed{W_{\rm PS}\subseteq(\text{JMP-已排除}\cup\text{Loewy-}v\text{-已排除})}\quad\Longrightarrow\ \boxed{\textbf{区域扩张}\ \times}\ (\text{两项均 }2021\ \text{前已知})$$ ✓✓✓
$$

## §4 判定（先生三分法 → 选项 1）

```
$$\boxed{\text{机制扩张}\ \checkmark}\ (\text{幂和／迹机制独立于 high-trace};\ \textbf{非"同墙重复"})$$ ✓✓
$$\boxed{\text{区域扩张}\ \times}\ (\text{完全包含于已证非实现区};\ \text{不是 2026 新不可行薄片})$$ ✓✓
$$\text{故 }(3b)\ \text{的定位}:\ \text{把 Loewy 2021 的必要条件\textbf{拉回本参数化}, 并解析化其与 }W\ \text{的交界 }\varepsilon_2(t)$$ ✓✓
```

## §5 ⭐ 真正的副产品：**地图修正**（本条最有价值）

```
$$\text{2026 原文 Remark 2.2 称未覆盖区}=\ R,\ \text{且 }R\setminus W="\text{potentially realizable}"$$ ⚠️
$$\text{但本档证明}:\ R\setminus W\ \text{的条带上半 }(\varepsilon_2(t),0)\ \textbf{在 2026 之前已被排除}（Loewy 2021 的 }v\ \text{或 }JMP\ \text{的 }u\text{）$$ ✓✓✓
$$\Longrightarrow\ \boxed{R\setminus W\ \supsetneq\ \text{真正未知区}};\quad \text{条带内真未知区}=\Bigl\{\varepsilon\in(4t-2,\ \varepsilon_2(t))\Bigr\}\ (t\in(\tfrac49,\tfrac{15}{31}))$$ ✓✓✓
$$\text{（该夹缝内}: v>0\ (\text{未被 Loewy 排除}),\ u>0\ (\text{未被 JMP 排除}),\ \text{且 2026 机制余量 }\varepsilon/18<0,\ \text{Soules-1 已排除）}$$ ✓✓
$$\textbf{地图修正措辞（可引）}:\ \text{"2026 的 }W\ \text{是新区域，但其补集 }R\setminus W\ \text{并非全为未知区；}$ W_{\rm PS}\ \text{型薄片早在 2021 年即被幂和／JMP 机制排除"}$$ ✓✓
```

## §6 下一步

```
$$\boxed{\text{(a)}}\ \text{把 }R\setminus W\ \text{与真未知区的分离登记为\textbf{地图资产}（本档已完成）}$$ ✓
$$\boxed{\text{(b)}}\ \text{真未知夹缝 }(4t-2,\varepsilon_2(t))\ \text{内继续找\textbf{与 high-trace 无关}的机制}: s_5\ \text{型／更高阶幂和／}S\text{-型必要条件}$$ ✓✓
$$\boxed{\text{(c)}}\ \text{或改为 }P2:\ \text{在夹缝内尝试构造（换机制）};\ \text{成功即 }\Lambda\ \text{类谱的可实现新点}$$ ✓✓
【⛔ 纪律】 本轮为**原文实读＋精确计算**（无搜索）；`U_{2,3}` 暂停；**不回 RH** ✓
【边界】 §2 四项对应为**双向核验**（两套记号逐式相等）；§3/§5 为本行自证；【技术词回查】见 §附 ✓

## §附 【技术词回查】（补录）
```
技术词 inclusion test   命中文件数=0    :: 
技术词 map correction   命中文件数=0    :: 
```
