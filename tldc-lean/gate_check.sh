#!/usr/bin/env bash
# 乙-3 门检验 G1–G5（机器可复核）
set -u
echo "===== G1 唯一 Core ====="
n_def=$(grep -rn "^theorem no_failure" TLDC/ | wc -l)
echo "① 名为 no_failure 的定义数 = $n_def   （须 = 1）"
n_wf_core=$(grep -c "lt_wfRel" TLDC/Core.lean)
echo "② Core 内良基引用数 = $n_wf_core   （= 1：核自身）"
echo "③ 各实例文件内良基引用（须**不得**用于复制核）："
grep -rn "lt_wfRel" TLDC/Instances/ | sed 's/^/     /'
echo
echo "===== G2 Core 零污染 ====="
for t in Prime prime Liou Fermat Gruppe group Brahmagupta Euclid Target H q p; do
  c=$(grep -c "\b$t\b" TLDC/Core.lean 2>/dev/null || echo 0)
  printf "   Core 中 \b%s\b 出现次数 = %s\n" "$t" "$c"
done
echo "   （Core.lean 全文：）"; sed -n '1,40p' TLDC/Core.lean | sed 's/^/     /'
echo
echo "===== G3 A2 层 ====="
grep -n "theorem derive_Target\|theorem reenter_P\|theorem a2_no_failure" TLDC/Instances/A2.lean | sed 's/^/   /'
echo "   derive_Target 是否引用 h（反证假设）？"; sed -n '/theorem derive_Target/,/^$/p' TLDC/Instances/A2.lean | grep -c "\bh\b" | sed 's/^/     出现次数 = /'
echo "   a2_no_failure 是否调用 TLDC.no_failure_of_slots？"; grep -c "TLDC.no_failure_of_slots" TLDC/Instances/A2.lean | sed 's/^/     出现次数 = /'
echo
echo "===== G4 Liouville 层 ====="
grep -n "theorem H_of_inner\|theorem outer_induction\|theorem liouville_step_via_core" TLDC/Instances/Liouville.lean | sed 's/^/   /'
echo "   外层强归纳是否在**层内**（Instances/Liouville.lean 中 lt_wfRel 出现次数）:"; grep -c "lt_wfRel" TLDC/Instances/Liouville.lean | sed 's/^/     /'
echo "   Core 是否引用 H／j<q（须为 0）:"; grep -c "H q\|H j\|IsGood\|exact'" TLDC/Core.lean | sed 's/^/     /'
echo "   H_of_inner 是否调用 Core:"; grep -c "TLDC.no_failure_of_slots" TLDC/Instances/Liouville.lean | sed 's/^/     /'
echo
echo "===== G5 双实例共享 ====="
echo "   实例文件对 Core 的 import："; grep -n "import TLDC.Core" TLDC/Instances/*.lean | sed 's/^/     /'
echo "   全仓 import TLDC.Core 的文件数 = $(grep -rl 'import TLDC.Core' TLDC/ | wc -l)"
echo "   公理足迹（Audit）："; grep -E "does not depend|depends on axioms" ../out/out_tldc_yi3_build.txt | sed 's/^/     /'
