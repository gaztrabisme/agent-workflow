# Lesson 47 · Sky Replacement 2

Anchor: 1343 · U30 · L47 · 12:27 · https://www.domestika.org/en/courses/1972-course-3-retouching-environmental-images/units/6447-sky-replacement#course_lesson_19496

## Reusing a group mask with another sky

Anchor: 1343 · U30 · L47 · 00:10–02:04

*Course 1343 · U30 · L47 · 00:10–02:04*

I call the group “sky replacement.” I open it and move the mask from the first sky layer onto the group. At first it looks as though nothing has changed, but anything I put into the group will now use that mask. I can try another sky by dragging its layer from the Layers panel onto the image tab and dropping it into the photograph. I hold Shift as I drop it to center it.

This layer ends up in the wrong place in the stack: the curve is clipped to this layer rather than to the sky underneath. I drag the curve above it, and now the Sky 2 layer is clipped to that curve. I release the clipping mask by right-clicking and choosing Release Clipping Mask. I call the new layer “Sky 2.” Replacing the sky is then as simple as dropping another image into the group. I change the blend mode to Multiply, but that makes the new sky multiply with the original sky underneath, creating strange colors. When I switch the original sky layer off, the result works better. With the Move tool and the sky layer selected, I can reposition the image; I move it far enough that the mountain is outside the frame.

![1343 · U30 · L47 · 00:28](frames/U30L47-F0028.00.jpg)

On screen: “Multiply” / “Opacity: 100%” / “Layer mask thumbnail” / “Sky replacement” / “Curves 1” / “Sky” / “Background” [rest omitted]  
Shows: The city sky replacement group, its mask, curve, and original sky layer.

![1343 · U30 · L47 · 01:21](frames/U30L47-F0121.00.jpg)

On screen: “Sky 2” [rest omitted]  
Shows: The colorful street with a second, pink sunset sky in the group.

![1343 · U30 · L47 · 01:31](frames/U30L47-F0131.00.jpg)

On screen: [rest omitted]  
Shows: The street composite as the pink sunset sky multiplies with the original sky, leaving blue-green and gray clouds above the buildings.

![1343 · U30 · L47 · 01:40](frames/U30L47-F0140.00.jpg)

On screen: “Indicates layer visibility” [rest omitted]  
Shows: The street composite with the pink sunset sky visible after the original Sky layer is switched off; the cursor is over that layer’s visibility control.

## Comparing and sampling sky colors

Anchor: 1343 · U30 · L47 · 02:04–04:41

*Course 1343 · U30 · L47 · 02:04–04:41*

For another example, I start with a fairly nice blue sky and want to add more interest.

![1343 · U30 · L47 · 02:14](frames/U30L47-F0214.00.jpg)

On screen: [none]  
Shows: A pale sky over a straight road through dry grassland.

I have found a sky with interesting clouds and a different color.

![1343 · U30 · L47 · 02:25](frames/U30L47-F0225.00.jpg)

On screen: [none]  
Shows: The replacement sky image, with clouds over a green hill.

I move this cloud sky into the road image to compare it with the original. It looks more cyan and a little colder than the original sky, so I’ll show how to match colors between images.

I use the Color Sampler tool, which is grouped with the Eyedropper tool. Their icons look similar, but they do different things: the Eyedropper picks up a color that can be used, for example, with the Brush, while the Color Sampler measures colors.

![1343 · U30 · L47 · 03:22](frames/U30L47-F0322.00.jpg)

On screen: “Eyedropper Tool I” / “Color Sampler Tool I” [rest omitted]  
Shows: The Eyedropper and Color Sampler tools are open together in the toolbar flyout.

I make sure the sample size is not Point Sample. The area is large enough that 11 by 11 could work, but I use 5 by 5.

![1343 · U30 · L47 · 03:32](frames/U30L47-F0332.00.jpg)

On screen: “Sample Size” / “Point Sample” / “3 by 3 Average” / “5 by 5 Average” / “11 by 11 Average” / “31 by 31 Average” / “51 by 51 Average” / “101 by 101 Average” [rest omitted]  
Shows: Photoshop’s Color Sampler sample-size menu, with 5 by 5 Average selected.

I place a Color Sampler point in a blue area of the sky. Photoshop opens the Info panel automatically; if it is closed, I can open it from Window > Info.

![1343 · U30 · L47 · 03:50](frames/U30L47-F0350.00.jpg)

On screen: “R: 136” / “G: 186” / “B: 240” / “#1 R: 138” / “G: 188” / “B: 241” [rest omitted]  
Shows: The road image’s sampled sky color and the Info panel’s RGB readings.

The panel gives RGB values. I move the point a little so it is not on a cloud. In the sky I am matching, the values are red 29, green 153, and blue 207. The values in the other image are quite different.

![1343 · U30 · L47 · 04:32](frames/U30L47-F0432.00.jpg)

On screen: “R: 38” / “G: 156” / “B: 209” / “#1 R: 29” / “G: 153” / “B: 207” [rest omitted]  
Shows: A Color Sampler point over the cloud sky and its RGB values in the Info panel.

Then I activate the sky layer and use Curves to match the colors.

## Matching the channels with Curves

Anchor: 1343 · U30 · L47 · 04:41–08:42

