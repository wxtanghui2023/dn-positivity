#!/usr/bin/env bash
# 开工前地图查（关键词逐字检索五图）—— 唐先生 11:43 立规；16:02 要求"必须真执行"
# 用法： scripts/prework_map_check.sh 关键词1 [关键词2 ...]
# 输出：命中行 + 结论行（可直接粘进新档首行）
set -uo pipefail
cd "$(dirname "$0")/.." || exit 1
MAPS=(docs/CLOSED-ROUTES-MAP.md docs/MASTER-STATUS-AND-CLOSURES.md docs/MASTER-NOGO-AND-LIVE-PATHS.md docs/ASSETS-REGISTRY.md docs/INDEX-BY-DIRECTION.md)
for f in "${MAPS[@]}"; do [ -f "$f" ] || echo "!! 缺档: $f"; done
if [ $# -eq 0 ]; then echo "用法: $0 关键词1 [关键词2 ...]"; exit 2; fi
PAT=$(printf '%s|' "$@"); PAT=${PAT%|}
echo "=== 关键词: $PAT ==="
HITS=0
for f in "${MAPS[@]}"; do
  [ -f "$f" ] || continue
  n=$(grep -a -c -E "$PAT" "$f" 2>/dev/null); n=${n:-0}
  if [ "$n" -gt 0 ]; then
    echo "--- $f : $n 命中 ---"
    grep -a -n -E "$PAT" "$f" 2>/dev/null | head -6
    HITS=$((HITS+n))
  fi
done
echo "=== 总命中: $HITS ==="
if [ "$HITS" -gt 0 ]; then
  echo "结论: 已查地图：命中 $HITS 处 —— 先逐条判 已DEAD/已封/已登记；命中即引既有条目，不得开新案"
else
  echo "结论: 已查地图：未覆盖（关键词: $PAT）—— 可开档，首行须照抄本行"
fi
