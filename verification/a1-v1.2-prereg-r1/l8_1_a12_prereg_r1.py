#!/usr/bin/env python3
"""A1 v1.2 pre-registration draft revision r1 generator.

Fixes operator item 5 (documentation completeness): the readable draft must carry the explicit
prohibition on using the round-1 cross-domain rejection as capability evidence, and must state that
round 1 is not re-judged.  The machine-readable draft is regenerated mechanically so the readable and
JSON versions cannot drift, the version differences are extended, and every artefact hash is
recomputed from disk (including the new shared scorer, runner and integration artefacts).

Records, honestly, that items 4 and 5 have AUTHOR evidence provided but remain subject to the
operator's review.  Zero model calls, zero network.
"""
import hashlib, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_JSON = os.path.join(HERE, 'A1-v1.2-PREREGISTRATION-DRAFT-r1.json')
OUT_MD = os.path.join(HERE, 'A1-v1.2-PREREGISTRATION-DRAFT-r1.md')

PROHIBITION = """## §1bis 第一轮材料使用禁令（本修订 **r1** 新增）

```text
⛔ 第一轮（c227e3e）已永久冻结：**不得复判**、**不得覆盖**、**不得追溯改判**。
⛔ 第一轮 no-core 提交在 r2 的【显式 null】约定下会被拒（原因：H3_tight 答 false 而非 null）
   —— 该拒绝属【格式合规差异】：**不是**关于 r2 的能力证据，**不得**用于推断 r2 的模型能力，
   也**不得**作为 r2 能力结论的任何支撑或反驳。
⛔ 未定义约定的选择【确实会改变判定】（(a) 忽略 → ACCEPT；(b) 显式 null → REJECT）
   ⟹ 正因如此，该约定必须在实验【之前】冻结——本轮修订即为此冻结该约定。
✔ 唯一允许的用法：作为【测量/格式语义差异】的说明性材料，且必须与能力讨论严格分离。
```
"""


def sha(p):
    return hashlib.sha256(open(os.path.join(HERE, p), 'rb').read()).hexdigest()


