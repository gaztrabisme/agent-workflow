import numpy as np

from scripts.color_math import delta_e_2000, rgb_to_lab


def _describe(values):
    if not len(values):
        return {"count": 0, "mean": None, "max": None, "p99": None}
    return {"count": int(len(values)), "mean": float(values.mean()),
            "max": float(values.max()), "p99": float(np.percentile(values, 99))}


def measure(rgb, mask=None):
    lab = rgb_to_lab(rgb)
    encoded = np.clip(rgb, 0, 1)
    flat = encoded.reshape(-1, 3)
    hist = [np.histogram(flat[:, c], bins=16, range=(0, 1))[0].tolist() for c in range(3)]
    clipped = ((flat <= .01).any(1), (flat >= .99).any(1))
    chroma = np.hypot(lab[..., 1], lab[..., 2])
    neutral = (chroma < 12) & (lab[..., 0] > 15) & (lab[..., 0] < 98)
    patch = lab[neutral]
    result = {"histogram_bins": 16, "histogram_rgb": hist,
              "channel_mean": flat.mean(0).tolist(), "channel_std": flat.std(0).tolist(),
              "clipped_shadows_pct": float(clipped[0].mean()*100),
              "clipped_highlights_pct": float(clipped[1].mean()*100),
              "neutral_patch": {"method": "Lab chroma < 12, 15 < L* < 98",
                                "count": int(len(patch)),
                                "a_mean": float(patch[:, 1].mean()) if len(patch) else None,
                                "b_mean": float(patch[:, 2].mean()) if len(patch) else None,
                                "a_std": float(patch[:, 1].std()) if len(patch) else None,
                                "b_std": float(patch[:, 2].std()) if len(patch) else None}}
    ab = result["neutral_patch"]
    abmean = np.array([ab["a_mean"], ab["b_mean"]], dtype=object)
    result["colour_cast"] = {"a_star": ab["a_mean"], "b_star": ab["b_mean"],
                             "chroma": float(np.hypot(*abmean.astype(float)))
                             if ab["a_mean"] is not None and ab["b_mean"] is not None else None}
    skin = None
    if mask is not None:
        skin = lab[(mask >= .5) & (chroma > 2)]
    if skin is None or not len(skin):
        result["skin_tone"] = {"count": 0, "hue_angle_deg": None, "circular_spread_deg": None}
    else:
        angles = np.arctan2(skin[:, 2], skin[:, 1])
        mean_angle = np.arctan2(np.sin(angles).mean(), np.cos(angles).mean())
        resultant = np.hypot(np.sin(angles).mean(), np.cos(angles).mean())
        spread = np.degrees(np.sqrt(max(0, -2*np.log(max(resultant, 1e-12)))) )
        result["skin_tone"] = {"count": int(len(skin)), "hue_angle_deg": float(np.degrees(mean_angle)%360),
                               "circular_spread_deg": float(spread)}
    return result


def compare_metrics(a, b, mask=None):
    if a.shape != b.shape:
        raise ValueError("comparison images must have matching dimensions")
    delta = delta_e_2000(rgb_to_lab(a), rgb_to_lab(b))
    out = {"delta_e_2000": {"all": _describe(delta.ravel())}}
    if mask is None:
        out["delta_e_2000"].update({"inside_mask": None, "outside_mask": _describe(delta.ravel())})
    else:
        inside = mask >= .5
        out["delta_e_2000"].update({"inside_mask": _describe(delta[inside]),
                                    "outside_mask": _describe(delta[~inside])})
    return out
