#!/usr/bin/env bash
# 规则4（唐先生 2026-10-01 14:03 立）：新断言档必须登记假设（防继续欠账）
set -uo pipefail
cd "$(git rev-parse --show-toplevel)" 2>/dev/null || exit 0
CLAIM_RE='^(docs|papers)/.*(RESULT|PROOF|LEMMA|THEOREM|AUDIT|ANALYSIS|VERIFY|DECISION|CORRECTION|FINGERPRINT|LOCALIZE|COMPARE|SURVEY|STATE).*\.md$'
bad=""
for f in $(git diff --cached --name-only --diff-filter=A); do
  printf '%s' "$f" | grep -qE "$CLAIM_RE" || continue
  case "$f" in *ERRATUM*) continue;; esac
  head -40 "$f" 2>/dev/null | grep -aq "外部复核件" && continue
  head -40 "$f" 2>/dev/null | grep -aqE '^[[:space:]]*ASSUMES:' && continue
  bad="$bad $f"
done
if [ -n "$bad" ]; then
  echo "✗ 规则4（假设登记）未通过 —— 以下新档缺 ASSUMES: 行（可用 'ASSUMES: N/A' 显式豁免）"
  for f in $bad; do echo "   - $f"; done
  echo "  模板：docs/CONVENTION-ASSUMES.md §写入即登记 ；登记：docs/ASSUMPTIONS.tsv"
  exit 1
fi
exit 0
