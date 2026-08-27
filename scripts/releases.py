import os
from pathlib import Path
import tarfile
import tomllib
import tomllib


ROOT = Path(__file__).parent.parent

templates_dir = Path(os.path.join(ROOT, "templates")) 
DIST = Path(os.path.join(ROOT, "dist"))




os.makedirs(DIST, exist_ok=True)

for lang in templates_dir.iterdir():
    if not lang.is_dir() or lang.name == "shipped":
        continue

    for template in lang.iterdir():
        if not template.is_dir():
            continue

        with open(os.path.join(template, "manifest.toml"), "rb") as f:
            data = tomllib.load(f)
        v = data["version"]

        with tarfile.open(os.path.join(DIST, f"{lang.name}-{template.name}-{v}.tar.gz"), "w:gz") as tar:
            tar.add(template)


