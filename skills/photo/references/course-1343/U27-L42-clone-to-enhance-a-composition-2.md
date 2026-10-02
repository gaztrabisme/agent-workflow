# Lesson 42 · Clone to Enhance a Composition 2

Anchor: 1343 · U27 · L42 · 20:15 · https://www.domestika.org/en/courses/1972-course-3-retouching-environmental-images/units/6442-clone-to-enhance-a-composition#course_lesson_19494

## Finish the first path edit

Anchor: 1343 · U27 · L42 · 00:00–02:10

*Adobe Photoshop: Beginner's Guide for Photographers · U27 · L42 · 00:00–02:10*

I undo the last mark because it is better to undo than to clone on top of a mistake. The result is not perfect, but the edit is beginning to work. Repeated patterns are a sign of cloning, and I want to avoid them, so I remove some of the obvious repeats and adjust the clone angle again. I see another repeated pattern and reduce its appearance. I also remove a small rock. The flowers are distracting, so I clone them out as well.

To draw more attention toward the people on the bridge, I darken the foreground. I add a Curves adjustment layer and rename it `foreground darken`.

![1343 · U27 · L42 · 00:40.00](frames/U27L42-F0040.00.jpg)

On screen: [none]  
Shows: The path image after the first round of cloning, with a cleaned section of path visible in the inset.

![1343 · U27 · L42 · 01:41.00](frames/U27L42-F0141.00.jpg)

On screen: [none]  
Shows: A closer view of the path and grass where the distracting flowers and small rock are being removed.

## Darken the foreground with a masked gradient

Anchor: 1343 · U27 · L42 · 02:10–05:28

*Adobe Photoshop: Beginner's Guide for Photographers · U27 · L42 · 02:10–05:28*

When an edit darkens an area, its colours tend to become more saturated. Changing the blend mode to Luminosity can help. I select the layer mask and choose the Gradient tool. The gradient I need is Foreground to Background; if I cannot see it, it is probably in the Basic folder. I dragged my frequently used gradients to the top. I set white as the foreground and black as the background because I want to reveal the adjustment from the bottom of the image. White reveals on a layer mask and black hides. I drag a straight gradient upward from the bottom toward the start of the bridge, holding Shift to keep it straight, then preview the result.

The darkening may be too strong. Instead of changing the curve, it is easier to lower the layer opacity, so I reduce it to 80%. I also want to darken the side of the image slightly. If I add a left-to-right gradient to the same mask using Foreground to Background, it will remove the bottom adjustment. I previously showed how to use Foreground to Transparent instead. With white as the foreground, that gradient would add to the previous one because transparency reveals the black from the earlier edit. I undo that attempt with Command or Control+Z and Alt or Option-click out of the mask. Then I place the side gradient. The road texture looks a little suspicious, so I could clone another sample from higher in the image. For this lesson, the example is enough to show the principle.

![1343 · U27 · L42 · 03:09.00](frames/U27L42-F0309.00.jpg)

On screen: "Presets" / "Basics" / "Blues" / "Purples" / "Name: Foreground to Transparent" [rest omitted]  
Shows: The Gradient Editor open over the landscape, with its preset folders and gradient thumbnails.

![1343 · U27 · L42 · 03:54.00](frames/U27L42-F0354.00.jpg)

On screen: "Luminosity" / "Foreground darken" [rest omitted]  
Shows: The bridge landscape with the foreground-darkening curve and its layer mask selected.

![1343 · U27 · L42 · 04:54.00](frames/U27L42-F0454.00.jpg)

On screen: [rest omitted]  
Shows: The selected layer mask in grayscale, with the bottom-to-top gradient combined with a left-to-right gradient.

![1343 · U27 · L42 · 05:11.00](frames/U27L42-F0511.00.jpg)

On screen: "Opacity 79%" [rest omitted]  
Shows: The foreground gradient in place, with the adjustment opacity lowered.

## Why puddles are difficult to clone

Anchor: 1343 · U27 · L42 · 05:28–10:00

*Adobe Photoshop: Beginner's Guide for Photographers · U27 · L42 · 05:28–10:00*

I move to the other photograph and consider removing its puddles. I duplicate the background with Command or Control+J, rename the new layer `Clone`, select the Clone Stamp with S, and enlarge the brush with the square-bracket keys. I try cloning, but it is difficult for several reasons. I repeat a pattern. I can remove that repetition, but the lines in the photograph do not match well. The shallow depth of field, created with a fairly large aperture, means the sharpness also changes across the scene. The lens is fairly wide, so foreground objects look larger than background objects. This happens with any lens, but the wider the lens, the more pronounced it is.

I need to sample from the same level as the area I’m covering. That makes sharpness and size match better, although the lines still do not flow well. Sampling from the other side of the image does not solve the problem: it reaches the edge of the frame and the lines still fail to line up. Whatever I try, it does not look quite right.

I open Clone Source, using Window if the panel is not visible. In addition to the angle control used earlier, Clone Source can flip the source horizontally or vertically. Here I turn on Flip Horizontal. When I sample from one side and move the brush the other way, the clone source moves in the opposite direction. This makes it possible to work at the same level while moving a source feature in the reverse direction. To remove the puddles on the other side, I switch back to the normal clone. I first need to remove the existing puddles. I reopen Clone Source and reset it; mirroring is now off.

