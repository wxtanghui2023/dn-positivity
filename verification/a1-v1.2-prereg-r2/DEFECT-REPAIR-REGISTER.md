# 审计缺陷修复登记（r1 → r2）

审查者裁定的每一条，对应到**修了什么 / 如何验证 / 证据在何处**。

| 编号 | 审查者裁定 | 修复 | 验证 | 证据 |
|---|---|---|---|---|
| D-A | `classify_response` 判定顺序与协议不一致：可解析内容 + 系统侧/未知终止被误判 `SCOREABLE` | `finish_reason` **先于**可解析性判定，全域完整（见 r2 草案 §12bis） | 回归 **I2c**：`content_filter`/`error`/缺失/未知值 + 可解析内容 ⟹ 四例均**不再** `SCOREABLE` | `A1-v1.2-INTEGRATION-TEST-RESULTS.json` → `I2c_parsable_with_abnormal_terminal` |
| D-B | `aggregate_c1b` 只认 `ACCEPT`/`REJECT`，`MODEL_NONCOMPLIANCE` 被排除 ⟹ `UNDECIDABLE` | 新增 `split_scoreable`：`MODEL_NONCOMPLIANCE` → `REJECT`；C1b/C1c 同一映射 | 回归 **I6**：仅该状态 ⟹ `FAILURE`；混合两例；排除集仅三类 | 同上 → `I6_aggregation_semantics` |
| D-⑤ | 集成测试把第一轮记录交新判分器并输出**新的** C1b 能力判定，与禁令冲突 | I4 改为**纯完整性**：哈希校验 + 冻结裁定**逐字报告** + **机械断言**判分函数零调用 | I4：`archive_unchanged`、`frozen_verdicts_unchanged`、`no_rejudge_guard.all_zero` | 同上 → `I4_round1_archive_integrity` |
| D-④ | 包内测试无法独立运行（`ModuleNotFoundError: l8_1_a1_evaluator`） | 导入闭包 **7 模块**随包发布至 `deps/`；补 `RUN-INTEGRATION.md` | 从**两个干净目录**执行并留存日志 | `INTEGRATION-RUN-LOG.txt`、`INTEGRATION-RUN-LOG-CLEAN2.txt` |
| D-5 | 可读版仍写「15 项哈希」且指向旧 JSON 名 | 哈希项数**机械注入**（本版 26 项）；文件名统一为 `-r2.json` | 生成后自检：无 `15 项`、无旧文件名 | r2 草案 §0 与 §产物哈希 |

> 修的是**实现**，不是判据：阈值、门禁与预注册的判定规则**未放宽**；**零模型调用**；第一轮冻结结果**未改**。

| D-⑤b | I4 零调用断言不可靠（共享可变计数器；`all_zero` 为早期快照；`contains_no_new_capability_verdict` 查错对象） | 专用计数器 + armed 期**不可变快照** + 立即还原 + 后段调用**独立标注** + 对实际输出的**递归结构断言** + **负控** | I4：`round1_phase_snapshot={0,0,0}`、负控 `delta={1,1,1}` ⟹ `detected=true`、`I4_record_stable_after_later_phases=true` | `A1-v1.2-INTEGRATION-TEST-RESULTS.json` → `I4_round1_archive_integrity.no_rejudge_guard` |
| D-④b | 发布目录含 9 个未追踪 `.pyc` 字节码 | 删除 `__pycache__` 两处；清单重建 | `sha256sum -c` 全 OK；目录内无 `pyc` | 本文件 §清理 |
