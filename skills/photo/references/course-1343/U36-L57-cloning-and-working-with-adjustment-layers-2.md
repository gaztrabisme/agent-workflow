# Lesson 57 · Cloning and Working With Adjustment Layers 2

Anchor: 1343 · U36 · L57 · 15:43 · https://www.domestika.org/en/courses/1973-course-4-retouching-portraits/units/6059-cloning-and-working-with-adjustment-layers#course_lesson_19500

## What goes wrong when a cloned area is adjusted afterward

Anchor: 1343 · U36 · L57 · 00:00–02:30

Here is the image before and after a few edits; it looks fine. The problem appears if I later need to change the colour. I will return to the Brightness curve and make the image darker, as a client might request. You should edit the original adjustment whenever possible. When I darken it now, the cloning breaks. This can be confusing. If I were zoomed out and did not notice what happened on the neck, I could deliver the image or post it on a website with a surprising new skin condition.

The clone layer needs to be in the right place. I will reset the curve. The first click on this reset button returns it to the previous curve; clicking it again resets it completely. I could also use History to go back, but the reset button is quicker. Now I will put the clone layer just above the Background. That is the correct location for a pixel layer, but because I did the cloning in the wrong order, the healing marks are still visible on the neck. I need to remove this layer and explain the order more clearly.

![1343 · U36 · L57 · 00:50](frames/U36L57-F0050.00.jpg)

On screen: “Clone” / “Colours” / “Brightness” / “Levels 1” / “Background”  
Shows: A close view of the man's neck with pale circular patches from the cloning, and the layer stack.

![1343 · U36 · L57 · 01:42](frames/U36L57-F0142.00.jpg)

On screen: [none]  
Shows: The Curves controls, with the reset button enlarged in a loupe.

![1343 · U36 · L57 · 02:12](frames/U36L57-F0212.00.jpg)

On screen: “Current & Below” [rest omitted]  
Shows: The full portrait with the Clone pixel layer below the adjustment layers and above Background.

![1343 · U36 · L57 · 02:17](frames/U36L57-F0217.00.jpg)

On screen: [rest omitted]  
Shows: A close view of the man's neck with a small circular Healing Brush mark visible and the Clone layer below the adjustments.

## Put the blank clone layer below the adjustments

Anchor: 1343 · U36 · L57 · 02:30–05:21

I said to make the adjustments first and then clone, but the layer order also matters. You can place a layer in the stack at any point in an edit, but you may not be able to move it later. When you add a blank cloning layer, put it above the Background and below the adjustment layers before you begin.

I will add a blank layer, name it Clone, select the Healing Brush, sample with Alt or Option, and make a couple of the same edits. Now I can change Brightness as much as I like without causing a problem. The same is true for Colours; I can remove some blue and the retouched area continues to match.

Pixel layers for cloning should sit above the Background and beneath the adjustment layers. Otherwise, if the clone layer is on top and I later want to darken the image, I would need to add another Curves layer above it. The new curve would counteract the earlier curve: one brightens while the other darkens. Even if their visual effects partly cancel, repeated adjustments break up the image further and reduce its quality. The histogram starts to show spikes and gaps, which means parts of the tonal range are being lost.

The file size also shows the benefit of adding only the pixels needed: it increases from 60 to 65 MB here. A duplicate of the Background would increase it from 60 to 120 MB.

![1343 · U36 · L57 · 03:39](frames/U36L57-F0339.00.jpg)

On screen: “Blue” / “Input: 124” / “Output: 129” [rest omitted]  
Shows: A close view of the man's neck and shirt beside the blue-channel Curves controls.

![1343 · U36 · L57 · 04:46](frames/U36L57-F0446.00.jpg)

On screen: “Curves 1” [rest omitted]  
Shows: The full portrait, the Curves adjustment and the layer stack after another curve is added.

![1343 · U36 · L57 · 05:02](frames/U36L57-F0502.00.jpg)

On screen: “Doc: 60.2M/65.2M” [rest omitted]  
Shows: The document-size readout beside the full portrait and its layer stack.

## Adjusting a scanned photograph before dust removal

Anchor: 1343 · U36 · L57 · 05:21–07:42

Sometimes a duplicate Background is useful. As we saw in the previous lesson, the Patch tool requires one. I will demonstrate another case with a scanned photograph. When I zoom in, there is a lot of dust in the scan.

I will make the main adjustments first, beginning with Levels. The histogram is far off. Hold Alt or Option as you move the black point to see where black begins to appear. Do not judge only by how the image looks: pulling the control far in may make the backdrop a nice black, but it will also lose detail elsewhere. Move it only to the point where black is just introduced.

For the white point, I do not necessarily want pure white. Find the white and then back off a little. A small spot of dust becomes visible there. At a setting around 222 to 224, more specks begin to appear, so I back off slightly. That is a good adjustment. The colours look a little cool, so I add a Curves adjustment called Colour and remove a little blue and a tiny bit of green to warm the image.

![1343 · U36 · L57 · 05:41](frames/U36L57-F0541.00.jpg)

On screen: “⌘=” [rest omitted]  
Shows: The full scanned portrait of a clown-costumed performer in a ruffled collar and diamond-patterned outfit.

![1343 · U36 · L57 · 05:44](frames/U36L57-F0544.00.jpg)

On screen: [rest omitted]  
Shows: A 300% close-up of the dark backdrop beside the yellow ruffled collar, with dust specks visible.

![1343 · U36 · L57 · 06:12](frames/U36L57-F0612.00.jpg)

