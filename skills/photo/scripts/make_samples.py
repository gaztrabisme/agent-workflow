#!/usr/bin/env python3
import json
import subprocess
import sys
from pathlib import Path

import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from scripts.image_io import save_rgb


def build():
    folder = ROOT/"samples"
    folder.mkdir(exist_ok=True)
    h, w = 128, 192
    yy, xx = np.mgrid[0:h, 0:w]
    portrait = np.zeros((h, w, 3), float)
    portrait[..., 0] = .13+.22*xx/w
    portrait[..., 1] = .25+.18*yy/h
    portrait[..., 2] = .42-.13*xx/w
    face = ((xx-91)/27)**2+((yy-51)/35)**2 <= 1
    skin = np.stack((.73-.10*yy/h, .43-.04*yy/h, .31-.02*yy/h), axis=-1)
    portrait[face] = skin[face]
    shoulders = ((xx-94)/45)**2+((yy-121)/34)**2 <= 1
    portrait[shoulders] = [.27, .31, .39]
    portrait[88:110, 148:180] = [.52, .53, .51]
    mask = np.zeros((h, w), np.uint8)
    mask[face] = 255
    save_rgb(portrait, folder/"portrait.png")
    Image.fromarray(mask).save(folder/"mask.png")
    good = portrait.copy()
    good[face] = np.clip(good[face]*[1.04, 1.015, 1.0], 0, 1)
    save_rgb(good, folder/"edited-good.png")
    leak = good.copy()
    leak[8:28, 8:28] = np.clip(leak[8:28, 8:28]+[.12, .025, -.02], 0, 1)
    save_rgb(leak, folder/"edited-leak.png")
    recipe = {"operations": [{"type": "exposure", "stops": .12},
                              {"type": "white_balance", "temperature": 6100, "tint": 1},
                              {"type": "levels", "black": .015, "white": .98, "gamma": 1.02},
                              {"type": "saturation", "factor": 1.05},
                              {"type": "vignette", "strength": .12, "radius": .72}]}
    (folder/"portrait-recipe.json").write_text(json.dumps(recipe, indent=2)+"\n", encoding="utf-8")
    land = np.zeros((h, w, 3), float)
    land[..., 0] = .34+.18*yy/h; land[..., 1] = .62+.13*yy/h; land[..., 2] = .85-.18*yy/h
    ridge1 = 43+13*np.sin(xx/21)+7*np.sin(xx/8)
    ridge2 = 72+10*np.sin(xx/28+1)+5*np.cos(xx/11)
    land[yy > ridge1] = [.31, .39, .43]
    land[yy > ridge2] = [.24, .38, .29]
    ground = yy > 93
    land[..., 0][ground] = .22+.08*xx[ground]/w
    land[..., 1][ground] = .39
    land[..., 2][ground] = .21
    sun = (xx-151)**2+(yy-27)**2 < 9**2
    land[sun] = [.99, .82, .55]
    save_rgb(land, folder/"landscape.png")
    out = folder/"out"
    out.mkdir(exist_ok=True)
    run = subprocess.run([sys.executable, str(ROOT/"scripts/roundtrip.py"), "verify",
                          str(folder/"portrait.png"), str(folder/"edited-good.png"),
                          "--mask", str(folder/"mask.png"), "--out", str(out)],
                         check=False, capture_output=True, text=True)
    print(run.stdout, end="")
    if run.returncode:
        print(run.stderr, file=sys.stderr, end="")
        raise SystemExit(run.returncode)


if __name__ == "__main__":
    build()
