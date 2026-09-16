#!/usr/bin/env bash
# id_claim.sh — dn-project 编号原子领用（防跨会话撞车）
# 用法: scripts/id_claim.sh <stream> <slug>
#   stream: main | audit | spare   （号段: main=E1xx, audit=E3xx, spare=E5xx）
# 语义: 在指定号段内取【第一个未被占用】的号，并用 mkdir 原子占位（防并发竞争），
#       随后把领用记录追加到 docs/ID-CLAIMS.tsv。输出: 一行 "E###"。
# 占用判定: ① docs/.idclaims/E###.lock 存在 ② docs/E###-* 或 scripts/E###_* / E###-* 存在
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LEDGER="$ROOT/docs/ID-CLAIMS.tsv"
STREAM="${1:?usage: id_claim.sh <stream> <slug>}"
SLUG="${2:?usage: id_claim.sh <stream> <slug>}"
case "$STREAM" in
  main)  PREFIX=E; BASE=100 ;;   # 主线：E1xx
  audit) PREFIX=V; BASE=100 ;;   # 审计线（小灵）：V1xx（与现有前缀零重叠 ✓）
  spare) PREFIX=Z; BASE=100 ;;   # 备用：Z1xx
  *) echo "unknown stream: $STREAM (main|audit|spare)" >&2; exit 2 ;;
esac
mkdir -p "$ROOT/docs/.idclaims"
for n in $(seq $((BASE+1)) $((BASE+299))); do   # 2026-09-15: 扩至 199 槽（V101–V299），原 99 槽已用满
  # 2026-09-16: 再扩至 299 槽（V101–V399），V299 已用满（见 docs/ID-ALLOCATION-PROTOCOL.md 治理行）
  id="${PREFIX}$n"
  [ -e "$ROOT/docs/.idclaims/$id.lock" ] && continue
  if compgen -G "$ROOT/docs/$id-*" >/dev/null 2>&1; then continue; fi
  if compgen -G "$ROOT/scripts/${id}_*" >/dev/null 2>&1; then continue; fi
  if compgen -G "$ROOT/scripts/$id-*" >/dev/null 2>&1; then continue; fi
  if mkdir "$ROOT/docs/.idclaims/$id.lock" 2>/dev/null; then
    # END_NEWLINE_GUARD: 防主线追加缺换行导致行粘连
    if [ -s "$LEDGER" ] && [ -n "$(tail -c1 "$LEDGER")" ]; then printf '\n' >> "$LEDGER"; fi
    printf '%s\t%s\t%s\t%s\n' "$id" "$STREAM" "$SLUG" "$(date -Iseconds)" >> "$LEDGER"
    echo "$id"; exit 0
  fi
done
echo "no free id in band ${BASE}xx" >&2; exit 1
