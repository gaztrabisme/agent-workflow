# Lesson 44 · Enhance Important Features 2

Anchor: 1343 · U28 · L44 · 20:53 · https://www.domestika.org/en/courses/1972-course-3-retouching-environmental-images/units/6444-enhance-important-features#course_lesson_19495

## Bring the man forward in Camera Raw

Anchor: 1343 · U28 · L44 · 00:00–02:38

Before moving the image into Photoshop, I want to draw attention to the man in the middle, so I brighten him slightly. I click New because I want different settings from the earlier adjustments: I do not want to apply Dehaze or Clarity to his face, only lift the Shadows. I make a mistake by not clicking the plus to reset the settings, so Clarity and Dehaze remain. Clicking the plus clears them. I lift the Shadows, compensate for the Blacks that are lost, and add a little Clarity, or midtone contrast. The brightest part is his belly, so I place the adjustment just above it; this adds a little light and helps show what interests me.

I do not feel completely finished, but the quality from the raw converter is good and the tones are fairly even. I press P to see the original.


I press P again to return to the edit. The transformation is dramatic, even though each change was small; small increments are how I keep the result natural. If the current image looks natural, remember how dark and uneven the original was.

![1343 · U28 · L44 · 00:40](frames/U28L44-F0040.00.jpg)

On screen: "TOBACCO" / "Cigarettes &" / "Tobacco on Sale" / "here...." [rest omitted]  
Shows: The edited kiosk photograph in Camera Raw before the final local lift on the man.

![1343 · U28 · L44 · 01:40](frames/U28L44-F0140.00.jpg)

On screen: [rest omitted]  
Shows: A radial adjustment around the man in the center of the kiosk.

![1343 · U28 · L44 · 02:10](frames/U28L44-F0210.00.jpg)

On screen: [rest omitted]  
Shows: The current Camera Raw image after the small local adjustments to the man.

![1343 · U28 · L44 · 02:16](frames/U28L44-F0216.00.jpg)

On screen: "White Balance" "As Shot" / "Temperature" 4850 / "Tint" -3 / "Exposure" 0.00 [rest omitted]  
Shows: The original kiosk photograph in Camera Raw after pressing P, with White Balance set to As Shot and the Basic adjustments reset to zero.

## Open the image as a Smart Object

Anchor: 1343 · U28 · L44 · 02:38–04:17

I can open an image into Photoshop as a Smart Object, which lets me return to the raw converter for more editing. To make that the default, I would open Workflow Options and check Open in Photoshop as Smart Objects. I will leave it off as my default. Instead, I hold Shift so Open Image changes to Open Object, then click Open Object.


Holding Alt or Option changes Cancel to Reset.


I can also use the menu's Camera Raw Defaults command to return the image to its original state.


When the image opens, a small symbol on the Background layer identifies it as a Smart Object. The layer is named after the image file instead of simply Background, which is the usual default.

![1343 · U28 · L44 · 03:09](frames/U28L44-F0309.00.jpg)

On screen: "Workflow Options" / "Open in Photoshop as Smart Objects" [rest omitted]  
Shows: The Workflow Options dialog over the kiosk image; the Smart Objects checkbox is off.

![1343 · U28 · L44 · 03:18](frames/U28L44-F0318.00.jpg)

On screen: "Open Object" [rest omitted]  
Shows: The Camera Raw Open Object button while Shift is held.

![1343 · U28 · L44 · 03:29](frames/U28L44-F0329.00.jpg)

On screen: "Reset" [rest omitted]  
Shows: The bottom-right button changed to Reset while Alt or Option is held.

![1343 · U28 · L44 · 03:39](frames/U28L44-F0339.00.jpg)

On screen: "Camera Raw Defaults" [rest omitted]  
Shows: The Camera Raw menu open with Camera Raw Defaults listed.

![1343 · U28 · L44 · 04:02](frames/U28L44-F0402.00.jpg)

On screen: "Embedded Smart Object" / "Andrew Weatherburn" / "Edit Contents" / "Convert to Linked..." / "Convert to Layers" [rest omitted]  
Shows: The opened Smart Object layer and its identifying icon in Photoshop.

## Build a masked darkening curve

Anchor: 1343 · U28 · L44 · 04:17–06:58

I want to dodge and burn by brightening and darkening parts of the image. The bottom and a few things at the top are still too bright, so I create a Curves adjustment layer and name it Darken. I darken the curve more than I think I will need because I will reveal the effect through its layer mask with a low-opacity brush.

Darkening also makes colors more saturated, which can be a nice side effect.

![1343 · U28 · L44 · 05:04](frames/U28L44-F0504.00.jpg)

On screen: "Normal" / "Darken" [rest omitted]  
Shows: The Darken adjustment visible over the kiosk photograph during the before-and-after check.

