#!/usr/bin/env python3
"""
check_archive.py -- enforce the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md).

Checks (each violation is reported and makes the exit code non-zero):
  V1  untracked .py files under scripts/
  V2  scripts that WRITE to /tmp (open(...,'w'), save/savez/savetxt/to_csv/np.save with /tmp)
  V3  scripts without a module docstring
  V4  untracked .txt files under scripts/
Usage:  python3 scripts/check_archive.py      (run from the repository root)
"""
import os, re, subprocess, sys
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS = os.path.join(ROOT, 'scripts')

def git_untracked():
    try:
        out = subprocess.run(['git','-C',ROOT,'status','--porcelain','--','scripts'],
                             capture_output=True, text=True, timeout=60).stdout
    except Exception:
        return []
    return [l[3:].strip() for l in out.splitlines() if l.startswith('??')]

WRITE_TMP = re.compile(r"""(open\s*\(\s*['"]/tmp|savez?\w*\s*\(\s*['"]/tmp|savetxt\s*\(\s*['"]/tmp|to_csv\s*\(\s*['"]/tmp|open\s*\(\s*['"]/tmp[^)]*['"]\s*,\s*['"][wa])""")

def main():
    viol = []
    untracked = git_untracked()
    for p in untracked:
        full = os.path.join(ROOT, p)
        if p.endswith('.py'): viol.append(('V1', p))
        elif p.endswith('.txt'): viol.append(('V4', p))
    for name in sorted(os.listdir(SCRIPTS)):
        if not name.endswith('.py'): continue
        path = os.path.join(SCRIPTS, name)
        try: src = open(path, encoding='utf-8', errors='replace').read()
        except Exception as e: viol.append(('V3', name + ' (unreadable)')); continue
        m = re.match(r'\s*(?:#![^\n]*\n)?\s*(?:"""(.*?)"""|\'\'\'(.*?)\'\'\')', src, re.S)
        if not m: viol.append(('V3', name))
        for i, line in enumerate(src.splitlines(), 1):
            if WRITE_TMP.search(line):
                viol.append(('V2', '%s:%d  %s' % (name, i, line.strip()[:90])))
    print("="*96); print("check_archive.py -- code-archive protocol check"); print("="*96)
    if not viol:
        print("  OK: no violations. (scripts tracked, no /tmp writes, headers present, outputs tracked)")
    else:
        byk = {}
        for k, v in viol: byk.setdefault(k, []).append(v)
        for k in sorted(byk):
            print("  [%s] %d violation(s):" % (k, len(byk[k])))
            for v in byk[k][:12]: print("      ", v)
            if len(byk[k]) > 12: print("       ... and %d more" % (len(byk[k])-12))
        print()
        print("  RULE: see docs/PROTOCOL-CODE-ARCHIVE.md (R1-R6). Commit the scripts, move data to")
        print("        data/, write outputs under scripts/, and add a module docstring.")
    print("="*96)
    return 1 if viol else 0
if __name__ == '__main__':
    sys.exit(main())
