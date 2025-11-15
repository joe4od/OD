#!/bin/bash
# 同時執行 momo/0928/momo_reg.py 與 momo/acsoar/momo_reg.py

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# 19:30
#python3 "$SCRIPT_DIR/0928/momo_ac.py" &

# 20:00
 python3 "$SCRIPT_DIR/acsoar/momo_reg.py" &
 python3 "$SCRIPT_DIR/acsoar/momo_ac.py" &
 python3 "$SCRIPT_DIR/0928/momo_reg.py" &

wait
echo "腳本已同時執行完畢"
