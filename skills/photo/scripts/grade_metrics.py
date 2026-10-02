import numpy as np

from scripts.color_math import delta_e_2000, rgb_to_lab


def _describe(values):
    if not len(values):
        return {"count": 0, "mean": None, "max": None, "p99": None}
    return {"count": int(len(values)), "mean": float(values.mean()),
            "max": float(values.max()), "p99": float(np.percentile(values, 99))}


def recipe_output_range_warnings(recipe):
    """Flag explicit curve/levels endpoints that lift black or lower white."""
    operations = recipe.get("operations") if isinstance(recipe, dict) else recipe
    if not isinstance(operations, list):
        raise ValueError("recipe must be an array or an object with an operations array")
    warnings = []
    for index, op in enumerate(operations):
        if not isinstance(op, dict):
            continue
        kind = op.get("type")
        low = high = None
        if kind == "tone_curve":
            points = sorted((float(x), float(y)) for x, y in op.get("points", []))
            if len(points) >= 2:
                low = points[0][1]
                high = points[-1][1]
        elif kind == "levels":
            black, white, gamma = (float(op.get("black", 0)), float(op.get("white", 1)),
                                   float(op.get("gamma", 1)))
            if white > black and gamma > 0:
                low = float(np.clip((0-black)/(white-black), 0, 1)**(1/gamma))
                high = float(np.clip((1-black)/(white-black), 0, 1)**(1/gamma))
        if low is not None and low > 1e-8:
            warnings.append(f"operation {index} ({kind}) lifts encoded black to {low:.6g}; shadow clipping may fall without recovered detail")
        if high is not None and high < 1-1e-8:
            warnings.append(f"operation {index} ({kind}) lowers encoded white to {high:.6g}; highlight clipping may fall without recovered detail")
    return warnings


def measure(rgb, mask=None, neutral_mask=None, neutral_rect=None):
    lab = rgb_to_lab(rgb)
    encoded = np.clip(rgb, 0, 1)
    flat = encoded.reshape(-1, 3)
    hist = [np.histogram(flat[:, c], bins=16, range=(0, 1))[0].tolist() for c in range(3)]
    clipped = ((flat <= .01).any(1), (flat >= .99).any(1))
    chroma = np.hypot(lab[..., 1], lab[..., 2])
    if neutral_mask is not None and neutral_rect is not None:
        raise ValueError("choose either a neutral mask or neutral rectangle")
    neutral_warnings = []
    if neutral_mask is not None:
        if neutral_mask.shape != rgb.shape[:2]:
            raise ValueError("neutral mask dimensions must match the image")
        selected = neutral_mask >= .5
        method = "user-selected neutral mask; all selected pixels included"
    elif neutral_rect is not None:
        x0, y0, x1, y1 = map(int, neutral_rect)
        h, w = rgb.shape[:2]
        if x0 < 0 or y0 < 0 or x1 > w or y1 > h or x1 <= x0 or y1 <= y0:
            raise ValueError("neutral rectangle must be a non-empty in-bounds x0,y0,x1,y1 box")
        selected = np.zeros((h, w), dtype=bool)
        selected[y0:y1, x0:x1] = True
        method = "user-selected neutral rectangle; all selected pixels included"
    else:
        selected = (chroma < 12) & (lab[..., 0] > 15) & (lab[..., 0] < 98)
        method = "fallback estimate: Lab chroma < 12 and 15 < L* < 98"
        if selected.mean() < .05:
            neutral_warnings.append("heuristic neutral selection is below 5% of the image; cast readings may be unstable")
        if selected.mean() > .5:
            neutral_warnings.append("heuristic selection covers over half the image; choose a neutral rectangle or mask for a local cast reading")
    patch = lab[selected]
    selected_share = float(selected.mean())
    if selected.sum() < 64:
        neutral_warnings.append("neutral selection has fewer than 64 pixels; the cast reading may be unstable")
    if neutral_mask is not None or neutral_rect is not None:
        if len(patch) and float(np.hypot(patch[:, 1], patch[:, 2]).mean()) >= 12:
            neutral_warnings.append("selected region has mean chroma at or above 12; verify it is neutral, but its pixels remain included")
    result = {"histogram_bins": 16, "histogram_rgb": hist,
              "channel_mean": flat.mean(0).tolist(), "channel_std": flat.std(0).tolist(),
              "clipped_shadows_pct": float(clipped[0].mean()*100),
              "clipped_highlights_pct": float(clipped[1].mean()*100),
              "neutral_patch": {"method": method,
                                "count": int(len(patch)),
                                "selection_share_of_image": selected_share,
                                "a_mean": float(patch[:, 1].mean()) if len(patch) else None,
                                "b_mean": float(patch[:, 2].mean()) if len(patch) else None,
                                "a_std": float(patch[:, 1].std()) if len(patch) else None,
                                "b_std": float(patch[:, 2].std()) if len(patch) else None,
                                "warnings": neutral_warnings}}
    ab = result["neutral_patch"]
    abmean = np.array([ab["a_mean"], ab["b_mean"]], dtype=object)
    result["colour_cast"] = {"a_star": ab["a_mean"], "b_star": ab["b_mean"],
                             "chroma": float(np.hypot(*abmean.astype(float)))
                             if ab["a_mean"] is not None and ab["b_mean"] is not None else None}
    skin = None
    if mask is not None:
        selected_mask = mask >= .5
        skin = lab[selected_mask & (chroma > 2)]
        masked_lab = lab[selected_mask]
        masked_rgb = encoded[selected_mask]
        masked_flat = masked_rgb.reshape(-1, 3)
        masked_hist = np.histogram(masked_lab[:, 0], bins=16, range=(0, 100))[0].tolist()
        masked_clipped = ((masked_flat <= .01).any(1), (masked_flat >= .99).any(1))
        masked_chroma = np.hypot(masked_lab[:, 1], masked_lab[:, 2])
        result["masked_region"] = {
            "count": int(len(masked_lab)),
            "share_of_image": float(selected_mask.mean()),
            "l_star_mean": float(masked_lab[:, 0].mean()) if len(masked_lab) else None,
            "l_star_std": float(masked_lab[:, 0].std()) if len(masked_lab) else None,
            "c_star_mean": float(masked_chroma.mean()) if len(masked_lab) else None,
            "c_star_std": float(masked_chroma.std()) if len(masked_lab) else None,
            "clipped_shadows_pct": float(masked_clipped[0].mean()*100) if len(masked_lab) else None,
            "clipped_highlights_pct": float(masked_clipped[1].mean()*100) if len(masked_lab) else None,
            "histogram_l_star_bins": 16,
            "histogram_l_star_0_100": masked_hist,
        }
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
        out["delta_e_2000"].update({"mask": None, "outside_mask": _describe(delta.ravel())})
    else:
        inside = mask >= .5
        out["delta_e_2000"].update({"mask": _describe(delta[inside]),
                                    "outside_mask": _describe(delta[~inside])})
    return out
