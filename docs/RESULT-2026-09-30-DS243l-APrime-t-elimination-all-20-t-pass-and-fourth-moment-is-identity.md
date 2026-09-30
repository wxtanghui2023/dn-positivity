# RESULT-2026-09-30-DS243l — (甲′) $t$-消元：**四层结构核验 ✓；单 $z$ 运输 $t{=}0..19$ \textbf{全部可行} ✗；四阶矩是恒等式 ✗** ⟹ 按 STOP 转 (乙′)

> 空间 B｜非 C 号｜唐先生 14:08「上 (甲′)，但先做 $t$-消元，不要直接 CP-SAT」｜**不主张任何新值**（V290）
> 时间：2026-09-30 15:0x

**已查地图**：承 `DS243i/j/k`（(乙) $f$-层 ⟹ $T{=}60$；矩族；商群投影饱和）
D0: 本档对象 = **档案已有**（$f$-层之嵌套层级）之**逐 $t$ 消元**（新数学对象：无 ✗）
D1: 0（产出 = **一条结构核验 ＋ 两条可行性判定 ＋ 一条恒等式判定** ⚠️✓）

---

## §0 四层结构（核验 ✓）

$$f=\mathbf 1_{T_1}+\mathbf 1_{T_2}+\mathbf 1_{T_3},\quad T_3\subseteq T_2\subseteq T_1;\quad A:=T_1\setminus T_2,\ B:=T_2\setminus T_3,\ C:=T_3,\ D:=H\setminus T_1$$
$$(|A|,|B|,|C|,|D|)=(1+3t,\ 60-3t,\ t,\ 20-t)\quad(0\le t\le19\ \text{因 }t{=}20\ \text{已被 }19/4\ \text{排除}) ✓\ (\text{唐先生式正确 ✓})$$
$$\text{自相关拆 10 项}:\ 180=\sum_{X,Y}w_Xw_Y\,C_{XY}(z),\quad (w_A,w_B,w_C,w_D)=(1,2,3,0),\quad C_{XY}(z)=|X\cap(Y+z)| ✓$$
$$\text{行和守恒}:\ \sum_Y C_{XY}(z)=|X|;\quad \sum_X C_{XY}(z)=|Y|\ ✓$$

## §1 **单 $z$ 运输层：$t=0,\dots,19$ 全部可行** ✗（ILP 精确判定）

$$\text{每 }t:\ \text{16 变量 }x_{XY}\in\mathbb Z_{\ge0},\ \text{行和}=|X|,\ \text{列和}=|Y|,\ \sum w_Xw_Yx_{XY}=180$$
| $t$ | 0 | 5 | 10 | 15 | 19 |
|---|---|---|---|---|---|
| $(|A|,|B|,|C|,|D|)$ | (1,60,0,20) | (16,45,5,15) | (31,30,10,10) | (46,15,15,5) | (58,3,19,1) |
| 单 $z$ 可行 | ✓ | ✓ | ✓ | ✓ | ✓ |

$$\therefore\ \textbf{无一 }t\ \text{被单 }z\ \text{运输排除} ✗\ (\text{20/20 全过})$$

## §2 **四阶全局矩：恒等式（非独立约束）** ✗

$$\sum_z(f\star f)(z)^2 = 241^2+80\cdot180^2 = 2650081 = \tfrac1{81}\big(121^4+80\cdot61^2\big)\ ✓\ (\text{两路数值相等，核验通过})$$
$$\therefore\ \text{四阶矩\ \textbf{被点态条件完全决定}} \Longrightarrow \textbf{唐先生所期待之 }t\text{-依赖约束不成立} ✗\ (\text{点态条件更强 ⟹ 矩层被 subsumed ✓})$$

## §3 **(甲′) 之四层判定汇总**

| 层 | 判定 | 出处 |
|---|---|---|
| ④ 计数层（一阶/二阶联合谱） | 饱和 ✗ | `DS243g/h` |
| ③ 商群投影层（$\lvert K\rvert=81,27,9,9$ 两型） | 全可行 ✗ | `DS243k` |
| ② 单 $z$ 运输层（$t{=}0..19$） | 全可行 ✗ | 本档 |
| ① 四阶全局矩 | 恒等式 ✗ | 本档 |

$$\Longrightarrow\ \boxed{\text{按唐先生预设 STOP 纪律：\textbf{不在同一层继续 moment polishing} ⟹ 转 (乙′)}} ✓$$

## §4 诚实评估（重要 ⚠️）

$$\text{本线至今\ \textbf{连续四层全部饱和}（计数／联合谱／投影／运输）} \Longrightarrow \text{与夜内在 }M{=}106\ \text{线上之“总量层饱和”经验\ \textbf{同型}} ⚠️$$
$$\text{且与 }AUDIT\text{-zj 之类级校准一致（聚合/谱类连 }n{=}9\ \text{阈值都测不出）} ✓$$
$$\therefore\ \text{剩余\ \textbf{唯一未饱和之候选} ＝ \textbf{0/1 元素级排布之高阶兼容性}（(乙′) 12 核联合可实现性）} ✓$$

## §6 【技术词回查】（`scripts/tech_word_check.sh` 逐字输出 ✓）

```
技术词 四层分区     命中文件数=0    :: 
技术词 单 z 运输     命中文件数=0    :: 
```

$$\textbf{分类}:\ \text{两词命中均 }0 \Longrightarrow \textbf{本档新增} ✓\ (\text{但均含空格 ⟹ 词级不可判，仅作标签级标注，\textbf{不作新性证据}} ⚠️\text{，照既有约定})$$
$$\text{空间 A/B 分离（AMEND-27）}:\ \text{无跨空间同名} ✓$$
$$\text{通用词（不计）}:\ \text{“分区”／“运输”裸词不计} ✓$$


## §5 边界与纪律

$$\textbf{(D1)}\ \text{本轮无 P1} ✗;\quad \textbf{(D2)}\ \text{探针零证据} ✓;\quad \textbf{(D3)}\ \text{未主张新值／未取文献原文／未碰 RH} ✓$$

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=FINGERPRINT-CITED R09=NA R10=NA R11=NA R12=NA R13=NA R14=NA R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
