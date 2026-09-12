# Lean 4 在本环境的安装档案（2026-09-12 实测成功 ✅）

**目的**：为「宣言」所要求的**机器可验证性**做准备（见 `DECLARATION-2026-09-11-AI-MISALIGNMENT.md` ✅）

## 一、**结论：可行 ✅**（已装好并编译通过 ✅）
```
**Lean 4.33.0**（x86_64-unknown-linux-gnu ✓）已装好 ✅
路径：`~/.elan/toolchains/leanprover--lean4---v4.33`（**~3.8 GB** ✅）
入口：`~/.elan/bin/elan`、`~/.elan/bin/lean`、`~/.elan/bin/lake` ✅
验证：**9 个定理编译通过** ✅（`rfl` ✓、核心引理 ✓、`omega` 自动化 ✓、手写归纳 ✓、列表归纳 ✓）
```
## 二、⚠️ **环境事实（与"沙箱"的关系）**
```
**沙箱是关闭的**（`mode=off` ✓）⟹ `exec` **直接在容器内执行** ✅
⟹ 因此"能不能在沙箱装 Lean"= **能不能在容器装 Lean** ✅ = **能** ✅（用户级安装 ✓ 无需 root ✓）
【资源】磁盘 **2.9 TB 可用** ✅｜网络：**DNS 正常** ✓、`elan.lean-lang.org` HTTP 200 ✓
```
## 三、⭐ **卡点与解法（关键经验 ✅）**
```
【卡点】**`github.com` 直连 HTTP 000** ✗（NAS 对 GitHub 时断时续 ✓ TOOLS.md 已记 ✓）
   · `elan toolchain install stable` 因此**挂了 8 分钟** ✗（只写 39 MB 后停 ✓）
   · 资产主机 `release-assets.githubusercontent.com` **可达** ✓（返回 404 = 有应答 ✓）
     但下载 URL **必须先经 github.com 跳转** ✗ ⟹ 卡在跳转 ✅
【解法】**GitHub 加速镜像** ✅ 实测速度差异极大：
   | 镜像 | 结果 |
   | **`https://ghfast.top/`** | ✅ **可用且快（约 2.7 MB/s ✓，548 MB ≲ 4 分钟 ✓✓）** |
   | `https://ghproxy.net/` | ⚠️ 可用但**极慢**（约 48 KB/s ✗ ⟹ 3 小时 ✗）|
   | `github.moeyy.xyz` / `gh.llkk.cc` | ✗ 不通（000）|
   用法：`curl -L -C - -o lean.tar.zst "https://ghfast.top/https://github.com/leanprover/lean4/releases/download/v4.33.0/lean-4.33.0-linux.tar.zst"`
【完整性】**按字节数核对** ✅：期望 **574,882,764 字节（548.3 MB）** ✓ 实测完全一致 ✅
【解压】**本环境无 `zstd` 命令** ✗ ⟹ 用 **python `zstandard`** ✅（`pip install --break-system-packages zstandard` ✓；流式解压 47 秒 ✓）
【注册】解压出 `lean-4.33.0-linux/` ⟹ **移到 `~/.elan/toolchains/leanprover--lean4---v4.33`** ✅
   ⟹ **elan 自动识别为 `leanprover/lean4:v4.33`** ✅ 再 `elan default leanprover/lean4:v4.33` ✅
   ⚠️ **坑**：`elan toolchain link v4.33 <路径>` 会产生**错名条目**（指向 `toolchains/v4.33/bin/lean` ✗）
      ⟹ 报错 `does not have the binary ...` ✗ ⟹ 用原生目录名即可 ✅，或 `elan toolchain uninstall v4.33` 清掉 ✅
【⚠️ 易失性】**切勿留在 `/tmp`** ✗（重启即失 ✓ G8 教训 ✓）⟹ 已置于 `~/.elan/toolchains/` ✅
```
## 四、**下一步：Mathlib（尚未安装 ⚠️）**
```
【现状】当前只有 **Lean 核心 + Std** ✅（`lib/lean/` 下无 Mathlib ✗）
【对我们的意义】Paper B 的引理链涉及**实数幂、sinh、Abel 求和** ✅ ⟹ **需要 Mathlib** ⚠️
   （且 ζ 零点/显式公式类输入在 Mathlib 中不存在 ✗ ⟹ 形式化应以**条件定理**形式做：
      "给定满足计数界的零点多重集 ⟹ 不等式成立" ✅ —— 这恰是本项目的诚实内容 ✅）
【成本】Mathlib4 需：clone 仓库 + `lake exe cache get` **数 GB 预编译 olean** ⚠️
【可行性】**同一镜像策略应可复用** ✅（但 Mathlib 缓存主机不同 ⟹ **需装时再测** ⚠️ 不预先断言 ✓）
```
## 五、**本文件不声称什么 ✗**
```
· 不声称 Mathlib 已装 ✅（**未装** ✗）
· 不声称本项目任何结论已形式化 ✅（**尚未** ✗ —— 本文件只记录**工具链就绪** ✅）
· 不声称形式化必然成功 ✅（Paper B 的引理链**初等但非平凡** ⚠️；工作量需评估 ✓）
```
