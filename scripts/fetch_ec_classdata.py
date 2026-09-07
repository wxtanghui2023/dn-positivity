#!/usr/bin/env python3
"""
LMFDB ec_classdata 拉取——同源类 ensemble
目标：conductor ≤ X 的同源类——aplist（a_p 素数序——）
"""
import requests
import numpy as np
import json, time

def fetch_classdata(max_classes=2000, offset=0):
    """拉取同源类数据——分页"""
    classes = []
    off = offset
    while len(classes) < max_classes:
        url = f'https://www.lmfdb.org/api/ec_classdata/?_format=json&_offset={off}'
        try:
            r = requests.get(url, timeout=30)
            data = r.json()
            batch = data['data']
            if not batch:
                break
            classes.extend(batch)
            off += len(batch)
            if off % 500 == 0:
                print(f"  已拉取 {len(classes)}——")
            time.sleep(0.3)  # 礼貌限速
        except Exception as e:
            print(f"  错误 @offset {off}: {e}")
            time.sleep(2)
            # 重试一次
            try:
                r = requests.get(url, timeout=30)
                data = r.json()
                batch = data['data']
                if batch:
                    classes.extend(batch)
                    off += len(batch)
            except:
                break
    return classes

def main():
    classes = fetch_classdata(max_classes=3000)
    print(f"\n总同源类: {len(classes)}")
    
    # 检查 conductor 分布 + aplist 结构
    conds = [c['conductor'] for c in classes]
    print(f"conductor 范围: [{min(conds)}, {max(conds)}]")
    # aplist 长度分布
    aplens = [len(c['aplist']) for c in classes]
    print(f"aplist 长度: min={min(aplens)}——max={max(aplens)}——多数 {np.median(aplens)}")
    
    # 索引确认：aplist[i] 对应哪个素数？
    # 用 anlist 交叉验证（anlist[n] = a_n——）
    c0 = classes[0]
    print(f"\n示例 {c0['lmfdb_iso']} (cond={c0['conductor']}):")
    print(f"  anlist[:15]: {c0['anlist'][:15]}")
    print(f"  aplist[:15]: {c0['aplist'][:15]}")
    # anlist[n] = a_n——a_2 = anlist[2] = ?——a_3 = anlist[3]——但 aplist 是素数序？
    # 检查：aplist[i] 是否 = a_{第 i+1 素数}——(aplist[0] = a_2?)
    # 素数 2,3,5,7,11...
    from sympy import primerange
    small_primes = list(primerange(2, 50))
    an = c0['anlist']
    print(f"  小素数 {small_primes[:8]}——anlist 对应: {[an[p] if p < len(an) else '?' for p in small_primes[:8]]}")
    print(f"  aplist[:8]: {c0['aplist'][:8]}")
    # 若 aplist[i] = a_{p_{i+1}}——aplist[0] 应 = a_2（但索引 0——）——看：aplist[1] 若 = a_3
    print(f"  → aplist[0] vs a_2: {c0['aplist'][0]} vs {an[2] if len(an)>2 else '?'}")
    print(f"  → aplist[1] vs a_3: {c0['aplist'][1]} vs {an[3] if len(an)>3 else '?'}")
    
    # 保存原始
    with open('/home/node/.openclaw/workspace/dn-project/data/ec_classdata_3000.json', 'w') as f:
        json.dump(classes, f)
    print(f"\n已保存 data/ec_classdata_3000.json")

if __name__ == "__main__":
    main()
