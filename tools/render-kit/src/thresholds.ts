export const DEFAULT_THRESHOLDS: Record<string, Record<string, number>> = {
  overflow: { tolerance_px: 1 }, collision: { min_overlap_px: 1 },
  contrast: { text_exclusion: 0.1, min_background_share: 0.3 }, cvd: { min_distance: 0.06 }, fidelity: { tolerance_px: 0.5 },
};

export function thresholdRows(overrides: Record<string, number>) {
  const out: Record<string, Record<string, number>> = structuredClone(DEFAULT_THRESHOLDS);
  for (const [key, value] of Object.entries(overrides)) {
    const [id, name] = key.split('.'); if (out[id]?.[name] !== undefined) out[id][name] = value;
  }
  return out;
}

export function thresholdFor(id: string, overrides: Record<string, number>) {
  return Object.fromEntries(Object.entries(DEFAULT_THRESHOLDS[id] ?? {}).map(([name, value]) => [name, overrides[`${id}.${name}`] ?? value]));
}
