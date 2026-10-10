# 版本差异说明 — r1 验证包 vs 596ea24 快照

原目录 `verification/a1-v1.2-596ea24` 为**不可变审查快照**，本包**未修改其任何文件**。

## ① 新增（本包首次发布）

| `A1-v1.2-PREREGISTRATION-DRAFT-r1.md` | 23afdaef3ac16205… | 新增 |
| `A1-v1.2-PREREGISTRATION-DRAFT-r1.json` | b850ee6d7cdd7b64… | 新增 |
| `l8_1_a12_scorer.py` | b01c3e4ae7df3b20… | 新增 |
| `l8_1_a12_runner.py` | c24d3ea4480312df… | 新增 |
| `l8_1_a12_integration.py` | 40444f9c5aff0cd6… | 新增 |
| `A1-v1.2-INTEGRATION-TEST-RESULTS.json` | b63911093075be90… | 新增 |
| `l8_1_a12_prereg_r1.py` | 0e5af59f3fde6448… | 新增 |
| `OLD-PACKAGE-SHA256SUMS.txt` | 旧包哈希清单原件 | 留存对照 |

## ② 内容变更（同一逻辑件的修订，以**新文件**形式发布，不覆盖旧件）

| 旧包文件 | 本包对应 | 变更 |
|---|---|---|
| `A1-v1.2-PREREGISTRATION-DRAFT.md` | `A1-v1.2-PREREGISTRATION-DRAFT-r1.md` | **新增 §1bis 第一轮材料使用禁令**（⑤ 修订）；新增 §10bis 未决事项状态 |
| `A1-v1.2-PREREGISTRATION-DRAFT.json` | `A1-v1.2-PREREGISTRATION-DRAFT-r1.json` | 同步禁令（`round1_material_use_prohibition`）；新增 `version_identifier`、`revision_notes`、`open_item_status`；哈希清单扩至 18 项 |

## ③ 未变更（与旧包逐字节相同，哈希见旧清单）

`l8_1_a12_r2_tests.py`、`A1-v1.2-R2-TEST-RESULTS.json`、`A1-v1.2-SPEC-CANDIDATE-r2.md`、`A1-v1.2-PREFLIGHT-CALIBRATION-PLAN.md`、`A1-v1.2-CONSISTENCY-CHECK.json`、`check_v12_consistency.py`、`README.md`、`SHA256SUMS.txt`

## ④ 第④项集成证据（新增）

- `l8_1_a12_scorer.py`：**共享 r2 判分器模块**（单一实现）
- `l8_1_a12_runner.py`：**正式实验运行器**，`SCORE_C1B = scorer.score_c1b`（同一函数对象）
- `l8_1_a12_integration.py` + `A1-v1.2-INTEGRATION-TEST-RESULTS.json`：集成测试证据

## ⑤ 第⑤项修订（本包）

可读版 §1bis 明确：第一轮 no-core 在 r2 下被拒系**格式**原因、**非**能力证据、**不得**用于推断 r2 能力、**不得**复判第一轮；JSON `round1_material_use_prohibition` 同义表述。

## ⑥ 状态

第④项 **作者证据已附，待审查者裁定**；第⑤项 **本修订已补，待审查者裁定**；Gate C **未通过**；预注册 **DRAFT / NOT APPROVED**；**零模型调用**；POC1/POC2 不变。

## ⑦ 校验方法
```bash
sha256sum -c SHA256SUMS.txt
```
