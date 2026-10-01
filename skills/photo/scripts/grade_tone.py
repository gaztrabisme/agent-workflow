import numpy as np


def levels(rgb, black=0, white=1, gamma=1):
    if white <= black or gamma <= 0:
        raise ValueError("levels require white > black and gamma > 0")
    return np.clip((np.asarray(rgb, float)-black)/(white-black), 0, 1) ** (1/gamma)


def tone_curve(rgb, points):
    pts = sorted((float(x), float(y)) for x, y in points)
    if len(pts) < 2 or any(pts[i][0] >= pts[i+1][0] for i in range(len(pts)-1)):
        raise ValueError("tone curve needs at least two points with unique increasing x")
    return np.interp(np.asarray(rgb, float), [p[0] for p in pts], [p[1] for p in pts])


def vignette(rgb, strength=.25, radius=.72, center=(.5, .5)):
    if not 0 <= strength <= 1 or radius <= 0:
        raise ValueError("vignette strength must be 0..1 and radius positive")
    h, w = rgb.shape[:2]
    yy, xx = np.mgrid[0:h, 0:w]
    distance = np.sqrt((2*(xx/max(1, w-1)-center[0]))**2+
                       (2*(yy/max(1, h-1)-center[1]))**2)
    falloff = np.clip((distance-radius)/(max(.01, np.sqrt(2)-radius)), 0, 1)**2
    return np.asarray(rgb, float)*(1-strength*falloff[..., None])
