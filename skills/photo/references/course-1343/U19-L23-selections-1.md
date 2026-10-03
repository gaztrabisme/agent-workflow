# Lesson 23 · Selections 1

Anchor: 1343 · U19 · L23 · 12:41 · https://www.domestika.org/en/courses/1971-course-2-retouching-fundamentals/units/6426-selections#course_lesson_19382

## Why we make selections

Anchor: 1343 · U19 · L23 · 00:00–01:01

Selections let us edit part of an image or cut something out. This lesson covers the basics, from a simple marquee selection to a complex cutout. Photoshop offers many selection methods because some jobs need pixel-perfect edges while others need only a fast, rough selection. The right tool depends on the work.

## Lasso selection modes

Anchor: 1343 · U19 · L23 · 01:01–03:10

For a rough selection, such as isolating one of the umbrellas or parasols to change its colour, I would use the Lasso tool. The four selection-mode icons are not especially intuitive at first, so it helps to learn what they mean and to use keyboard shortcuts as well as, or instead of, the buttons.

The first mode creates a new selection. Each new stroke replaces the previous selection. Add to Selection lets me build up a selection; the plus sign beside the cursor shows that this mode is active, and I can keep separate areas selected at once. Subtract from Selection removes an area I draw around, or a larger part of the existing selection. Intersect with Selection keeps only the area where two selections overlap. I rarely use intersect, and find it a little counterintuitive, though it can be useful with shapes.

![1343 · U19 · L23 · 01:17](frames/U19L23-F0117.00.jpg)

On screen: [none]  
Shows: The beach photograph with several bright orange parasols and turquoise chairs.

![1343 · U19 · L23 · 02:54](frames/U19L23-F0254.00.jpg)

On screen: "Feather: 0 px" [rest omitted]  
Shows: A lasso selection around a patch of sand, with the selection-mode controls enlarged.

## Feathering and selection shortcuts

Anchor: 1343 · U19 · L23 · 03:10–05:54

Feather softens the edge of a selection. I can type a feather value in the options, but I usually prefer Select and Mask because I can see the effect. A number alone does not tell me what the edge will look like until I apply the selection. In Select and Mask, Overlay is a useful view for judging the soft edge. The default Marching Ants view does not show the feathering result clearly; switching to Overlay gives a better indication. Increasing Feather makes the edge soften gradually.

I cancel the dialog and deselect with Command or Control+D. When I return to the first selection mode, I can hold Shift while drawing to add to the selection; the plus sign appears beside the cursor. Holding Alt or Option temporarily switches to subtract mode, shown by a minus sign, so I can remove part of the selection. I recommend ticking “Don't show again” in the mode prompt. I usually leave Add to Selection as the default because I rarely want every new stroke to replace the selection, and use Alt or Option when I need to subtract. Command or Control+D deselects again. Another way to make a broad selection is Command or Control+A to select the whole image, then subtract an area; the result is everything except that removed area.

![1343 · U19 · L23 · 03:54](frames/U19L23-F0354.00.jpg)

On screen: "View Mode" / "Indicates: Masked Areas" / "Smooth: 0" / "Feather: 0.0 px" / "Contrast: 0%" / "Shift Edge: 0%" [rest omitted]  
Shows: The parasol photograph under a red Overlay preview in Select and Mask, with the refinement controls visible.

![1343 · U19 · L23 · 04:21](frames/U19L23-F0421.00.jpg)

On screen: "Feather: 15.1 px" [rest omitted]  
Shows: The small sand selection has a softened edge against the red Overlay.

## Refine the parasol selection

Anchor: 1343 · U19 · L23 · 05:54–09:29

As I showed in an earlier video, I could change the colour of this umbrella with the Colour Replacement tool, but here I use a much quicker method: I make a quick selection around it. A very sharp edge could leave a yellow fringe against the sand, so I soften the edge in Select and Mask. The available views help me judge different cutouts: On Black is useful when the cutout will sit on a dark background, and On White when it will sit on a light one.

Black & White can be especially useful as the work becomes more advanced because it shows how Photoshop reads the selection: white is fully selected, black is fully deselected, and shades of grey represent partial selection. A feathered edge therefore appears as greyscale. Smooth and Feather are not the same: a little Smooth can straighten a jagged edge, while Feather softens it. We will learn more about this when we start talking about layer masks. I return to Overlay so I can see the parasol against the photograph, apply some feathering, and check that the edge has softened.

![1343 · U19 · L23 · 06:56](frames/U19L23-F0656.00.jpg)

On screen: "Onion Skin (O)" / "Marching Ants (M)" / "Overlay (V)" / "On Black (A)" / "On White (T)" / "Black & White (K)" / "On Layers (Y)" [rest omitted]  
Shows: The view-mode menu over the parasol photograph, with the selected parasol outlined and the other parasols under the red Overlay.

A useful Select and Mask option is Invert, which turns the selection inside out: selected areas become deselected and everything else becomes selected. In versions without this button, use Select > Select and Inverse. I leave the refined parasol selection ready for the colour adjustment.

![1343 · U19 · L23 · 07:46](frames/U19L23-F0746.00.jpg)

On screen: [rest omitted]  
Shows: The parasol selection displayed as a black-and-white mask: the selected parasol is white and the rest of the image is black.

![1343 · U19 · L23 · 07:52](frames/U19L23-F0752.00.jpg)

On screen: "Feather: 57.4 px" [rest omitted]  
Shows: In Black & White view, the selected parasol appears white against black with a blurred, feathered edge.

![1343 · U19 · L23 · 09:16](frames/U19L23-F0916.00.jpg)

On screen: "Select" / "Inverse" [rest omitted]  
Shows: The Select menu is open with Inverse highlighted over the feathered parasol selection.

## Recolour the parasol with an adjustment layer

Anchor: 1343 · U19 · L23 · 09:29–12:41

For colour changes, Hue/Saturation is the best adjustment layer. I add it by clicking the black-and-white circle at the bottom of the Layers panel and choosing Hue/Saturation. In the drop-down menu, I choose Yellows. To tell Photoshop which precise yellow shade to change, I use the eyedropper and click the parasol.

The small grey range on the hue bar shifts to show the sampled colour. Its centre is the colour being changed, fading into neighbouring colours at either side, so those nearby colours also shift a little. The slider can seem counterintuitive: although red appears at one end of the bar, dragging the control all the way there can make the parasol cyan. The two colour bars are the guide: the top shows the existing colours and the bottom shows the replacement. To turn this yellow-orange into red, I move the slider until red reaches the middle of the grey range.

When the adjustment layer is added, the marching ants disappear because Photoshop has converted the selection into a layer mask. The mask works like the black-and-white view: white marks the selected area and black marks areas without the selection. This is something we will learn a lot about throughout the course. The Lasso tool is a quick, simple choice when the selection does not need to be accurate.

![1343 · U19 · L23 · 09:53](frames/U19L23-F0953.00.jpg)

On screen: "Hue/Saturation" / "Hue" / "Saturation" / "Lightness" [rest omitted]  
Shows: The parasol photograph with a Hue/Saturation adjustment layer and its mask in the Layers panel.

![1343 · U19 · L23 · 10:29](frames/U19L23-F1029.00.jpg)

On screen: "Yellows" / "55°|85°" [rest omitted]  
Shows: The Yellows range selected in Hue/Saturation, with the grey sampled-colour range on the colour bars.

![1343 · U19 · L23 · 11:47](frames/U19L23-F1147.00.jpg)

On screen: "Custom" / "Yellows" / "Hue: -23" [rest omitted]  
Shows: The upper-right parasol changed from yellow-orange to red while the other parasols remain yellow-orange.