![1343 · U27 · L42 · 06:13.00](frames/U27L42-F0613.00.jpg)

On screen: [none]  
Shows: The second photograph before the puddles are removed, with the car and people in the muddy foreground setting.

![1343 · U27 · L42 · 08:26.00](frames/U27L42-F0826.00.jpg)

On screen: "Clone Source" [rest omitted]  
Shows: The Clone Source panel open over the car photograph while horizontal mirroring is introduced.

![1343 · U27 · L42 · 08:46.00](frames/U27L42-F0846.00.jpg)

On screen: [rest omitted]  
Shows: The Clone Source panel with the Flip Horizontal icon selected, over the car photograph.

![1343 · U27 · L42 · 09:53.00](frames/U27L42-F0953.00.jpg)

On screen: "X: 5054 px" / "Y: 42 px" / "Angle: 0.0°" [rest omitted]  
Shows: The Clone Source panel after its transform is reset.

## Remove puddles and check for cloning artifacts

Anchor: 1343 · U27 · L42 · 10:00–16:14

*Adobe Photoshop: Beginner's Guide for Photographers · U27 · L42 · 10:00–16:14*

I make the brush smaller with the square-bracket keys and clone out the puddles. When an attempt looks wrong, I zoom in, undo with Command or Control+Z, and redo that area rather than painting over the mistake. After the first pass, I zoom out and toggle the layer on and off. If anything jumps out as suspicious, I redo it.

Once those puddles are covered, I turn mirroring on again in Clone Source. I zoom out enough to see the frame edges because I’m working close to an edge. I sample at the same level and close to the edge, keeping the brush just inside the frame. I place that sample near the opposite edge and brush it down. As the brush moves left, the mirrored clone source moves right.

I use the same method to remove a smudgy area. At boundaries such as mud meeting grass, I often sample directly on the edge because it helps me keep track of where I am. I sample near the car, align the source, and clone across. When I get too close to the car, I undo the whole stroke and try again. I watch the small cross that marks the clone source so I can see when it approaches the car, then let go before it reaches it.

After cloning large areas, the image may look tampered with. I turn mirroring off or reset the Clone Source transforms, then make smaller corrections. At 100%, I look for marks that seem out of place, including tiny background details; those are the kinds of artifacts I do not want to leave. It is better to find my own mistakes before someone else does. When I toggle the clone layer, one line still stands out, so the edit needs more work. As in the previous image, this is not fully finished, but it is enough for the lesson.

![1343 · U27 · L42 · 10:36.00](frames/U27L42-F1036.00.jpg)

On screen: [none]  
Shows: A 100% close-up of the car and two people, with the clone area nearby in the muddy ground.

![1343 · U27 · L42 · 11:15.00](frames/U27L42-F1115.00.jpg)

On screen: [none]  
Shows: The full car photograph after the first puddle-cleanup pass, with the clone layer active.

![1343 · U27 · L42 · 15:36.00](frames/U27L42-F1536.00.jpg)

On screen: [none]  
Shows: A 100% close-up of the muddy ground beside the car, with the brush outline near the center of the image.

![1343 · U27 · L42 · 15:50.00](frames/U27L42-F1550.00.jpg)

On screen: [none]  
Shows: The car photograph at the final clone check, with the clone layer ready to be compared against the original.

## Darken the foreground and the distant tones

Anchor: 1343 · U27 · L42 · 16:14–20:15

*Adobe Photoshop: Beginner's Guide for Photographers · U27 · L42 · 16:14–20:15*

As with the previous photograph, I finish by darkening the foreground, which is bright and draws attention. I use a Curves adjustment and darken it slightly. The soil becomes redder, so I change the blend mode to Luminosity to avoid that colour shift. I could also work in the red channel to remove red, but with Luminosity selected that would not make a difference. I select the Gradient tool with G. It is currently set to Foreground to Transparent, so I switch it to Foreground to Background and make sure the mask is selected. The outlines show which mask is selected; I think Adobe could make this clearer.

I add a gradient to darken the foreground, stopping it before the people’s feet. For the sky and mountains, I choose a separate Curves adjustment because that is a different kind of edit and should not continue in the same mask. I darken the image, then darken the deepest tones more than the rest. I again use Luminosity to avoid changing colour. With the Gradient tool, I put white at the top and black at the bottom so the effect applies at the top. I drag from near the top of the mountain, holding Shift to keep the line straight. The effect may be too strong or the transition too sharp, so I draw the line farther out and lower the layer opacity. I compare the original and edited image.

I hope you enjoyed learning how to add or remove objects to improve a composition. In the next lesson, we’ll look at enhancing the most important features in a few different ways.

![1343 · U27 · L42 · 17:36.00](frames/U27L42-F1736.00.jpg)

On screen: "Curves 1" [rest omitted]  
Shows: The foreground curve adjustment and mask on the car photograph.

![1343 · U27 · L42 · 19:50.00](frames/U27L42-F1950.00.jpg)

On screen: "Curves 2" [rest omitted]  
Shows: A second masked curve for the sky and mountain tones above the first curve.

![1343 · U27 · L42 · 19:56.00](frames/U27L42-F1956.00.jpg)

On screen: "Opacity 67%" [rest omitted]  
Shows: The final darkened comparison with the second curve’s opacity reduced.
