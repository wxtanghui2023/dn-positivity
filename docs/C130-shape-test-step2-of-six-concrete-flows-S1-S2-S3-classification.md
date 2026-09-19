已查地图（**先查后写**）：`P3-B2-transport-to-zeta-and-the-exponent-crux.md`（§3.3 静态三源全堵 ＋ §5 "½ 必须动态产生＝不动点线性化本征值" ＋ P2 三条硬要求）、`CLOSED-ROUTES-MAP:228`（DBN/BN 变形型）、`C-111`（端点 ½ 阶分支）、`C-115`（Λ≤0 ⟺ RH）、`C-125`（sumset 饱和／尺度感知）、`C-126`（SUSPENDED ＋ 唯一破口）、`V188 §2`（线性层饱和）、`V192 §③`（β 只经重数）、`C-96`（Kakeya/sticky 只是方法模板）、`REVIEW-V2`（BC 一次成功、无迭代规则）。关键词回查：`形状检验` 命中文件数=1（`A4-2-optimal-coefficient-shape.md`，**沿用**）、`难度不可分离`=0（**新**）、`固定点流`=0（**新**）。
**本档任务（唐先生 2026-09-19 10:58 直接提问）**：**给出一个具体的算术流，把"第 2 步"（不动点落在 ½）写出来，看它像不像已知 RH 等价形式。**
**结论（先行）**：$$\textbf{(一)}\ \text{拆分}\ \textbf{合法（非循环）}✓;\ \textbf{真实困难＝}\boxed{\textbf{难度不可分离}}✓✓$$
$$\textbf{(二)}\ \text{执行形状检验}：\text{现有}\ \textbf{六个具体流} \text{的 step 2 全部写出} \Longrightarrow \text{全部落}\ \textbf{两类}：\text{S1（≡已知 RH 等价）}／\text{S2（比例型，封顶）}✓✓$$
$$\textbf{(三)}\ ⭐\ \text{新构造一个候选（卷积重整化流）} \Longrightarrow \text{step 2}\ \textbf{是恒等重述}（\text{线性重标定}）\Longrightarrow \text{归 S2 家族}✓✓$$
$$\textbf{(四)}\ ⭐⭐\ \textbf{结构判据}：\text{"某聚合量达某值"型 step 2} \Longrightarrow \text{必落 S1／S2};\ \text{唯有}\ \textbf{非聚合（位置级）} \text{形状才可能是新的} \Longrightarrow \textbf{实例数＝0}✓✓$$

FREEZE-ACK: 本档即冻结期内的形状检验与外部机制审计（依 `§8.1`；不产候选结论）

D0: 本档对象 = **六流＋一新构造的「step 2 形状检验」＋ S1/S2/S3 三分类 ＋ 对 P2(iii) 的加强条件** —— 关系 = 判定与收束，非新机制
D1: 0

# C-130 · **形状检验：具体算术流的「第 2 步」写出来，像不像已知 RH 等价形式**

> **唐先生 2026-09-19 10:58**：拆成"存在不动点"＋"不动点在 ½"**合法**（收回"循环"一词，改为**难度不可分离**）；
> 第 1 步**很可能平凡**；难度几乎全压第 2 步；建议**拿具体流写出第 2 步，看形状** ✓

---

## §1 拆分（逐条采纳）

$$\text{(1)}\ \text{拆分}\ \textbf{合法}：\text{第 1 步不需要用到"}\beta=\tfrac12\text{"} \Longrightarrow \textbf{非循环}✓✓$$
$$\text{(2)}\ \text{"循环"一词}\ \textbf{收回}，\text{改为}\ \textbf{难度不可分离}（\text{拆分合法，但子命题难度＝原问题}）✓✓$$
$$\text{(3)}\ \text{第 1 步}\ \textbf{很可能平凡}：\text{压缩映射／紧性论证是标准工具}✓✓$$
$$\text{(4)}\ \text{难度}\ \textbf{几乎全在第 2 步}✓✓$$

## §2 六个具体流的 step 2 形状检验（**逐流写出**）

$$\begin{array}{c|c|c|c}
\text{流} & \text{step 1（存在性）} & \text{step 2（写出来）} & \text{形状}\\
\hline
\text{DBN 热流}\ t\mapsto\Xi*G_t & \Lambda:=\inf\{\cdot\}\ \text{存在（平凡）} & \Lambda\le0 & \textbf{S1}\ (=RH)\\
\text{Nyman–Beurling}\ d_N & \text{单调有界}\Longrightarrow\text{收敛（平凡）} & \lim d_N=0 & \textbf{S1}\ (\text{NB 判据})\\
\text{Li 系数}\ n\mapsto\lambda_n & \text{有限可算} & \lambda_n\ge0\ \forall n & \textbf{S1}\ (\text{Li 判据})\\
\text{Weil 二次形}\ Q_T(\varphi) & \text{有限}\ T\ \text{可算} & Q\ge0 & \textbf{S1}\ (\text{POS1／POS2})\\
\text{Euler 截断}\ y\mapsto\prod_{p\le y} & \text{极限}=\zeta\ (\mathrm{Re}\,s>1\ \text{平凡}) & \text{临界带零点位于}\ \tfrac12 & \textbf{S1}\ (\text{且 TESTABLE-1}\ \✗)\\
\text{谱实现族（自伴）} & \text{实谱存在} & \text{无退化}：N_0^s/N_d\to1 & \textbf{S2}\ (\text{比例型}，0.6818\ \text{封顶})\\
\end{array}$$
$$⚠️\ \text{另列（不计入六流）}：\text{pair correlation／form factor}\ F(\alpha)=1\ (\alpha\ge1) \Longrightarrow \textbf{S3}\ (\text{已知}\ \textbf{不蕴含} RH)\ \text{[文献级·待核]}✓$$

