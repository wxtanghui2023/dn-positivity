已查地图：已跑 scripts/prework_map_check.sh 自检门 m=120 已知可行 ⟹ 续 `P2SEARCH-2026-09-27-119-directed-repair-spec.md`（规范 ✓）；本档 = **自检门失败记录（决定性 ✓）**。
D0: 本档对象 = 首轮实现的 m=120 自检门结果与归因
D1: 3（**自检门失败 ✗（连已知 120 码都找不到）**；**归因：机制太弱 ✗ 非数学结论 ✓**；**下一步＝可复现文献级搜索（reproduction 目标 ✓）**）

# 搜索自检门失败：m=120 找不到 ⟹ 机制太弱（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(UA-1 🔴自检门失败（决定性 ✓）)}\ \text{已知 }K(10,1)\le120\ \text{（历史构造 ✓）} \Longrightarrow m{=}120\ \text{时解\textbf{必然存在} ✓}$$
$$\qquad\text{实测（targeted repair ＋ tabu ＋ SA）}:\ m{=}120\ \text{六次 restart 的 best\_unc} = 34/28/34/28/31/25\ ✗\ \textbf{全部远未到 0} \Longrightarrow \boxed{\textbf{自检门 FAIL ✗}}$$
$$\qquad\Longrightarrow\ \boxed{\text{当前搜索机制\textbf{太弱} ✗}:\ \text{连已知可解的 }m{=}120\ \text{都解不出 ⟹ \textbf{不能}对 }m{=}119\ \text{作任何判断 ✗✓}}$$
$$\qquad\textbf{（对比 ✓）裸 SA }m{=}119:\ \text{best\_unc }=24\text{--}27\ ✗;\ \text{两半构造}:\ 124\ \text{词合法但不可约 ✗ ⟹ 三条实现路径均未达文献水准 ✓}$$
$$\boxed{\textbf{(UB-1 ⭐归因与正确读法)}\ \text{这不是数学结论 ✗，而是\textbf{实现/参数不足} ✓:\ 速度够（}\sim8\times10^3\text{--}2\times10^4\ \text{步/秒 ✓）但\textbf{邻域与能量设计不足} ✗}}$$
$$\qquad\text{可能缺口 ✓}:\ \text{① 能量只用 }|H|\ \text{（无二阶项／无"洞的分布"信息 ✗）；② 邻域只用 }"B_1(y)\ \text{中随机取 }c'"\ \text{（未做 }\arg\min\ \text{精确评估 ✗）；③ tabu tenure 固定随机 ⟹ 未调参 ✗；④ 无重启扰动策略／无种群 ✓}$$
$$\qquad\Longrightarrow\ \textbf{正确读法 ✓}:\ \boxed{\text{实现未过自检门 ⟹ 一切 }m{=}119\ \text{的"找不到"都\textbf{无效} ✗（红线保持 ✓）}}$$
$$\boxed{\textbf{(UC-1 ⭐下一步（reproduction 优先 ✓，与档案 L0/L1 纪律一致 ✓）)}\ \text{目标改为可复现}:\ \boxed{\text{先把 }m{=}120\ \text{搜到覆盖（}h{=}0\text{）}} \Longrightarrow \text{证明实现达到文献水准 ✓}$$
$$\qquad\text{达标后才做 }m{=}119\ ✓;\ \text{若 }m{=}120\ \text{长期搜不到 ⟹ 需升级为文献级实现（精确 }\arg\min\ \text{＋二阶能量＋tabu 调参＋模拟退火温度表 ✓）}$$
$$
$$
```

## §1 状态（**✓**）

```
$$\boxed{P0:\ K(10,1);\ P2:\ \le120\ (\text{历史 ✓});\ P1:\ \ge120\ \text{未证};\ \textbf{target}:\ \le119\ ✓}$$
$$\qquad\textbf{当前阶段 ✗}:\ \text{搜索实现\textbf{未过自检门} ⟹ 停在 reproduction 阶段（}\textbf{不产生任何 }P1/P2\ \text{结论} ✓\text{）}$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：自检门（m=120 已知可行）之失败记录与归因、三条实现路径之对比、reproduction 优先之下一步
- **档案已有（引用，不列为提出）**：A-P2SEARCH-1（规范四要素）、A-MIPRUN-1/2、21 条封口表、历史文献结论（唐先生 (甲) 核验 ✓）


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 自检门        命中文件数=7    :: ./B-2026-09-26-n9-construction-status-and-line-snapshot.md ./P2SEARCH-VALIDATION-2026-09-27-m120-gate-failed.md ./ASSETS-REGISTRY.md 
技术词 reproduction     命中文件数=6    :: ./P2SEARCH-VALIDATION-2026-09-27-m120-gate-failed.md ./LEVELS-2026-09-27-four-tier-separation-and-3B-pending.md ./E12-A3-5-bombieri-crosscheck.md
```
- **本档新增**：自检门（$m{=}120$ 已知可行）之失败记录与归因、三条实现路径对比、reproduction 优先下一步（见上方命中数；0 命中者为自造语／内部标签 ✓）


## §2 续：向下删＋修之瓶颈（2026-09-27 17:00+ ✓）

```
$$	extbf{(UD-1 诊断 ✓)}:\ 	ext{从 124 词码向下（删最无用者＋repair ✓）}:\ m{=}123\ 	ext{删 1 词产生 3 洞，}	extbf{两次 restart 卡在 3 洞 ✗（50s/次）}$$
$$\qquad	extbf{根因 ✓}:\ 	ext{124 词码	extbf{不可约}（每词有独有点 ✓）} \Longrightarrow 	ext{删一词后	extbf{移动任何他词都造新洞} ✗ ⟹ 	extbf{1-opt 邻域无解} ✗}$$
$$\qquad\Longrightarrow\ oxed{	ext{必须用	extbf{ruin \& recreate（LNS）}：随机删 }kpprox3	ext{--}8\ 	ext{词 ⟹ 贪心重覆盖（每洞取"覆盖面最大"的词 ✓）⟹ 补回词数 }<\ 	ext{删掉词数即下降 ✓✓}}$$
$$\qquad	ext{这与文献一致 ✓}:\ 	ext{Östergård 1997 明确指出其贡献即	extbf{新邻域函数} ✓ ⟹ 邻域设计是本问题的核心 ✓}$$
```
