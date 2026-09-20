已查地图（**先查后写**）：查 `C-222`（B：X0 严格盒）、`C-221`（A：区间局部刚性）、`C-220`（闭合审计）、`C-216`（同规模成功运行）。回查见 §7 ✓

D0: 本档对象 = **C 的 capped diagnostic（frontier census）＋ 两个实现 bug 定位** —— 关系 = 把"箱数爆炸"判定为【实现问题】而非结构性墙，并留下可核查的 census 记录
D1: 0
FREEZE-ACK: 本档即冻结期内的收束与登记（依 §8.1；不产候选结论）

---

## §0 状态（严格区分"进程未结束"与"证明未完成"）

$$\boxed{\text{A：PASS}✓\quad \text{B：PASS}✓\quad \text{C-223 v1：STOP/FAIL（实现＋内存）✗}}$$
$$\qquad \text{v1 事实}：\text{RSS}\ 3.18\ \text{GB}✓，\text{宿主仅}\ 1.19\ \text{GB free}✗ \Longrightarrow \textbf{立即终止}✓（\text{保护宿主机}✓）$$
$$\qquad \text{v1 \textbf{不能作为任何下界证书}}✗✓（\text{含【静默丢弃】覆盖 bug}✓）$$

## §1 ⭐ 决定性诊断结论

$$\textbf{箱数爆炸是 100\% 实现问题}✗，\textbf{不是结构性墙}✓✓ —— \text{证据：修 bug 后 frontier 单调收缩至清零}✓，\text{最大深度}26✓，\text{总箱数}\ 66{,}564✓（\text{与历史同规模}\ 70{,}805\ \text{同量级}✓）$$

## §2 ⭐ 两个实现 bug（逐字）

$$\textbf{bug A（坐标维数）}✗✗：\texttt{/tmp/c222\_B.json}\ \text{的 box 含【7 坐标】}(\varphi_1\varphi_2\varphi_3\lambda_1\lambda_2\lambda_3\lambda_4)✓；$$
$$\qquad \text{误把 7 个全当}\ \varphi\ \text{求和}✗ \Longrightarrow F_3(X_0)=4.44215470\ldots✗（\text{应为}\ 0.7640811\ldots✓） \Longrightarrow T=4.4421647\ldots✗$$
$$\qquad \Longrightarrow \text{门槛高到天上}✗ \Longrightarrow \textbf{0\% 认证}✗ \Longrightarrow \text{frontier 每层翻倍}✗ \Longrightarrow \text{爆炸}✓$$
$$\qquad \text{修正}：\texttt{X0=[[float(a),float(b)] for a,b in d['box'][:3]]}✓$$

$$\textbf{bug B（决定性：numpy 版下界算错）}✗✗✗：$$
$$\qquad \texttt{nl=floor(a/}π\texttt{);\ nh=floor(b/}π\texttt{)}\ \textbf{✗ 应为}\ \texttt{ceil(a/}π\texttt{)}✗；\quad \texttt{odd=(nl==nh ? nl\%2==1 : True)}\ \textbf{✗ 判定逻辑亦错}✗$$
$$\qquad \Longrightarrow \text{任何【跨越}\ \pi\ \text{格线】的箱都被误判"含奇倍}\ \pi\text{"}✗ \Longrightarrow \text{强行置}\ \min\cos=-1✗ \Longrightarrow LB\ \textbf{被系统性压低}✗$$
$$\qquad \Longrightarrow \text{约 70\% 箱无法认证}✗ \Longrightarrow \text{frontier 倍增}✗ \Longrightarrow \text{爆炸}✓$$
$$\qquad \textbf{正确判定}✓：\text{区间}\ [a,b]\ \text{含奇倍}\ \pi \iff \exists\ \text{奇整数}\ m\in[\lceil a/\pi\rceil,\lfloor b/\pi\rfloor]✓；\text{含偶倍} \iff \exists\ \text{偶整数}✓$$
$$\qquad \qquad \text{实现：}\texttt{same=(nl==nh);\ res=where(same,\ nl\%2==\text{parity},\ nh-nl>=1);\ res\ \&\ (nl<=nh)}✓（\text{≥2 连续整数必含奇／偶}✓）$$
$$\qquad ⚠️\ \text{注}：\texttt{c221}/\texttt{c223}\ \text{的【mpmath 版】}\ \texttt{cos\_minmax}\ \text{用}\ \texttt{floor→ceil}\ \text{枚举并逐点判}\ \texttt{a<=t<=b}✓ \Longrightarrow \textbf{那版正确}✓（\text{仅 numpy 快版有此 bug}✓）$$

## §3 ⭐ Census（硬上限 2e6，未触发）

