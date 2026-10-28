# -*- coding: utf-8 -*-
from pathlib import Path

t = Path("_zn_t4_gen.py").read_text(encoding="utf-8")
t = t.replace(
    "batch-T4 (Spring-Autumn / Warring States)",
    "batch-T5 (Qin-Han, first half)",
).replace(
    'for part in ("_zn_t4_e1.py",):',
    'for part in ("_zn_t5_e1.py", "_zn_t5_e2.py"):',
)
Path("_zn_t5_gen.py").write_text(t, encoding="utf-8", newline="\n")
print("rewritten")
