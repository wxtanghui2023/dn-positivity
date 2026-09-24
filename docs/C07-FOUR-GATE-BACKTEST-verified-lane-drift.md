已查地图：命中（`WHY-POOL-EMPTY-intake-and-lane-diagnosis` ＋ `S2-C07-STAGE-REPORT-CLOSED`）⟹ 回溯核验，不开新案
D0: 本档对象 = **`C07` 四闸回溯核验（零计算）**：逐闸判定 ＋ **结论（错配由推断升级为已核验）** ＋ **`AMEND-23` 双轨入口架构** ＋ 记录缺口可得性新要求
D1: 0（架构实验型，零计算）
[REVIEW]

# **`C07` 四闸回溯核验**

## §0 被回溯对象（逐字取自结案档）

```
$$\textbf{C07} = \text{【}q\text{-ary 小参数 covering radius 表缺口】}（F5,P_4,\texttt{FT}）;\ \text{具体两格}:$$
$$\qquad t_2[19,9]=\boxed{4}\ (\textbf{档级}／外部:\ \text{Struik 下界＋球覆盖下界＋历史上界});$$
$$\qquad t_2[20,9]=\boxed{4}\ (\textbf{机器级}／\textbf{自有证书}:\ \text{显式 }11\times20\ \text{parity-check 矩阵，}R=4,\ \text{全 }2048\ \text{syndrome 覆盖},\ \text{下界 }1351<2048)$$
$$\textbf{可及表原记录}:\ (20,9)\ \text{格原记 }\boxed{4\text{-}5};\quad \textbf{未取得}:\ \text{《Covering Codes》Table 7.3}、\text{BPW 1989} \Longrightarrow (11,4)\ \text{格状态未知}$$
```

## §1 逐闸判定

```
$$\textbf{G1 独立问题}:\ \boxed{\textbf{PASS}}$$
$$\qquad \text{covering-radius 表格格＝独立编码论问题};\ \textbf{非 RH 变体};\ \textbf{非我方资产换壳}（\text{所用 }t\leftrightarrow\ell\ \text{对换为标准工具，非已有结论的重贴标签}）$$
$$\textbf{G2 新量}:\ \boxed{\textbf{FAIL}}$$
$$\qquad \text{量本身＝covering radius／覆盖码规模（古典）};\ \text{我方产出＝\textbf{显式构造＋证书}，}\textbf{无新不变量};$$
$$\qquad \text{两资产经查亦\textbf{非新量}}:\ A\ \text{证明链压缩＝标准对偶等价的重用（}\textbf{方法}）;\ B\ \text{计数张力非充分＝\textbf{方法学告诫}，非量}$$
$$\textbf{G3 可证明性}:\ \boxed{\textbf{PASS}}$$
$$\qquad P1\ \text{与}\ P2\ \textbf{正面碰撞}:\ \text{上界＝显式矩阵＋}2048\ \text{syndrome 全覆盖};\ \text{下界＝}1{+}20{+}190{+}1140=1351<2048\Rightarrow R\le3\ \text{不可能};$$
$$\qquad \text{双侧皆\textbf{有限、显式、可机器复核}（方法 A 组合枚举 6196／方法 B 按重量 BFS 分布一致）};\ \textbf{非开放式大搜索}$$
$$\textbf{G4 前沿新性}:\ \boxed{\textbf{WATCH}}$$
$$\qquad (20,9)\ \text{在可及表中原记 }4\text{-}5\Longrightarrow\textbf{记录缺口真实存在};\ \textbf{但}\ \text{现代权威表未取得} \Longrightarrow \text{无法判定"dent"还是"重验证"}$$
$$\qquad （\text{结案档 §5 已自设禁写：“文献从未有人做到”}）$$
```

## §2 ⭐ 结论：错配由**推断**升级为**已核验**

