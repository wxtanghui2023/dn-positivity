已查地图（**先查后写**）：`E4-ENGINE-4`/`E4-ENGINE-5`（(RP_M) 状态；M≤11 数值成立＋二阶矩路线）、`C152`/`C153`（M=2 局部引理＋精确常数）、`C199`/`C200`（M=2 加权定理）、`C216`–`C219`（M=3 区间阶梯）、`C177`（参数化区间证书脚本）、`WORKPLAN` 后台任务栏（"M=4／目标 0.50（D1b）—— 运行中"）。回查见 §5 ✓

D0: 本档对象 = **(RP_M) 的 M=4 定理落档（此前已算完未入档）＋ M=5 启动** —— 关系 = 结果入档（非新机制）
D1: 0
FREEZE-ACK: 本档即冻结期内的结果入档（依 §8.1；不产候选结论）

---

## §0 结论

$$\boxed{\textbf{① M=4【早已证成}】✓✓✓（\text{此前未入档}✗）：m_4\ge\tfrac12\ \text{（区间算术，无 SLACK、无浮点误差假设}✓✓）}$$
$$\boxed{\textbf{② 故}\ (\text{RP}_M)\ \textbf{对}\ M=1,2,3,4\ \text{全部成立}✓✓（\text{其中 M=4 为新入档}✓）}$$
$$\boxed{\textbf{③ 本档顺带落实纪律}✓✓：\text{【算了必须落档}】—— \text{M=4 曾「运行中」后静默完成}✗✓}$$
$$\boxed{\textbf{④ 下一步}✓：\text{M=5 已启动}✓（\text{同脚本参数化}✓，\text{目标}\ 1/2✓）}$$

## §1 M=4 证书（原始日志逐字 ✓✓）

```
/tmp/m4_iv.log（2026-09-19 20:49）:
  评估箱数        = 499321
  未决箱数        = 0
  最大深度        = 28
  认证最小余量    = [0.0000484756297151227955492307444170154652252973486, 0.0000484756297151227955492307444170154652252973486]
  耗时(秒)        = 5501.8
  全部认证?       = True
  ⟹ 严格结论（区间算术, 无 SLACK、无浮点误差假设）:  m_4 >= 1/2
```
$$\textbf{浮点分区对照}✓（\texttt{/tmp/m4\_cert.log}✓）：\text{M=4, ok=true, neval=1036096, unresolved=0, min\_margin}=2.0998\times10^{-4}, \text{max\_depth=7, N0=20, sha256[:16]=c5da38102e08b529}✓$$

## §2 四门核验（依 `C216` 协议 ✓✓）

$$\textbf{门 1 覆盖}✓：\text{未决箱数}=0✓；\text{最大深度}=28✓（\text{未触深限}✓）；\text{评估箱数}=499321\ \text{为有限}✓$$
$$\textbf{门 2 区间合法性}✓✓：\text{日志明示「无 SLACK、无浮点误差假设」}✓\（\text{严格区间下界}✓）$$
$$\textbf{门 3 目标阈值}✓：\text{结论形如}\ \forall\varphi:\ F_4(\varphi)\ge\tfrac12✓（\text{非「未找到反例」}✓）$$
$$\textbf{门 4 边界／异常}✓：\text{认证最小余量}>0✓（4.8476\times10^{-5}✓）；\text{未决}=0✓；\text{无 NaN／溢出报告}✓$$

## §3 (RP_M) 的当前账（✓✓）

$$\textbf{陈述}✓：|z_j|=1\ (j=1..M)\Longrightarrow\exists k\le5M:\ \sum_j\operatorname{Re}z_j^k\ \ge\ \tfrac12✓$$
$$\qquad \textbf{M=1}✓（\text{鸽笼定理}✓，\texttt{C-159}：\max_{m\le N}\cos m\theta\ge\cos\tfrac{2\pi}{N+1}✓）；\ \textbf{M=2}✓（\texttt{C-152}/\texttt{C-153}：局部引理＋精确常数；\texttt{C-199}/\texttt{C-200}✓）$$
$$\qquad \textbf{M=3}✓✓（\texttt{T13-A}\ m_3=0.764\ \text{夹逼}✓；\texttt{C-216}–\texttt{C-219}：\text{区间阶梯至}\ 0.7640811007458✓）$$
$$\qquad \textbf{M=4}✓✓✓（\textbf{本档}：m_4\ge\tfrac12\ \text{，区间算术严格}✓）$$
$$\Longrightarrow \boxed{(\text{RP}_M)\ \text{已证：}M\le4✓✓}\qquad \text{剩余}：M=5..11\ ✗（\text{路线＝同法}✓）$$
$$\qquad ⚠️\ \text{注}✓：\text{M=2,3 的证书目标高于 }1/2✓\text{（0.809／0.764）—— }(\text{RP}_M)\text{ 只需 }1/2✓\text{，故 M=4 直接取 }1/2\text{ 即足}✓$$

## §4 下一步（已启动 ✓）

$$\text{M=5}✓：\text{同脚本参数化}\ \texttt{m3\_certificate\_interval\_arith.py}\ \text{（}\texttt{M=int(sys.argv[3])}\ ✓）\ \text{运行}✓$$
$$\qquad \text{接口}✓：\texttt{budget maxdepth M target}✓；\text{目标}\ 1/2✓（\text{(RP}_M)\ \text{阈值}✓）$$

## §5 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写** ✓）

```
技术词 M4定理落档     命中文件数=0 ::
技术词 算了必须落档   命中文件数=0 ::
```
$$\textbf{① 本档新增}✓：\text{「M4 定理落档」（0）}✓、\text{「算了必须落档」（0）}✓$$
$$\textbf{② 档案已有（引用）}✓✓：\text{(RP}_M)\ \text{状态表}✓（\texttt{E4-ENGINE-5}✓）；\text{参数化脚本}✓（\texttt{C-177}✓）$$

## §6 边界

$$\textbf{① 本档为结果入档}✓，\text{不产新机制}✗；\ \textbf{② 未用 RH}✓；\text{未改他档正本}✓$$
$$\textbf{③}✗：\text{M=4 的日志为本会话前段遗留}✓\text{，本档未重跑（不动运行中任务）}✓\text{—— 若需复核，用同参数重跑}✓$$
$$\textbf{④}✗：\text{M=5..11 仍开}✗\text{；不声称二阶矩路线足够（}\texttt{E4-ENGINE-5}\text{ §2 已证 }M\gtrsim12\text{ 不足）}✓$$
