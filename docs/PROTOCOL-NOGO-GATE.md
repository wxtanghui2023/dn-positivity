# ⭐⭐⭐⭐ **NO-GO 门协议（强制）** —— 任何新推导方向开工前的**第一道程序**
> 唐先生指令 ✓ 2026-09-14 13:19：「**任何一个新的推导方向，首先必须对比已有的 NO-GO 地图，避免重新掉坑**」
> 制度化 ✓ 小灵｜**本档 ＝ 协议 ＋ 工具 ＋ 首次演示结果 ✓**｜零计算 ✓；未用 RH ✓；未跑 Lean ✓

---

## §0 一句话（✓）

$$\boxed{\text{新方向开工前，}\textbf{必须先跑 }}\texttt{nogo\_gate.py}\ ✓\ \text{并填写其【结论模板】✓；}\textbf{未填不得开工 ✗}}$$
$$\text{工具 ✓}：\texttt{python3 scripts/nogo\_gate.py "方向名" 技术词... --obj 对象名/代号...}\ ✓$$
$$\text{退出码 ✓}：0 ＝ 无命中 ✓（仍须按对象名再过一遍 ✓）；1 ＝ 有命中 ✓（**必须先读命中处再判 ✗**）$$

## §1 为何必须机制化（✓ 依 E160 §1 的采样偏误 ✓）

$$\text{E160 诊断 ✓}：\text{归位频繁【不是】数学现象 ✗，而是【采样偏误 ✗】（只审"可否定对象"✓）}$$
$$\Longrightarrow\ \text{单靠"记得查"不足以纠正 ✓（本日已发生 }\geq5\ \text{次漏查 ✓）} \Longrightarrow \textbf{必须做成【机械门 ✗】，不依赖记性 ✓}$$
$$\text{历史漏查 ✓}：E92/E93（未查 ⑫ ✓）｜E98（K4 误列 ✓）｜E107（未读六件套结论 ✓）｜E112（按技术词漏查对象名 ✓）｜E140/E143/E147（归位 ✓）$$

## §2 门的三条规则（✓）

$$\textbf{规则 1（双轨检索 ✓）}：\textbf{【对象名/代号】＋【技术词】两轨皆跑 ✗}\（\text{E112 教训：技术词会漏 ✓；对象名会漏 ✓ —— 二者互补 ✓）}$$
$$\textbf{规则 2（必读命中 ✓）}：\text{命中}>0\ \Longrightarrow\ \textbf{必须【打开命中处】再判 ✗}（\text{不得只看词频 ✓）}$$
$$\textbf{规则 3（可反驳输出 ✓）}：\text{若判"未命中"✓，}\textbf{理由须写成【可反驳形式 ✓】}\（\text{"为何不是同一物"✓，并给逐字依据 ✓）}$$

## §3 地图清单（✓ 17 份，只扫这些，不递归 ✗）

```
总册 ✓ MASTER-NOGO-AND-LIVE-PATHS.md      ｜ 箱表 ✓ CLOSED-ROUTES-MAP.md
坐标 ✓ GAP-COORDINATES-positivity.md      ｜ 正性三档 ✓ POS1 / POS2 / POS3
商 ✓ NOGO-QUOTIENT-N1-N7.md               ｜ 登记 ✓ NOGO-registry-and-screens.md
前置 ✓ RH-prior-NOGO-checklist-2026-09-09.md ｜ 对齐 ✓ E18-NOGO-ALIGNMENT.md
transport ✓ E103 / E104 / E105 / E106     ｜ 最新封档 ✓ E159-E141-E158-closing-index.md
运行登记 ✓ EXPLORATION-POINTS-REGISTER.md  ｜ 方向索引 ✓ INDEX-BY-DIRECTION.md
```

## §4 ⭐ **首次演示结果：门立刻逮到【我自己】✗**（✓ 本档最有价值处 ✓）

