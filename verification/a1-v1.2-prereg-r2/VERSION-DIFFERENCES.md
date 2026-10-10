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


## r2c（第三轮审计修复）
- **禁键检查改为对「组装完成的 I4 输出对象」递归扫描两次**（填充自身字段前/后各一次），`pass` **依赖两次结果**；并新增**扫描正控**（注入 `C1b_verdict` 与 `nest.per_instance` ⟹ 必须检出）。
- **负控覆盖全部评分入口**：`runner.score_records`、**`runner.SCORE_C1B`（导入期绑定，此前未纳管）**、`scorer.score_c1b`、`scorer.aggregate_c1b` —— 要求**每个入口**均产生增量（`guard_delta` 四项均 ≥1），否则 I4 失败。
- 修正 `find_verdict_keys` 路径拼接的前导点缺陷（`'.nest.per_instance'` → `'nest.per_instance'`），使位置比对可精确成立。
- 复验：两次独立全新解压运行，结果一致。


## r2d（第四轮审计修复：必需依赖 fail-closed）
- **审查者裁定（可复现的验收缺陷）**：差分测试模块的导入用了宽泛 `except Exception`，失败时 I3 记为 `pass=None`，而汇总用 `all(v for v in values if v is not None)` ⟹ **必需依赖缺失仍可能输出 `ALL PASS: True`**（错误放行路径）；且脚本失败时**仍返回 0**。
- **修复**：`REQUIRED_DEP_MODULES`/`REQUIRED_CHECKS` 显式声明；模块不可用时 I3 = **`False`**（附 import 错误），**绝不为 `None`**；`all_pass` 要求每项必需检查 **严格 `is True`** 且 `summary_none_keys` 必须为空；**失败时进程 `exit 1`**。
- **新增 I8 负控**：在**一次性副本**中删除 `deps/l8_1_a12_r2_tests.py` 并以子进程重跑本套件 ⟹ 子进程必须 `exit != 0`、`all_pass=false`、`I3=false`（而非 `None`）。
- 复验：两次独立全新解压运行，结果一致。