```
$$\boxed{C07:\ G1=\text{PASS},\quad G2=\boxed{\textbf{FAIL}},\quad G3=\text{PASS},\quad G4=\text{WATCH}}$$ ✓✓（\text{与先生预判一致}）
$$\Longrightarrow\ \textbf{现行四闸会把 }C07\ \textbf{DROP}$$ ⟹\ \text{而我方}\textbf{唯一实产出恰是 }C07$$
$$\textbf{精确定性（避免过度指控）}:\ \text{四闸\textbf{不是错误}，而是}\boxed{\textbf{作用域未声明}}\ ——\ \text{它实质是}\textbf{LANE-B（新机制）专用};\ \text{却被当作}\textbf{普适入口}使用}$$
$$\textbf{漂移链条}:\ \text{AMEND-10/11 双赛道（LANE-A 主力）}\to E\text{-gate}\to\text{HUNT}\to P1\text{–}P6\to\text{SURVIVOR-5}\to\text{四闸}\ \Longrightarrow\ \text{闸门逐步全部 LANE-B 化};\ \text{LANE-A 无对应闸门集}$$
$$\textbf{这正是"池为空"的架构原因}:\ \text{在 LANE-B 闸门下，}\textbf{凡不产新量者皆 DROP};\ \text{而我方可交付类型主要为 dent}\Longrightarrow\text{必然空池}$$
```

## §3 `AMEND-23`：双轨入口架构（正式拆轨）

```
$$\textbf{入口}:\ \boxed{\text{具名独立来源}\to\text{具体问题}\to\begin{cases}\text{LANE-A（dent）}\\\text{LANE-B（mechanism）}\end{cases}}$$ ✓✓
$$\textbf{LANE-A（dent）四闸}:\ \boxed{\text{① 明确记录缺口}\ \wedge\ \text{② 可机器验证}\ \wedge\ \text{③ 独立复核}\ \wedge\ \text{④ 非纯算力堆砌}}$$
$$\qquad \text{基准样本}:\ C07\ (\text{四闸全过})$$
$$\qquad \textbf{①的加严（本轮新增）}:\ \text{“明确记录缺口”须包含}\boxed{\text{权威记录源可得并已读}};\ \text{否则缺口仅算}\textbf{暂定}（C07\ \text{即栽在此：现代表未取得}）$$
$$\qquad \text{要求}:\ \text{证书可公开复验，并明确}\ \boxed{\text{旧记录／改进值／证明对象／验证脚本}}$$
$$\qquad \textbf{不要求}:\ \text{新机制／新不变量（此为 LANE-B 要求，不得混入）}$$
$$\textbf{LANE-B（mechanism）四闸}:\ \text{沿用现行}\ G1\to G2\to G3\to G4;\ \textbf{尤其保留 }G2$$
$$\qquad \text{功效证据}:\ G2\ \text{已成功杀掉 }C06/D03/M04/Au06/G06\ \text{整类“开放但无新量”伪机会}$$
$$\textbf{\textsc{amend-22} 作用域澄清（本轮）}:\ \text{它约束}\textbf{“进入候选池之后不得偷换对象/重新发明对象”}，\textbf{不约束来源};$$
$$\qquad \Longrightarrow\ \boxed{\text{\textsc{amend-22} 防重复投资};\ \text{HUNT-R3 负责供给};\ \text{二者非竞争关系}}$$ ✓✓
$$\textbf{HUNT-R3（供给端）}:\ \text{候选不再要求属于旧资产驱动 census};\ \text{改为具名独立来源（Erdős 问题库／动态综述未收割格／期刊问题栏／会议问题表）}\to\text{具体问题}\to\text{双轨分派}$$
【⛔ 纪律】 本轮**零计算、零新候选**；`U_{2,3}` 暂停；**不回 RH** ✓
【边界】 本档为**架构核验**（对单一历史样本）；不得据以宣称"四闸普遍无效"——其作用域为 LANE-B ✓
