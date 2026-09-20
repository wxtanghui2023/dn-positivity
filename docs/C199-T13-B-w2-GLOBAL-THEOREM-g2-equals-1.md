已查地图（**先查后写**）：查 `C-198`（远场探针）、`C-197`（局部引理 PROVED）、`C-196`（归约）、`C-194`（w=2 结构）。回查见 §6 ✓

D0: 本档对象 = **T13-B $w=2$ 的完整定理 $g_2(10)=1$**：远场两尺度自适应证书 ＋ 与 C-197 局部引理的合成 ＋ 等号集 —— 关系 = 新构造（把数值候选升级为定理）
D1: 0
FREEZE-ACK: 本档即冻结期内的收束与登记（依 §8.1；不产候选结论）

---

## §1 待证命题（唐先生锁定）

$$F(\delta_1,\delta_2)=\max_{1\le k\le10}S_k✓,\qquad S_k=2\cos(k\tfrac\pi3+k\delta_1)+\cos(k\tfrac\pi2+k\delta_2)✓$$
$$\textbf{目标}：F\ge1\ \ \forall\delta\in D✓,\qquad D:=[-\tfrac{P}3,\tfrac{2P}3]\times[-\tfrac P2,\tfrac P2]✓\supseteq\ \text{真域}\ [-\tfrac\pi3,\tfrac{2\pi}3]\times[-\tfrac\pi2,\tfrac\pi2]✓✓$$
$$\qquad （P\ \text{为}\ \pi\ \text{的有理上界}✓（P=3.14159265358979323847）\Longrightarrow \text{在超集上证明更强}✓）$$
$$\qquad ⚠️\ \textbf{锁死}：\text{C-198 的}\ 1.0194821\ \textbf{只是探针}✗，\textbf{不可} \text{写成}\ F\ge1.01948✗；\text{本档必须产出}\ F\ge1✓✓$$

## §2 设计：自适应两尺度（**不手划** A_boundary/A_bulk）

$$\text{每箱三分支}：\ \textbf{(i)}\ \text{箱整体落在闭球}\ B_{0.1}(0)\ \text{内}⟹\textbf{丢弃}✓（\text{由 C-197 覆盖}）✓；$$
$$\qquad\qquad\qquad \textbf{(ii)}\ \mathrm{LB}(\text{箱})\ge1⟹\textbf{认证}✓；\qquad \textbf{(iii)}\ \text{否则沿最宽维二分}✓$$
$$\mathrm{LB}(\text{箱})=\max_{k\le10}\Big[2\min_{\delta_1\in I_1}\cos(k\tfrac\pi3+k\delta_1)+\min_{\delta_2\in I_2}\cos(k\tfrac\pi2+k\delta_2)\Big]✓\ \le\ \min_{\text{箱}}\max_k S_k✓✓$$
$$\qquad （S_k\ \text{二维可分}⟹\text{逐坐标 min 精确}✓；\text{最远角判定闭球用精确有理}✓）$$
$$\Longrightarrow \textbf{两尺度结构由证明驱动自动出现}✓✓（\text{边界层细分、bulk 粗化}）✓$$

## §3 结果（脚本 `scripts/c199_farfield_certificate.py`）

$$\textbf{Phase1（float 建分区）}：N_0=40✓\ \text{评估}=1{,}922✓\ \text{终端认证}=1{,}759✓\ \text{球内丢弃}=2✓\ \text{深度}=9✓\ 0.11\ \mathrm{s}✓$$
$$\qquad \text{float 下界最小值}=1.000314949✓（\text{余量}+3.1495\times10^{-4}）✓\qquad \text{最小箱}\ \delta_1\in[0.067086,0.071995],\ \delta_2\in[0.098175,0.107992]✓$$
$$\qquad \textbf{两尺度自动结构}：\text{终端箱宽度}\ \min=2.454\times10^{-3}✓\ \text{中位}=7.854\times10^{-2}✓\ \max=7.854\times10^{-2}✓；\text{边界层（距原点}<0.25）66\ \text{箱}／\text{bulk}\ 1{,}693\ \text{箱}✓✓$$

$$\textbf{Phase2（区间算术验证，严格）}：\text{终端箱}\ 1{,}759✓\ \Longrightarrow\ \textbf{违反数}=0✓✓$$
$$\qquad \textbf{区间下界最小值}=1.000314949✓（\text{严格余量}+3.1495\times10^{-4}）✓\qquad 7.95\ \mathrm{s}✓$$

$$\textbf{Phase3（精确有理体积核对）}：\text{域}=9.869604401089✓,\ \text{终端}=9.857267395588✓,\ \text{丢弃}=0.012337005501✓$$
$$\qquad \text{终端}+\text{丢弃}=\text{域}\ \textbf{逐位相等}=\mathrm{True}✓✓\Longrightarrow \textbf{铺砌无孔无叠}✓✓$$

$$\Longrightarrow \boxed{F\ \ge\ 1\ \ \text{于}\ D\（\textbf{区间算术认证}）}✓✓$$