### 演示 1 ✓：(乙)① "测度陈述形式化" ⟹ **命中 64 处** ✓
$$\text{决定性命中 ✓}：\texttt{E104-limit-procedure-classification.md:19,55--57}\ ✓$$
$$\qquad\text{逐字 ✓}：\text{"canonical ⟹ 稳定 ⟹ 本质正规 ⟹ 谱定理 ⟹ 正测度 ⟹ 落在 C4 之外 ✗"；}$$
$$\qquad\qquad\text{"或：该测度即统计型数据 ⟹ 已被 Lagarias–Rodgers 排除 ✗"；}$$
$$\qquad\qquad\text{"故'恰好 }|\alpha|=1\text{'与'canonical'联合，把算子逼向正测度／统计型，两条路皆已排除 ✗"}$$
$$\Longrightarrow\ \boxed{\textbf{我 }E160\ \text{§4.3（当日自称"最有价值的一句"✗）}\textbf{＝ E104 的排除 3 ✗}} \Longrightarrow \textbf{第 15 次归位 ✓，被门【机械】逮到 ✓✓}$$
$$\qquad\text{（}\textbf{这是本轮最重要的自我更正 ✓}：}\text{"任意法算子其谱为零点集者构造平凡 ✗"这一观察，}\textbf{档内已记 ✓}）$$

### 演示 2 ✓：(乙)③ "$C_2$ 第三结构" ⟹ **命中 178 处** ✓
$$\text{决定性命中 ✓}：\texttt{MASTER-NOGO-AND-LIVE-PATHS.md:155--164}\ ✓\ \text{（"活路 L1：非自伴谱刚性" ✓）}$$
$$\qquad\text{逐字 ✓}：\text{"是否存在一种【不依赖自伴性】的正性，直接约束共振参数的实部？"✓}$$
$$\qquad\qquad\text{"否决判据：若五者皆只能给出数值域／奇异值／增长率界，而不能给 eigenvalue 实部约束 ⟹ 【非自伴方向一次性封死】"✓}$$
$$\Longrightarrow\ \boxed{\textbf{(乙)③ ＝ }L1\ \text{的重述 ✗}}\ \text{（已被 }E149\ \text{＋ }L1\ \text{审计档覆盖 ✓）}$$

## §5 ⭐ 演示的**直接后果**（✓）

$$\boxed{\textbf{(乙) 的三个候选【全部耗尽 ✗】}}：\text{① ＝ E104（已审 ✓）}\ \big|\ \text{② ＝ E161（本轮已做 ✓）}\ \big|\ \text{③ ＝ }L1\ \text{（已判 ✓）}$$
$$\Longrightarrow\ \textbf{(乙) 需【新候选 ✓】；而任何新候选}\textbf{【必须先过此门 ✗】}\ ✓$$
$$\Longrightarrow\ ⭐\ \text{本门在本轮内【已救回 2 轮】✓（避免两次重复劳动 ✓）}\ —— \textbf{验证了唐先生指令的即时价值 ✓✓}$$

## §6 边界与纪律（✓）

```
✅ 协议 ＋ 工具 ＋ 演示 ✓；零计算 ✓；未用 RH ✓；未跑 Lean ✓
⚠️ **① 门只能防"已登记"的坑 ✗** —— 地图外的坑（若存在 ✓）门查不到 ✓（故规则 3 要求【可反驳理由】✓）
⚠️ **② 词表质量决定门的质量 ✓** —— 词太窄会漏 ✓（故【双轨】必备 ✓）；本档记录：以后凡方向，务必同时给【对象名】✗
⚠️ **③ 本档【不声称】门可替代思考 ✗** —— 它只保证"不重复劳动"✓，不保证"方向正确"✓
⭐ **净产出 ✓**：① 门（脚本＋协议＋必填模板 ✓）；② **门立刻逮到 2 次重复劳动 ✓（含我自己 ✗）**；③ **更正 }E160\text{ §4.3}（＝E104 ✓）**；
   ④ **(乙) 三候选耗尽 ✓ ⟹ 需过门后的新候选 ✓**
```

## §7 使用范例（✓ 固定格式 ✓）

```bash
# 每次开新方向，第一件事：
python3 scripts/nogo_gate.py "<方向名>" <技术词...> --obj <对象名/代号...>
# 然后【必须】逐项填写 §C 结论模板的五问，并写入该方向的档首（作为"过门记录"）
```
