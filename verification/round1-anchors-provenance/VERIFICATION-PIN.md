# 验证锚定（Verification Pin）

> 目的：把「**独立验证过的载荷**」与「**会继续前进的分支头**」分开。引用请用**内容哈希**，不要用分支头。

| 项 | 值 |
|---|---|
| 被独立验证的包 | `verification/a1-v1.2-prereg-r2`（24 文件） |
| 独立验证所依据的提交 | `1cca3a19` |
| 该目录最后一次变更提交 | `1cca3a19`（2026-10-10T05:03:03Z） |
| 本文件写入时的 `main` 头 | `a394e6a9`（2026-10-10T05:52:06Z）—— `Add provenance README` |
| 载荷交叉核验 | 逐字节比对 **24/24** 文件 git blob SHA 一致；差异 **0**；仅本地 0；仅远端 0 |

## 为什么这样锚定
分支头会被后续提交推进（本次即因新增溯源文档而前进），但**已验证载荷的字节未变**。
因此正确引用方式是：**已验证包 = 内容哈希锁定**；而 `1cca3a19` 只是「当时被验证的那个提交」，
不应当作"当前分支头"来引用。

## 复核方法（任何人可做）
```bash
# 1) 远端当前 blob 哈希（API 直查，不用本地跟踪引用）
curl -s https://api.github.com/repos/wxtanghui2023/dn-positivity/contents/verification/a1-v1.2-prereg-r2/l8_1_a12_integration.py | grep '"sha"'
# 2) 与已验证包内登记值比对
sha256sum -c SHA256SUMS.txt          # 在已验证包目录内
```

## 诚实边界
- 本文件是**新增文档**，位于**独立目录** `verification/round1-anchors-provenance`，**未修改**已验证包的任何一个字节。
- blob SHA 一致只证明**内容相同**；不构成对 Gate C、预注册或任何科学结论的背书。
