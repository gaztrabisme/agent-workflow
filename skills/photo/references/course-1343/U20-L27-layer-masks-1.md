# Lesson 27 · Layer Masks 1

Anchor: 1343 · U20 · L27 · 14:58 · https://www.domestika.org/en/courses/1971-course-2-retouching-fundamentals/units/6430-layer-masks#course_lesson_19387

## What a mask protects

Anchor: 1343 · U20 · L27 · 00:00–02:27

A layer mask is one of the features that sets Photoshop apart from many other programs, and one of its most important features. A mask hides or reveals pixels, or hides or reveals the effect of an adjustment. In this studio portrait, the model has been cut out without deleting any pixels or erasing the background: the cutout is made with a layer mask. If I later notice that I missed part of the subject, I can reveal it again. Copying and pasting a selection can look the same at first, but it does not let me restore something I removed when I reach a later stage of the edit.

The Layers panel has two layers: Backdrop and Layer 0. When a Background layer is converted to a normal layer, Photoshop names it Layer 0 by default. I often leave that name as a reminder that it was the original background, though it can be renamed. Layer 0 contains the model. Its mask was made from a selection of the model, and I will also show how to add masks and make them from scratch.

![1343 · U20 · L27 · 01:50](frames/U20L27-F0150.00.jpg)

On screen: "Layer 0" / "Backdrop" [rest omitted]  
Shows: Studio portrait of the model isolated against the blue backdrop, with the model layer and its white silhouette mask above the Backdrop layer.

![1343 · U20 · L27 · 02:04](frames/U20L27-F0204.00.jpg)

On screen: [rest omitted]  
Shows: The model and an enlarged view of the two layer thumbnails, including the linked image and mask.

## Viewing and toggling the mask

Anchor: 1343 · U20 · L27 · 02:27–04:57

It is useful to inspect a mask itself. Adobe has not made this especially easy to discover: hold Alt or Option and click the layer-mask thumbnail to see the mask by itself. In this example it is a black field with a white silhouette of the model. Alt- or Option-click again to return to the image.

Right-clicking the mask thumbnail opens options including disabling, deleting, and applying the mask. Disabling it puts a red cross on its thumbnail and shows the layer without the mask. The original studio photograph has some wall beyond the backdrop and a strip of floor. The shoot used a white backdrop, which I found a little boring, so I cut the model out and placed him on the blue backdrop. To turn the mask back on, right-click and choose Enable Layer Mask. I usually use the shortcut instead: hold Shift and click the mask to switch it on or off.

![1343 · U20 · L27 · 03:08](frames/U20L27-F0308.00.jpg)

On screen: "Layer Mask" / "Density: 100%" / "Feather: 0.0 px" / "Select and Mask..." / "Color Range..." / "Invert" [rest omitted]  
Shows: The mask displayed by itself as a white silhouette on black.

![1343 · U20 · L27 · 03:40](frames/U20L27-F0340.00.jpg)

On screen: [rest omitted]  
Shows: The unmasked studio portrait on its original white backdrop; a red cross covers the mask thumbnail.

![1343 · U20 · L27 · 04:53](frames/U20L27-F0453.00.jpg)

On screen: [rest omitted]  
Shows: The model cut out against the blue backdrop again, with the mask enabled.

## Reusing a mask and moving its layer

Anchor: 1343 · U20 · L27 · 04:57–06:38

Command-click on Mac, or Control-click on Windows, on the mask thumbnail to load the mask as a selection. The dashed “marching ants” show that the selection is active. This is useful when I need another selection of the model: I can reuse the mask rather than starting again. Command-D deselects.

The link symbol between the layer and mask controls whether their contents move together. Keep them linked when cutting out a subject. For some design work I may unlink them, although that use is outside this lesson. Press V for the Move tool. With the link on, moving the layer moves the model and its mask together. With the link off, the mask stays put while the model moves inside it. That could make an interesting effect, but it is not usually what I want. I undo with Command-Z or Control-Z and switch the link back on. A mask makes a cutout useful because I can return and edit it later.

![1343 · U20 · L27 · 05:21](frames/U20L27-F0521.00.jpg)

On screen: "Indicates layer mask is linked to layer" [rest omitted]  
Shows: The portrait with the link symbol between the image and mask thumbnails, enlarged in the Layers panel.

![1343 · U20 · L27 · 06:24](frames/U20L27-F0624.00.jpg)

On screen: [rest omitted]  
Shows: The model has moved independently of the stationary mask, leaving a white silhouette offset behind him.

## Creating a mask from a selection

Anchor: 1343 · U20 · L27 · 06:38–08:37

I can load the model selection again by Command- or Control-clicking the mask, then right-click and delete the mask. This returns the image to its original state. Once the selection is ready, the mask symbol at the bottom of the Layers panel can apply it as a mask.

The Layer menu also has a Layer Mask submenu. Reveal All creates a white mask, even when a selection exists; Hide All creates a black mask that hides all the layer’s content, whether or not a selection exists. Reveal Selection makes the selected area white and everything outside it black. Hide Selection reverses that: the selected area is black and everything outside it is white. White reveals and black hides. For this model I choose Reveal Selection, which brings back the cutout mask.

![1343 · U20 · L27 · 07:46](frames/U20L27-F0746.00.jpg)