## §4 ⭐⭐ 合成定理

$$\text{远场}：F\ge1+3.1495\times10^{-4}>1\ \text{于全部终端箱}✓\（\text{覆盖}\ D\ \text{减 2 个球内箱}）✓$$
$$\text{球内}：\text{C-197 局部引理}\ \Longrightarrow\ F\ge1✓✓$$
$$\Longrightarrow \textbf{全域}\ F\ge1✓✓\qquad \text{又}\ (\delta_1,\delta_2)=(0,0)\ \text{即}\ (\varphi_1,\varphi_2)=(\tfrac\pi3,\tfrac\pi2)：F=2\cos\tfrac\pi3+\cos\tfrac\pi2=1✓\ \textbf{精确}✓$$
$$\boxed{\ g_2(10)\ =\ \inf_{\varphi}\max_{k\le10}\big[2\cos k\varphi_1+\cos k\varphi_2\big]\ =\ 1\ }✓✓\qquad \textbf{（Cassels 型加权家族 }w=2\text{ 的第一个完整定理）}✓✓$$

## §5 ⭐ 等号集（顺带得到，且比预期干净）

$$\text{终端箱上}\ \mathrm{LB}\ge1+3.15\times10^{-4}\Longrightarrow F>1\ \text{处处}✓✓ \Longrightarrow \text{等号点只能在【球内丢弃箱}／\text{球内}】✓$$
$$\text{球内（C-197）}：\text{区域}\ B'\ \text{内一维证书给严格余量}\ (\min\approx8.0\times10^{-11}>0)✓ \Longrightarrow F>1✓；\text{球内其余部分}\ S_6\ge1✓\ \text{且边界曲线}\ |{\sin3\delta_2}|=\sqrt2|{\sin3\delta_1}|\ \textbf{含于}\ B'✓$$
$$\qquad （\text{因}\ \sqrt2<\sqrt2/c=1.5567=K✓）\Longrightarrow \text{该曲线上} F>1✓✓$$
$$\Longrightarrow \boxed{\ \text{等号集}=\Big\{(\tfrac\pi3,\tfrac\pi2)\Big\}\ \textbf{单点}✓✓\ }$$
$$\qquad ⚠️\ \textbf{注意}：\text{交换点}\ (\tfrac\pi2,\tfrac\pi3)\ \textbf{不是} \text{等号点}✗（\text{权重不对称}：2\cos\tfrac{k\pi}2+\cos\tfrac{k\pi}3\ \text{在}\ k=1\ \text{仅}\ 0.5<1✓）✓$$

## §6 本档抓到并修掉的两处自我 bug

$$\textbf{bug ①}：\text{Phase2 的"含}\ \pi\ \text{奇数倍"检测写成}\ \texttt{range(n0-1,n1+2)}✗ \Longrightarrow \textbf{几乎必然命中}✗ \Longrightarrow \text{一律返回}-1✗ \Longrightarrow \text{报出 1,759 个假违反}✗$$
$$\qquad \Longrightarrow \text{改为紧检测}（\text{只查}\ [y_0,y_1]\ \text{内是否真有奇数整数}）✓ \Longrightarrow \textbf{违反骤降为 0}✓✓$$
$$\textbf{bug ②}：\text{报告行用}\ \texttt{Fraction.hypot}✗（\text{不存在}）\Longrightarrow \text{已修}✓$$
$$\qquad \textbf{教训}：\text{全违反与全通过一样都是红旗}✓✓；\text{两次均为实现错，非数学错}✓（\text{第}\ 14/15\ \text{次同类应验}）✓$$

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 两尺度自适应证书   命中文件数=1    ::  ./C199-T13-B-w2-GLOBAL-THEOREM-g2-equals-1.md
技术词 等号集单点         命中文件数=1    ::  ./C199-T13-B-w2-GLOBAL-THEOREM-g2-equals-1.md
```
⚠️ **实测各 1 命中，均为本档自身**（检查在落档后执行 ⟹ 必然自命中）✓ ⟹ **扣除后 0 命中** ⟹ 两项**本档首次命名** ✓（依 `C-168` §6 惯例 ✓）

## §8 边界

- Phase1 用 float **建分区**✓；**严格性全部由 Phase2 的区间算术承担**✓✓（端点精确有理✓，$\pi$ 取区间✓）
- Phase3 体积核对用**精确有理**（`Fraction`）✓ ⟹ 铺砌无孔无叠 ✓
- §5 等号集结论依赖：Phase2 的箱级严格余量 ✓ ＋ C-197 的球内严格余量 ✓ ＋ $\sqrt2<K$ ✓ ⟹ 结论**可靠**✓（但 §5 的表述仍属**推论**，非独立定理 ✓）
- 本档**未**声称 $w\ne2$ 的任何情形 ✓；**未**声称推广到 $M\ge3$ ✓
- **未用** RH；**未改**他档 ✓
