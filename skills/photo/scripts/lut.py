import numpy as np
from pathlib import Path


def parse_cube(source):
    is_text = isinstance(source, str) and ("\n" in source or source.lstrip().startswith("LUT_"))
    lines = source.splitlines() if is_text else Path(source).read_text(encoding="utf-8").splitlines()
    size, low, high, values = None, np.zeros(3), np.ones(3), []
    for line in lines:
        row = line.split("#", 1)[0].strip()
        if not row or row.startswith("TITLE"):
            continue
        parts = row.split()
        if parts[0] == "LUT_3D_SIZE":
            size = int(parts[1])
        elif parts[0] == "DOMAIN_MIN":
            low = np.array(parts[1:], float)
        elif parts[0] == "DOMAIN_MAX":
            high = np.array(parts[1:], float)
        elif parts[0] == "LUT_1D_SIZE":
            raise ValueError("1D LUT sections are not supported")
        else:
            values.append([float(v) for v in parts[:3]])
    if size is None or size < 2 or len(values) != size**3:
        raise ValueError("invalid .cube 3D LUT size or data count")
    if np.any(high <= low):
        raise ValueError(".cube DOMAIN_MAX must exceed DOMAIN_MIN")
    return size, low, high, np.asarray(values).reshape(size, size, size, 3)


def apply_cube(rgb, source):
    size, low, high, table = parse_cube(source)
    p = np.clip((np.asarray(rgb, float)-low)/(high-low), 0, 1)*(size-1)
    base = np.floor(p).astype(int)
    upper = np.minimum(base+1, size-1)
    frac = p-base
    out = np.zeros_like(p)
    for bz in (0, 1):
        for gy in (0, 1):
            for rx in (0, 1):
                w = ((frac[..., 2] if bz else 1-frac[..., 2])
                     *(frac[..., 1] if gy else 1-frac[..., 1])
                     *(frac[..., 0] if rx else 1-frac[..., 0]))
                ri = upper[..., 0] if rx else base[..., 0]
                gi = upper[..., 1] if gy else base[..., 1]
                bi = upper[..., 2] if bz else base[..., 2]
                out += table[bi, gi, ri] * w[..., None]
    return out
