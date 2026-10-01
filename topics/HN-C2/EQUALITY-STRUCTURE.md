已查地图：见 docs/TOPIC-INDEX.md（HN-C2 课题子档）
D0: 本档对象 = 等号结构理论推导（HN-C2 L4 路径 C 之稳定性分析）；非新数学值主张（结构定理）
D1: 0
ASSUMES: C(11,5,3)=20（库内已封闭精确值）｜C(10,4,2)=9（同）｜Schönheim 递归 $C(v,k,t)\ge\lceil\frac vkC(v-1,k-1,t-1)\rceil$

# EQUALITY-STRUCTURE — 若 $M{=}40$ 存在，其**等号结构**（理论推导 ✓ 未用计算）

## §0 递归取等之推导（Schönheim）

$$\\text{固定点 }x:\ \text{含 }x\\text{ 之块删去 }x\\Longrightarrow 11\\text{ 点上之 }5\\text{-块族, 覆盖全部 }3\\text{-子集}（\\text{因为}\\ \\forall T\\in\\binom{[12]\\setminus x}{3},\\{x\\}\\cup T\\ \\text{须被某块覆盖}）$$
$$\\Longrightarrow \\#\\{B\\ni x\\}\\ \\ge\\ C(11,5,3)=20\\ \\text{（库内精确值）};\\quad \\sum_x\\#\\{B\\ni x\\}=\\sum_B|B|=6M=240=12\\times20$$
$$\\boxed{\\text{故 }M{=}40\\ \\Longrightarrow\\ \\textbf{①每点恰在 20 块中（正则性）}；\\textbf{② }\\forall x,\\ \\text{派生设计}D_x:=\\{B\\setminus x: x\\in B\\}\\ \\text{为 20 块}\\ (11,5,3)\\ \\textbf{\\text{最优覆盖}}}\\ ✓$$

## §1 二阶取等（对 $D_x$ 再用一次递归）

$$\\text{在 }D_x\\ (11\\text{ 点},20\\text{ 块},5\\text{-块})\\ \\text{中固定 }y:\\ \\#\\{\\text{含}y\\text{之块}\\}\\ge C(10,4,2)=9;\\quad \\sum_y \\deg_{D_x}(y)=20\\times5=100=11\\times9+1$$
$$\\boxed{D_x\\ \\textbf{\\text{恰有一个 }10\\text{ 度点}，其余十点皆 }9\\text{ 度}}\\ ✓$$

## §2 由此得**原设计的配对结构**（关键 ✓）

$$\\text{设 }\\lambda(x,y):=\\#\\{B\\ni\\{x,y\\}\\}\\ \\text{（点对共现数）}。\\text{由 }§1,\\ \\deg_{D_x}10\\ \\text{之点 }y\\ \\text{满足 }\\lambda(x,y)=10,\\ \\text{其余 }z\\ \\text{满足 }\\lambda(x,z)=9$$
$$\\text{因 }\\lambda\\ \\text{对称}\\ \\Longrightarrow\\ \\textbf{f{:}x\\mapsto\\text{唯一 }10\\text{-伙伴}\\ \\text{是不动点自由的}\\ \\textbf{对合}}\\ \\Longrightarrow\\ 12\\text{ 点\\textbf{配成 6 个互不相交的"特对"}}$$
$$\\boxed{\\text{特对之内 }\\lambda=10;\\ \\text{特对之间 }\\lambda=9;\\quad 6\\times10+60\\times9=600=\\sum_B\\binom62=15\\times40\\ ✓\\ \\text{自洽}}$$

## §3 二阶一致性核验（**未发现矛盾** ⚠️）

$$\\text{特对内公共邻域：}\\sum_{\\text{特对}\\{x,x'\\}}\\lambda(x,x')=60\\ ;\\quad \\forall \\text{特对},\\ \\sum_{y\\notin\\{x,x'\\}}\\lambda(x,x',y)=10\\times4=40$$
$$\\text{逐块特对计数 }a_B\\in\\{0,1,2,3\\}\\ (\\text{特对互不相交}\\Rightarrow\\text{块内至多 3 对})\\ ;\\ \\sum_B a_B=60\\ (\\text{平均 }1.5,\\ \\text{上限 }3)\\ ✓\\ \\text{自洽}$$

## §4 现状裁定

$$\\textbf{路径 C（等号稳定性）＝ ALIVE ✓ 未得矛盾}；\\text{但已获\\textbf{强结构约束}}（正则性／6 特对／派生设计最优）：\\text{这些是}\\ 40\\text{-设计必须满足的\\textbf{必要条件}} ✓$$
$$\\text{下一刀二选一}：\\textbf{(a) 理论}：\\text{继续二阶/三阶整除性（特对与块交互的模约束}）;\\quad \\textbf{(b) 计算}：\\text{枚举 20 块}\\ (11,5,3)\\ \\text{最优设计（度型 }10,9^{10}\\text{）}＋\\text{"拼合"检验}$$

## §5 量级分析（照 2026-10-01 之三重前置制度 ✓）

| 计算步骤 | 规模 | 可行性 |
|---|---|---|
| 枚举全部 20 块 $(11,5,3)$ 最优设计 | 候选块 $C(11,5)=462$；选 20；朴素 $\\binom{462}{20}\\approx10^{30}$ | **难** ⚠️（须精确覆盖枚举＋同构约化） |
| 仅枚举**指定度型** $(10,9^{10})$ 者 | 约束更紧 | **中** ⚠️ |
| 拼合检验（12 个 $D_x$ 相容性） | 组合检验 | **中低** ⚠️ |

$$\\Longrightarrow\\ \\text{依制度：(b) 之前提（枚举可行）\\textbf{未被验证}} \\Longrightarrow\\ \\textbf{先做 (a) 理论}；\\text{仅当 (a) 无效再评估 (b)} ✓$$
