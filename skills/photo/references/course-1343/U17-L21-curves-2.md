# Lesson 21 · Curves 2

Anchor: 1343 · U17 · L21 · 18:48 · https://www.domestika.org/en/courses/1971-course-2-retouching-fundamentals/units/6423-curves#course_lesson_19484

## Starting with brightness

Anchor: 1343 · U17 · L21 · 00:00–01:00

Again, I’ll start by adding a curve and adjusting brightness. This image is quite bright, and I cannot immediately tell whether it should be brighter or darker. I often add a point and pull it up or down; if I think the image improves, I leave it where it looks better. Sometimes I am not sure whether it should be brighter or darker. In that case, I can leave the point in the middle and return to brightness after working on colour or contrast.

![1343 · U17 · L21 · 00:40](frames/U17L21-F0040.00.jpg)

On screen: "Brightness" / "Input: 120" / "Output: 132" [rest omitted]  
Shows: A harbour village photograph with a slight upward brightness curve.

## Working carefully in individual colour channels

Anchor: 1343 · U17 · L21 · 01:01–03:45

I add another curve for colour. I want to warm the image, so I go to the Blue channel, put a point in the middle, and adjust it. The values here are Input 128 and Output 129, which shows that I have moved the point. This has always bothered me a little about Curves: when you try to click on a point, you often move it slightly. I think Adobe should make a new point land directly on the line by default, or let you select a point without moving it.

You can move points with the keyboard arrows. Pressing Up or Down changes the value, so it is easy to return the point to its original value. The arrows are also useful for precise adjustments. To remove 20 units of blue, you could press the Down arrow 20 times. There is also a modifier that moves points in units of 10 instead of single units: hold Shift and press Down twice.

Here is an important point: when I pressed Down twice, I removed more than 20 units. The Curves window was not as large as it could be. I’ll widen it to show you: the curve grows as I pull the window wider, and I should stop when it no longer grows. Then the adjustment is more fine-tuned. Now, when I hold Shift and press Down, the units work as expected. Put the cursor on the little sidebar and pull it out until the curve stops getting bigger.

![1343 · U17 · L21 · 01:40](frames/U17L21-F0140.00.jpg)

On screen: "Blue" / "Input: 128" / "Output: 129" [rest omitted]  
Shows: The harbour photograph with the Blue-channel point selected and its input and output values enlarged.

## Removing colour and compensating for lost light

Anchor: 1343 · U17 · L21 · 03:46–06:03

My recipe is to remove blue, then remove half as much green. I add a point in the middle of the Green channel. When the input and output are the same, the point is directly on the line, which is what I want. I hold Shift and press Down once to remove 10 units of green.

If you remove colour, you also remove light, so the image becomes dark. I toggle the visibility using the eye icon to compare before and after, and you can see the image getting darker. In the RGB channel, the other channels appear as a visual guide to what you have done. You cannot move those other-channel lines there. Here I have removed twice as much blue as green: 20 units of blue and 10 units of green.

To compensate, I adjust the RGB channel. RGB combines red, green, and blue, so an adjustment there is three times as strong as one in an individual channel. Adding 10 units in RGB is like adding 10 red, 10 green, and 10 blue: 30 units in total, matching the 20 plus 10 I removed. I hold Shift and press Up. When I toggle before and after, the brightness stays the same; only the colours change.

As I compensate, I notice that I tried to click on the RGB line but landed two units off, so I bring the point back to the line.

![1343 · U17 · L21 · 04:27](frames/U17L21-F0427.00.jpg)

On screen: "Green" / "Input: 128" / "Output: 118" [rest omitted]  
Shows: The harbour photograph with the Green-channel curve lowered by 10 units.

![1343 · U17 · L21 · 05:46](frames/U17L21-F0546.00.jpg)

On screen: "RGB" / "Input: 127" / "Output: 127" [rest omitted]  
Shows: The RGB curve with the blue- and green-channel curves visible as guides.

## Reducing the strength with opacity

Anchor: 1343 · U17 · L21 · 06:04–07:12

Suppose you like the colour adjustment but find it a little too strong. Instead of returning to Blue, pulling some of it back, going to Green, pulling that back, and then working out how much to compensate in RGB, use the layer’s opacity slider. In the Layers panel, click the opacity drop-down. When you hover over the word “Opacity,” the cursor becomes a hand; click and drag left or right to change the value.

