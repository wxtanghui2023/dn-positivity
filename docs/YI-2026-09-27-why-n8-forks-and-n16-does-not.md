已查地图：已跑 scripts/prework_map_check.sh n=8 分叉 n=16 刚性 平均化 ⟹ 执行自 `STEP01-2026-09-27-...`（✓）＋ 唐先生 14:10（先乙后甲，三层 gate ✓）；本档 = **(乙) 三层判定：乙-1 否定普遍性 ✓；乙-2 机制假设（平均化）✓；乙-3 靶点精确化 ✓**。
D0: 本档对象 = n=8 分叉 vs n=16 刚性的机制差异
D1: 3（**乙-1：J≠f(A₁,A₂) 普遍不成立（有反例 ✓）**；**乙-2：机制=平均化（假设 ＋ 强支持 ⚠️）**；**乙-3：靶点精确化 ✓**）

# (乙) 为何 n=8 分叉而 n=16 不分叉（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(CH-1 ⭐乙-1 = 否定普遍性 ✓（有反例）)}\ \textbf{不存在普遍恒等式 }J=f(A_1,A_2)\ ✗\ \text{—— }n{=}8\ \text{三见证码反例 ✓}:}$$
$$\qquad\text{三码\textbf{不等价}，\textbf{全距离分布完全相同} }A=(0,16,160,176,64,48,32,0)\ ✓,\ (A_1,A_2)=(0,16)\ ✓,\ \text{却 }J_7\in\{64,128,256\}\ ✓✗$$
$$\qquad\text{唯一\textbf{普遍}成立的是等号链给的 }\boxed{A_2=\tfrac M2-A_1}\ ✓\ \text{（仅需 near-perfectness ✓，与构造无关 ✓）};\ \text{另 }A_1{+}A_2{=}M/2\ \text{在两侧均成立 ✓}$$
$$\qquad\Longrightarrow\ \textbf{n=16 的刚性必须来自\textbf{额外结构}（不是普遍代数 ✓）} \Longrightarrow \text{下一步应钉住那条结构 ✓}$$
$$\boxed{\textbf{(CH-2 ⭐乙-2 = 机制 = 平均化（假设，强支持 ⚠️）)}\ n=16\ \text{侧（已推导并验证 ✓）}:\ q=X*C,\ X\ \text{的像}=W=\{0,2,4,6\}\ (\textbf{真子群}4\ \text{元}\ ✓),\ \text{纤维}=32\ ✓}$$
$$\qquad\Longrightarrow\ \textbf{平均化} \Longrightarrow q\ \text{在每个 }W\text{-陪集恒定（强制）} \Longrightarrow \text{自由值仅剩 }(32s,\ 32(16-s))\ \text{两个} \Longrightarrow J=32^2(3s^2+4(16-s)^2)\ \text{被 }s\ \text{钉住 ✓}$$
$$\qquad n=8\ \text{侧（本次会话记录 ✓）}:\ \text{三见证码的射线计数形状为 }(4\times4),\ (2\times8),\ (1\times16)\ \text{—— \textbf{三种形状，同一个 }A_2{=}16 \Longrightarrow \textbf{无任何子群强制} ✓✗}$$
$$\qquad\Longrightarrow\ \textbf{第一处失去强制的位置 = "陪集常值"这一步 ✓（}n{=}16\ \text{有，}n{=}8\ \text{无 ✓）};\ \text{其结构性原因是\textbf{ }x\text{-部映射是否集中到真子群 ✓}$$
$$\boxed{\textbf{(CH-3 ⭐乙-3 = 靶点精确化 ✓)}\ \text{ENP1CC puncturing 的任务不是"搜分叉"，而是}:\ \boxed{\textbf{刻意破坏"集中化/平均化"同时保留两个完美半码与 }(A_1,A_2)\ \text{桶}}\ ✓}$$
$$\qquad\text{具体可测指标}:\ \text{对候选码算 }x\text{-部映射的\textbf{像大小与纤维谱};\ \text{若像 = 整个标签群（无平均化 ✓）则该候选有希望产生 }J\text{-分叉 ✓}$$
$$
$$
```

---

## §1 证据（**✓ 本机/档内**）

```
$$\text{(1) 见证档 }work/k10/c62/np1cc/witness\_0\_16.txt\ \text{首行逐字}:\ \texttt{\# J7=64\ \ A1=0 A2=16\ \ A=[0,16,160,176,64,48,32,0]}\ ✓$$
$$\text{(2) 全距离分布相同（三码）+ 不等价 + 同 }(A_1,A_2)\ \text{+ 异 }J_7\ ✓\ \text{（P12-PASS 记录 ✓）}$$
$$\text{(3) }n{=}16\ \text{侧：}X\text{-分布 }\{0{:}32,2{:}32,4{:}32,6{:}32\}\ ✓;\ C\subseteq V=\mathrm{span}\{2,4,9\}\ ✓;\ \max_z|q_{\rm pred}-q_{\rm meas}|=0\ ✓\ \text{（16 syndrome）}$$
$$
$$
```

---

## §2 诚实边界（**⚠️ 关键**）

```
$$\text{(i) 乙-2 的"平均化机制"在 }n{=}16\ \text{侧是\textbf{定理}（已推导＋验证 ✓），但 }n{=}8\ \text{侧\textbf{未用同一语言分解} ⚠️} \Longrightarrow \text{机制目前是\textbf{强支持假设}，非已证判据 ⚠️}$$
$$\text{(ii) 按唐先生 gate: 乙-1 给出\textbf{否定}（无普遍恒等式 ✓）、乙-2 给出\textbf{假设}（未证 ⚠️）} \Longrightarrow \text{应做一次\textbf{廉价判定性微步}再决定是否转甲 ✓}$$
$$\qquad\Longrightarrow\ \textbf{微步}:\ \text{把 }n{=}8\ \text{三见证码用同一语言分解（找其 }x\text{-部映射的像与纤维谱 ✓）；若像 = 全标签群 ⟹ 机制成立 ✓ → 转甲（靶点已明 ✓）；若不然 ⟹ \textbf{STOP}，直接转甲（不继续猜 ✓）}$$
$$
$$
```

---

## §3 资态与下一步（**✓**）

```
$$\textbf{已成立 ✓}:\ A_2=\tfrac M2-A_1\ \text{普遍 ✓};\ n{=}16\ \text{族内 }(A_1,A_2,J)\ \text{单参数塌缩 ✓（}s\ \text{参数 ✓）};\ \text{族外池 28 对无分叉 ⚠️（未发现，不等于定理 ✗）}$$
$$\textbf{下一步（二选一，按 gate ✓）}:\ \text{(i) 跑上述 }n{=}8\ \text{分解微步（廉价 ✓，能否把机制升为判据）};\ \text{(ii) 直接转甲：ENP1CC puncturing};\ \text{(iii) 119（暂不碰 ✓）}$$
$$\text{119}: \textbf{完全不碰} ✓$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：乙-1 否定普遍性（$J=f(A_1,A_2)$ 有反例）、乙-2 平均化机制假设、乙-3 靶点精确化
- **档案已有（引用，不列为提出）**：A-STEP01-1、A-CLOSEDFORM-1、A-SUBSPACE-1、P12-PASS、内蕴 $\nu$、等号链


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 平均化机制  命中文件数=1    :: ./YI-2026-09-27-why-n8-forks-and-n16-does-not.md 
技术词 靶点精确化  命中文件数=2    :: ./V179-finite-support-criterion-and-spectral-capacity-conflict.md ./YI-2026-09-27-why-n8-forks-and-n16-does-not.md
```
- **本档新增**：乙-1 否定普遍性（$J=f(A_1,A_2)$ 有反例）、乙-2 平均化机制假设、乙-3 靶点精确化（见上方命中数；0 命中者为自造语／内部标签 ✓）
