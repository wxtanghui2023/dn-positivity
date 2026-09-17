#!/usr/bin/env bash
# tech_word_check.sh <技术词1> [词2 ...] —— 技术词回查（查"手段/核/定理名"，不只查编号）
cd "$(dirname "$0")/../docs" || exit 1
for kw in "$@"; do
  n=$(grep -a -r -l -E "$kw" . 2>/dev/null | wc -l)
  f=$(grep -a -r -l -E "$kw" . 2>/dev/null | head -3 | tr '\n' ' ')
  printf '技术词 %-16s 命中文件数=%-4s :: %s\n' "$kw" "$n" "$f"
done
