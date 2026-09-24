已查地图：命中（`C3-source-hunt-status-three-pdfs-and-remaining-gap`）⟹ 引用，不开新案
D0: 本档对象 = `1992 CMH` 下载失败诊断（**站点返回人机校验页**）＋ 替代路线 ＋ 复验判据
D1: 0 （[REVIEW] 轮次：诊断，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`1992 CMH` 下载：撞人机校验墙（诊断）**

## §1 收到的文件不是论文

```
【诊断（本地实测）】 文件：`sources/McMullen-Schulte-1992-CMH67-locally-toroidal-rank4.pdf` ✓
　· **页数 `2`**（论文应为 **`42`** 页：`CMH 67`（1992）`77`–`118`）✗
　· **`metadata.title` ＝ "Verification required"** ✓✓ ← **站点人机校验页**
　· 页尺寸 `400\times600`、**无图像、无文本**（`textlen` 首末为 `0`／`50`）✗
$$\Longrightarrow\ \textbf{未取得论文正文（撞站点校验墙，非您操作失误）}$$ ✓
```

## §2 复验判据（下次一眼可判）

```
$$\boxed{\text{页数}\approx42\quad\land\quad\text{首页含 "Commentarii Mathematici Helvetici 67 (1992) 77-118" 或 "Locally toroidal regular polytopes of rank 4"}}$$ ✓
【反面样本】**页数 `2` ＋ 标题 `Verification required` ＋ 无文本** ⟹ **校验页，直接弃** ✓
```

## §3 替代路线（不依赖 `e-periodica`）

```
**【A】`Springer`**：`DOI 10.1007/BF02566490`（`link.springer.com/article/10.1007/BF02566490`）—— 常给**首页预览**；若只有摘要，则弃 ✓
**【B】`McMullen` 主页**（`UCL`）—— 作者自存 PDF 列表，**历史上常可下** ⟹ 值得一试 ✓
**【C】`GDZ`／`DigiZeitschriften`**（德/瑞期刊数字化）—— `CMH` 老卷常有扫描 ✓
**【D】图书馆/机构通道**（您若所在机构有 `Springer` 订阅）✓
**【E】书 `[42] §11E`（`pp.417`–`422`，`6` 页）** —— 若能取到章节，**等效于** `1992` 的参数清单（`2002` 整合版）✓✓
```

## §4 状态（缺口未变）

```
$$\boxed{\text{唯一剩余缺口：\textbf{已决 universal 情形清单}}\quad(\text{书 }§11E,H\ \text{或}\ 1992\ CMH)}$$ ✓
【已到手仍有效】三份免费 PDF（`Problems 2006`／`MS2008`／`RGPF-II`）✓
【本轮未推进数学】仅完成"下载渠道诊断＋复验判据＋替代路线" ⟹ **无新数学内容** ✓
【⛔ 纪律】**不计算、不实现**；`C2` 暂停 ✓
【边界】 §1 为**本地 `pymupdf` 实测**（页数/元数据/文本长度）；§2–§4 为**本档诊断与建议**；未制造候选／未启动搜索／未碰 RH。

## §5 【技术词回查】（补录）
```
技术词 Verification required 命中文件数=1    :: ./C3-eperiodica-download-hit-verification-wall.md 
```
