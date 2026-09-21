已查地图（**先查后写**）：`C-181`（阻尼缩放约化引理，u≤5 假定）、`C186`（**1/20 级单模对一切 M 已证**）、`C268`（E4 依赖地图）、`C269`（A 项审计：第二实例已存在）、`C270`（**GAP-A：应用侧 u≤5 缺证**）、`PLAN §12`（待办队列与冻结依赖图）。回查见 §6 ✓

D0: 本档对象 = **M=5 / 1/2 二十万箱预算未闭合的正式记录 ＋ failure mode 精确化** —— 关系 = 证书运行的终点定性 + 下一刀诊断协议（不产新定理、不提预算）
D1: 0
FREEZE-ACK: 本档即冻结期内的状态记录与诊断协议（依 §8.1）

---

## §0 结论（四条）

$$\boxed{\textbf{① 正式记录}✗：M=5,\ m_5\ge\tfrac12：\ 19{,}971{,}000\ \text{箱耗尽},\ 226{,}948\ \text{未决} \Longrightarrow \text{「20M budget 未闭合」}}$$

$$\boxed{\textbf{② 不回退}✗：\text{不跑}\ 47\ \text{小时慢版；}\textbf{不提预算盲跑}✗；\textbf{不跑}\ M=6\text{–}11✗}$$

$$\boxed{\textbf{③ failure mode 精确化}✓✓：\text{瓶颈不是「分离式下界错误」}✗，\text{而是 box 级}\ \textbf{max–min 交换间隙}✓}$$

$$\boxed{\textbf{④ 下一刀}✓：\text{只审 pending 箱的 failure mode}（\text{协议见}\ \S3）\ \text{—— 不提预算、不跑慢版、不扩梯}✓}$$

## §1 最终读数与判读（**逐项**✓）

| 指标 | 结果 | 判读 |
|---|---|---|
| unresolved | **0** | 认证逻辑全程无未处理异常 ✓ |
| pending | 226,948 | **真正的未闭合搜索空间** ✗ |
| max depth | 18 | **远未触及** depth=80 硬上限 ✓（非深度卡死） |
| min margin | 1.8225642425040434e-05 | 已认证箱余量正常 ✓ |
| volume rel gap | 8.670e-02 | **未闭合箱体积缺口**，**不是** v4 体积自检失败 ✗✓ |
| completed | **False** | 证书未闭合 ✗ |
| 耗时 | 736.1 秒 | v4 速率约 2.7e4 箱/秒 ✓ |
| 认证箱数 | 9,886,371 | 约 49.5% 的评估箱 ✓ |

$$\text{体积缺口的换算}✓：\frac{306.0196848-279.488755}{306.0196848}=8.67\%$$
$$\qquad \Longrightarrow \text{该 8.67\% 应读作}\ \textbf{incomplete certificate 的体积缺口}✓，\textbf{不是} \text{volume self-check 失败}✗✓$$

## §2 交换间隙的逻辑（**诊断精确化**✓✓）

$$\text{证书实际证明的是}✓：\quad \max_{k}\ \min_{\theta\in B}F_k(\theta)\ \ge\ T$$
$$\text{目标真正需要的是}✓：\quad \min_{\theta\in B}\ \max_{k}F_k(\theta)\ \ge\ T$$
$$\text{一般只有}✓：\qquad \max_{k}\min_{\theta\in B}F_k(\theta)\ \le\ \min_{\theta\in B}\max_{k}F_k(\theta)$$

$$\textbf{关键}✓✓：\text{每个}\ k\ \text{看起来都被某个「坏坐标点」压低，但}\textbf{不同}\ k\ \textbf{的坏点未必是同一个}\ \theta✗$$
$$\qquad \Longrightarrow \text{真实的}\ \max_k\ \text{可以随}\ \theta\ \text{改变}✓ \Longrightarrow \text{松弛损失} = \textbf{box 级交换间隙}✓$$

$$\textbf{须澄清}✓（\text{同一性本身无错}）：\quad \min_{\theta\in B}\sum_j\cos(k\theta_j)=\sum_j\min_{\theta\in I_j}\cos(k\theta)\ \ \checkmark$$
$$\qquad \text{该等式对【固定}\ k\ \text{的可加目标】成立}✓；\text{问题不在它，而在外层}\ \max_k\ \text{与}\ \min_B\ \text{的交换}✓$$

$$\textbf{正式标签}✓：\ \boxed{\text{M=5 failure_candidate} = \text{box-wise}\ \max_k\min_B\ \textbf{认证间隙}}$$

## §3 判据：pending 箱 failure-mode 诊断协议（**下一刀**✓）

$$\textbf{对象}✓：\text{从 pending 集合抽样}\ N_{\rm aud}\ \text{个箱}\ B=I_1\times\cdots\times I_5$$
$$L(B):=\max_{k}\sum_j\min_{\theta\in I_j}\cos(k\theta) \qquad（\text{证书下界}✓）$$
$$U_{\rm sample}(B):=\min_{\theta\in S_B}\max_{k}\sum_j\cos(k\theta_j) \qquad（\text{中心 ＋ 少量代表点}✓）$$

$$\textbf{判定}✓✓：\text{若大量箱满足}\ L(B)<\tfrac12\ \textbf{且}\ U_{\rm sample}(B)>\tfrac12\ \Longrightarrow\ \boxed{\text{瓶颈＝证书松弛}\ \text{而非}\ m_5<\tfrac12}✓✓$$
$$\qquad \textbf{反之}✗：\text{若 pending 箱的真实局部上确界也}\ \le\tfrac12\ \Longrightarrow\ \textbf{必须重审 M=5 命题本身}✗，\text{不得简单归因证书松弛}✗✓$$

