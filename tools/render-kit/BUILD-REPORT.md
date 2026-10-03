# Build report

**Verdict: PASS.** The render-kit contract is implemented. No dependencies were added and no files outside the project or `/tmp` were changed.

## Built

- `bin/rk` CLI with direct Node 24 TypeScript execution; local HTTP serving, deterministic Chromium rendering, PNG/PDF output, scene-time seeking, color simulation, and text measurement/wrapping.
- All eleven checks, threshold overrides, JSON reports, `brief` generation/verification, and sample selftest.
- Chart and slide question sets, six good samples, eleven isolated bad samples, and expectations. No sample needs a bundled font, so `samples/fonts/README.md` records that no OFL font or licence file is required.
- Unit tests and acceptance coverage for AT01–AT21 plus AT23–AT27.

## Verification

- `npm run typecheck`: passed.
- `npm test`: exit 0; 33 passed, 0 failed. Its final lines were:

  ```text
  ℹ tests 33
  ℹ suites 0
  ℹ pass 33
  ℹ fail 0
  ℹ cancelled 0
  ℹ skipped 0
  ℹ todo 0
  ℹ duration_ms 106242.57525
  ```

- `./bin/rk selftest`: exit 0; all 17 good/bad samples matched their expectations. The final JSON summary reported `"ok":true`.
- AT22, `time ./bin/rk check samples/good/slide.html`: **2.795 s total**, under the 20 s limit.
- AT26 dense sample: **7.69 s**, under the 60 s limit.
- AT02 PDF inspection: one 720 × 405 pt page; `pdfimages -list` reports no raster images.
- `git diff --check`: passed.

## Deviations and choices

- Chromium emitted a 404.88 pt PDF height for a 405 CSS px SVG. `src/pdf-size.ts` normalizes the PDF page boxes in place to the exact 720 × 405 pt size required by AT02; the export remains vector.
- If the configured contrast text-exclusion distance removes every pixel in a text box, the sampler retries at 0.01 OKLab distance so solid, low-contrast text such as AT10 still gets a measured ratio. The configured exclusion and minimum background share are otherwise honored.
- The SVG input is served in a transparent HTML wrapper sized from its intrinsic dimensions. This gives the SVG the same local HTTP origin and predictable capture/PDF page size as HTML inputs.
- Axe runs in a fresh browser context because it does not complete reliably under the render page's frozen clock. The context uses the same URL and network policy. Resource-owned browser console messages are left to the `resources` check so a blocked request does not also fail `console` (AT05).
- When color-theory prints no `T<n>` result line, `value` is skipped unless another parsed test line failed; a parsed failure remains a failure even if the chroma command has no `T` line.

## Open issues

- Sample fonts are not bundled; output can vary across machines with different installed fonts. The `fonts` check identifies fallback.
- Raster output may vary across machines with different graphics hardware. Byte-identical determinism is verified on this build machine.
- The remaining open questions in SPEC.md section 12 (including WebGPU, PDF/UA, and a second accessibility engine) are deferred as specified there.
