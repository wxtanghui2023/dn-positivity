# AOB5：$(+,\times,\mid)$ 内部事件的 compatibility defect —— **计算终审**

**依据**：唐先生 2026-09-11 09:54（未句：检查 $\operatorname{Ext}(h\overset{+}\to h')$ 与 $\operatorname{Ext}(h\overset{\times}\to h')$ 是否产生不可消去的高阶 defect；若被分配律消掉则宣布 $(+,\times,\mid)$ 历史边界无新相位）｜**约束**：无 $1/2$ 输入；L2 未动
**脚本**：`scripts/AOB5_internal_event_defect.py`（**先校准**；输出 `/tmp/aob5_out.txt`）｜标注：【核验】【引用】

---

## §0 校准（5/5 通过；含**两个自捉错误**）
```
[OK] x≡1(2),x≡2(3) ⟹ 5 mod 6 ｜ x≡0(2),x≡1(4) 不可解 ｜ x≡1(4),x≡2(6) 不可解
[OK] x≡1(4),x≡3(6) 【可解】（gcd=2，1≡3 mod 2 ✓，解 9,21,…） ｜ x≡1(2),1(3),1(5) ⟹ 1 mod 30
⚠️ ERR-1：我最初把 x≡1(4),x≡3(6) 误标为"不可解"（我的期望错，非代码错）—— 校准救回 ✓
⚠️ ERR-2：TEST A 初版搜索上限固定 5000 < lcm（可达 27720）⟹ 4 个假"不可解"反例
   修正为按 lcm 整周期搜索后 ⟹ 0 反例 ✓
```

## §1 【核验】TEST A：CRT 无高阶 obstruction —— **你的 §1 得到计算确认**
```
4000 组随机同余系统（k=2..5，模数 ≤12），每组在【整周期 lcm】上穷举
"可解 ⟺ 两两兼容" 一致率：4000/4000；两两兼容但不可解的【反例：0】
```
$$\boxed{\text{广义 CRT 的两两判据成立 ⟹ 兼容复形确是 flag complex ⟹ 无三体/四体新 obstruction}}$$
$$\boxed{\text{你的 }\S1\text{ 结论确认：CRT "因果性是真的，曲率不是真的" ✓}}$$

## §2 【核验】TEST B：两种延拓顺序的**精确**关系
$$\text{对有限集 }S:\quad (S+a)\cdot m=(S\cdot m)+(ma)\qquad\text{（312/312 精确集合恒等式）}$$
$$\boxed{\operatorname{Mul}_m\circ\operatorname{Add}_a=\operatorname{Add}_{ma}\circ\operatorname{Mul}_m\qquad\text{（分配律，精确）}}$$
⟹ 两个顺序**确实不同**，而差别**恰好**是加性参数的重标定 $a\mapsto ma$ ✓

## §3 【核验】TEST C：defect 落在**平移群**（阿贝尔）
```
119/119 组 (m,a)：交换子都是【纯平移】；非平移者：0
精确律：[Mul_m, Add_a] = 平移 by a(1−m)
⟹ 交换子 ∈ 平移群（阿贝尔正规子群）⟹ 生成群亚交换/可解
   —— 与 D1 对 Aff(ℤ) 的结论一致 ✓
```

## §4 【核验】TEST D：defect 律的**正确**类型（自捉过度声称）
```
d(m,a) = a(m−1)
  D1 公式精确                152/152 ✓
  D2 对 a 加性：d(m,a+b)=d(m,a)+d(m,b)   968/968 ✓
  D3 底层配对 B(m,a)=ma 对 m 双加性      325/325 ✓
  D4 底层配对 B(m,a)=ma 对 a 双加性     1352/1352 ✓
⚠️ ERR-3（自捉）：我一度称之为"双乘性 bicharacter"，但 d(m·n,a) ≠ d(m,n·a)+d(n,a)（96/396 ✗）
   正确：对 a【加性】、对 m【仿射】、取值为【阿贝尔群（平移）】
⟹ 正确陈述：defect 是【阿贝尔取值】，由【双加性乘法配对】(m,a)↦ma 支配 ⟹ character/上同调世界 ✓
```

## §5 结论（对你未句判据的回答）
$$\boxed{\text{分配律【不】把 defect 消成 }0\ ——\ \text{而是把它【归类】为 character 型}}$$
```
按 AOB2 的穷举：阿贝尔取值 / bicharacter 型 ⟹ character 世界 ⟹ L-函数 ⟹ 【不携带新相位】
⟹ **你的声明成立**：所有由 (+,\times,\mid) 内部事件生成的历史边界【均无新相位】⟹ 该类【封闭】
⟹ 因此【不存在】值得继续计算的"新相位对象" ⟹ 不必再做数值实验
```
**精确化建议**（供登记）：你的判据句宜由"是否被分配律消掉"改为
$$\boxed{\text{"defect 是否被分配律【归类】为 character 型"}}$$
——因为 defect 非零，但零的内容（"新相位"）确实不存在 ✓

## §6 边界
```
· §0 校准 5 项 + §1–§4 的计数为【核验】（可复现：scripts/AOB5_internal_event_defect.py）
· 广义 CRT 两两判据为【引用·经典】（本轮 4000 组整周期穷举亦未找到反例）
· AOB2 的"阿贝尔取值 ⟹ character ⟹ L-函数"分类为【引用·本项目已登记】
· 【未做】未输入 1/2；未构造模型；未改 L2；未声称与 ζ 连接
```

## §7 提交链
```
b59953c AOB4 → 本篇（AOB5：内部事件 defect 计算终审 + 三个自捉错误）
```