$$\textbf{审计本档要点}✓：\text{记录}\ \#\{L<\tfrac12\},\ \#\{U_{\rm sample}>\tfrac12\},\ \text{间隙分布}、\text{箱宽与深度分布}✓$$

## §4 工程限制（**诚实记录**✓）

$$\textbf{限制}✗：\text{v4 停止时【只保留计数器】}，\textbf{未落盘 pending 箱}✗ \Longrightarrow \text{「抽取那 226,948 箱」必须}\textbf{重放搜索}✗$$
$$\text{本次处置}✓：\textbf{预算降至 800 万重放 ＋ 落盘}（\text{pending 同性质、可审间隙}✓），\text{遵守「不重跑 20M」}✓$$
$$\qquad \text{已加落盘分支}✓（\text{仅预算耗尽处}）\ \text{—— 属工程改动，不改数学}✓$$

### §4.1 账本钉死（**226,948 的来源**✓✓，2026-09-21 09:36）

$$\textbf{写入点}✓（\texttt{rpm\_certificate\_v4.py}）：\text{L108（pending 超内存）}✗、\text{L114（}\textbf{预算终止}✓）、\text{L139（深度} \ge 80）✗$$
$$\textbf{全程进度行均显示}\ \texttt{unres=0}✓ \Longrightarrow \text{L139 路径}\textbf{一次未走}✗ \Longrightarrow \text{无隐藏认证失败}✓✓$$
$$\textbf{超装机制}✓（\text{L110–111}）：\texttt{while pending and cnt < BATCH: pop()} \text{先判后弹}⟹ \text{末项可远大于}\ BATCH=150000✗$$
$$\textbf{精确对上}✓：\text{最后进度}\ \texttt{neval=19971000, pend=447090}✓；\text{弹出}\ 226{,}948 \text{箱}⟹ \texttt{19971000+226948+下一项}>20{,}000{,}000 ⟹ \text{触发 L114}✓✓$$
$$\boxed{\text{未决（全量）}=447{,}090✓；\text{未决（报告值）}=226{,}948✓；\textbf{差值}\ 220{,}142\ \textbf{未计入}✗（\text{记账口径}✓）}$$
$$\textbf{交叉验证}✓✓：\text{① 体积缺口}\ 26.53 \text{对应}\ 447{,}090\ \text{箱}✓（\text{非}\ 226{,}948✗）；\text{② 全程}\ \texttt{unres=0}⟹ \text{每箱要么认证、要么分裂}✓$$

### §4.2 正式状态与预注册实验（**下一刀**✓）

$$\boxed{\text{M=5/0.5：}\ \textbf{SEARCH-BUDGET LIMITED}✓；\textbf{failure mode 未定}✓（\text{非 FAIL}✗）}$$
$$\textbf{预注册单次实验}✓：M=5,\ \text{target}=0.5,\ \textbf{budget}=60M✓（\text{非}\ 100M✗）$$
$$\qquad \text{理由}✓：60M \text{同时回答两问 —— ① 是否只是预算不足}✓；\text{② 实际总成本量级}✓；\text{若仍未闭合，再据实测}\ \texttt{neval/depth/pending}\ \text{定下一步}✓$$
$$\qquad \textbf{不动}✗：\text{不改数学模型}✓、\text{不跑慢版}✓、\text{不跑}\ M=6\text{–}11✗$$

## §5 纪律（锁定 ✓）

$$\boxed{\text{M=5 主搜索}\ \textbf{STOP}✗ \rightarrow \text{只审 pending 箱 failure mode}✓ \rightarrow \text{再定下一版证书}}$$
$$\qquad \textbf{不提预算}✗、\textbf{不跑慢版}✗、\textbf{不跑}\ M=6\text{–}11✗$$

$$\textbf{本刀的价值}✓✓：\text{若证实 max–min 间隙} \Longrightarrow \text{下一版 v5 应给箱证书加入}\textbf{共享}\ k／\text{相位信息}✓，\text{逼近}\ \min_B\max_k\ \text{而非继续堆}\ \max_k\min_B✓$$

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**✓）

```
技术词 认证间隙     命中文件数=0    ::
技术词 交换损失     命中文件数=0    ::
技术词 待审箱诊断   命中文件数=0    ::
```
$$\textbf{① 本档新增}✓：\text{三项各 0 命中} \Longrightarrow \textbf{本档首次命名}✓$$
$$\textbf{② 档案已有（引用）}✓✓：\text{最大最小交换}✓（\text{经典}✓）；\text{分离式下界}✓（\S2\quad \text{等式}✓）；\text{pending 落盘}✓（\S4\ \text{工程}✓）；\text{体积缺口}✓（\S1✓）$$

## §7 边界

$$\textbf{① 本档为状态记录 ＋ 诊断协议}✓，\text{不产定理}✗，\text{不跑计算}✗（\text{重放属抽取数据}✓）$$
$$\textbf{② 未用 RH}✓；\text{未改他档正本}✓；\text{未改动数学模型}✓（\text{仅加落盘分支}✓）$$
$$\textbf{③ 不判 M=5 命题真伪}✗（\text{这正是}\ \S3\ \text{要查的}✓）；\text{不声称交换间隙已被证实}✗（\text{当前是}\ \textbf{failure-mode hypothesis}✓）$$
$$\textbf{④ }m_5\ \text{真值未定}✗：\text{档案}\ \text{E4-ENGINE-1}\ \text{的} \approx1.27\ \text{为}\textbf{爬山启发式}✗，\text{不可作依据}✓；\text{本档仅记「认证区已下探到}\ 0.5000182✓」$$
$$\textbf{⑤ }\texttt{C-181}\ \text{的}\ u\le5\ \text{仍为}\ \text{GAP-A}\ ✗（\texttt{C-270}✓），\text{本档不改变该结论}✓$$