def main():
    r2 = json.load(open(os.path.join(HERE, 'A1-v1.2-PREREGISTRATION-DRAFT.json')))
    r1 = json.loads(json.dumps(r2))                    # deep copy
    r1['spec'] = 'A1-v1.2-PREREGISTRATION-DRAFT-r1'
    r1['version_identifier'] = 'A1-v1.2-PREREG-R1'
    r1['supersedes'] = 'A1-v1.2-PREREGISTRATION-DRAFT (r2 draft) — kept unchanged as history'
    r1['revision_notes'] = [
        'item 5 FIXED: the readable draft now carries the explicit prohibition on using the round-1 '
        'cross-domain rejection as capability evidence, and states that round 1 is not re-judged',
        'item 4 ADDRESSED with author evidence: a shared scorer module, a formal runner that imports '
        'it, and integration tests proving the runner scores through that implementation; operator '
        'review still pending',
        'artefact hashes recomputed to include the new scorer / runner / integration artefacts',
        'the readable and machine-readable drafts are regenerated together so they cannot drift']
    r1['round1_material_use_prohibition'] = {
        'text': 'Round 1 is frozen and must not be re-judged or overwritten. The round-1 cross-domain '
                'submission would be rejected under the r2 explicit-null convention for a FORMAT '
                'reason (H3_tight answered false rather than null); that rejection is NOT capability '
                'evidence about r2 and must not be used to infer, support or refute r2 capability.',
        'rationale': 'the undefined-value convention genuinely changes the verdict, which is precisely '
                     'why it had to be frozen before the experiment rather than after',
        'permitted_use': 'explanatory material about measurement / format semantics only, kept '
                         'strictly separate from capability discussion'}
    r1['open_item_status'] = {
        'item_4_runner_integration': {
            'status': 'AUTHOR EVIDENCE PROVIDED — operator review pending',
            'evidence': 'A1-v1.2-INTEGRATION-TEST-RESULTS.json: identity of the scoring callable, '
                        'four mandated end-to-end cases through the runner, differential equivalence '
                        'with the earlier test module, round-1 replay, and the model-call gate',
            'not_self_certified': 'the author does not declare this PASS; the reviewer decides'},
        'item_5_readable_draft_prohibition': {
            'status': 'FIXED IN THIS REVISION — operator review pending',
            'where': 'section 1bis of the readable draft and round1_material_use_prohibition here'}}
    r1['version_differences']['r2_to_r1_revision'] = [
        'readable draft gains the explicit round-1 prohibition (item 5)',
        'new shared scorer module l8_1_a12_scorer.py becomes the single scoring implementation',
        'new formal runner l8_1_a12_runner.py imports that scorer (item 4 evidence)',
        'new integration test suite l8_1_a12_integration.py']
    r1['artefact_hashes'] = {k: sha(v) for k, v in {
        'spec_v1.2_candidate': 'A1-v1.2-SPEC-CANDIDATE.md',
        'spec_r1': 'A1-v1.2-SPEC-CANDIDATE-r1.md',
        'spec_r2': 'A1-v1.2-SPEC-CANDIDATE-r2.md',
        'r2_test_results': 'A1-v1.2-R2-TEST-RESULTS.json',
        'shared_scorer_module': 'l8_1_a12_scorer.py',
        'formal_runner': 'l8_1_a12_runner.py',
        'integration_test_results': 'A1-v1.2-INTEGRATION-TEST-RESULTS.json',
        'integration_test_script': 'l8_1_a12_integration.py',
        'open_items_resolution': 'A1-v1.2-OPEN-ITEMS-RESOLUTION.json',
        'gate_ab_results': 'A1-v1.2-GATE-AB-RESULTS.json',
        'calibration_plan': 'A1-v1.2-PREFLIGHT-CALIBRATION-PLAN.md',
        'defect_register_addendum': 'A1-DEFECT-REGISTER-ADDENDUM.json',
        'round1_final_results': 'A1-ROUND-1-FINAL-RESULTS.md',
        'round1_final_verdicts': 'A1-FINAL-VERDICTS.json',
        'raw_records': 'RAW-A1.jsonl',
        'prereg_v1.1': 'A1-PREREGISTERED-EXPERIMENT-v1.1.json',
        'r2_scorer_tests': 'l8_1_a12_r2_tests.py',
        'consistency_check': 'A1-v1.2-CONSISTENCY-CHECK.json',
    }.items()}
    json.dump(r1, open(OUT_JSON, 'w'), indent=1)

    # regenerate the readable draft from the previous readable draft (single source, no drift)
    md = open(os.path.join(HERE, 'A1-v1.2-PREREGISTRATION-DRAFT.md')).read()
    md = md.replace('# A1 v1.2 预注册草案 —— **DRAFT / NOT APPROVED**',
                    '# A1 v1.2 预注册草案 **修订 r1** —— **DRAFT / NOT APPROVED**', 1)
    banner = ('\n> **修订标识**：`A1-v1.2-PREREG-R1`（前身 r2 草案**保持原样不覆盖**）\n'
              '> **本修订内容**：⑤ 补齐第一轮材料使用禁令（§1bis）｜④ 运行器集成证据已附'
              '（`A1-v1.2-INTEGRATION-TEST-RESULTS.json`）｜哈希清单已重算并含新增件\n'
              '> ⛔ 仍为 **DRAFT / NOT APPROVED**；Gate C 未通过；零模型调用\n')
    idx = md.find('\n')
    md = md[:idx + 1] + banner + md[idx + 1:]
    anchor = '## §2 能力操作性定义与阈值'
    md = md.replace(anchor, PROHIBITION + '\n---\n\n' + anchor, 1)
    # item status section
    status_block = ('\n## §10bis 未决事项状态（r1）\n\n'
                    '```text\n'
                    '④ 运行器集成：**已提供作者证据**（集成测试全过：调用身份、四例端到端、与旧测试模块\n'
                    '   差异等价、第一轮回放、调用闸门）—— **由审查者裁定**，作者不自宣 PASS\n'
                    '⑤ 可读版禁令：**本修订已补**（§1bis + JSON 的 round1_material_use_prohibition）\n'
                    '   —— 仍待审查者确认\n'
                    '其余未决项（Gate C 复核、标定执行、预算冻结、k 与阈值固定、r2/r1 正式批准）不变\n'
                    '```\n')
    md = md.rstrip() + '\n' + status_block
    open(OUT_MD, 'w').write(md)

    print('wrote:', os.path.basename(OUT_JSON), 'and', os.path.basename(OUT_MD))
    print('version:', r1['version_identifier'], '| hashes:', len(r1['artefact_hashes']))
    print('prohibition in readable draft:', '§1bis' in md and '不得' in md)
    print('item4 status:', r1['open_item_status']['item_4_runner_integration']['status'])
    print('item5 status:', r1['open_item_status']['item_5_readable_draft_prohibition']['status'])
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
