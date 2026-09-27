已查地图：已跑 scripts/prework_map_check.sh 后台 run L3B R2 Level4 ⟹ 本档 = **(乙) 清账：两个后台 run 无产物 ✗；但定位到唯一剩余工程项 R2（含已知 bug）✓**。
D0: 本档对象 = 被遗弃后台 run 的可恢复性与 L3B 剩余项清账
D1: 2（**运行环境已干净、产物不可恢复 ✗**；**剩余项精确定位（R2 bmat bug ＋ η/λ 约定钉死 ✓）**）

# (乙) 清账：后台 run 与剩余项（2026-09-27 15:40）

## §0 结论（先给）

```
$$\boxed{\textbf{(NA-1 运行环境 ✓ 干净)}\ \texttt{ps}\ \text{全表仅 gateway 进程（tini/1 ✓）；无 python3 残留 ✓；无 core dump ✓；无 lasserre/reduced/block 相关存活进程 ✓}}$$
$$\qquad\textbf{但产物不可恢复 ✗}:\ \text{两个后台 run（tidal-glade／marine-nudibranch）\textbf{未留日志/输出} ⚠️};\ \text{work 树内无 reduced-SDP/bmat/border/Terwilliger 产物 ✗（仅无关的 gamma\_d4、ljcr）}$$
$$\qquad\Longrightarrow\ \textbf{低成本恢复路已尽 ✗（结论：需重算 ✓，无现成结果可取）}$$
$$\boxed{\textbf{(NB-1 ⭐真正的剩余项（已定位 ✓，L3B 线今日 12:01--12:07 有进展 ✓）)}\ \text{今日新增档（本会话后）}:}$$
$$\qquad\texttt{A-L3B-2-...classical-two-row-input.md}\ (12{:}01)\ ✓;\quad \texttt{B-L3B-1-...Mpp-border-normalization.md}\ (12{:}04)\ ✓;\quad \texttt{C-L3B-1-...lasserre-eta-closed-form.md}\ (12{:}07)\ ✓$$
$$\qquad\text{C-L3B-1 判定 ✓}:\ \text{D1}=\mathbf 0\ \text{（闭式重建＋约定核对，\textbf{不产生新数学命题} ✓）};\ \boxed{\text{AC-5 ⚠️ 约定未钉死}:\ \text{论文 Prop 2.4(iii) 定 }d=|w|\ ✓\ \text{而作者代码用 }\texttt{dist}=d(v,w)\ ⚠️ \Longrightarrow \textbf{最终数值钉死须 R2 ⏳}}$$
$$\qquad\textbf{唯一剩余工程项 ✓}:\ \boxed{\text{R2 = 块约化 SDP（外部钉死 ＋ 钉 }(\eta,\lambda)\ \text{索引约定）}}\ ✓;\ \text{且其 }\texttt{bmat}\ \text{border-assembly bug 已知}:\ \texttt{cp.vstack}\ \text{尺寸 }6\ \text{vs}\ 5\ (k{=}0\ \text{bordered 块}) ✗$$
$$\qquad\textbf{期望收益（诚实 ⚠️）}:\ \text{完成 R2 ⟹ \textbf{关闭 Level 3}（复现/验证层 ✓）};\ \text{但它\textbf{不}直接产出 }\ge120\ \text{的新界 ✗（档案 SDP 值 = }\mathbf{105.2223}\ ✓ < 119\ ✓\text{）}$$
$$
$$
```

## §1 状态（**✓**）

```
$$\boxed{K(10,1)=119\ \text{保持 UNKNOWN};\ \text{本档为清账、无新障碍 ✗};\ \text{未跑 solver ✓};\ \text{不写禁止表述 ✓}}$$
$$\textbf{三选（供唐先生 ✓）}:\ \text{(甲) 就地修 R2 的 bmat bug 并重算（\textbf{有界工程}，关闭 Level 3 ✓，但\textbf{不}直接推进 119 ✗）};\ \text{(乙) 直接做 Level 4（}n{=}10\ \text{未约化 }1024\times1024\ \text{PSD，重 ✓，风险高 ⚠️）};\ \text{(丙) 停手并更新总图（写"未闭合" ✓）}$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：后台 run 产物不可恢复之结论、R2（bmat bug ＋ $(\eta,\lambda)$ 约定）为唯一剩余项之定位
- **档案已有（引用，不列为提出）**：A-L3B-2／B-L3B-1／C-L3B-1（今日 12:01–12:07）、L3B 三项分解、SDP 105.2223、M-2A


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 清账           命中文件数=3    :: ./LEDGER-119-2026-09-27-abandoned-runs-check-and-R2-item.md ./C129-verification-n-off-is-the-already-audited-object-and-map-check-fails-on-renaming.md ./IMPACT-ASSESSMENT-2026-09-12.md 
技术词 剩余项        命中文件数=5    :: ./LEDGER-119-2026-09-27-abandoned-runs-check-and-R2-item.md ./C257-mechanism-space-search-third-family-quantity-change-outside-FZ1-grid.md ./d7-boundary-audit.md
```
- **本档新增**：后台 run 产物不可恢复之结论、R2（bmat bug ＋ $(\eta,\lambda)$ 约定）为唯一剩余项之定位（见上方命中数；0 命中者为自造语／内部标签 ✓）