On screen: “26” / “1.00” / “255” [rest omitted]  
Shows: The Levels controls over the scanned portrait, with the black-point setting at 26.

![1343 · U36 · L57 · 06:51](frames/U36L57-F0651.00.jpg)

On screen: “222” [rest omitted]  
Shows: The Levels controls over the scanned portrait as the white point is backed off.

![1343 · U36 · L57 · 07:42](frames/U36L57-F0742.00.jpg)

On screen: “Colour” [rest omitted]  
Shows: The scanned portrait with its Colour and Levels adjustment layers above the Background copies.

## Use Dust & Scratches, then restore only the parts that need it

Anchor: 1343 · U36 · L57 · 07:42–10:35

I will now show a case for working on a duplicate Background, and introduce the History Brush in a new way. I will duplicate the Background and name the layer Dust removal. Removing all these tiny specks can take a long time. The next technique is quick and gives reasonably good quality; even if you do not work with scanned negatives, it can also be used to remove things such as beard stubble.

Go to Filter, Noise, Dust & Scratches. The filter has Radius and Threshold controls. As Radius increases, more dust is removed, but so is more texture. Threshold controls where the filter applies. At zero, a brightness difference of zero is enough for the filter to apply everywhere. A higher Threshold brings back more of the original image. If it is too high, the dust returns. Find a Radius that removes the main specks, then raise Threshold to restore as much original texture as possible without bringing those specks back.

In this image, one speck is removed with the current settings, while a second is still just visible. I will use a slightly higher Radius and a slightly lower Threshold. The result looks good. The filter damages much of the picture, but what matters here is how it looks where the dust is. I will click OK.

![1343 · U36 · L57 · 08:43](frames/U36L57-F0843.00.jpg)

On screen: “Dust & Scratches” / “Radius: 1 Pixels” / “Threshold: 0 levels” / “Dust removal” [rest omitted]  
Shows: The Dust & Scratches dialog over a close view of the performer and costume; the duplicate layer is named Dust removal.

![1343 · U36 · L57 · 09:22](frames/U36L57-F0922.00.jpg)

On screen: “Radius: 4 Pixels” [rest omitted]  
Shows: The filter dialog over the diamond-patterned costume, where the enlarged radius also softens the fabric texture.

## Paint the filtered state back with the History Brush

Anchor: 1343 · U36 · L57 · 10:35–13:41

Open the History panel from Window if it is not visible. You can undo by clicking a step above, but the box to the left of a step sets the History Brush source. I will choose the Dust & Scratches step as the source, then click the step above it to undo the filter. The dust returns, while the source remains set to Dust & Scratches.

Select the History Brush, not the Art History Brush. Its options bar lets you change a tool's blend mode; tools are set to Normal by default. I will change this one to Darken. That tells Photoshop to apply the brush only where it darkens something. Even if the surrounding pixels are imperfect, the filtered state is applied only where it darkens the dust speck. This works well, and I can move across the image quickly with a fairly large brush. Be careful at edges so that you do not remove detail.

Here is a darker speck. Darken will not remove it, apart from a little of its surrounding halo. Because Photoshop needs to lighten these pixels to remove this spot, I will set the mode to Lighten. Normal would work on both light and dark spots, but choosing a mode is more efficient because it limits the tool to the pixels that need that change. I would work through the light bits first, then switch modes for the dark bits.

![1343 · U36 · L57 · 11:10](frames/U36L57-F1110.00.jpg)

On screen: [rest omitted]  
Shows: The History panel open with the Dust & Scratches state listed as a History Brush source.

![1343 · U36 · L57 · 12:25](frames/U36L57-F1225.00.jpg)

On screen: “Mode: Darken” [rest omitted]  
Shows: The History Brush set to Darken over a close view of the yellow ruffled collar.

![1343 · U36 · L57 · 13:24](frames/U36L57-F1324.00.jpg)

On screen: “Mode: Lighten” [rest omitted]  
Shows: The History Brush set to Lighten over a close view of the diamond-patterned fabric.

## Reserve cloning tools for larger defects

Anchor: 1343 · U36 · L57 · 13:41–15:43

For large pieces of dust, this technique is not suitable. I will leave a larger lump and use the Clone Stamp or Healing Brush to remove it. Press J for the Healing Brush. I previously customized the toolbar so that J now selects the Healing Brush rather than the Spot Healing Brush. The brush can sample from one image to another; in this demonstration, the sampled skin is from the neck of the man in the previous image. I will Alt- or Option-click to sample it and apply it over the dust.

That is how to combine cloning and adjustment layers. Layer order is essential: pixel layers should sit at the bottom of the stack, above the Background but below the adjustment layers, or the edits will not work properly together. Keep the layer stack organized and neat. In the next lesson, I will teach you how to correct and enhance skin tone.

![1343 · U36 · L57 · 14:21](frames/U36L57-F1421.00.jpg)

On screen: [rest omitted]  
Shows: A large dark speck on the scanned image's black backdrop, with the History Brush set to Lighten.

![1343 · U36 · L57 · 14:47](frames/U36L57-F1447.00.jpg)

On screen: “Source: Sampled” [rest omitted]  
Shows: A close view of the dark backdrop with the Healing Brush cursor over the remaining speck.

![1343 · U36 · L57 · 15:27](frames/U36L57-F1527.00.jpg)

On screen: [rest omitted]  
Shows: The full scanned portrait beside its finished four-layer stack, with two adjustment layers above two pixel layers.
