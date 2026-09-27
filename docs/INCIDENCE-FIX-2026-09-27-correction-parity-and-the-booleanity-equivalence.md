已查地图：已跑 scripts/prework_map_check.sh 满秩 单射 T 可逆 Booleanity ⟹ 修订自 `INCIDENCE-2026-09-27-...`（本档 = 纠错 ✓）＋ 核档案 Fourier audit（`ec8d20d`："Booleanity 步 ⟺ 原问题（坐标变换而非松弛）" ✓）；本档 = **修正 §② 论证 ✗ ＋ 校正定理（含 n 奇偶 ✓）＋ Booleanity Gate 的等价性判定 ✓**。
D0: 本档对象 = (JB-1) 之论证修正与 Booleanity Gate 之可松弛性
D1: 3（**接受纠错 ✓（论证跳跃）**；**校正定理：T 可逆 ⟺ n 偶 ⟹ C↦b 单射 ✓✓**；**Booleanity Gate = 可证等价（非松弛）⟹ 该形状封口 ✓**）

# Incidence 修正与 Booleanity 等价性（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(KA-1 ✅接受纠错（唐先生 ✓）)}\ \text{我原 §② 的\textbf{论证}是跳跃 ✗}:\ A_C=T P_C\ \text{满列秩只给\textbf{固定 }C\ \text{内部}的单射 ✓;\ \text{反解 }\mathbf 1_C=(A_C^{\mathsf T}A_C)^{-1}A_C^{\mathsf T}b\ \textbf{必须先知道 }C\ \text{本身} ✗✓}$$
$$\qquad\text{抽象反例（唐先生 ✓，一般情形成立 ✓）}:\ A{=}I,\ B{=}\begin{pmatrix}0&1\\1&0\end{pmatrix}\ \text{皆满列秩但 }A(1,0)^{\mathsf T}=B(0,1)^{\mathsf T}\ ✗ \Longrightarrow \text{"矩阵族各自满秩"}\not\Rightarrow\text{"像集互不相交"}\ ✓✓$$
$$\boxed{\textbf{(KB-1 ⭐⭐校正定理（结论仍成立，理由改为 }T\text{ ✓）)}\ T=I+\sum_{i=1}^n\sigma_i\ \text{的谱}=\{n+1-2w\}_{w=0}^{n}\ \Longrightarrow\ \boxed{0\in\sigma(T)\iff n\ \text{奇}}\ ✓\ \text{（}n=10:\ \{11,\dots,-9\}\ \text{无零 ✓）}}$$
$$\qquad\Longrightarrow\ n\ \text{偶}:\ \boxed{\mathbf 1_C=T^{-1}b}\ ✓\ \text{（\textbf{唐先生原式 ✓}）} \Longrightarrow\ \boxed{\text{映射 }C\mapsto b=T\mathbf 1_C\ \textbf{单射}（n\ \text{偶 ✓）}}\ ✓✓\ \text{—— \textbf{且与 }A_C\ \text{无关、与 }|C|\ \text{无关 ✓}}$$
$$\qquad\textbf{必要性 ✓}:\ n\ \text{奇时 }T\ \text{奇异 ⟹ 可塌};\ n{=}1:\ T=\begin{pmatrix}1&1\\1&1\end{pmatrix},\ \mathbf 1_{\{0\}}\ \text{与}\ \mathbf 1_{\{1\}}\ \text{同像 ✗✓}（\text{故"偶"不可去 ✓）$$
$$\qquad\textbf{净效果 ✓}:\ \text{校正后的定理\textbf{更强}（不用 }A_C\ \text{满秩、不用 }M=119 ✓），且\M 原论证（经 }A_C\text{）应\textbf{删去} ✗}$$
$$\boxed{\textbf{(KC-1 🔴Booleanity Gate = 可证等价（不是松弛）)}\ \text{因 }T^{-1}\ \text{是 }\mathbb R^{1024}\ \text{上的\textbf{双射} ⟹ 约束集} \{\,b:\ T^{-1}b\in\{0,1\}^{1024}\ \wedge\ \sum =119\,\}\ \textbf{恰是} \{\,T\mathbf 1_C\,\}\ \text{的像集本身 ✓}}$$
$$\qquad\Longrightarrow\ \boxed{\text{"}b\ \text{可实现"} \iff T^{-1}b\in\{0,1\}^{1024}\ \text{—— \textbf{与原问题逐字等价}，无松弛 ✗✓}}\ \text{（与档案 Fourier audit 判定逐字一致 ✓："坐标变换而非松弛" ✓）}$$
$$\qquad\textbf{Walsh 形 ✓}:\ \widehat f(\chi)=\widehat b(\chi)/(11-2|\chi|)\ ✓;\ \text{Booleanity 的等价二阶形}:f^2=f \iff \widehat b(\chi)=\tfrac{1}{1024}\sum_\psi\tfrac{\widehat b(\psi)\widehat b(\chi+\psi)}{(11-2|\psi|)(11-2|\chi+\psi|)}\ (11-2|\chi|)\ ✓$$
$$\qquad\textbf{其自然松弛皆已在档 ✗}:\ \text{(i) }0\le f\le1\ (\text{M-1 BQP-lift})\ ⟹ \text{CIRCULAR ✗};\ \text{(ii) 能量 }{}\sum f^2=\sum f\ (\text{Parseval})\ \text{只含 profile 信息 ✗};\ \text{(iii) 线性/谱 Delsarte ⟹ CLOSED ✗}$$
$$
$$
```

## §1 判定（**✓**）

```
$$\textbf{对唐先生提案 ✓}:\ \text{"Booleanity Gate 能否给出 profile 之外的必要条件" —— \textbf{可证否定} ✗（KC-1：因 }T^{-1}\ \text{双射 ⟹ 逐字等价 ⟹ 不存在"松弛"}）}$$
$$\qquad\textbf{但\textbf{诚实的净收益 ✓}（值得留档 ✓）}:\ \text{本档把 119 的难点\textbf{定式化}成} \boxed{b\ge1,\ \sum b=1309,\ T^{-1}b\in\{0,1\}^{1024},\ \sum T^{-1}b=119}\ \text{—— \textbf{定理级精确}（先前是口语表述 ✓）}$$
$$\qquad\textbf{真正的剩余缺口 ✓}:\ \text{不是"看不见支撑"、也不是"缺必要条件"，而是 \textbf{可实现集（achievability）本身} —— 任意非等价松弛都必须\textbf{新发明}且过 AMEND-35 支撑可见性门 ✓}$$
$$
$$
```

## §2 状态（**✓**）

```
$$\boxed{K(10,1)=119\ \text{保持 UNKNOWN};\ \text{本档纠正论证并封 Booleanity 形状 ✗};\ \text{未跑 solver ✓};\ \text{不写禁止表述 ✓}}$$
$$\textbf{本次会话 119 线累计（均已注明"未闭合"而非"不可能" ✓）}:\ \text{局部强制→支撑禁制（14）;\ 全局同余（15）;\ 统计↔支撑耦合（16）;\ incidence/谱（17）;\ Booleanity（18）}$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：$A_C$ 满秩 $\not\Rightarrow$ 族单射之纠错、校正定理（$T$ 可逆 $\iff n$ 偶 $\Rightarrow C\mapsto b$ 单射）、Booleanity Gate 的可证等价性
- **档案已有（引用，不列为提出）**：Fourier audit（`ec8d20d`）、M-1（CIRCULAR）、M-2A（CLOSED）、AMEND-35、$T$ 谱 $\{11-2|\chi|\}$


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 校正定理     命中文件数=1    :: ./INCIDENCE-FIX-2026-09-27-correction-parity-and-the-booleanity-equivalence.md 
技术词 可证等价     命中文件数=9    :: ./V274-cell-existence-nontrivial-cylinder-nonzeta-local-and-V270-erratum.md ./V278-finite-proof-vs-finite-data-certificate-reduction-refutation.md ./V275-certificate-barrier-theorem-conditional-capstone.md
```
- **本档新增**：$A_C$ 满秩 $\not\Rightarrow$ 族单射之纠错、校正定理（$T$ 可逆 $\iff n$ 偶 $\Rightarrow C\mapsto b$ 单射）、Booleanity Gate 的可证等价性（见上方命中数；0 命中者为自造语／内部标签 ✓）