If half the effect looks right, set opacity to 50%. That is easier than returning to the individual channels. If you later decide that you want a result between the original and the current adjustment, change the opacity again; for example, set it to 75%. I am now fairly happy with the colours and will work on contrast.

![1343 · U17 · L21 · 07:01](frames/U17L21-F0701.00.jpg)

On screen: "Opacity: 50%" / "Set the master opacity for the layer" [rest omitted]  
Shows: The harbour photograph and the colour-curve layer opacity set to 50%.

## Contrast, clipping, and returning to brightness

Anchor: 1343 · U17 · L21 · 07:13–09:50

I come down to the black-and-white circle and choose Curves. I call this layer Contrast, then put one point in the highlights and another in the shadows. I compare before and after. The result looks good, though I may make the shadow adjustment a little stronger. If I want a stronger effect only on the blackest part of the image, I can add a third point there and pull it down.

Be careful when moving that point or using the slider: you can cause clipping. The histogram gives you an idea of the tonal range. If I move the point too far, I start clipping the blacks and lose information in the darkest tones. That is why I put my point further down instead, to darken those blacks without clipping them.

After adjusting colour and contrast, I may return to brightness. The image now seems a little dark overall, so I brighten it slightly. The sky is somewhat washed out, but it is not the main attraction of this image; overall, I think it should be slightly brighter. Before I sign anything off, I always check before and after.

When you make a second adjustment to a layer—not just a Curves layer, but any adjustment layer—a small symbol becomes active. It lets you view the previous adjustment versus the current one. One icon switches the layer on and off; another shows the previous adjustment. Clicking it returns to the previous adjustments, and clicking it again resets them altogether.

![1343 · U17 · L21 · 08:17](frames/U17L21-F0817.00.jpg)

On screen: "Contrast" / "Input: 27" / "Output: 17" [rest omitted]  
Shows: The harbour photograph, histogram, and a shadow point on the contrast curve.

![1343 · U17 · L21 · 09:07](frames/U17L21-F0907.00.jpg)

On screen: "Brightness" / "Input: 117" / "Output: 130" / "Toggle layer visibility" [rest omitted]  
Shows: The harbour photograph with the Brightness layer selected and its visibility control highlighted.

![1343 · U17 · L21 · 09:28](frames/U17L21-F0928.00.jpg)

On screen: "Press to view previous state (can also press \ key)" [rest omitted]  
Shows: The previous-adjustment control is highlighted in an enlarged view of the adjustment-layer controls.

![1343 · U17 · L21 · 09:46](frames/U17L21-F0946.00.jpg)

On screen: "Reset to adjustment defaults" [rest omitted]  
Shows: The reset control is highlighted in the enlarged adjustment-layer controls.

## Matching the colour and contrast of two forest photographs

Anchor: 1343 · U17 · L21 · 09:51–12:19

Now let’s look at another image—or, in fact, two images. I have a forest-fern photograph and a forest photograph, and I want to use them together. Their colours are different: one is very warm, and the other is quite cool. I will warm the colours in one image and then apply contrast to make the two images match a little better.

I start with a colour curve. To warm the image, I go to the Blue channel and remove some blue. It may seem strange to remove green from an image of a forest, but think of it as a filter that you apply over everything; in that case, removing some green helps. The images now have a better relationship because their colour schemes are closer than they were before.

Next I add contrast: brighten the highlights and darken the shadows. I also darken the blacks to make the image a little more dramatic. I compare before and after. If I Option-click the background layer’s eye, I can see the original and compare it with the current version. I rename the layer Contrast. One way to reuse this adjustment is to drag the Contrast layer from one image to the other; after I drop it, the contrast is applied to that image.

![1343 · U17 · L21 · 10:13](frames/U17L21-F1013.00.jpg)

On screen: [none]  
Shows: A forest photograph with tall trunks, a fallen log, and a mossy floor.

![1343 · U17 · L21 · 10:20](frames/U17L21-F1020.00.jpg)

On screen: [none]  
Shows: A second forest photograph with dense ferns in the foreground.

![1343 · U17 · L21 · 11:00](frames/U17L21-F1100.00.jpg)

On screen: "Green" / "Input: 131" / "Output: 124" [rest omitted]  
Shows: The fern photograph with the Green channel adjusted on its Colours curve layer.

