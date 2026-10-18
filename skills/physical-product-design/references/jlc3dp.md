# JLC3DP (checked 2026-10-17 on the quote page)

- Design guide pages (help/article/...) give no size, wall or tolerance numbers for most materials. The material pages do: PA12-HP nylon is ±0.3 mm within 100 mm and ±0.4% above, 1 mm minimum wall, 370 x 276 x 360 mm. Gap between assembled nylon parts is 0.2–0.4 mm; between moving parts, 0.6 mm.
- Hollow parts need an escape hole. Put a remark on the part saying the hollow is intentional and asking them to clear all powder from inside.
- TPU is FDM here, with a 9 x 9 x 30 mm minimum part size. Join smaller parts (plugs, feet) into one tree with 2.5 x 1.4 mm tabs on a runner and cut them apart on arrival. The quote page accepted a 114 x 24 x 10 mm tree.
- Black dyeing is a Dyeing option on PA12-HP nylon. Black resins cost about 2x white 9600 resin.
- Quote price for nylon is about $0.38 per cm³ plus about $19 fixed (two points: 387 cm³ = $165.72, 284 cm³ = $126.72).
- Each part needs a customs "Product Desc": Office Appliance and Accessories > others, free text of 30 characters or fewer.
- Wood is not offered.

## Quote page in Chrome (mcp__claude-in-chrome)

- Load tools first: ToolSearch select:mcp__claude-in-chrome__tabs_context_mcp,navigate,computer,find,file_upload,browser_batch,javascript_tool.
- The page has one hidden multi-file input. A 19-file upload in one call added nothing; upload one STL per call and wait about 6 s for "Edit Specifications" to appear.
- Refs go stale after any dialog. Re-run find before each click, or click by coordinate.
- Read the list with javascript_tool on document.body.innerText. location.href comes back "[BLOCKED: Cookie/query string data]".
- Parts go to the cart only after Save to Cart, and the cart items are not ticked for checkout. Never tick the terms box; if it is pre-ticked, tell Huy.
- Quote-only price checks: open the part, change the material, read the price, close with Discard. The cart stays untouched.
- Uploaded-but-unsaved files stay on the quote page. Delete them before finishing.

## Order handling

Add parts to the cart only when Huy asks; never check out. Delete only the quote-page items this session uploaded. Report what the cart holds, what is ticked and what Huy must tick. Quote "price before shipping".
