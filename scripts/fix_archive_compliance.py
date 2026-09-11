#!/usr/bin/env python3
"""
fix_archive_compliance.py -- one-off repair pass for the code-archive protocol.

  (a) prepends a standard provenance header to every scripts/*.py that lacks a module docstring
      (the header is explicitly marked as retroactively added, so nothing is misrepresented);
  (b) rewrites output paths that point into /tmp so that they land in scripts/ instead
      (only for WRITE contexts; /tmp reads are left alone, they are restored by setup_data.sh).

Run from the repository root:  python3 scripts/fix_archive_compliance.py
"""
import os, re, shutil
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS = os.path.join(ROOT, 'scripts')
HEADER = ('"""\n'
          'Provenance: retroactive archive header added {date} by scripts/fix_archive_compliance.py\n'
          'under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).\n'
          'The analysis itself was performed earlier; this header only records the file\'s existence\n'
          'in the committed archive so that the computation is reproducible. Original code below.\n'
          '"""\n')
has_doc = re.compile(r'\s*(?:#![^\n]*\n)?\s*(?:"""|\'\'\')')
write_tmp = re.compile(r"(open\s*\(\s*['\"])(/tmp/[^'\"]+)(['\"]\s*,\s*['\"][wa])")
save_tmp  = re.compile(r"((?:savez?\w*|savetxt|to_csv)\s*\(\s*['\"])(/tmp/[^'\"]+)")
n_hdr = n_red = 0
for name in sorted(os.listdir(SCRIPTS)):
    if not name.endswith('.py') or name == 'fix_archive_compliance.py': continue
    path = os.path.join(SCRIPTS, name)
    src = open(path, encoding='utf-8', errors='replace').read()
    new = src
    if not has_doc.match(src):
        if src.startswith('#!'):
            i = src.index('\n') + 1
            new = src[:i] + HEADER.format(date='2026-09-11') + src[i:]
        else:
            new = HEADER.format(date='2026-09-11') + src
        n_hdr += 1
    new2 = write_tmp.sub(lambda m: m.group(1) + 'scripts/' + os.path.basename(m.group(2)) + m.group(3), new)
    new2 = save_tmp.sub(lambda m: m.group(1) + 'scripts/' + os.path.basename(m.group(2)), new2)
    if new2 != new: n_red += 1
    if new2 != src:
        shutil.copy2(path, path + '.bak')
        open(path, 'w', encoding='utf-8').write(new2)
print("headers added: %d ; /tmp output paths redirected: %d" % (n_hdr, n_red))
