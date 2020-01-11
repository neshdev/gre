import os
from pathlib import Path

for x in range(1, 28):
    folder = f"test{x:02d}"
    Path(folder).mkdir(exist_ok=True)
    for s in range(1, 8):
        section = f"section{s:02d}"
        Path(f"{folder}/{section}").mkdir(exist_ok=True)