On screen: "Reveal All" / "Hide All" / "Reveal Selection" / "Hide Selection" / "From Transparency" [rest omitted]  
Shows: The Layer > Layer Mask submenu over the portrait, with a selection around the model and the mask options visible.

## Targeting a color with an adjustment layer

Anchor: 1343 · U20 · L27 · 08:37–10:20

A second use for masks is controlling a color adjustment. In the photograph of three green apples, I could make one apple red, or make a brush that lets me paint one or all three red, or another color. When changing an existing color with adjustment layers, I choose a Hue/Saturation adjustment layer rather than the Color Replacement brush.

In the Properties panel, Master means all colors. Photoshop uses RGB when all colors are selected in other contexts, but Hue/Saturation calls it Master because I can target colors such as yellows, cyans, and magentas. Greens in photographs are often foliage that is actually yellow. I will choose Greens for this demonstration, although I suspect Photoshop sees the apples as more yellow than green. The lower color bar shows the range Photoshop has targeted. I use the eyedropper to sample an apple so Photoshop targets that particular color.

![1343 · U20 · L27 · 09:20](frames/U20L27-F0920.00.jpg)

On screen: "Hue/Saturation" / "Preset: Default" / "Master" / "Hue: 0" / "Saturation: 0" / "Lightness: 0" [rest omitted]  
Shows: Three green apples with a Hue/Saturation adjustment layer and its Properties panel.

![1343 · U20 · L27 · 10:17](frames/U20L27-F1017.00.jpg)

On screen: "Greens" / "Hue" / "Saturation" / "Lightness" [rest omitted]  
Shows: The three apples and the selected green range in the Hue/Saturation Properties panel.

## Refining the target and changing the apples

Anchor: 1343 · U20 · L27 · 10:20–12:28

After sampling, the selected channel changes to Yellows 2. This is Photoshop’s compromise: I think the color is green and Photoshop thinks it is yellow, so it names the sampled range Yellows 2 while still letting me return to the default Yellows. To shift the apples’ color, I move the Hue slider to the left, which takes green toward yellow, then orange, and finally red. I am using the lower color bar to see the targeted range, rather than treating the large slider at the top as the range itself.

Part of the apple at the bottom has not changed because it falls outside the selected color range. I select the eyedropper with the plus sign and click that area to add it. The selected band in the range display grows. I can also adjust the range sliders manually. The outer slider controls the fade, or falloff, into neighboring colors.

![1343 · U20 · L27 · 11:37](frames/U20L27-F1137.00.jpg)

On screen: "Yellows 2" / "Hue: -63" / "Saturation: 0" / "Lightness: 0" [rest omitted]  
Shows: All three apples have shifted from green to red, with the sampled Yellows 2 range and Hue adjustment visible.

![1343 · U20 · L27 · 12:18](frames/U20L27-F1218.00.jpg)

On screen: [rest omitted]  
Shows: The red apples and the adjusted color-range band, with its boundary handles visible.

## Painting the adjustment onto one apple

Anchor: 1343 · U20 · L27 · 12:28–14:10

Adjustment layers start with a white mask, so their effect is revealed everywhere. Clicking the mask thumbnail opens its Properties; Invert turns the white mask black, hiding the adjustment everywhere. I then use the Brush tool by pressing B. For this example I choose a semi-hard brush at about 50% hardness, 175 pixels, and 100% opacity and flow. I will show reduced opacity and flow later.

Painting on the black mask reveals the red adjustment where I paint. A scribble across an apple is a useful way to think of the mask: I have made a brush that changes this particular green into this particular red. There is no standalone tool for that exact color change. I made it by adding an adjustment layer, putting a black mask on it, and painting white into the mask.

![1343 · U20 · L27 · 13:11](frames/U20L27-F1311.00.jpg)

On screen: "Hue/Saturation 1" / "Background" [rest omitted]  
Shows: The apples are still green while a black mask hides the Hue/Saturation adjustment.

![1343 · U20 · L27 · 13:22](frames/U20L27-F1322.00.jpg)

On screen: "Size: 175 px" / "Hardness: 49%" / "Opacity: 100%" / "Flow: 100%" [rest omitted]  
Shows: The brush picker is open over the still-green apples, showing the brush settings.

![1343 · U20 · L27 · 14:01](frames/U20L27-F1401.00.jpg)

On screen: [rest omitted]  
Shows: A red brush stroke is being painted across the middle apple on the black mask.

## Revealing the whole apple

Anchor: 1343 · U20 · L27 · 14:10–14:58

To color the whole apple, I enlarge the brush with the square-bracket keys next to P. I do not need to be very precise on the broad surface. I paint over the apple; if there were green in the background or on the floor, I would need a more precise brush. The result is one red apple between two green ones.

![1343 · U20 · L27 · 14:54](frames/U20L27-F1454.00.jpg)

On screen: [rest omitted]  
Shows: The middle apple is fully red while the apples on either side remain green.

### Key points (derived)

- A layer mask stores what is visible without deleting the hidden pixels.
- White reveals and black hides; the same rule controls whether an adjustment affects an area.
- Reuse, inspect, invert, or edit the mask to refine a result instead of rebuilding it.
- A mask can turn an adjustment into a brush for a specific color change.
