已查地图：命中（`S2-C07-all-free-tables-checked-ell11-4-still-missing`）⟹ DBLP OA 链接追索终报，不开新案
D0: 本档对象 = **DBLP “unpaywalled version” 链接的追索结果**：**三条 OA API 独立判 CLOSED** ＋ **DBLP 页面/API 与文本代理\textbf{全部被 Anubis 或超时拦截}** ⟹ 自动路线穷尽，**需人工浏览器入口**
D1: 1（首次把 OA 状态核到三家聚合器；产出"自动化不可达"的确定结论）
[RESEARCH]

# **DBLP `unpaywalled version`：自动路线全部不可达**

## §1 三家 OA 聚合器独立判定（本轮实证）

```
$$\boxed{\text{Semantic Scholar}}\ \texttt{isOpenAccess:false},\ \texttt{openAccessPdf.status: CLOSED}$$ ✓✓
$$\boxed{\text{Unpaywall}}\ \texttt{is\_oa:false},\ \text{无 }best\_oa\_location,\ \text{无任何 }oa\_location$$ ✓✓
$$\boxed{\text{OpenAlex}}\ \texttt{open\_access.is\_oa:false},\ \texttt{oa\_status: }\boxed{\texttt{closed}},\ \texttt{oa\_url: null};\ \textbf{唯一 }location =\ IEEE\ \text{DOI}$$ ✓✓✓
$$\Longrightarrow\ \text{三家独立源一致}:\ \text{该文\textbf{无 OA 全文}$$ ✓✓
```

## §2 页面/API/代理 全部不可达

```
$$\text{① }dblp.org/rec/\dots\ \Longrightarrow\ \textbf{Anubis 反爬挑战页}（7{,}439\ \text{字节}）$$ ✗
$$\text{② }dblp.uni-trier.de/rec/\dots.html\ \Longrightarrow\ \textbf{同一 Anubis 挑战页}（7{,}439\ \text{字节}）$$ ✗
$$\text{③ }dblp.org/search/publ/api\ \dots\ \text{format=json}\ \Longrightarrow\ \textbf{返回 HTML 挑战页而非 JSON}（\texttt{parse fail}）$$ ✗✗
$$\text{④ }\texttt{r.jina.ai}\ \text{文本代理（两路）}\ \Longrightarrow\ \textbf{75 秒连接超时}，无输出$$ ✗
$$\Longrightarrow\ \boxed{\text{自动化路线穷尽}：无法自行取得 DBLP 所示链接的实现地址}$$ ⚠️
```

## §3 判定与两个入口

```
$$\text{已锁}:\ \boxed{\text{BPW 1989 原始表存在且必含 }(11,4)\ \text{（摘要逐字：表覆盖 }m\le12,\ r\le12\text{）}}$$ ✓✓
$$\text{未锁}:\ \boxed{\ell_2(11,4)\ \text{的具体格值}} —— \textbf{不得把"表覆盖该格"误写成"该格已查到"}$$ ✓✓✓
$$\boxed{\text{入口①}\ (\text{先生优先})}:\ \text{在\textbf{浏览器}打开 DBLP 该记录},\ \text{点其 }unpaywalled\ version,\ \text{发来页面／PDF}$$ ✓✓✓
$$\boxed{\text{入口②}}:\ \text{《Covering Codes》(1997) \textbf{Table 7.3}}\ (\text{Davydov 2001 引其为基准})$$ ✓✓
$$\text{任一取得} \Longrightarrow \text{读 }(11,4)\ \text{格} \Longrightarrow \textbf{一步定 }C07\ \text{生死}$$
$$\textbf{若两入口皆不可得} \Longrightarrow \text{再议 }P2\ (\text{本轮不开})$$ ✓
【⛔ 纪律】 零数学计算；`U_{2,3}` 暂停；**不回 RH**；`S3` 冻结；不转 `Zone-B`；**不开 }P2$$ ✓
【边界】 §1 为三家 API 实证；§2 为四路失败实证；均\textbf{不含推测} ✓

## §附 【技术词回查】（补录）
```
技术词 unpaywalled      命中文件数=2    :: ./S2-C07-all-free-tables-checked-ell11-4-still-missing.md ./S2-C07-dblp-oa-link-all-auto-routes-blocked.md 
技术词 open access      命中文件数=2    :: ./S2-C07-all-free-tables-checked-ell11-4-still-missing.md ./E29-A5-4-burnol-li-isomorphism-check.md 
```
