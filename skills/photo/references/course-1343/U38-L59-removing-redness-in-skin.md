# Lesson 59 · Removing Redness in Skin

Anchor: 1343 · U38 · L59 · 18:39 · https://www.domestika.org/en/courses/1973-course-4-retouching-portraits/units/6459-removing-redness-in-skin#course_lesson_19416

## Why Curves is not always the right tool

Anchor: 1343 · U38 · L59 · 00:00–01:50

Digital cameras often bring out too much redness in skin. In this lesson I show several ways to remove it with targeted adjustment layers and layer masks. I normally use Curves when changing colors in Photoshop because it is a powerful tool with many options. If I need to target one color in particular, though, Curves may not be the best choice.

In the first portrait, the man's skin is strongly red. I add a Curves adjustment, choose the Red channel and lower the red slightly. The redness improves, but the rest of the picture looks unnatural and cold, with a blue cast. I could use the layer mask to limit the change, but that would require a precise masking job. I will use a more targeted color adjustment instead.

His general rule is that when you want to change the color of a color, Hue/Saturation is a better method to consider.

![1343 · U38 · L59 · 01:04](frames/U38L59-F0104.00.jpg)

On screen: [none]  
Shows: Photoshop canvas with the full portrait of a red-faced man, before the color adjustment.

![1343 · U38 · L59 · 01:42](frames/U38L59-F0142.00.jpg)

On screen: "Curves" / "Red" / "Input: 137" / "Output: 110" [rest omitted]  
Shows: Close view of the portrait with a Curves adjustment on the Red channel; the surrounding skin looks cooler while the face remains red.

## Sample the red you want to change

Anchor: 1343 · U38 · L59 · 01:50–03:12

I delete the Curves adjustment and add a Hue/Saturation layer, which I name “Redness.” I select the Reds channel. When I want to target a color with Hue/Saturation, I do not rely only on its default color range; I tell Photoshop which color I mean with the three eyedroppers. The first samples the color to target, the plus eyedropper adds another color to the sample, and the minus eyedropper subtracts colors from it.

I look for the strongest problem area and sample the red above the eye. I avoid the bright pink in the eye because that is usually a color we want to keep. The color-range bar moves to center on the sampled color. Hue/Saturation does not show a direct preview of what has been sampled, so I temporarily move Hue to −180. This shifts the selected color to its opposite, cyan, and makes the affected areas visible.

![1343 · U38 · L59 · 02:12](frames/U38L59-F0212.00.jpg)

On screen: "Hue/Saturation" / "Preset: Default" / "Reds" / "Hue: 0" / "Redness" [rest omitted]  
Shows: Close portrait with the Hue/Saturation panel on the Reds channel and the adjustment layer named Redness.

## Refine the sampled range

Anchor: 1343 · U38 · L59 · 03:12–06:04

The cyan preview shows that nearly all of the skin is being affected. The central part of the range represents the sampled color, which is quite light here, and the selection also fades into neighboring colors: from red through orange to bright yellow on one side, and toward pink-magenta on the other. I need to narrow the range to colors I want to change.

I switch off the Hue adjustment temporarily, choose the minus eyedropper and click-drag across skin with a good tone. The range shrinks, so fewer colors are sampled. When I switch the adjustment back on, the cyan preview follows the problem colors more closely. I also check for other red areas that I want included. If there is redness there, I use the plus eyedropper to add it to the sample; the band grows and more of that area turns cyan.

The preview can still show pink or purple, and the lips and part of the eye turn bright cyan. Those areas will need masking later. I am looking for the strong red that I want to change, so that it turns bright cyan in this temporary preview. Once the selection looks useful, I return Hue to zero.

![1343 · U38 · L59 · 03:46](frames/U38L59-F0346.00.jpg)

On screen: "Hue: -180" [rest omitted]  
Shows: The man's face and upper body appear cyan in the temporary preview, revealing the colors selected by the adjustment.

![1343 · U38 · L59 · 05:42](frames/U38L59-F0542.00.jpg)

On screen: "Hue: -180" [rest omitted]  
Shows: A later cyan and purple preview of the same portrait, with a zoomed inset of the eye; the lips and eye are also affected.

## Shift the reds toward the surrounding skin tone

Anchor: 1343 · U38 · L59 · 06:04–08:20

The small slider above the color bars can be confusing: it does not show the color range selected, so it does not tell me which red I sampled. I look at the two bars at the bottom instead. The upper bar shows the existing color and the lower bar shows the color it will become. Moving Hue left from red shifts it toward pink, magenta and blue; moving it right shifts red toward orange and then yellow. Here I want the red to become a little more orange so it matches the rest of the skin.

