# AUDIT-2026-09-28m — **$P_{-1}^{\rm spectral}$ 门检：$Q1$ 不过 ⟹ 表示层总审计结论**

> **性质**：**审计**——**不占 C 号** ✓；**不作路线裁定** ✗；空间 B ✓
> **时间**：2026-09-28 20:59 ✓
> **唐先生令**：选 (ii) 重估表示层；**只测 spectral/Fourier** 一种；三问全过才进 $P_1$ ✓

**已查地图**：接续 `AUDIT-k/l`（边界层降级）／`AUDIT-j`（$\Phi_2$）✓

D0: 本档对象 ＝ **档案已有**（$1_C$／Walsh 谱／Krawtchouk——无新数学对象 ✓）
D1: 0（产出＝**谱门 $Q1$ 否决 ＋ 表示层总审计结论** ⚠️）

---

## §1 三问逐条（**照唐先生 ✓**）

$$\text{设定}:\ f=1_C,\ g=1_{B_1(0)},\ \text{覆盖条件}\ \Longleftrightarrow\ f*g\ge1\ \text{逐点};\ \hat g(S)=11-2|S|\ ✓$$

### Q1：是否只是距离分布的 Krawtchouk 重编码？—— **是 ✗（经典）**

$$\text{Delsarte--MacWilliams}:\ \text{Walsh \textbf{功率谱} }\Big\{P_j:=\sum_{|S|=j}\hat f(S)^2\Big\}_{j=0}^{10}\ \Longleftrightarrow\ \text{距离分布 }\{D_i\}\ \text{（Krawtchouk 变换，可逆）}$$
$$\therefore\ \boxed{Q1\ \textbf{不过}:\ \text{功率谱（Fourier 之自然内容）＝距离分布之重编码}}\ ✗$$

**⚠️ 诚实记录（数值 spot-check 有 bug）**：

$$\text{本档核验}\ \sum_S\hat f(S)^2(-1)^{S\cdot x}=2^nD_{wt(x)}:\ x{=}0\ \textbf{通过}（{=}153600\ ✓\ \text{Parseval}）;\ \textbf{但}\ x{\ne}0\ \text{不过}（18432\ vs\ 151552）$$
$$\therefore\ \text{我之 FWT 字符/索引配对有\ \textbf{约定错误}（未修）} ⚠️;\ \text{但 Q1 之答案由经典定理给出，\textbf{不依赖}该 spot-check}\ ✓$$

### Q2：同距离分布、不同谱结构之可能？—— **有（符号型）✓**

$$\text{功率谱}\ \{P_j\}\ \text{只给 }|\hat f(S)|;\ \textbf{符号}\ \operatorname{sgn}\hat f(S)\ \text{不被其决定}\ \checkmark$$

### Q3：能否对 $K{=}118$ 产生方向性约束？—— **未见，且结构上无中间层 ⚠️**

$$\text{功率谱}:\ \sim11\ \text{个参数}\ ({\Longrightarrow}\ \text{KILL，Q1});\quad \text{完整谱}\ \{\hat f(S)\}\in\mathbb R^{1024}:\ \text{反变换}\ \Longleftrightarrow\ C\ \textbf{完全不变量}\ ({\Longrightarrow}\ \textbf{无归约})$$
$$\text{中间层（符号型）}:\ 1024\ \text{bits}\ \approx\ \text{完整谱} \Longrightarrow \textbf{近完全不变量},\ \text{无可压缩中间层}\ ⚠️$$
$$\boxed{\therefore\ \text{谱表示面临\ \textbf{同一双分岔}}:\ \text{要么}\sim11\ \text{参数（被 KILL），要么完全不变量（无归约）}}\ ⚠️$$

## §2 表示层总审计结论（**照唐先生 §"否则"分支 ✓**）

$$\boxed{\text{三问未全过（}Q1\ \text{不过，}Q3\ \text{结构上无中间层）} \Longrightarrow \text{谱表示\ \textbf{亦无入口}}\ ✗}$$

**七类表示总表**：

| # | 表示层 | 归宿 |
|---|---|---|
| 1 | incidence/multiplicity（$a_x,N_i,\Phi_2$） | 基本剥除（$\Phi_2\to$ 三点层） |
| 2 | coset/subspace | 剥除（LP $=93.09$、整性＝重编码） |
| 3 | complement boundary | 低阶退化（补图恒连通） |
| 4 | **全局算子/谱** | **功率谱＝距离分布重编码；完整谱＝完全不变量（无中间层）** |

$$\boxed{\text{四层表示类皆无独立 }P_1\ \text{入口}}\ \Longrightarrow\ \text{按唐先生 §"否则" ⟹ }\boxed{\text{119 之数学新表示路线\ \textbf{暂时没有可见入口}}}\ ✓$$
$$\text{（\textbf{非}"所有表示都死" ✗ —— 准确表述限于\ \textbf{已检验之四类}}\ ✓\ V290)$$

## §3 建议（**待唐先生定 ✓**）

$$\text{按唐先生之分支设计}:\ \text{此时转\ \textbf{certificate 路线}，}\textbf{不是退而求其次}\ ✓$$
$$\qquad \because\ \text{表示审计已给出\ \textbf{充分负证据}（四类 {$+$} 六个具体候选皆无独立 accounting）}\ ✓$$

## §4 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "谱表示门" "功率谱重编码" "表示层总审计"
技术词 谱表示门    命中文件数=0    ::
技术词 功率谱重编码  命中文件数=0    ::
技术词 表示层总审计  命中文件数=0    ::
```

## §5 边界（硬 ✓）

- 经典定理引证 ＋ 有限数值 spot-check（含**已记录的 bug** ⚠️）✓；**不占 C 号** ✓；**不作路线裁定** ✗；不跨空间 ✓
- **明确否认** $C{=}3{\Rightarrow}{\neg}1111$ 已 ✗；**明确否认** $128{=}145{-}17$ 已 ✗；**明确否认** 119 不存在已 ✗（V290）
- §2 之结论**限于已检验四类表示**，**非**"一切表示皆死" ✗（V290 ✓）
