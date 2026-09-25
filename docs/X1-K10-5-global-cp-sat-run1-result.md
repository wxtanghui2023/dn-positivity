已查地图：命中（`X1-K10-4-global-cp-sat-launch`）⟹ `X1` 第五轮：全局 CP-SAT 首轮结果，不开新案
D0: 本档对象 = **全局 `Σx=119` CP-SAT 首轮（3600s）结果**：`status=UNKNOWN`／`incumbent=0`／无 UNSAT 证书 ＋ **solver summary 原样** ＋ **搜索轨迹诊断（LP 松弛平凡可行 ⟹ 无剪枝）** ＋ **判定树锁死** ＋ **运维教训（cron 投递失败）**
D1: 1（实际计算；全局搜索完成一轮）
[RESEARCH]

# **全局 CP-SAT 首轮结果（3600 s）**

## §0 判定（锁死）

```
$$\boxed{\text{未找到 119-cover}};\quad status=\textbf{UNKNOWN};\quad \text{预算用尽};\quad \textbf{无}\ \text{UNSAT 证书};\quad \textbf{无}\ \text{best bound}$$
$$\boxed{\text{允许表述}:\ \text{“全局 CP-SAT 在给定模型/对称性/预算下未找到 119”}}$$
$$\boxed{\textbf{禁止}:\ \text{“119 不存在”}\ (\text{需 UNSAT 证书或独立数学下界 120})}$$
```

## §1 `CpSolverResponse summary`（原样）

```
status: UNKNOWN
objective: NA
best_bound: NA
integers: 1083
booleans: 1023
conflicts: 24511331
branches: 63431966
propagations: 1450458064
integer_propagations: 3778681017
restarts: 5569
lp_iterations: 74032
walltime: 3600.07
usertime: 3600.07
deterministic_time: 17423.2
gap_integral: 0
```
$$\text{另}:\ \texttt{[incumbent]}\ \text{出现}\ \boxed{0}\ \text{次};\quad \texttt{code119\_GLOBAL.json}\ \text{未生成};\quad \text{子求解器}:\ \texttt{default\_lp},\ \texttt{max\_lp\_sym},\ \texttt{no\_lp},\ \texttt{fj},\ \texttt{feasibility\_pump},\ \texttt{rins/rens}$$
```

## §2 搜索轨迹诊断（**核心读数**）

```
$$\textbf{(1) 整解一个都没找到}:\ \text{在 } \Sigma x=119\ \text{固定下，任何可行整解}\ \textbf{就是}\ \text{一个 119-cover};\ \text{一轮 }3600\ \text{s 内}\ \boxed{\text{incumbent}=0}\ \Longrightarrow\ \text{连“较差但可行”的解也没有}$$
$$\textbf{(2) 纯冲突驱动}:\ \text{conflicts } 2.45\times10^7,\ \text{propagations } 1.45\times10^9,\ \text{branches } 6.34\times10^7,\ \text{restarts } 5569\ ——\ \text{典型“无梯度引导”的组合搜索画像}$$
$$\textbf{(3) LP 为何帮不上（本模型的结构原因，本轮独立得出）}:$$
$$\qquad \text{取均匀分数解}\ x_c=119/1024\ \text{对全部 }1024\ \text{个字}:\quad \sum_c x_c=119\ \checkmark;\quad \text{每顶点被覆盖}\ 11\cdot\tfrac{119}{1024}=1.278\ge1\ \checkmark$$
$$\qquad \Longrightarrow\ \boxed{\text{LP 松弛\textbf{平凡可行}},\ \text{故 LP 界无法否证 }119}\ \Longrightarrow\ \text{LP 子求解器几乎无剪枝能力（}lp\_iterations=74{,}032\ \text{偏低}）$$
$$\qquad \Longrightarrow\ \text{问题在此模型下是}\textbf{纯组合的};\ \text{要提升，需换}\ \textbf{搜索策略或引导}，\text{而非指望 LP 界}$$
$$\textbf{(4) 与前三层的关系}:\ \text{局部刚性证书（}(1,1)/(2,1)/(3,2)\text{）独立成立，}\textbf{不因全局未找到而作废};\ \text{二者是不同层级的结果} ✓$$
```

## §3 本轮交付 / 未交付

```
$$\textbf{交付}:\ \text{① 全局精确模型（可复现）};\ \text{② 一轮 }3600\ \text{s 全局搜索的完整统计};\ \text{③ LP 平凡可行的结构诊断};\ \text{④ incumbent 独立验证出口（全程 }0\ \text{误报，纪律有效）}$$
$$\textbf{未交付}:\ \text{119-cover 证书};\ \text{UNSAT 证书};\ \text{任何下界改进}$$
```

## §4 下一刀（三选，**待先生裁**）

```
$$\text{(B1)}\ \text{换搜索策略（同模型）}:\ \text{如 }\texttt{no\_lp}\ \text{专项、不同 }\texttt{random\_seed}/workers\ \text{配比、}\texttt{use\_lns}\ \text{强化、或 }\texttt{add\_assumptions}\ \text{分层};\ \text{仍解同一可行性问题}$$
$$\text{(B2)}\ \text{固定 }\Sigma x=119\ \text{＋最小未覆盖为 secondary objective}:\ \text{给出}\ \textbf{梯度式引导};\ \textbf{注意}:\ \text{这解的是}\boxed{\text{不同的优化问题}},\ \text{其 incumbent 只能说明“缺口尽可能小”，}\textbf{不构成可行性证明}\ (\text{先生已指出})$$
$$\text{(B3)}\ \text{受控 global diversification}:\ \text{用 120-码结构做定向扰动/重启生成器，仍保持全局（不受限邻域）}$$
$$\textbf{不建议}:\ (4,3)\ \text{局部邻域（与全局实验混层，降低信息量）}$$
```

## §5 ⚠️ 运维教训（本轮真实故障，须记）

```
$$\text{现象}:\ \text{00:40 定时汇报}\ \textbf{未送达};\ \text{用户次日晨才察觉}$$
$$\text{根因}:\ \text{cron 任务 }\texttt{delivery.mode="announce"}\ \text{且}\ \textbf{未指定 }channel/to\ \Longrightarrow\ \text{路由到 }\texttt{last}\ \text{（Feishu）}\ \Longrightarrow\ \texttt{"Delivering to Feishu requires target"}\ \text{投递失败}$$
$$\textbf{修复（今后约定）}:\ \text{① 定时汇报一律用 }\boxed{\texttt{sessionTarget="current"}}\ \text{（绑本会话，回复直接落本对话）};\ \text{② 或显式写 }\texttt{delivery.channel="webchat"}\ \text{并给 }to;\ \text{③ 任务须能自检投递（失败时告警）}$$
【⛔ 纪律】 未改模型、未启动新搜索、未装新包 ✓
【边界】 记录 }[107,120]\ \text{取自 OEIS（抽取级）；本轮数值均为本地实测} ✓
