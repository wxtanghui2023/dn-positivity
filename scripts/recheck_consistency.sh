#!/usr/bin/env bash
# recheck_consistency.sh —— 「先跑后写」硬门：校验文档内声明的技术词/地图命中数是否与实测一致
# 用法: bash scripts/recheck_consistency.sh <doc.md>
# 退出码: 0 = 全部一致；1 = 存在不一致或无法解析
set -uo pipefail
doc="${1:-}"; [ -f "$doc" ] || { echo "用法: bash scripts/recheck_consistency.sh <doc.md>"; exit 1; }
cd "$(dirname "$0")/.." || exit 1
fail=0
# 1) 技术词行: “技术词 <term> 命中文件数=<N>”
while IFS= read -r line; do
  term=$(printf '%s' "$line" | sed -n 's/.*技术词 *\([^ ]*\) *命中文件数=\([0-9]\+\).*/\1/p')
  claim=$(printf '%s' "$line" | sed -n 's/.*命中文件数=\([0-9]\+\).*/\1/p')
  [ -n "$term" ] || continue
  # 词级不可判者（含空格/纯大写通用词）跳过并提示
  case "$term" in *[!A-Za-z0-9_一-龥]*) echo "  ⚠️ 跳过（含分隔符，词级不可判）: $term"; continue;; esac
  meas=$(bash scripts/tech_word_check.sh "$term" 2>/dev/null | head -1 | sed -n 's/.*命中文件数=\([0-9]\+\).*/\1/p')
  if [ "$claim" = "$meas" ]; then echo "  ✅ $term: 声明=$claim 实测=$meas"
  else echo "  ❌ $term: 声明=$claim 实测=$meas（文档自身可能计入 1）"; fail=1; fi
done < <(grep -a -o '技术词 [^ ]* 命中文件数=[0-9]*' "$doc" 2>/dev/null)
# 2) 地图行: “已查地图：命中 <N> 处”
claim=$(grep -a -o '已查地图：命中 \*\*[0-9]*\*\* 处' "$doc" 2>/dev/null | grep -a -o '[0-9]*' | head -1)
[ -n "$claim" ] && echo "  ℹ️ 地图声明命中=$claim（请人工核对 prework_map_check.sh 输出）"
[ "$fail" = 0 ] && echo "✅ 一致性校验通过" || echo "❌ 存在不一致 —— 禁止提交，先按实测改正"
exit $fail
