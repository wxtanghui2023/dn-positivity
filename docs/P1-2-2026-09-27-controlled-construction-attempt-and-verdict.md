已查地图：已跑 scripts/prework_map_check.sh switching 去重 (A₁,A₂) 分桶 ⟹ 执行自 `P1-2026-09-27-support-layer-screen-results`（✓）＋ 唐先生 12:33（受控构造实验 ✓）；本档 = **P1-2 受控构造实验：未能取得桶内多码 ⟹ Gate 仍 OPEN** ⚠️。
D0: 本档对象 = P1-2（固定 $(A_1,A_2)$ 桶内的 $J$ 分叉）的可测性
D1: 1（新增：**n=6 受控生成只出 2 类且 $(A_1,A_2)$ 各异 ✓**；**n=7 结构性无效的判定 ✓**）

# P1-2 受控构造实验（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(BB-1 n=6 受控生成 ✓)}\ \text{4000 次随机贪婪＋修复（95 s ✓）} \Longrightarrow \textbf{仅 2 个不等价类}:\ (A_1,A_2)=(4,8)\ \text{与}\ (0,12)\ \text{—— \textbf{互不相同}} ✗}$$
$$\qquad\Longrightarrow\ \textbf{无任何 }(A_1,A_2)\ \text{桶含 }\ge2\ \text{码} \Longrightarrow \textbf{P1-2 无法测试（vacuous）} ⚠️$$
$$\boxed{\textbf{(BB-2 n=7 结构性无效 ✓)}\ K(7,1)=16,\ E=0 \Longrightarrow \text{全部最小覆盖码} = \text{完美 1-码};\ \text{而 }n=7\ \text{完美 1-码\textbf{经典唯一（至等价）}} \Longrightarrow \textbf{单一同构类} ⟹ n=7\ \text{对分叉测试\textbf{无效}} ✗}$$
$$\boxed{\textbf{(BB-3 P1-2 判定 ⚠️)}\ \text{Gate}\ \textbf{未建立亦未否证}:\ \text{所有可用 }n\ (5,6,9)\ \text{的桶均 singleton} \Longrightarrow \textbf{测试空洞} ✓\ \text{（不是"发现塌缩" ✗）}$$
$$\boxed{\textbf{(BB-4 模式性证据（仅证据 ✓）)}\ \text{在每一处有 }\ge2\ \text{个最优码的 }n\ \text{上，它们\textbf{都}在 }(A_1,A_2)\ \text{上不同};\ n=5\ \text{的 320 码同类且全钉住} \Longrightarrow \text{与"}(A_1,A_2)\ \text{决定该类"一致 ✓ 但未证 ⚠️}}$$
$$
$$
```

---

## §1 实验记录（**✓ 本机**）

```
$$\text{生成器}:\ \text{随机贪婪（球覆盖优先 ✓）＋ 修复（去私有覆盖最少词再贪婪补全 ✓）};\ \text{去重} = \text{平移}\times\text{坐标置换规范形（}2^6\cdot6!=46080\ ✓\text{）}$$
$$\text{结果（n=6, K=12, tries=4000, 95 s ✓）}:\ \text{2 类} \left\{\ (A_1,A_2)=(4,8)\ \text{with}\ J_3=4;\quad (0,12)\ \text{with}\ J_3=0\ \right\}$$
$$\text{附加尝试（定向 switching）}:\ \text{plain 随机贪婪 6000 次\textbf{竟未复现 }(4,8)\ \text{种子} ⚠️\ \text{（说明该类别罕见，须走修复路径 ✓）} \Longrightarrow \text{定向 switching 未能启动} ✗$$
$$
$$
```

---

## §2 为何 Gate 无法关闭（**诊断 ✓**）

```
$$\text{要测 P1-2 需}:\ \exists C_i,C_j\ \text{with}\ (A_1,A_2)_i=(A_1,A_2)_j\ \text{且}\ \mathbf J(C_i)\ne\mathbf J(C_j)\ ✓$$
$$\text{现状}:\ n=5\ \text{（320 码，单类，}(2,4)\ ✓\text{）};\ n=6\ \text{（2 类，各异 ✓）};\ n=7\ \text{（单类 ✓）};\ n=9\ \text{（2 码，各异 ✓）}$$
$$\Longrightarrow\ \textbf{所有 }(A_1,A_2)\ \text{桶都是 singleton} \Longrightarrow \text{桶内比对\textbf{空转} ✗（不等于塌缩已证 ✓）}$$
$$\text{文献侧缺口（诚实 ✓）}:\ \text{我没有 }(6,12)\ \text{或 }(9,62)\ \text{最优覆盖码的完整分类表};\ \text{若文献有，可直接取多码建桶 ✓（下一步可查 ✓）}$$
$$
$$
```

---

## §3 按唐先生协议的分支判定（**✓**）

```
$$\text{协议 ✓}:\ \text{"若所有固定 }(A_1,A_2)\ \text{桶里的 support-2 fingerprint 都钉死 ⟹ 强方向性信号 ⟹ 跳到 2-face/triple"}$$
$$\text{本档实际}:\ \text{桶全为 singleton} \Longrightarrow \textbf{既非"钉死"亦非"分叉"} \Longrightarrow \text{该分支条件\textbf{未真正触发} ⚠️}$$
$$\text{但方向性上有两条可用读数 ✓}:\ \text{(i) 模式性证据偏向"(}A_1,A_2)\ \text{决定类"（§0 BB-4 ✓）};\ \text{(ii) 生成机器已到极限（}K(n,1)\ \text{型码稀有 ✓）}$$
$$\Longrightarrow\ \textbf{建议}:\ \text{(a) 先查文献/档案是否有 }(6,12)/(9,62)\ \text{的完整分类（可一举关闭 Gate ✓）};\ \text{(b) 若无，则按你原议\textbf{转 2-face/triple} ✓}$$
$$
$$
```

---

## §4 边界（诚实标注）

- §1 为**本机实验记录** ✓；§2–§3 为**诊断 ＋ 分支配对** ✓
- **未**声称 support 层塌缩 ✗（桶 singleton ⟹ 测试空洞 ✓）；**未**声称新机制 ✗；**未**改动 119 UNKNOWN ✓
- **未**跑未授权的大规模搜索／$n=10$ ✓（遵守 STOP ✓）
- ⚠️ 本档未产生 P1 candidate ✗（Gate P1-2 仍未关闭 ✓）

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：P1-2 受控构造实验记录、桶 singleton 诊断、n=7 结构性无效判定
- **档案已有（引用，不列为提出）**：separation pair、$A_1,A_2$、$K(n,1)$、完美码唯一性、G-PROGRESS


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 桶 singleton 诊断 命中文件数=1    :: ./P1-2-2026-09-27-controlled-construction-attempt-and-verdict.md 
技术词 受控构造实验 命中文件数=1    :: ./P1-2-2026-09-27-controlled-construction-attempt-and-verdict.md
```
- **本档新增**：P1-2 受控构造实验记录、桶 singleton 诊断、n=7 结构性无效判定（见上方命中数；0 命中者为自造语／内部标签 ✓）
