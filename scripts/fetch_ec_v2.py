#!/usr/bin/env python3
"""
修复分页——拉取更多同源类（带健壮重试——）
"""
import requests, json, time

def fetch_batch(offset, retries=4):
    url = f'https://www.lmfdb.org/api/ec_classdata/?_format=json&_offset={offset}'
    for attempt in range(retries):
        try:
            r = requests.get(url, timeout=30)
            if r.status_code == 200:
                data = r.json()
                if 'data' in data:
                    return data['data']
            time.sleep(1.5)
        except Exception as e:
            time.sleep(2 + attempt)
    return None

def main():
    classes = []
    offset = 0
    while len(classes) < 3000:
        batch = fetch_batch(offset)
        if batch is None or len(batch) == 0:
            print(f"offset {offset}: 失败/空——停止")
            break
        classes.extend(batch)
        offset += len(batch)
        if len(classes) % 300 < 100:
            print(f"  已拉取 {len(classes)}——最新 conductor {classes[-1]['conductor']}")
        time.sleep(0.5)
    
    print(f"\n总同源类: {len(classes)}")
    # 按 conductor 分层统计
    conds = sorted(c['conductor'] for c in classes)
    import numpy as np
    print(f"conductor: min={conds[0]}——median={conds[len(conds)//2]}——max={conds[-1]}")
    # 各 conductor 范围数量
    for lo, hi in [(1, 1000), (1000, 10000), (10000, 100000), (100000, 1000000), (1000000, 10**9)]:
        n = sum(1 for c in conds if lo <= c < hi)
        print(f"  cond ∈ [{lo}, {hi}): {n} 类")
    
    with open('/home/node/.openclaw/workspace/dn-project/data/ec_classdata_3000.json', 'w') as f:
        json.dump(classes, f)
    print("已保存")

if __name__ == "__main__":
    main()
