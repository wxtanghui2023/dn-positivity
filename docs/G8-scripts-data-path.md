# ✅ **G8：115 个脚本的 `/tmp` 依赖已消除**（除合理例外 ✓）

**依据**：唐先生 2026-09-12 09:56（"继续…逐项实施" ✓）｜**制度依据**：`PROTOCOL-CODE-ARCHIVE.md` R2（脚本须读 `data/` ✓）

---

## §1 **问题**
```
【审计发现 ✓】`scripts/*.py` 中有 **115 个**引用 `/tmp` ✗ —— 而 `/tmp` 在容器重启后**全部丢失** ✗✓
   ⟹ 这 115 个脚本**名义上可复跑、实际不可** ✓（**静默失效** ⚠️ —— 最危险的一类技术债 ✓）
【涉及的 5 个数据文件（全部已在 `data/` ✓）】
   zeros_odlyzko_2M.npy ×57 ✓｜zeros_odlyzko_100k.npy ×64 ✓｜zeros_2000.npy ×3 ✓
   ｜dn_results.json ×1 ✓｜trackB_vals.npy ✓
```

## §2 **处置（✓）**
```
【方法】把字面量 `/tmp/<name>` 批量改写为 **`data/<name>`** ✓（仅限 `data/` 中**确实存在**的文件 ✓）
【⚠️ 安全措施】只改写 **今日（9-12）之前**创建/修改的脚本 ✓ —— 避免与**正在运行的子代理**冲突 ✓
【✅ 结果】**109 个脚本已改写** ✓｜**7 个保留**（见 §3 ✓）
【✅ 验证】检查器 **OK, no violations** ✓（scripts tracked ✓、no /tmp writes ✓、headers present ✓）
   抽查：`BL6`/`BL11` 均已含 `data/zeros_odlyzko…` ✓
```

## §3 **保留的 7 个（均为【合理】✓）**
```
【① 4 个我今日写的脚本】`BL16`/`BL17`/`E30_2`/`G6_p27g82` ✓ —— 采用
   **"`data/` 优先 + `/tmp` 兜底"** 模式 ✓（`ZP if os.path.exists(ZP) else '/tmp/...'` ✓）
   ⟹ 这是**有意的** ✓：数据在 `data/` 时读 `data/` ✓；仅有 `/tmp` 副本时也能跑 ✓ —— **不构成风险** ✓
【② 3 个工具脚本】`check_archive.py` ✓（**按设计**检测 `/tmp` 写入 ✓）、`fix_archive_compliance.py` ✓、
   `fix_my_scripts_data_path.py` ✓ —— 它们**引用** `/tmp` 是为了**检查**它 ✓，非依赖 ✓
```

## §4 **效果与残余**
```
【✅ 效果】109 个脚本从"**重启即失效**" ✗ 变为"**读已入仓数据**" ✓✓
【⚠️ 残余风险】`data/` 中的 `zeros_odlyzko_2M.npy`（16 MB ✓）等**已入仓** ✓，
   但 **`setup_data.sh`** ✓ 仍保留（用于在 `/tmp` 建符号链接 ✓，兼容旧脚本 ✓）
【📌 建议】今后新脚本**一律**用 `os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', ...)` ✓
   （**路径无关 CWD** ✓ —— 我今日新写的脚本已按此模式 ✓）
```