*Course 1343 · U30 · L47 · 04:41–08:42*

Curves is the best tool for this. I add a curve, call it “Color match” (shown as “Colour match” in Photoshop), and clip it to the sky layer. With the target adjustment tool—the little finger symbol—I can move over the image and see a small ball follow the brightness value. In the Red channel, I click in the area to place a point that represents the amount of red there. I do the same in Green and Blue.

The target Red value is 142, while the current value is 30. I use the arrow keys to raise it. Holding Shift makes the value move in steps of ten, but here the change is so large that it goes a little crazy, so I remove that point and move this one instead. The readout shows the original value at 29 and the new value at 72. I keep moving until I reach 142. If I click in a slightly different spot, the values will differ, so I should match the sky in my own image. The Green value starts at 153 and I raise it to 189. In Blue, I move from 207 to 241. This matches both color and brightness values.

I am really interested in matching the color values. Blend modes can be difficult to understand, so if you guessed the right one, well done; if not, you will get it. I change the blend mode to Color. The displayed values now change, and the image is a slightly darker version of essentially the same color: this mode changes color without the brightening effect. With the sky layer switched off, the match is closer than before. Switching off the “Colour match” curve shows the original cyan, aqua-like color again.

![1343 · U30 · L47 · 05:32](frames/U30L47-F0532.00.jpg)

On screen: “Colour match” / “Red” / “R: 30/30” / “G: 153/153” / “B: 207/207” [rest omitted]  
Shows: The sampled cloud sky with the Color match curve open in the Red channel.

![1343 · U30 · L47 · 06:08](frames/U30L47-F0608.00.jpg)

On screen: “Input: 30” / “Output: 90” [rest omitted]  
Shows: The red curve pushed too far, turning the cloud sky and hill pink.

![1343 · U30 · L47 · 08:03](frames/U30L47-F0803.00.jpg)

On screen: “Input: 207” / “Output: 241” / “Color” [rest omitted]  
Shows: The blue-channel curve at its target value, with the blend-mode menu open.

![1343 · U30 · L47 · 08:18](frames/U30L47-F0818.00.jpg)

On screen: “#1 R: 29/83” / “G: 153/130” / “B: 207/182” [rest omitted]  
Shows: The cloud sky blended to the target color above the green hill, with the Color mode and Info panel readings visible.

![1343 · U30 · L47 · 08:39](frames/U30L47-F0839.00.jpg)

On screen: “R: 142/142” / “G: 189/189” / “B: 241/241” [rest omitted]  
Shows: The dry road image with the sky layer hidden while the sampled RGB values match.

## Positioning and blending the sky at the horizon

Anchor: 1343 · U30 · L47 · 08:42–12:27

*Course 1343 · U30 · L47 · 08:42–12:27*

Next I put this sky into the other image. I switch it off for a moment so I can see where the horizon is. Guidelines are useful for this: I choose View > Rulers, put the cursor in the center of the ruler, and drag down to the horizon. The guide marks where the original sky ends, so I can blend the two images.

I switch the sky back on. It happens to match quite well. I add a layer mask; by default it is white. I choose the Gradient tool with G and select the first gradient, foreground to background, in the options bar. I press D for the default colors and X to swap foreground and background. I want black at the bottom, gradually changing to white above. Black hides and white reveals: I hide the bottom of the sky layer and reveal the sky above. I start the gradient at the guide, hold Shift to keep the drag straight, and experiment with how far to drag. Then I turn off the rulers and hide the guides.

When I remove the “Colour match” curve, the color does not feel right. The original sky was a lot brighter than this replacement, so if I want more brightness, I make a separate curve because the “Colour match” curve is set to Color. I clip that new curve as well, then brighten the sky. The result looks convincing and is simple to make for this kind of image. This lesson has shown two kinds of sky replacement and how to match colors between images. That wraps up the lesson on sky replacement. I hope you enjoyed it; in the next lesson we’ll add creative effects to images.

![1343 · U30 · L47 · 09:06](frames/U30L47-F0906.00.jpg)

On screen: [none]  
Shows: The cursor is positioned near the road’s distant horizon.

![1343 · U30 · L47 · 09:57](frames/U30L47-F0957.00.jpg)

On screen: [rest omitted]  
Shows: A horizontal cyan guide crosses the green hill below the cloud sky.

![1343 · U30 · L47 · 10:39](frames/U30L47-F1039.00.jpg)

On screen: “Mode: Normal” / “Opacity: 100%” [rest omitted]  
Shows: The Gradient tool is active as the sky mask is dragged across the horizon guide.

![1343 · U30 · L47 · 11:10](frames/U30L47-F1110.00.jpg)

On screen: [none]  
Shows: The cloud sky blended into the dry road photograph.

![1343 · U30 · L47 · 12:10](frames/U30L47-F1210.00.jpg)

On screen: “Input: 121” / “Output: 141” [rest omitted]  
Shows: The finished road composite with a separate curve brightening the image.

### Key points (derived)

- A group mask lets you try different sky layers without rebuilding the mask each time.
- Use the Color Sampler and Curves to match the sampled RGB values, then set the color correction to Color so it changes color without brightening.
- A straight gradient on a sky-layer mask can blend the replacement sky across the horizon; a separate clipped curve can control its brightness.
