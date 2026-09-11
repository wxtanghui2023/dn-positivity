#!/bin/sh
# setup_data.sh -- restore the volatile /tmp data paths that legacy scripts expect.
#
# Many older scripts in this repository read their inputs from /tmp (e.g. /tmp/zeros_odlyzko_2M.npy).
# /tmp is cleared on container restart, which would break them silently. The authoritative copies live
# in dn-project/data/ (committed). Run this script after any restart:
#
#     sh scripts/setup_data.sh
#
# New scripts MUST read from data/ directly, not from /tmp (see docs/PROTOCOL-CODE-ARCHIVE.md).
set -e
HERE=$(cd "$(dirname "$0")" && pwd)
DATA="$HERE/../data"
mkdir -p /tmp
for f in "$DATA"/*.npy "$DATA"/*.json; do
  [ -e "$f" ] || continue
  b=$(basename "$f")
  if [ ! -e "/tmp/$b" ]; then cp "$f" "/tmp/$b" && echo "restored /tmp/$b"; fi
done
echo "data restored from $DATA"