![1343 · U17 · L21 · 11:09](frames/U17L21-F1109.00.jpg)

On screen: [none]  
Shows: The companion forest photograph with tall trunks, a fallen log, and a mossy floor.

![1343 · U17 · L21 · 12:12](frames/U17L21-F1212.00.jpg)

On screen: "Contrast" [rest omitted]  
Shows: The companion forest photograph with its Contrast adjustment layer selected and a curve applied.

## Reusing a Curves adjustment

Anchor: 1343 · U17 · L21 · 12:20–13:54

The other way to reuse a curve is to save it as a preset, which I recommend if you use a type of curve often.

To save it, open the menu at the top right of the Properties panel and choose Save Curve Preset. You can also load presets, for example one you downloaded or one you are moving to another computer. Photoshop will put this curve in its presets folder by default, but you can save it anywhere. In particular, if you want to share the preset, choose a simpler location such as your desktop. I name it “contrast with the blacks” in the spoken demonstration; the filename shown in the save dialogue is “Contrast with deep blacks.” Click Save.

To apply the preset, reset the curve, then open Presets. Photoshop has a few presets, followed by the ones you have saved. Click the saved preset and the curve is applied to the image.

![1343 · U17 · L21 · 13:00](frames/U17L21-F1300.00.jpg)

On screen: "Save curves in:" / "Save As:" / "Untitled" / "Tags:" / "Presets" / "Curves" / "Cancel" / "Save" [rest omitted]  
Shows: The save dialogue open in Photoshop’s Presets/Curves folder.

![1343 · U17 · L21 · 13:20](frames/U17L21-F1320.00.jpg)

On screen: "Contrast with deep blacks" [rest omitted]  
Shows: The preset filename entered in the save dialogue.

## Targeting subtle tones with the Curves hand tool

Anchor: 1343 · U17 · L21 · 13:55–17:58

Finally, here is an image with very subtle tones. In the top-left area, you can see fine gradations. If you add contrast to a picture like this to separate those tones, but all the tones fall in the highlights, you will brighten them all rather than separating them. For example, I want to separate these two tones a little. Curves is the best tool for that.

I call this curve Contrast. Instead of placing points randomly on the curve, I use the hand tool to adjust contrast. It lets me target tones directly in the image. Remember that a place on the curve represents a tone when you follow it to the left or down. If you want to use a specific image tone rather than choosing a point at random, use the hand tool to select it precisely.

In the options bar, the Sample Size setting determines how Photoshop measures a tone. The default, Point Sample, is useful for graphics but not very good for photography. Set it to at least 3 by 3 Average so Photoshop uses the average of nine pixels to find the tone, rather than one pixel.

As I move the cursor over the image, a small circle moves up and down along the curve in the Properties panel to represent the tones under the cursor. It moves higher for lighter tones and lower for darker tones. If I want to brighten one tone and darken another, I can click the tone and drag. I could also return to the Properties panel and move the point on the curve there. While I hold the mouse button down, the cursor becomes a finger with an up arrow and a down arrow, showing that I can pull the point up or down.

I pull the lighter tone up, then move to the darker tone and drag it down. In the curve, the lighter point brightens not just the exact tone I clicked but the whole tonal range at that value and brighter. The darker point lowers the tone I clicked and the darker range. That creates contrast. Comparing before and after, the difference between the two tones is stronger and they are more pronounced in the picture.

![1343 · U17 · L21 · 14:30](frames/U17L21-F1430.00.jpg)

On screen: [none]  
Shows: A misty mountain landscape with clouds filling the valley.

![1343 · U17 · L21 · 16:23](frames/U17L21-F1623.00.jpg)

On screen: "Sample Size: 3 by 3 Average" [rest omitted]  
Shows: The Curves hand tool sampling a tone in the cloud-and-mountain photograph.

## Practising the adjustment

Anchor: 1343 · U17 · L21 · 17:59–18:48

When I first learned Curves, I struggled to understand it. Make sure you practise this quite a lot, and feel free to ask me any questions if you do not understand. In the next lesson, we will look at black and white.

![1343 · U17 · L21 · 18:07](frames/U17L21-F1807.00.jpg)

On screen: "Input: 88" / "Output: 86" [rest omitted]  
Shows: The targeted-tone curve over the cloud-and-mountain photograph after the two tones have been adjusted.
