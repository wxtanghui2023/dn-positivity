已查地图：已跑 scripts/prework_map_check.sh 16 点闭式 单缺陷 15-移位 ⟹ 执行自 `H7WALSH-2026-09-27-...`（✓）＋ 唐先生 15:04（彻底展开 16 点 Walsh ✓）；本档 = **闭式 ＋ 单缺陷定理（annihilation 已证 ✓✓）**。
D0: 本档对象 = 二阶 Walsh 消失（annihilation）的 16 点级证明
D1: 3（**16 点闭式 ✓✓**；**单缺陷定理 ✓✓（16/16 验证 ✓）**；**两案例被同一机制解释 ✓✓**）

# (甲″-iv-a″) 16 点闭式与单缺陷定理（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(DG-1 ⭐⭐16 点闭式（已推导 ＋ 验证 ✓✓）)}\ \beta:\mathbb F_2^7\to\mathbb F_2^4\ \text{是\textbf{线性}的}（\beta(y)=\sum_{j\in y}(j{+}8)\ ✓\text{）},\ \mathrm{im}\,\beta|H_7=\{0,4,11,15\}\ (\text{各 4 次 ✓}) \Longrightarrow}$$
$$\qquad\boxed{c(a)=n_a^{0}+n^{1}_{a\oplus15}},\qquad n_a^{\epsilon}=\#\{u\in H_7:\ \beta(u)=a,\ \lambda(u)=\epsilon\}\ (\text{纤维-移位闭式 ✓✓})$$
$$\boxed{\textbf{(DH-1 ⭐⭐单缺陷定理（已推出 ✓✓）)}\ \text{若 }\lambda=1-\delta_{u_0}\ (\text{单缺陷}:\ u_0\ \text{处取 0、其余取 1 ✓}) \Longrightarrow\ \boxed{c=(4,4,4,4)+\delta_{\beta(u_0)}-\delta_{\beta(u_0)\oplus15}}\ ✓✓}$$
$$\qquad\text{实测（}u_0\ \text{取遍 16 点 ✓，}\mathbf{16/16\ ✓}\text{）}:\ u_0{=}0\Rightarrow(5,4,4,3);\ u_0{=}7\Rightarrow(4,3,5,4);\ u_0{=}25\Rightarrow\mathbf{(3,4,4,5)};\ u_0{=}30\Rightarrow(4,5,3,4)\ ✓$$
$$\qquad\Longrightarrow\ \textbf{"均匀 }(4,4,4,4)\ +\ \textbf{单个 }\pm1\ \text{扰动}"是\textbf{定理}（对该类 ✓），不再是观测 ✓✓$$
$$\boxed{\textbf{(DI-1 ⭐⭐annihilation 的 Fourier 一步（已推导 ✓✓）)}\ \delta_a-\delta_{a\oplus15}\ \text{的 Fourier 变换}:\ \widehat{(\delta_a-\delta_{a\oplus15})}(\chi)=\chi(a)\bigl(1-\chi(15)\bigr) \Longrightarrow \mathrm{supp}=\{\chi:\chi(15)=-1\}\ (\textbf{2 元} ✓\text{）}}$$
$$\qquad\Longrightarrow\ \boxed{\widehat F(S)=0\ (|S|\ge2)}\ ✓✓\ \text{—— \textbf{annihilation 成立（在该类上 ✓）}}\ \text{（}k'{=}2\ \text{即 }4\ \text{点商群上恰 2 个一阶特征 ✓）}$$
$$\boxed{\textbf{(DJ-1 ⭐⭐两案例同一机制 ✓✓)}\ \text{基案 }\lambda{=}\mathbf 1\iff u_0{=}0\ (u_0{=}0\in\ker\beta\ ✓) \Longrightarrow (5,4,4,3)\ ✓\ \text{（本机实测 ✓✓）};}$$
$$\qquad k'{=}2\ \text{反例之推断 }c\text{-质量}=[3,4,4,5]\ \text{\textbf{恰为} }u_0\in\beta^{-1}(15)\ \text{之单缺陷像 ✓✓} \Longrightarrow \textbf{同一机制解释两案 ✓✓}$$
$$
$$
```

---

## §1 推导链（**✓ 严格**）

```
$$\text{(1) }\beta\ \text{线性 ⟹ 值集 }\{0,4,11,15\}\ \text{各 4 次（}\ker\ \text{在 }H_7\ \text{上维数 2 ✓）}$$
$$\text{(2) }c(u)=\beta(u)\oplus15\lambda(u) \Longrightarrow c=a\iff[\beta(u){=}a\wedge\lambda{=}0]\vee[\beta(u){=}a\oplus15\wedge\lambda{=}1] \Longrightarrow \text{闭式 (DG-1) ✓}$$
$$\text{(3) 单缺陷 }\lambda \Longrightarrow n^0_a{=}[a{=}\beta(u_0)],\ n^1_a{=}4{-}[a{=}\beta(u_0)] \Longrightarrow c{=}4+\delta_{\beta(u_0)}-\delta_{\beta(u_0)\oplus15}\ ✓\ \text{(DH-1 ✓)}$$
$$\text{(4) Fourier: 差-δ 的变换 }=\chi(a)(1-\chi(15)) \Longrightarrow \text{支撑}=\{\chi:\chi(15){=}{-}1\}\ \text{恰 2 元 ✓（对 4 元群 ✓）} \Longrightarrow\ \text{二阶项为零 ✓ (DI-1 ✓)}$$
$$
$$
```

---

## §2 判定（**✓ 按唐先生 gate**）

```
$$\textbf{判定 ✓}:\ \boxed{\text{annihilation 在"单缺陷类"上 = THEOREM ✓✓}}\ \text{（不再仅 SUPPORTED ✓ —— 唐先生要求的"从 }H_7\ \text{十六点结构直接得到 }\widehat F(S){=}0\ (|S|{=}2)\ "\ ✓✓\text{）}$$
$$\qquad\textbf{剩余缺口 ⚠️（诚实 ✓）}:\ \text{需证\textbf{打孔（}k'{=}2\text{）后的 }c\text{-分布仍属单缺陷类 ✓}（现为"其质量谱恰与单缺陷像一致 ✓"之强证据 ⚠️，非证明 ✗）}$$
$$\qquad\Longrightarrow\ \text{状态}:\ \boxed{k'{=}1\ \text{分支 = THEOREM}\ ✓✓;\ k'{=}2\ =\ \text{annihilation 已证\textbf{条件于}单缺陷类}\ ✓\ +\ \text{类归属观测} ⚠️}$$
$$
$$
```

---

## §3 下一步（**✓**）

```
$$\text{(甲″-iv-a‴) 攻"打孔保持单缺陷"}:\ \text{算两坐标打孔对 }(\beta,\lambda)\ \text{参数化的作用（}H_7\ \text{16 点上的显式映射 ✓）；若打孔 = "在 }H_7\ \text{上移动缺陷点" ⟹ 闭合 ✓✓}$$
$$\text{(甲″-iv-b) 三坐标 sanity —— 仍挂起 ✓};\ \text{(丙) 119（暂不碰 ✓）}$$
$$\text{119}: \textbf{完全不碰} ✓$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：16 点纤维-移位闭式 $c(a)=n_a^0+n^1_{a\oplus15}$、单缺陷定理（均匀 $+$ 单个 $\pm1$ 扰动）、annihilation 的 Fourier 一步、两案例同一机制
- **档案已有（引用，不列为提出）**：A-H7WALSH-1、A-PROOF-1、A-WALSH-1、$\beta$ 线性、$15\in V$


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 单缺陷定理  命中文件数=1    :: ./H7CLOSED-2026-09-27-single-defect-theorem-closes-the-annihilation.md 
技术词 纤维-移位闭式 命中文件数=1    :: ./H7CLOSED-2026-09-27-single-defect-theorem-closes-the-annihilation.md
```
- **本档新增**：16 点纤维-移位闭式 $c(a)=n_a^0+n^1_{a\oplus15}$、单缺陷定理（均匀 $+$ 单个 $\pm1$ 扰动）、annihilation 的 Fourier 一步、两案例同一机制（见上方命中数；0 命中者为自造语／内部标签 ✓）
