import numpy as np


def srgb_to_linear(rgb):
    rgb = np.asarray(rgb, dtype=np.float64)
    return np.where(rgb <= 0.04045, rgb / 12.92, ((rgb + 0.055) / 1.055) ** 2.4)


def linear_to_srgb(rgb):
    rgb = np.asarray(rgb, dtype=np.float64)
    return np.where(rgb <= 0.0031308, rgb * 12.92, 1.055 * np.maximum(rgb, 0) ** (1 / 2.4) - 0.055)


def rgb_to_lab(rgb):
    r, g, b = np.moveaxis(srgb_to_linear(rgb), -1, 0)
    xyz = np.stack((.4124564*r+.3575761*g+.1804375*b,
                    .2126729*r+.7151522*g+.0721750*b,
                    .0193339*r+.1191920*g+.9503041*b), axis=-1)
    xyz /= np.array([.95047, 1.0, 1.08883])
    d = 6 / 29
    f = np.where(xyz > d**3, np.cbrt(xyz), xyz / (3*d*d) + 4/29)
    x, y, z = np.moveaxis(f, -1, 0)
    return np.stack((116*y-16, 500*(x-y), 200*(y-z)), axis=-1)


def delta_e_2000(lab1, lab2):
    l1, a1, b1 = np.moveaxis(np.asarray(lab1, float), -1, 0)
    l2, a2, b2 = np.moveaxis(np.asarray(lab2, float), -1, 0)
    c1, c2 = np.hypot(a1, b1), np.hypot(a2, b2)
    cb = (c1+c2)/2
    g = .5*(1-np.sqrt(cb**7/(cb**7+25**7)))
    ap1, ap2 = (1+g)*a1, (1+g)*a2
    cp1, cp2 = np.hypot(ap1, b1), np.hypot(ap2, b2)
    hp1 = np.mod(np.degrees(np.arctan2(b1, ap1)), 360)
    hp2 = np.mod(np.degrees(np.arctan2(b2, ap2)), 360)
    hp1, hp2 = np.where(cp1 == 0, 0, hp1), np.where(cp2 == 0, 0, hp2)
    dl, dc = l2-l1, cp2-cp1
    dh = hp2-hp1
    dh = np.where(dh > 180, dh-360, np.where(dh < -180, dh+360, dh))
    dh = np.where(cp1*cp2 == 0, 0, dh)
    d_h = 2*np.sqrt(cp1*cp2)*np.sin(np.radians(dh/2))
    lm, cm = (l1+l2)/2, (cp1+cp2)/2
    hs = hp1+hp2
    hm = np.where(np.abs(hp1-hp2) <= 180, hs/2,
                  np.where(hs < 360, (hs+360)/2, (hs-360)/2))
    hm = np.where(cp1*cp2 == 0, hs, hm)
    t = (1-.17*np.cos(np.radians(hm-30))+.24*np.cos(np.radians(2*hm))
         +.32*np.cos(np.radians(3*hm+6))-.20*np.cos(np.radians(4*hm-63)))
    sl = 1+.015*(lm-50)**2/np.sqrt(20+(lm-50)**2)
    sc, sh = 1+.045*cm, 1+.015*cm*t
    rt = -2*np.sqrt(cm**7/(cm**7+25**7))*np.sin(np.radians(60*np.exp(-((hm-275)/25)**2)))
    x, y, z = dl/sl, dc/sc, d_h/sh
    return np.sqrt(np.maximum(0, x*x+y*y+z*z+rt*y*z))
