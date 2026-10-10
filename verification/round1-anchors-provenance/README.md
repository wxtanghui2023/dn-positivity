# 第一轮锚点溯源（外部基准指针）

本目录**不修改**已通过第三方验证的 r2 包（`verification/a1-v1.2-prereg-r2`，其哈希保持原样）。
它只是把 r2 包内 `ROUND1-ARCHIVE/ANCHORS.json` 所引用的**外部基准指针**独立公开，回应审查者「未独立重算第一轮锚点外部基准」的保留说明。

## 可核对内容
```bash
# 在已验证包目录内
cd verification/a1-v1.2-prereg-r2/ROUND1-ARCHIVE && sha256sum RAW-A1.jsonl A1-FINAL-VERDICTS.json A1-RUN-LEDGER.json
# 与本目录 PROVENANCE.json 的 sha256_now 及包内 ANCHORS.json 的 sha256_at_freeze 比对
```

## 诚实边界
* **证明**：包内归档字节的 SHA-256 / git blob SHA 与其冻结提交时的版本**一致**，且与包内 `ANCHORS.json` 记录值**相符**（内容寻址可独立复核）。
* **不证明**：冻结提交的**时间**（无外部时间戳/透明日志）；提交元数据为**作者声明**——作者仓库未公开，第三方无法独立确认提交本身。

生成时作者侧仓库 HEAD：`84dd657 Makes required dependencies fail closed and records the fourth audit round. The differential test modu`
