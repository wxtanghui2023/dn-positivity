#!/usr/bin/env bash
# 攻坚卡工具（唐先生 16:44 工作单）
# 用法：scripts/attack_card.sh W1 关键词1 关键词2 ...   —— 先跑闸门，再开档首行
set -uo pipefail
cd "$(dirname "$0")/.." || exit 1
K="$1"; shift
echo "=== 攻坚卡 $K：先跑闸门 ==="
./scripts/prework_map_check.sh "$@" 2>&1 | tail -12
echo
echo "=== 新档首行请照抄： ==="
echo "已查地图：$(./scripts/prework_map_check.sh "$@" 2>&1 | tail -1)"