I move the Hue slider a little to the positive side. The result is not quite right yet, but the skin is less red and pink and more orange-yellow. I initially go a little too far, so I bring the value back to about +7. I also reduce the sampled range manually because too much of the correct skin tone is included. After adjusting that range a little further, the result looks better. The correction still needs masking.

![1343 · U38 · L59 · 06:07](frames/U38L59-F0607.00.jpg)

On screen: "Hue: 0" [rest omitted]  
Shows: The man's face after the temporary cyan preview has been reset to the original colors, ready for the final hue adjustment.

![1343 · U38 · L59 · 07:48](frames/U38L59-F0748.00.jpg)

On screen: "Hue: +7" [rest omitted]  
Shows: The red skin is shifted toward orange, with the Hue/Saturation range adjusted around the selected reds.

## Mask the lips and eye

Anchor: 1343 · U38 · L59 · 08:20–10:32

For any adjustment, I decide whether I want it across most of the image or only in a few places. This correction works over most of the portrait, so I keep a white layer mask and paint black where I do not want the effect. If I wanted the adjustment only in small areas, I would begin with a black mask and paint with white (the captions read “pinged with Y”).

I zoom out with Command or Control + 0 and compare before and after. The correction looks good across most of the image, except for the lips and the inside of the eye. I select the layer mask thumbnail with a single click and make a habit of doing so. I zoom in, use the Space bar to reposition the canvas, press D to restore the default black and white colors, and press X to make black the foreground color. I press B for the brush. I keep opacity and flow at 100% because I want to hide the effect completely in these places; if I wanted to hide it gradually, I would lower opacity and flow. I reduce the brush size with the square bracket keys next to P and paint around the eye corners and lips.

I recommend inspecting the mask after painting. I hold Alt or Option and click the mask thumbnail to view it directly. In this view, small gaps are easy to spot even when they are hard to see while toggling the image before and after. I finish the mask in this view by painting over the gaps so the protected areas are solid. A small leak can matter if the file is going to print or to a client.

![1343 · U38 · L59 · 09:25](frames/U38L59-F0925.00.jpg)

On screen: "Layer Mask" / "Invert" [rest omitted]  
Shows: Close view of the man's face while the white adjustment mask is selected and the brush is set for precise work.

![1343 · U38 · L59 · 10:10](frames/U38L59-F1010.00.jpg)

On screen: "Layer Mask" / "Density: 100%" / "Feather: 0.0 px" / "Select and Mask..." / "Color Range..." / "Invert" / "Redness" / "Background" [rest omitted]  
Shows: The layer mask displayed by itself: black marks protect the eyes and lips, while the rest of the mask remains white.

## Review the first result and introduce a harder image

Anchor: 1343 · U38 · L59 · 10:32–11:36

I return from the mask view by Alt- or Option-clicking the thumbnail. I compare the before and after. If the effect feels too strong, I reduce the adjustment layer's opacity; if I need to refine the color, I return to the Reds channel and make another adjustment.

The next portrait has a similar redness problem, but red appears throughout the picture: the woman wears a red top and has red hair. That means I need to be more careful and use the mask differently.

![1343 · U38 · L59 · 10:52](frames/U38L59-F1052.00.jpg)

On screen: "Opacity: 100%" / "Fill: 100%" / "Redness" [rest omitted]  
Shows: Close view of the man's face at 300%, with the Redness layer mask selected and layer opacity still at 100%.

![1343 · U38 · L59 · 11:08](frames/U38L59-F1108.00.jpg)

On screen: "Opacity: 84%" / "Fill: 100%" / "Redness" [rest omitted]  
Shows: The man's full portrait zoomed out, with the redness correction applied at 84% layer opacity.

![1343 · U38 · L59 · 11:36](frames/U38L59-F1136.00.jpg)

On screen: "Background" [rest omitted]  
Shows: The second portrait, a woman with red hair and a red top, before the redness adjustment.

## Target skin when red is everywhere

Anchor: 1343 · U38 · L59 · 11:36–14:55

I add Hue/Saturation, name the layer “Redness in skin,” choose Reds and sample the strong red on the woman's cheek. I again move Hue to −180 so the targeted color becomes cyan. I recommend doing this even after the process becomes familiar: it is difficult to see exactly what is selected otherwise, and repeating the same check can make work quicker and more efficient. Taking Hue to −180 is optional; its benefit is that the targeted problem area always appears as the same cyan-blue color.

I turn the adjustment off and use the minus eyedropper to click a couple of areas with a good color. The central range gets a little smaller. When I zoom out, the whole top is being changed, which I do not want; the lips and inside of the eyes are also affected. The color targeting is useful, but I see artifacts that may come from sampling the color inaccurately. I add another sample with the plus eyedropper, and the result looks better. The cheek beneath the lips is now less affected.

