# Slide design with the brand profile

## Select a governing identity

Follow the client's or company's brand system when one applies. The owner's profile is for owner-directed work without another governing identity; its README says review is pending and the missing external references have not yet confirmed which traits recur. [brand-profile README](../../../../brand-profile/README.md); [brand-profile PROFILE](../../../../brand-profile/PROFILE.md), “Evidence and confidence”.

The profile describes two distinct source projects and labels its repeated personal style as a working hypothesis. Choose one coherent visual world for a piece and treat the profile's chosen token values as reviewable defaults, not a permanent palette or owner-approved specification. [brand-profile PROFILE](../../../../brand-profile/PROFILE.md), “Palette”; [brand-profile README](../../../../brand-profile/README.md), “Review status”. (derived: the profile itself limits the evidence for generalizing its observations.)

The shell in [deck-shell.html](../../templates/deck-shell.html) embeds a copy of [tokens.css](../../../../brand-profile/tokens.css) so it renders on its own; update that copy if the profile tokens change, and record the profile's pending owner review when it affects a deliverable. [brand-profile README](../../../../brand-profile/README.md), “For producers”.

## Keep design decisions with their owners

Ask visual-design to establish composition, hierarchy, typography, and repeated structure; ask color-theory to decide palette roles, color meaning, and color checks. This skill applies those decisions to the deck and checks the real slide sizes. [visual-design/SKILL.md](../../../visual-design/SKILL.md#principles--anchoring-rules); [color-theory/SKILL.md](../../../color-theory/SKILL.md#principles).

Do not force a fixed font scale, color recipe, layout variety rule, or visual on every slide. The audience, evidence, and governing identity set those choices; a decorative element that does not help the message can be removed. [visual-design/SKILL.md](../../../visual-design/SKILL.md#principles--anchoring-rules); [book:storytelling-with-data], “Chapter 5: think like a designer”. (derived: the retired production guide's fixed recipes are not source-backed universal rules.)

Carry forward the QA habit of looking for overlap, overflow, wrapping, contrast, alignment, and placeholder content, then fixing and verifying the affected slides. (field rule (pptx))

## HTML slide markup

Keep slide content as document text and mark the slide region with `data-rk-stage`; mark an intended focal region with `data-rk-focal` when it is useful to render-kit. Use meaningful headings and sequence in the HTML instead of hiding the communication inside a bitmap. [render-kit AGENTS.md](../../../../render-kit/AGENTS.md), “Markup the checks read”; [book:whatwg-html], “Conformance requirements for authors”. (derived: semantic source improves inspection and preserves content beyond the pixels.)

## Return when

Return to the governing identity if the visual world conflicts with client rules; return to the brief if the system makes the content illegible; return to visual-design or color-theory for decisions in their remit. [visual-design/SKILL.md](../../../visual-design/SKILL.md#composition); [color-theory/SKILL.md](../../../color-theory/SKILL.md#composition). (derived: route each defect to the decision owner.)
