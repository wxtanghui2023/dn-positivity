已查地图：命中（本档更正 `LJCR-B1-batch-E4-audit-and-cell243-RESOLVED.md` 与 `B-LJCR-1-E4-result-and-ledger-fix.md`）
D0: 本档对象 = **语义越界更正**：CXS 指数界只约束 **skew Hadamard** 子问题，而 LJCR 数据库问的是**一般差集**存在性
D1: 0（核验/更正型）
[REVIEW]

# **ERRATUM：`B-LJCR-1` 的"已判 `No`"结论越界**（语义层 F-4）

## §1 发生了什么（自查发现）

```
$$\text{我此前记}:\ \boxed{DS(243,121,60,[3,9,9])\ \text{由 CXS 指数界判 }No}\ \text{并据此批量判 }74\ \text{格}$$
$$\text{触发自查的\textbf{信号}}:\ \text{把"abelian skew Hadamard 要求 }v=p^m" \text{套到全库} \Longrightarrow \textbf{44 个 }Yes\ \text{格且 }v\ \text{非素数幂} \Longrightarrow \text{与定理预测冲突}$$
$$\text{追查语义后确认真相}:\ \boxed{\text{数据库问的不是 skew，而是一般差集}}$$
```

## §2 决定性证据（数据库自身定义，逐字）

`work/ljcr/unz/difference-sets-main/README.md` 逐字：
> *"A (v,k,λ)-difference set in a group G is a subset D = {d_1,...,d_k} of G such that each nonzero element of G can each be represented as a difference (d_i − d_j) in exactly λ different ways."*

⟹ **定义中无 skew 条件** ✓；数据库自述 "possible parameters for difference sets in abelian groups G … an attempt has been made to include all known difference sets"。

**旁证（数据库自身数据）**：44 个 `Yes` 且 v 非素数幂的 SHDS 型格，其 comment 为具体**非 skew** 构造：
```
DS(575,287,143,[5,115])      comment=TPP(23)
DS(675,337,168,[3,15,15])    comment=TPP(25)
DS(2047,1023,511,[2047])     comment=(10,2) Singer
DS(4095,2047,1023,[4095])    comment=(11,2) Singer
DS(1763,881,440,[1763])      comment=TPP(41)
```
（TPP = twin prime power；Singer = 射影几何构造；两者皆**一般差集**）

## §3 更正后的正确结论

```
$$\textbf{① skew 子问题（我们此前锁定的重述对象）}:\ \boxed{\text{已判 }No}\ \text{（CXS 1994／Schmidt Thm 4.4／Ding–Wang–Xiang 2007 Thm 1.1，双源）} ✓$$
$$\qquad Z_3{\times}Z_9{\times}Z_9\ \text{不存在\textbf{skew Hadamard} 差集（等价：不存在以 }G\text{ 为正则自同构群的 DRT）} ✓$$
$$\textbf{② 数据库的那一格（一般差集存在性）}:\ \boxed{\textbf{仍未解决（Open）}}\ \text{—— CXS 不适用} ✗\ \text{（我此前的"判 }No"\textbf{越界}）}$$
$$\textbf{③ 74 格批量结论}:\ \boxed{\text{作为"数据库更正"无效，予以撤回}};\ \text{仅保留为"\textbf{skew 子问题批量判定}"（对该子问题成立）}$$
$$\textbf{④ 参数合法性}:\ \text{该格通过数据库所载基本检验（counting／Schützenberger／BRC）} \Longrightarrow \text{数据库留下 }Open\ \text{无误}$$
```

## §4 教训（制度级）

```
$$\boxed{\text{新故障模式 }F4\text{-}s:\ \text{定理的\textbf{问题语义}与被审计数据源的\textbf{问题语义}不一致}}$$
$$\qquad \text{形式}:\ \exists T:\ T\ \text{约束 }Q_{\rm sub}(C),\ \text{但数据源问 }Q_{\rm src}(C)\ \text{且}\ Q_{\rm sub}\neq Q_{\rm src}\ \Longrightarrow\ \text{不可用该定理判 }No$$
$$\textbf{捕捉机制（已验证有效）}:\ \boxed{\text{把定理的预测\textbf{回灌}数据库自身的 }Yes\ \text{格};\ \text{若冲突}\Longrightarrow\text{语义不匹配（先怀疑自己，非定理有误）}}$$
$$\textbf{本次即由此捕捉}:\ 44\ \text{个 }Yes\ \land v\ \text{非素数幂} \Longrightarrow \text{追查 README} \Longrightarrow \text{确认语义越界} ✓$$
```

**新增制度（见 `RESEARCH-CONSTITUTION` AMEND-28 §7）**：**E4-0 语义闸** —— 任何"上位定理判 `No`"之前，必须先逐字锁定**数据源的问题定义**与**定理的问题定义**，二者不一致者禁止使用。

## §5 边界（诚实）

```
(i)\ \text{本更正\textbf{不改动} CXS 双源证据的有效性};\ \text{仅更正其\textbf{适用范围}}
(ii)\ \text{一般差集版本的批量审计\textbf{尚未做}};\ \text{其正确工具是 Turyn 型指数界／Camion–Mann／Johnsen 等（\textbf{待取原文并逐字锁定}）}
(iii)\ \textbf{不声称}该格"已解决"或"无法解决"；其一般差集状态维持 \boxed{Open}
```
