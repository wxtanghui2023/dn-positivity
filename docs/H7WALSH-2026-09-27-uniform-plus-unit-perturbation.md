已查地图：已跑 scripts/prework_map_check.sh H₇ 16 点 c 分布 单元素扰动 ⟹ 执行自 `PROOF-2026-09-27-...`（✓）＋ 唐先生 15:03（走 (ii) 手算 ✓）；本档 = **16 点 c-计算：均匀 ＋ 单元素一阶扰动 ✓✓（k'=1 与 k'=2 同一模式 ✓）**。
D0: 本档对象 = c-分布在 W-陪集上的质量结构（annihilation 之机制候选）
D1: 3（**基案 c-计数 (5,4,4,3) ✓✓**；**反例 c-质量 (3,4,4,5) ✓✓ 同模式**；**归约为 16 点级命题 ✓**）

# (甲″-iv-a) H₇ 十六点计算：均匀 ＋ 单元素扰动（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(DD-1 ⭐基案（λ=1）16 点 c-计算 ✓✓)}\ \text{对 }c(u)=\beta(u)\oplus15\lambda(u)\ (u\in H_7,\ 16\ \text{点 ✓}):\ \mathrm{supp}(c)=\beta(H_7)=\{0,4,11,15\}\subseteq V\ ✓;\ \text{计数}=(5,4,4,3)\ ✓}$$
$$\qquad\textbf{关键}: \boxed{(5,4,4,3)=(4,4,4,4)+(+1,0,0,-1)}\ \text{—— \textbf{均匀 ＋ 单个 }±1\ \text{扰动} ✓✓}\ \Longrightarrow\ \text{按 }W\text{-陪集聚合}: c(W)=5{+}4=9,\ c(9{+}W)=4{+}3=7\ ✓$$
$$\qquad\Longrightarrow\ f=32\cdot(9,\ 7)=(288,\ 224)\ ✓\ \text{（与实测一致 ✓✓）} \Longrightarrow \text{两级 ✓ 且 }9+7=16\Longrightarrow v_1{+}v_2=512=2\bar m\ ✓✓$$
$$\boxed{\textbf{(DE-1 ⭐⭐}k'{=}2\ \text{反例同模式 ✓✓)}\ \{96^4,128^8,160^4\}\ (\bar m{=}128\ ✓):\ W\text{-陪集值 }[96,128,128,160]\Longrightarrow \text{推出 }c\text{-质量}=[3,4,4,5]\ ✓}$$
$$\qquad\boxed{[3,4,4,5]=(4,4,4,4)+(-1,0,0,+1)}\ \text{—— \textbf{同一"均匀 ＋ 单个 }±1\ \text{扰动"模式 ✓✓}}\ \text{（和 }=16\ ✓,\ \text{偏离均值 }=0\ ✓\text{）}$$
$$\qquad\Longrightarrow\ \text{扰动 }\varepsilon\in\{\pm1\}\ \text{只落在一个陪集对 ✓} \Longrightarrow \text{其 }Q\cong\mathbb F_2^2\ \text{上的 Fourier 支撑}\subseteq 2\ \text{个一阶特征 ✓✓} \Longrightarrow \textbf{二阶 Walsh 恒零 ✓✓（即 annihilation）}$$
$$\boxed{\textbf{(DF-1 ⭐归约（本档最重要 ✓）)}\ \text{原子命题（}k'{=}2\ \text{之 annihilation）\textbf{被归约为 16 点级命题}:\ \boxed{\text{"}c\ \text{在 }W\text{-陪集上的质量分布}=\text{均匀}+\text{单个 }±1\ \text{扰动"}}\ ✓}$$
$$\qquad\textbf{等价形式}:\ \text{在 }\beta(H_7)=\{0,4,11,15\}\ \text{的 4 个值上，}\lambda\ \text{对 }\beta\text{-纤维的\textbf{扰乱恰好等量相反}（即 }(5,4,4,3)\ \text{型 ✓）} \Longrightarrow \text{这是\textbf{显式、有限、可手算}的命题 ✓✓}$$
$$
$$
```

---

## §1 数据（**✓ 本机**）

```
$$\text{(A) 基案 }(\lambda{=}1):\ c\ \text{分布}=\{0{:}640,\ 4{:}512,\ 11{:}512,\ 15{:}384\}\ \text{—— 除以 }128\ (\text{每 }x\ \text{一次 ✓})\ \text{得计数 }(5,4,4,3)\ ✓$$
$$\qquad\mathrm{supp}(c)\subseteq V\ ✓\ \text{（自动 ✓）};\ W\text{-聚合 }(9,7)\Longrightarrow f=(288,224)\ ✓✓$$
$$\text{(B) 反例 }(k'{=}2):\ |I|{=}16,\ |W|{=}4,\ [I{:}W]{=}4;\ W\text{-陪集值 }[96,128,128,160]\ ✓;\ c\text{-质量 }[3,4,4,5]\ ✓;\ \text{和 }16\ ✓$$
$$
$$
```

---

## §2 判定与下一步（**✓**）

```
$$\textbf{本档判定 ✓}:\ \boxed{\text{annihilation 机制候选 = "均匀 ＋ 单个 }±1\ \text{扰动"}\ ✓✓\ \text{（}k'{=}1\ \text{与 }k'{=}2\ \text{实测同模式 ✓）}} \Longrightarrow \text{原子命题已归约为 16 点级命题 ✓✓}$$
$$\qquad\textbf{诚实边界 ⚠️}:\ \text{"为何打孔后仍是单元素扰动"仍\textbf{未证} ⚠️};\ \text{故 }A\text{-WALSH-1\ 仍标 \textbf{强 SUPPORTED}（}k'{=}1\ \text{已 THEOREM ✓）}$$
$$\text{(甲″-iv-a″) 下一最小攻击}:\ \text{在 16 点上直接算 }(5,4,4,3)\ \text{的来源}:\ \lambda\ \text{在 }\beta\text{-纤维上的符号数（}\pm\text{配平 ✓）};\ \text{若 }\lambda\ \text{的符号函数在 }\beta\text{-纤维上"至多一处不配平"则命题成立 ✓}$$
$$\text{(甲″-iv-b) 三坐标 sanity —— 仍挂起 ✓};\ \text{(丙) 119（暂不碰 ✓）}$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：$H_7$ 十六点 $c$-计算（计数 $(5,4,4,3)$）、$k'{=}2$ 之 $c$-质量 $[3,4,4,5]$、"均匀 ＋ 单个 $\pm1$ 扰动"机制候选、原子命题之 16 点级归约
- **档案已有（引用，不列为提出）**：A-PROOF-1、A-WALSH-1、$X*C$ 卷积、$\beta(H_7)\subseteq V$、$W$-陪集常值


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 单元素扰动  命中文件数=1    :: ./H7WALSH-2026-09-27-uniform-plus-unit-perturbation.md 
技术词 16 点级归约  命中文件数=1    :: ./H7WALSH-2026-09-27-uniform-plus-unit-perturbation.md
```
- **本档新增**：$H_7$ 十六点 $c$-计算（计数 $(5,4,4,3)$）、$k'{=}2$ 之 $c$-质量 $[3,4,4,5]$、「均匀 ＋ 单个 $\pm1$ 扰动」机制候选、原子命题之 16 点级归约（见上方命中数；0 命中者为自造语／内部标签 ✓）