![1343 · U28 · L44 · 05:06](frames/U28L44-F0506.00.jpg)

On screen: [rest omitted]  
Shows: The Darken adjustment hidden during the same check, showing the brighter image without the Photoshop curve.

If I do not want that, I change the blend mode from Normal to Luminosity. Luminosity keeps the colors closer to their previous saturation. I invert the layer mask by selecting it and clicking Invert in Properties, or by pressing Command or Control and I. The black mask thumbnail means the layer is hidden; toggling its preview on and off shows no change yet.

I select the Brush with B and reset its colors with D. D gives me pure white and pure black, the colors I generally want to paint with a layer mask. I set brush Opacity to about 50%, so one stroke can apply at most half the layer's effect, then lower Flow to 10% for gradual application. I often start with large, broad strokes, similar to a gradient or an oval from the raw converter. The brush is 800 pixels, very large for this task, but it is a useful starting size.

![1343 · U28 · L44 · 05:26](frames/U28L44-F0526.00.jpg)

On screen: "Normal" / "Luminosity" [rest omitted]  
Shows: The Darken Curves layer and the blend-mode menu with Luminosity available.

![1343 · U28 · L44 · 05:53](frames/U28L44-F0553.00.jpg)

On screen: "Invert" / "Invert layer mask" [rest omitted]  
Shows: The mask Properties panel and its Invert control.

![1343 · U28 · L44 · 06:26](frames/U28L44-F0626.00.jpg)

On screen: "Luminosity" / "Layer Mask" [rest omitted]  
Shows: The black layer mask thumbnail that hides the Darken adjustment.

## Paint back detail and assess local contrast

Anchor: 1343 · U28 · L44 · 06:58–10:26

The fridges stand out because they are too bright. The small box and the paper are also bright, so I paint broad strokes over the fridges, then the orange area, and check the result. The strokes bring more definition to the fridge. The corner areas are still bright, and the step into the newsstand is too bright, so I darken that as well. I make the brush smaller with the left bracket key next to P and larger with the right bracket. I brush over the paper and box. A light at the top makes those areas stand out more than I want, so I darken them too. I compare before and after.


I add a couple of strokes over the orange.

The image's overall contrast is strong, but the man's tone looks thin and washed out (captions: “wish washing”). I add another Curves layer for contrast. Another area also looks thin, and I want more definition in the box, so I darken the area around the tobacco sign to help it stand out. The sign now stands out enough (captions: “Pipette enough”). I add a further curve and name it Local contrast, then zoom in with Command or Control and Plus to work on a specific tone.

![1343 · U28 · L44 · 08:12](frames/U28L44-F0812.00.jpg)

On screen: "Opacity" 50% / "Flow" 10% [rest omitted]  
Shows: Broad brushwork beginning on the Darken layer mask over the kiosk photograph.

![1343 · U28 · L44 · 09:08](frames/U28L44-F0908.00.jpg)

On screen: [rest omitted]  
Shows: The full kiosk image after the broad Darken-mask brushwork, with the mask and Darken layer visible.

![1343 · U28 · L44 · 09:26](frames/U28L44-F0926.00.jpg)

On screen: [rest omitted]  
Shows: The kiosk image after strokes have darkened the fridges, paper, box, orange area and bright corners.

![1343 · U28 · L44 · 10:26](frames/U28L44-F1026.00.jpg)

On screen: "Local contrast" [rest omitted]  
Shows: A zoomed view of the man, box, paper and fridge as the local-contrast curve is prepared.

## Shape the local-contrast curve

Anchor: 1343 · U28 · L44 · 10:26–12:50

The target adjustment tool lets me tell Photoshop which tone to work with. I check that Sample Size is not Point Sample. A three-by-three average is useful for this small area: Point Sample takes one pixel and can give confusing results. I find a shadow I want to darken, not necessarily the darkest shadow. There is a small shadow on the man's face, so I click it to place a point on the curve, keep the mouse button down and drag the point lower. I then find a highlight I want to brighten and drag it upward.

This curve gives more midtone contrast than a normal S-shaped contrast curve, which would typically have one point up here and another down there. When I toggle the preview, the curve has also added saturation. I change the blend mode from Normal to Luminosity (captions: *spline mode*) so the result looks more natural and keeps saturation closer to its previous value. I zoom back out with Command or Control and Zero and compare the result. It works well on the man, the box and another area, but makes contrast too strong in the rest of the image.

![1343 · U28 · L44 · 11:01](frames/U28L44-F1101.00.jpg)

On screen: "Sample Size" / "3 by 3 Average" / "Point Sample" [rest omitted]  
Shows: The zoomed face and the sample-size menu, with 3 by 3 Average selected.

![1343 · U28 · L44 · 12:05](frames/U28L44-F1205.00.jpg)

On screen: "Local contrast" [rest omitted]  
Shows: The local-contrast curve with lowered shadow and raised highlight points.

