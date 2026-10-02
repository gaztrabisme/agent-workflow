import numpy as np

from scripts.color_math import linear_to_srgb, srgb_to_linear


def _rgb_to_hsl(rgb):
    mx, mn = rgb.max(-1), rgb.min(-1)
    d, l = mx-mn, (mx+mn)/2
    s = np.divide(d, 1-np.abs(2*l-1), out=np.zeros_like(d), where=d != 0)
    h = np.zeros_like(d)
    r, g, b = np.moveaxis(rgb, -1, 0)
    nz = d != 0
    mr = nz & (mx == r); mg = nz & (mx == g); mb = nz & (mx == b)
    h[mr] = np.mod((g[mr]-b[mr])/d[mr], 6)
    h[mg] = (b[mg]-r[mg])/d[mg]+2
    h[mb] = (r[mb]-g[mb])/d[mb]+4
    return np.mod(h/6, 1), s, l


def _hsl_to_rgb(h, s, l):
    c = (1-np.abs(2*l-1))*s
    x = c*(1-np.abs(np.mod(h*6, 2)-1))
    m = l-c/2
    z = np.zeros_like(h)
    channels = np.stack((np.select([h<1/6,h<2/6,h<3/6,h<4/6,h<5/6], [c,x,z,z,x], default=c),
                         np.select([h<1/6,h<2/6,h<3/6,h<4/6,h<5/6], [x,c,c,x,z], default=z),
                         np.select([h<1/6,h<2/6,h<3/6,h<4/6,h<5/6], [z,z,x,c,c], default=x)), -1)
    return channels+m[..., None]


def white_balance(rgb, op):
    out = np.asarray(rgb, float)
    linear = srgb_to_linear(out)
    if "neutral_rect" in op:
        x0, y0, x1, y1 = map(int, op["neutral_rect"])
        h, w = linear.shape[:2]
        if x0 < 0 or y0 < 0 or x1 > w or y1 > h or x1 <= x0 or y1 <= y0:
            raise ValueError("neutral_rect must be a non-empty in-bounds x0,y0,x1,y1 pixel box")
        col = linear[y0:y1, x0:x1].mean(axis=(0, 1))
        if np.any(col <= 1e-8):
            raise ValueError("neutral_rect must have non-zero values in every RGB channel")
        gains = np.mean(col)/(col+1e-8)
    elif "neutral" in op:
        x, y = op["neutral"]
        col = linear[min(linear.shape[0]-1, round(y*(linear.shape[0]-1))),
                     min(linear.shape[1]-1, round(x*(linear.shape[1]-1)))].copy()
        if np.any(col <= 1e-8):
            raise ValueError("neutral pixel must have non-zero values in every RGB channel")
        gains = np.mean(col)/(col+1e-8)
    else:
        kelvin = float(op.get("temperature", 6500))
        if not 1000 <= kelvin <= 40000:
            raise ValueError("white-balance temperature must be 1000..40000 K")
        gains = _kelvin_gains(kelvin)
    gains[1] *= 1-float(op.get("tint", 0))/100
    # Normalize the diagonal gains so an equal-channel neutral keeps its Rec.709
    # linear-light luminance after the white-balance shift.
    gains /= np.dot(gains, np.array([.2126, .7152, .0722]))
    return linear_to_srgb(linear*gains)


def _kelvin_gains(k):
    gains = np.asarray(_kelvin_rgb(6500))/np.maximum(_kelvin_rgb(k), 1)
    return gains/np.dot(gains, np.array([.2126, .7152, .0722]))


def _kelvin_rgb(k):
    t = k/100
    r = 255 if t <= 66 else 329.698727446*(t-60)**-.1332047592
    g = 99.4708025861*np.log(t)-161.1195681661 if t <= 66 else 288.1221695283*(t-60)**-.0755148492
    b = 255 if t >= 66 else (0 if t <= 19 else 138.5177312231*np.log(t-10)-305.0447927307)
    return np.array([r, g, b])


def color_adjust(rgb, saturation=1, vibrance=0):
    x = np.asarray(rgb, float)
    lum = np.sum(x*np.array([.2126, .7152, .0722]), axis=-1, keepdims=True)
    span = x.max(-1, keepdims=True)-x.min(-1, keepdims=True)
    adaptive = 1+float(vibrance)*(1-span/(x.max(-1, keepdims=True)+1e-8))
    return lum+(x-lum)*float(saturation)*adaptive


def hsl_bands(rgb, bands):
    h, s, l = _rgb_to_hsl(np.clip(rgb, 0, 1))
    deg = h*360
    for band in bands:
        center = float(band["hue"])%360
        width = max(1, float(band.get("range", 30)))
        distance = np.abs((deg-center+180)%360-180)
        weight = np.clip(1-distance/width, 0, 1)
        h = (h+float(band.get("hue_shift", 0))*weight/360)%1
        s = np.clip(s+float(band.get("saturation", 0))*weight, 0, 1)
        l = np.clip(l+float(band.get("lightness", 0))*weight, 0, 1)
    return _hsl_to_rgb(h, s, l)