I return Hue to zero and move it to about +8 or +9. I find that pushing a color more than 10 degrees can make the shift look artificial and would require a much better mask, so I try to keep the adjustment to around +10 at most. In the before-and-after view, the dress, lips and eyes are changing too, along with other areas that I do not want to change. I will apply the adjustment selectively with a mask. He describes the next step as creating a paintbrush that removes redness from skin; with a layer mask, you create your own tools.

![1343 · U38 · L59 · 12:22](frames/U38L59-F1222.00.jpg)

On screen: "Hue: -180" / "Redness in skin" [rest omitted]  
Shows: Close view of the woman's face in the cyan preview as the red skin tones are sampled.

![1343 · U38 · L59 · 13:23](frames/U38L59-F1323.00.jpg)

On screen: "Hue: -180" [rest omitted]  
Shows: Full portrait in the cyan preview; the skin, red top and parts of the hair are all affected by the current selection.

![1343 · U38 · L59 · 13:42](frames/U38L59-F1342.00.jpg)

On screen: "Hue: -180" [rest omitted]  
Shows: Close-up of the cyan and purple preview after another color has been added to the sample; the selection still includes the lips and other facial areas.

![1343 · U38 · L59 · 14:41](frames/U38L59-F1441.00.jpg)

On screen: "Hue: +9" [rest omitted]  
Shows: The hue adjustment shifts the woman's facial redness while the red hair and clothing remain prominent.

## Build a brush from the layer mask

Anchor: 1343 · U38 · L59 · 14:55–18:39

I want to think of the adjustment as a paintbrush that removes redness from skin. A layer mask lets me make a tool for a particular job. I select the mask and invert it from the Properties panel, or use Command or Control + I, to make it black. With a black mask, the change is hidden. I choose the normal brush and use white as the foreground color, pressing X to swap foreground and background colors. Wherever I paint, the hue adjustment is applied: the red shifts toward a more orange color.

The effect is strong, so I undo the first stroke with Command or Control + Z. I lower brush opacity to 50% by pressing 5 and flow to 50% with Shift + 5. This limits how much I can apply in one stroke and how quickly the paint is laid down, letting me choose the amount more freely in different areas. I enlarge the brush. Under the woman's chin there is strong redness reflected from her dress. I paint over it once to reduce it rather than pushing it further, and use the Space bar to reposition the image.

I compare before and after and inspect the mask again. There are large gaps where I chose not to paint; a gap does not always need to be covered.

![1343 · U38 · L59 · 17:14](frames/U38L59-F1714.00.jpg)

On screen: "Opacity: 50%" / "Flow: 50%" / "Layer Mask" / "Density: 100%" / "Feather: 0.0 px" / "Select and Mask..." / "Color Range..." / "Invert" [rest omitted]  
Shows: The second portrait's layer mask displayed by itself, with a large unpainted black area between the gray and white painted regions.

I also see that the woman's ear is still a little red, so I brush over it. The change looks slightly too strong, so I reduce the adjustment a little. The finished mask applies the correction only where I painted.

This approach is not limited to skin. I could use the same technique to shift the red of the woman's dress toward pink, or to change foliage in a landscape photograph. For every technique, consider how it could work beyond the example in front of you. Hue changes are useful for many kinds of objects and colors. In the next lesson, I will show how to brighten eyes in photographs.

![1343 · U38 · L59 · 15:25](frames/U38L59-F1525.00.jpg)

On screen: "Layer Mask" / "Redness in skin" / "Opacity: 100%" / "Fill: 100%" [rest omitted]  
Shows: The woman's portrait with the “Redness in skin” adjustment hidden by a black layer mask, before painting the effect back in.

![1343 · U38 · L59 · 16:25](frames/U38L59-F1625.00.jpg)

On screen: "Opacity: 50%" / "Flow: 50%" [rest omitted]  
Shows: Close-up of the woman as the white brush applies the adjustment, with brush opacity and flow at 50%.

![1343 · U38 · L59 · 16:59](frames/U38L59-F1659.00.jpg)

On screen: "Opacity: 50%" / "Flow: 50%" / "Layer Mask" [rest omitted]  
Shows: Close view of the corrected portrait and the mask with painted white areas controlling where the adjustment appears.

![1343 · U38 · L59 · 17:30](frames/U38L59-F1730.00.jpg)

On screen: "Opacity: 50%" / "Flow: 50%" [rest omitted]  
Shows: Full portrait of the woman after selective color correction, with the red top and hair still visible.
