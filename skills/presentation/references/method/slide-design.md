# Slide design with the brand profile

## Select a governing identity

Follow the client's or company's brand system when one applies. The owner's profile is for owner-directed work without another governing identity; its README says review is pending and the missing external references have not yet confirmed which traits recur. [brand-profile README](../../../../tools/brand-profile/README.md); [brand-profile PROFILE](../../../../tools/brand-profile/PROFILE.md), “Evidence and confidence”.

The profile describes two distinct source projects and labels its repeated personal style as a working hypothesis. Choose one coherent visual world for a piece and treat the profile's chosen token values as reviewable defaults, not a permanent palette or owner-approved specification. [brand-profile PROFILE](../../../../tools/brand-profile/PROFILE.md), “Palette”; [brand-profile README](../../../../tools/brand-profile/README.md), “Review status”. (derived: the profile itself limits the evidence for generalizing its observations.)

The shell in [deck-shell.html](../../templates/deck-shell.html) embeds a copy of [tokens.css](../../../../tools/brand-profile/tokens.css) so it renders on its own; update that copy if the profile tokens change, and record the profile's pending owner review when it affects a deliverable. [brand-profile README](../../../../tools/brand-profile/README.md), “For producers”.

## Keep design decisions with their owners

Ask visual-design to establish composition, hierarchy, typography, and repeated structure; ask color-theory to decide palette roles, color meaning, and color checks. This skill applies those decisions to the deck and checks the real slide sizes. [visual-design/SKILL.md](../../../visual-design/SKILL.md#principles--anchoring-rules); [color-theory/SKILL.md](../../../color-theory/SKILL.md#principles).

Do not force a fixed font scale, color recipe, layout variety rule, or visual on every slide. The audience, evidence, and governing identity set those choices; a decorative element that does not help the message can be removed. [visual-design/SKILL.md](../../../visual-design/SKILL.md#principles--anchoring-rules); [book:storytelling-with-data], “Chapter 5: think like a designer”. (derived: the retired production guide's fixed recipes are not source-backed universal rules.)

Carry forward the QA habit of looking for overlap, overflow, wrapping, contrast, alignment, and placeholder content, then fixing and verifying the affected slides. (field rule (pptx))

## Focal marking for checks

Set `data-rk-focal` on the element that carries the main point: on a headline panel for an illustration-plus-copy slide when the illustration is supporting imagery; on the screenshot or meaningful crop when the interface evidence is the point; and on the action title or short takeaway/callout on a dense-text slide. Mark the illustration itself only when the image is the evidence or takeaway. Keep long text as readable evidence without making the whole slide its own focal. A required focal larger than half the stage can make render-kit's `value` result `incomplete`; this is acceptable only as a documented limitation with a vision review, not as an automatic pass. (derived: dogfood 2026-10-02, F7)

If the owner approves changing the `value.min_edge_share` threshold for a documented slide type, pass `--threshold value.min_edge_share=<number>` to `rk check`; record the default result, override value, reason, owner, and affected slides in the review notes, then judge the affected slide visually. Do not silently normalize a threshold change across the deck. (derived: dogfood 2026-10-02, F7)

## Fonts for PowerPoint

HTML font choices do not guarantee the same fonts in PPTX: scene-engine's PowerPoint writer has a limited font set, and unsupported glyphs may fall back. Once the brand profile publishes its Office-safe display/body pair, use that pair for editable PPTX text and verify the exported fonts; until then, record the chosen PPTX fallback and use a native shape or vector asset for a required glyph that does not render reliably. (derived: dogfood 2026-10-02, F9)

## HTML slide markup

Use semantic, media-independent, style-independent markup rather than presentational markup. [book:whatwg-html], “Conformance requirements for authors”. Keep slide content as document text, use meaningful headings and sequence instead of embedding the communication in a bitmap, and mark the slide region with `data-rk-stage` or an intended focal region with `data-rk-focal` when useful to render-kit. [render-kit AGENTS.md](../../../../tools/render-kit/AGENTS.md), “Markup the checks read”. (derived from the source’s accessibility and maintenance rationale for semantic, media-independent markup.)

## Return when

Return to the governing identity if the visual world conflicts with client rules; return to the brief if the system makes the content illegible; return to visual-design or color-theory for decisions in their remit. [visual-design/SKILL.md](../../../visual-design/SKILL.md#composition); [color-theory/SKILL.md](../../../color-theory/SKILL.md#composition). (derived: route each defect to the decision owner.)
