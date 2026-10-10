# 版本差异 — r2 验证包

| 目录 | 状态 |
|---|---|
| `verification/a1-v1.2-596ea24` | **未改动**（Gate C 首次审查基线快照） |
| `verification/a1-v1.2-prereg-r1` | **未改动**（被审计的 r1 包，保留为审计对象） |
| `verification/a1-v1.2-prereg-r2` | **本包**：修复 D-A / D-B / D-⑤ / D-④ 与文档缺陷 |

## 相对 r1 的变更
- `l8_1_a12_scorer.py`：判定优先级重写（`finish_reason` 优先、全域完整）；`split_scoreable` 使 `MODEL_NONCOMPLIANCE` 计为拒绝（C1b/C1c 一致）；`SCORER_ID` → `A1-v1.2-SCORER-r2.1`。
- `l8_1_a12_runner.py`：`MODEL_NONCOMPLIANCE` 条目补 `counts_as='REJECT'` 显式追踪。
- `l8_1_a12_integration.py`：I4 改为纯完整性 + 防重判；新增 I2c / I6 / I7；I3 在未随包发布时降级 `SKIPPED_UNAVAILABLE`。
- 新增 `deps/`（7 模块）与 `ROUND1-ARCHIVE/`（3 件 + `ANCHORS.json`）；新增 `RUN-INTEGRATION.md`、`DEFECT-REPAIR-REGISTER.md`。
- 草案 r2：修哈希项数（机械注入 = **26**）与旧文件名；新增 §12bis/§12ter/§12quater/§12quinquies。

## 校验
```bash
sha256sum -c SHA256SUMS.txt
python3 l8_1_a12_integration.py     # 期望 ALL PASS: True
```

## r2b（审计第二轮修复，原地更新）
- **I4 守卫缺陷修复**：启用**专用** round-1 计数器、在 armed 期间取**不可变快照**、随即**还原受护函数**（后段 I6/I7 调用**单独计数并明确标注**）、`contains_no_new_capability_verdict` 改为对**实际 I4 输出结构**递归检查、新增**负控**（故意重判一条 round-1 记录 ⟹ 守卫**必须**检出，否则 I4 失败）。
- **发布目录清理**：删除 **2 个 `__pycache__` / 9 个 `.pyc`**；清单覆盖全部应纳入文件。
- **复验**：从**两次独立全新解压**运行，结果一致。