![1343 · U28 · L44 · 12:50](frames/U28L44-F1250.00.jpg)

On screen: [rest omitted]  
Shows: The full kiosk image during the local-contrast before-and-after review, with the Local contrast curve selected.

## Paint the contrast only where it helps

Anchor: 1343 · U28 · L44 · 12:50–16:35

I select the mask and invert it so the whole mask is black. Even if the brush is already selected, I press B before brushwork; I press D for default colors and click the mask thumbnail even if it is already selected. Making these steps automatic helps prevent mistakes. If the curve itself is selected, the brush shows a no-entry symbol and I cannot paint. Clicking the layer-mask thumbnail restores the brush so I can continue.

I zoom out a little more with Command or Control and Minus and use fairly large strokes, making the brush slightly smaller. I add strokes in a few areas. If it feels as though nothing is happening, that may mean the edit is subtle, or it may mean nothing is changing. If you can see your brush stroke (captions: *brush droll*), someone else may notice that you edited the picture; but it is also easy to paint without applying anything. A common mistake is using the wrong brush color: painting black on a black mask does nothing. If I thought that made the picture better, it is a sign to take a break.

I finish with a few strokes on the box, the tobacco sign, and the tops of the fridges. I check the image. The man now looks slightly darker than his surroundings; although I have darkened him, this helps the photograph feel believable.

![1343 · U28 · L44 · 14:49](frames/U28L44-F1449.00.jpg)

On screen: "Local contrast" / "Darken" [rest omitted]  
Shows: The two painted layer masks and the broad local adjustments across the kiosk image.

![1343 · U28 · L44 · 16:15](frames/U28L44-F1615.00.jpg)

On screen: [rest omitted]  
Shows: The final local-contrast mask over the man, tobacco sign, box and fridges.

## Add a subtle vignette

Anchor: 1343 · U28 · L44 · 16:35–18:46

As a final step, a vignette could help this image. I do not use one often and am not a great fan of them, but here it can draw attention toward the center. I usually use the regular Lasso tool rather than the Elliptical Marquee tool. I draw around the center, which selects the opposite of what I want, then open Select and Mask, choose the Overlay view and invert the selection so the edges are selected. I raise Feather until the selection edge is no longer visible, then click OK.

I add a Curves layer and call it Vignette, or Darkened Edges; the name only needs to make sense to me. I darken the edges very slightly and compare the result.


Holding Alt or Option and clicking the Background layer lets me compare the Camera Raw image with the Photoshop adjustment layers hidden and the final result with them restored. To change the raw-converter settings, I can double-click the Smart Object's layer icon.

![1343 · U28 · L44 · 17:23](frames/U28L44-F1723.00.jpg)

On screen: "View Mode" / "Overlay" / "Invert" [rest omitted]  
Shows: Select and Mask displaying the inverted selection as a white center against black.

![1343 · U28 · L44 · 18:09](frames/U28L44-F1809.00.jpg)

On screen: "Vignette" / "Local contrast" / "Darken" [rest omitted]  
Shows: The subtle darkened-edge curve above the other adjustment layers.

![1343 · U28 · L44 · 18:40](frames/U28L44-F1840.00.jpg)

On screen: "Input: 137" / "Output: 125" [rest omitted]  
Shows: The Camera Raw image with the Vignette, Local contrast and Darken layers hidden during the comparison.

![1343 · U28 · L44 · 18:42](frames/U28L44-F1842.00.jpg)

On screen: [rest omitted]  
Shows: The final Photoshop result with the Vignette, Local contrast and Darken layers visible again after the comparison.

## Revisit Camera Raw and finish the composition

Anchor: 1343 · U28 · L44 · 18:46–20:53

I reopen the Smart Object's raw settings. For example, I could change the overall Exposure here. I add a little Clarity, reduce Color Temperature slightly, and click OK. Photoshop updates the background. Because the local contrast and other adjustment layers were made on the earlier version, changing the raw conversion may mean I need to update those layers too.

The broader point is that Photoshop continues the composition. It brings out what attracted the photographer in the first place. The image now looks very different from the original, but this is what the photographer saw and wanted to capture. Editing in Photoshop helps visualize that original intention. I hope this gives you a good understanding of how to bring out the most important features of an image. In the next lesson, we will look at cloning while keeping it within perspective.

![1343 · U28 · L44 · 19:23](frames/U28L44-F1923.00.jpg)

On screen: "Temperature" 5300 / "Clarity" +20 [rest omitted]  
Shows: The Smart Object reopened in Camera Raw with a small temperature reduction and increased Clarity.

![1343 · U28 · L44 · 20:32](frames/U28L44-F2032.00.jpg)

On screen: [rest omitted]  
Shows: The final kiosk composition in Photoshop with the Darken, Local contrast and Vignette layers.
