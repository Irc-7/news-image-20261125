#!/usr/bin/env python3
"""Write the entry image to /output/entry.png (standard library only)."""
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.environ.get("MAKEFUN_OUTPUT_DIR") or (sys.argv[1] if len(sys.argv) > 1 else "/output")

os.makedirs(OUT, exist_ok=True)
shutil.copyfile(os.path.join(HERE, "entry.png"), os.path.join(OUT, "entry.png"))