$$\Longrightarrow\ \boxed{\text{S1}\ \text{＝难度不可分离（6 项中 5 项）};\quad \text{S2}\ \text{＝比例型封顶（1 项）};\quad \text{S3}\ \text{＝不蕴含 RH}}✓✓$$

## §3 新构造候选（**可能性二的诚实尝试**）：卷积重整化流

$$\text{定义}\ A_k:=\Lambda\ \text{的}\ k\ \text{重加性卷积};\quad DS(A_k)=(\zeta'/\zeta)^k;\quad \sigma_c(A_k)=k✓$$
$$\text{重标定}\ \hat s:=s/k,\ \text{令}\ k\to\infty\ \text{取极限物（自相似不动点）}✓$$
$$\textbf{step 1}：\text{极限物存在（自相似）—— 似可由 CLT／压缩给出}\ [\text{待核}]✓$$
$$\textbf{step 2（写出来）}：\text{极限物的临界指数}\ =\ 1/2 ✓$$
$$\qquad \text{而}\ k\beta^*/k=\beta^* \Longrightarrow \text{"临界指数}=1/2"\ \textbf{就是}\ \text{"}\beta^*=1/2\text{"} \Longrightarrow \boxed{\textbf{恒等重述，无新形状}}✓✓$$
$$\qquad \text{根因}：\textbf{重标定是线性的} \Longrightarrow \text{把}\ \beta^*\ \text{改名成"临界指数"而不改变信息量}✓✓$$
$$\qquad \text{且与}\ \text{`C-125`}\ \text{一致}：\text{信息恰位于收敛边界}（k\beta^*<k=\sigma_c）\Longrightarrow \textbf{饱和}✓✓$$
$$\Longrightarrow\ \text{归入}\ \textbf{S2 家族（边界饱和）}，\text{不是新形状}✓$$

## §4 ⭐⭐ 结构判据（本档核心，强于 `C-126`）

$$\text{(甲)}\ \text{若 step 2 形如"}\textbf{某聚合量达到某值}" \Longrightarrow \text{该量的信息只到}\ \textbf{线性统计层}（\text{`V188` §2 饱和}）✓✓$$
$$\qquad \Longrightarrow \text{要么}\ \textbf{重述已知等价}（\text{S1}），\ \text{要么}\ \textbf{比例型}（\text{S2}，\text{封顶}<1）✓✓$$
$$\text{(乙)}\ \text{唯有}\ \textbf{非聚合（位置级／逐点）} \text{形状才可能是新形状};\ \text{而位置级读数＝}S(T)\iff RH\ \text{本身}✓✓$$
$$\Longrightarrow\ \boxed{\text{S1}\ \text{不可分离}／\text{S2}\ \text{封顶}／\text{S3}\ \text{不蕴含};\quad \textbf{第四类（新形状）实例＝0}}✓✓$$
$$\text{(丙)}\ \textbf{对 P2(iii) 的加强}：\text{`P3-B2` 要求"}\tfrac12\ \text{动态产生＝不动点线性化本征值}"；$$
$$\qquad \text{本档补充}：\text{该本征值必须是}\ \textbf{非聚合读数}，\ \text{否则落 S1／S2}✓✓$$

## §5 边界

- ⚠️ **未找到**新形状；**不声称**其不存在 ✓
- ⚠️ S3 的"不蕴含 RH"为**文献级**陈述，标 `[待核]` ✓
- ⚠️ §3 的 step 1 存在性标 `[待核]`（未构造极限物）✓
- ⚠️ **未用** RH；**未改**任何原档 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 11:0x）`[纪律]`（先跑后写）

```
技术词 形状检验     命中文件数=1 :: ./A4-2-optimal-coefficient-shape.md   ⟹ 沿用（引用）
技术词 难度不可分离  命中文件数=0 ::                                      ⟹ 本档新增
技术词 固定点流     命中文件数=0 ::                                      ⟹ 本档新增
```
**读数（按实测）**：`形状检验`为**沿用**；`难度不可分离`／`固定点流` 为**本档新增** ✓