$$F_3(X_0)\ \text{浮点区间}\approx[0.76408110074585622318,\ \cdot]✓\ (\text{修好后}\approx0.76408✓);\qquad T=\sup F_3(X_0)+10^{-9}=0.76408110174585619490✓$$
$$\text{排除球}：6\ \text{个}\ S_3\ \text{轨道中心}✓，RB=\rho_{\rm up}-10^{-6}=1.4648\times10^{-3}✓；\text{球心互距}>10^{-3}✓；X_0\ \text{宽}\ll\rho_{\rm up}✓$$

| 层 | $N_{\rm in}$ | $N_{\rm cert}$ | $N_{\rm unres}$ | $N_{\rm split}$ | $N_{\rm disc}$ | frontier |
|---|---|---|---|---|---|---|
| 0 | 13824 | 4123 | 0 | 9701 | 0 | 9701 |
| ⋯ | | | | | | |
| 20 | 136 | 66 | 0 | 70 | 0 | 70 |
| 25 | 12 | 8 | 0 | 4 | 0 | 4 |
| 26 | 8 | 8 | 0 | 0 | 0 | **0** ✓ |

$$\textbf{累计}：\text{评估}\ 66{,}564✓；\text{认证}\ 40{,}156✓；\text{未决}\ \mathbf{0}✓✓；\text{分裂}\ 26{,}370✓；\text{丢弃}\ 38✓；\textbf{frontier 清零}✓✓$$

## §4 ⭐ 覆盖纪律（唐先生指定，硬性）

$$\boxed{\text{达到最小宽度的箱}\ \Longrightarrow\ \textbf{进入}\ \texttt{unresolved}\ \text{计数}✗\textbf{绝不静默丢弃}}✓✓$$
$$\qquad \text{本档实现}：\texttt{tiny=wmax<MINW}\ \text{单独统计并留存样本}✓（\text{本次}\ \texttt{minw}=10^{-13}✓ ⟹ \text{未决}\ 0✓）$$
$$\qquad \textbf{v1 的违规写法已撤销}✗：\texttt{d2=(w[:,j]>...);\ B=B[d2]}\ \text{会丢掉未证明的箱}✗（\text{v1 因此不能作为证书}✓）$$
$$\qquad \text{丢弃（\texttt{N\_disc}=38）仅指【整箱位于球内】}✓ \Longrightarrow \text{该区域由}\ \textbf{A}\ \text{覆盖}✓，\text{非由 B\&B 覆盖}✓（\text{须在证书里显式登记}✓）$$

## §5 仍缺什么（严格证书）

$$\textbf{① 区间版}✗：\text{本 diagnostic 是 float}✗ \Longrightarrow \text{终端箱须用【mpmath 区间】复核}✓（\text{按}\ \texttt{C-195}\ \text{速率：}\sim40{,}000\ \text{箱}\approx4\ \text{分钟}✓）$$
$$\textbf{② }T\ \text{的严格性}✗：T\ \text{现用 float}\ b_0✗ \Longrightarrow \text{须改为}\ X_0\ \text{上的【区间上界】}✓$$
$$\textbf{③ 域覆盖}✗：\text{须做精确有理体积核验}✓（\text{终端}＋\text{丢弃}＋\text{未决}=\text{全域}✓，\text{无重叠}✓）$$
$$\textbf{④ 排除球的严格性}✗：\text{球心}=\varphi_0\ \text{仅知在}\ X_0\ \text{内}✓ \Longrightarrow \text{须用}\ X_0\ \text{的包围盒保证}\ B(\varphi_0,\rho')\subseteq\text{所用球}✓$$
$$\qquad \text{⚠️ 未用 RH}✓；\text{未改他档}✓；\text{丙仍不开}✓$$

## §6 §0-§1 复述（防误用）

$$\text{进程未结束}\ \neq\ \text{证明未完成}✓✓；\qquad \textbf{本档只给 diagnostic，不给证书}✗；\qquad \textbf{不宣布 T13-A 全局闭合}✗✓$$

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 覆盖纪律     命中文件数=1    ::  ./C223-C-diagnostic-two-implementation-bugs-frontier-census.md
技术词 静默丢弃     命中文件数=1    ::  ./C223-C-diagnostic-two-implementation-bugs-frontier-census.md
技术词 下界压低     命中文件数=1    ::  ./C223-C-diagnostic-two-implementation-bugs-frontier-census.md
```
⚠️ 实测各 1 命中且均为本档自身（检查在落档后执行）✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）

## §8 下一刀（严格证书）

$$\text{① 把 diagnostic 的【正确】判定移植进区间版}✓（\text{用 mpmath 版}\ \texttt{cos\_minmax}✓，\text{那版本已正确}✓）；\text{② 区间上界定}\ T✓；\text{③ 精确有理体积核验}✓；\text{④ 终端箱区间复核}✓$$
$$\qquad \text{完成后才可写：}\forall\varphi\notin\bigcup_\sigma B(\sigma\varphi_0,\rho')⟹F_3(\varphi)>F_3(\varphi_0)✓ \Longrightarrow\text{再由 A 得局部严格极小}✓ \Longrightarrow m_3=F_3(\varphi_0)✓✓$$
