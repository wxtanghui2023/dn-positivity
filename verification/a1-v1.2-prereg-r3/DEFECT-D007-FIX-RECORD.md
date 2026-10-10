# D-⑦ 修复记录（r3）

## 根因
`build_publish_r2.py:237` 以构建期 `len(files)`（=26）向 MD 注入数量，而 JSON 的
`artefact_hashes` 覆盖的是**较窄集合**（=22）；后续修订只重生成 JSON，**MD 常量从未重生成**
⟹ 两个互不相干的数量源漂移。

## 修复（单源 + 自动校验 + 负控）
1. **单一数据源**：全部数量声明由 `artefact_hashes` 的**键集**机械生成（数量是**集合属性**，
   与内容无关，故可在改写 MD 之前确定），不再手填常量。
2. **入包校验器**：`check_consistency.py` 实现契约 §2.3 五项检查（含负控）。
3. **负控**：在一次性副本中把声明改错，检查器必须失败（见 `CONSISTENCY-TEST-RESULTS.json`）。
4. **覆盖与排除规则（显式）**：
   - `artefact_hashes` 覆盖本包**除** `SHA256SUMS.txt`、`A1-v1.2-PREREGISTRATION-DRAFT-r3.json` 与 `CONSISTENCY-TEST-RESULTS.json`（自身测试产物）**以外**的全部文件；
   - `SHA256SUMS.txt` 覆盖**除其自身与 `CONSISTENCY-TEST-RESULTS.json` 以外**的全部文件。
5. **构建顺序**（本次即由此暴露两处真实缺陷）：先改 MD → 再算哈希 → 再写清单 → 再测。

## 与 r2 的关系
- r2 **逐字节未改动**；本版为**新修订版**。
- r2 的第三方测试结果**仍然有效**，但**不得**当作本版已修复 D-⑦ 的证据。
