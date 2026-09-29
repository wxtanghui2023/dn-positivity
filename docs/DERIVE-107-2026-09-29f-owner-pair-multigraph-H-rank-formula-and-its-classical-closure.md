# DERIVE-107-f（2026-09-29）—— **owner-pair 多重图 $H$：你的公式 $\text{rank}A{=}120{-}b(H)$ 被\ \textbf{精确证实}；但正因此谱支线落回经典**

> **性质**：**纯推导 ＋ 全量实测**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-29 13:5x ✓
> **唐先生令**：不打谱半径/秩，做四项（$\text{rank}A$／$b(H)$／连通分量／重边数）✓

**已查地图**：`DERIVE-107-e`（$G$ 谱、独立性门）／`DERIVE-107-d`✓

D0: 本档对象 ＝ **档案已有**（$H$ 为无向多重图；其 incidence／signless Laplacian 皆经典 ✓）
D1: 0（产出＝**四处数据 ＋ 一公式之精确证实 ＋ 一处因子 $2$ 纠正 ＋ 经典归位** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① 四项}:\ |V|{=}120,\ |E|{=}136\ (110\ \text{单}\ +\ 13\ \text{双});\ \text{分量 }38\ (30\ \text{二分} + 8\ \text{非二分})}$$
$$\boxed{\text{② ✓✓ 你的公式精确成立}:\ \boxed{\text{rank}(A)=120-b(H)=120-30=\mathbf{90}};\ \ \dim\ker A^\top=136-90=\mathbf{46}=\mathbf{16}+30}$$
$$\boxed{\text{③ ✓ 且 }\text{nullity}(G)=120-90=\mathbf{30}=b(H)\ \text{（经典 signless-Laplacian 零化）}}$$
$$\boxed{\text{④ ⚠️ 自指与重边之关系}:\ \#\text{self-ref}=\mathbf{26}=\mathbf{2}\times13=\mathbf{2}\times\#\{\text{双edge}\}\ (\text{非相等，差因子 }2)}$$
$$\boxed{\text{⑤ ✗ 归位}:\ \text{全部秩/零化数据}\ \textbf{恰为经典图论所预言}\ \Longrightarrow\ \textbf{无独立内容}}$$

## §1 ① $H$ 之结构（**✓**）

$$H:\ \text{顶点}=\text{码字};\ \text{边}=\mu{=}2\ \text{点}\ y\ \text{之 owner 对}\ \{c_1,c_2\};\ \text{每条边对应 }H\ \text{之一行}✓$$
$$\textbf{实测}:\ |E|=136=110\ (\text{单}) + 13\ (\text{双});\ \text{无三重}✓$$
$$\textbf{连通分量 }38\ \text{个}:\ \text{大小多为 }1{-}6;\ \text{较大者 }15,\ 6,\ 6,\dots;\ \textbf{二分 }30\ \text{个};\ \textbf{非二分 }8\ \text{个}$$
$$\therefore\ H\ \textbf{高度碎裂}（38\ \text{分量} / 120\ \text{顶点}）✓$$

## §2 ② 你的公式（**✓✓ 精确**）

$$\text{无向 unsigned incidence 之经典秩公式}:\ \text{rank}(A)=|V|-b\ (b=\text{二分连通分量数})$$
$$\textbf{实测}:\ \text{rank}(A)=\mathbf{90}=120-30\ \Longrightarrow\ \text{与 }b(H)=30\ \textbf{精确吻合}✓✓$$
$$\therefore\ \boxed{\dim\ker A^\top=136-90=\mathbf{46}=\underbrace{16}_{136-120}+\underbrace{30}_{b(H)}}\ ——\ \text{正是你 §8/§9 所推之式}✓✓$$

## §3 ③ $G=A^\top A$ 之零化（**✓ 亦经典**）

$$\text{实测 }\text{nullity}(G)=120-\text{rank}(G)=120-90=\mathbf{30}=b(H)✓$$
$$\text{经典事实}:\ \text{signless Laplacian}\ G=D+B\ \text{之零化重数}=H\ \text{之二分分量数}$$
$$\therefore\ \text{你 §6 之 }\lambda_{\min}(G)=0\iff\exists\ \text{二分分量}\ \text{完全被证实}✓$$

## §4 ④ 自指 $\leftrightarrow$ 重边（**⚠️ 因子 $2$ 纠正**）

$$\text{实测}:\ \#\{y\in Y_2:z(y)\in Y_2\}=\mathbf{26};\qquad \#\{\{c,c'\}:m_{cc'}=2\}=\mathbf{13}$$
$$\therefore\ \boxed{\#\text{self-ref}=2\times\#\{\text{双 edge}\}}\ ——\ \text{你之判据\ \textbf{方向正确}，但每对双 edge 贡献 }2\ \text{个 }y\ (\text{即 }y\ \text{与 }z(y)\ \text{皆在 }Y_2)✓$$
$$\text{故}\ z(z(y))=y\ \text{之对合性}\ \text{亦被证实}✓$$

## §5 ⑤ 归位：为何这条线到经典为止（**✗**）

$$\text{秩缺口}:\ 120-90=\mathbf{30}=b(H)\ \text{（全由二分分量解释，非额外）}$$
$$\text{零化}:\ \dim\ker A^\top=\mathbf{46}=\mathbf{16}+b(H)\ \text{（全由}\ |E|-|V|\ \text{与 }b(H)\ \text{解释）}$$
$$\therefore\ \boxed{\text{无一项超出经典 unsigned-incidence／signless-Laplacian 理论}}✗$$
$$\therefore\ \text{按你之判门表}:\ \text{「rank}A<120$ ⟹ 追额外 nullity」\ \text{之答案为：}\textbf{额外 nullity 即 }b(H)\ \text{本身}（经典）✓$$

## §6 关于"cycle $\to E$"（**守你 §10 之纪律，未强塞**）

$$\text{须证}:\ \text{每条独立 cycle relation}\ \Longrightarrow\ \text{至少一个额外 }E\text{-贡献}\ \Longrightarrow\ E\ge E_0+\kappa\dim\ker A^\top$$
$$\textbf{本档未做此项};\ \text{亦未做跨码相关性}\ (\text{本会话仅一个 }M{=}120\ \text{码 ＋ greedy 族可作对照})$$
$$\boxed{\text{建议下一刀（若继续）}:\ \text{对 }120\text{-code 与 }3\ \text{个 greedy 码同时算}\ (\text{rank}A,\ b(H),\ \dim\ker A^\top,\ E)\ \text{看是否同变}}$$

## §7 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "owner-pair多重图H" "秩120-b(H)" "自指与双重边"
技术词 owner-pair多重图H  命中文件数=0    ::
技术词 秩120-b(H)        命中文件数=0    ::
技术词 自指与双重边        命中文件数=0    ::
```

## §8 边界（硬 ✓）

- **120-code 全量实测（$H$ 构造、分量、二分性、秩、零化、重边、自指）** ✓；**不占 C 号** ✓；**不作方向性决策** ✗
- **不主张** $107$ 不可达 ✗（V290）；**未拟合** $E$ ✓（遵你令）
