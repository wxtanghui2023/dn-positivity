已查地图（**先查后写**）：`C-271`（M=5/0.5 未闭合正式记录 ＋ §3 诊断协议）、`C-268`（E4 依赖地图）、`C-270`（GAP-A）、`C-181`（阻尼引理）、`v4` 引擎（`scripts/rpm_certificate_v4.py`，**可证余弦包围**✓）。回查见 §6 ✓

D0: 本档对象 = **M=5/0.5 pending 箱的 failure-mode 审计**（协议出自 `C-271` §3）—— 关系 = 执行已定协议、给未闭合定性（不产新定理、不提预算）
D1: 0
FREEZE-ACK: 本档即冻结期内的审计结果记录（依 §8.1）

---

## §0 结论（三条 ✓✓）

$$\boxed{\textbf{① 零反例}✓✓：\text{抽样}\ 20{,}000\ \text{个 pending 箱中，}\ U_{\rm sample}(B)\le\tfrac12\ \text{的箱数}=\mathbf{0}✗ \Longrightarrow \text{无}\ m_5<\tfrac12\ \text{的证据}}$$
$$\boxed{\textbf{② 间隙极大}✓✓：\text{中位}\ U-L=\mathbf{1.83}\ ✓ \Longrightarrow \text{box 级}\ \max_k\min_B\ \text{交换损失被实测确认}✓}$$
$$\boxed{\textbf{③ pending 是粗箱 backlog}✗✓：\text{宽度中位}\ 0.26\approx\pi/12 \Longrightarrow \textbf{M=5 是吞吐／预算受限，}\text{不是证书强度受限}✓✓}$$

## §1 数据来源与方法（✓）

$$\textbf{数据}✓：\texttt{/tmp/v4\_pending.npz}（\text{由}\ 800\ \text{万预算重放时落盘}✓，\text{全量 pending}\ 670{,}091\ \text{箱}✓）$$
$$\textbf{抽样}✓：20{,}000\ \text{箱（均匀随机，占}\ 3.0\%✓）\qquad \textbf{盒内采样集}✓\ S_B=\{\text{中心}\}\cup\{8\ \text{个内部随机点}\}$$
$$L(B):=\max_{k}\sum_j\min_{\theta\in I_j}\cos(k\theta)✓（\text{证书下界}✓）\qquad U_{\rm sample}(B):=\min_{\theta\in S_B}\max_{k}\sum_j\cos(k\theta_j)✓$$

## §2 实测数值（✓✓）

| 量 | 结果 |
|---|---|
| pending 箱总数 | 670,091 |
| 箱宽度中位（最大坐标宽） | **2.618e-01** |
| $L(B)<1/2$ | 14,052（70.3%）|
| $U_{\rm sample}(B)>1/2$ | 20,000（**100.0%**）|
| ★ 松弛嫌疑（两者同时） | 14,052（70.3%）|
| ⚠ **真反例嫌疑**（$U_{\rm sample}\le1/2$） | **0（0.0%）** |
| $L$ 中位 / $U$ 中位 | +0.3827 / +2.1766 |
| 间隙中位 $U-L$ | **+1.8319** |
| $L<1/2$ 那批的 $L$ 中位 / $U$ 中位 | +0.2412 / +2.1615 |

## §3 判读（✓✓）

$$\textbf{① }\text{按}\ \texttt{C-271}\ \S3\ \text{判据}✓：\text{大量箱满足}\ L<\tfrac12\ \textbf{且}\ U_{\rm sample}>\tfrac12 \Longrightarrow \boxed{\text{瓶颈＝证书松弛}✓✓（\text{而非}\ m_5<\tfrac12✓）}$$
$$\textbf{② }\text{宽度中位}\ 0.26\ \Longrightarrow \text{pending 主要由}\textbf{只被拆过}1\text{–}2\ \text{次的粗箱}\ \text{组成}✗✓$$
$$\qquad \text{五坐标同时宽}\ 0.26\ \text{时，拆一维后【最大坐标宽仍为}\ 0.26✓】 \Longrightarrow \text{中位}\ 0.26\ \text{对应深度}\ \lesssim4✓$$
$$\textbf{③ }\text{粗箱上分离式下界天然弱}✓（\text{区间含}\ \pi\ \text{奇数倍即取}\ -1⟹\text{和被拖垮}✓），\text{而盒内真值}\ \approx2.18✓ \Longrightarrow \text{大量分裂需求}✗$$

## §4 对下一步的含义（✓✓）

$$\textbf{① 预注册实验（\texttt{C-271} §4.2）得到支持}✓：60M \text{单次预算扩展}\ \text{—— 因 backlog 属「可认证型」}✓（\text{零反例 ＋ 巨大间隙}✓）$$
$$\textbf{② 但更根本的方向}✓✓：\text{给盒证书加入}\ \textbf{共享}\ k／\text{相位信息}✓ \Longrightarrow \text{在粗箱上直接认证}✓，\text{逼近}\ \min_B\max_k✓ \text{而非堆}\ \max_k\min_B✗$$
$$\qquad \text{否则每次扩预算都只是在同一松弛下多拆箱}✓（\text{吞吐换进度}✓）$$

## §5 边界（✓）

$$\textbf{① }U_{\rm sample}\ \text{是盒内最小值的}\textbf{上估计}✓ \Longrightarrow \text{「零反例」}\textbf{不是证明}✗（\text{只否证「抽样可见的反例」}✓）$$
$$\textbf{② 抽样率}\ 3.0\%✓；\text{采样点}\ 9／\text{箱}✓；\text{采样用 float cos}✓（\text{误差}\ \sim10^{-12}✓，\text{与}\ 0.05\ \text{级判据无关}✓）$$
$$\textbf{③ 未用 RH}✓；\text{未改他档正本}✓；\text{未动}\ v4\ \text{数学}✓；\text{未提高预算}✓（\text{重放仅为抽取 pending}✓）$$
$$\textbf{④ }m_5\ \text{真值仍未知}✗：\text{本档只证「pending 中无可见反例」及「backlog 为粗箱」}✓$$

## §6 【技术词回查】输出（**先跑后写**✓）

```
技术词 粗箱积压     命中文件数=0    ::
技术词 采样上界     命中文件数=0    ::
技术词 零反例审计   命中文件数=0    ::
```
$$\textbf{① 本档新增}✓：\text{三项各 0 命中} \Longrightarrow \textbf{本档首次命名}✓$$
$$\textbf{② 档案已有（引用）}✓✓：\text{认证间隙／交换损失}✓（\texttt{C-271}✓）；\text{可证余弦包围}✓（v4✓）；\text{pending 落盘}✓（\texttt{C-271} §4✓）$$
