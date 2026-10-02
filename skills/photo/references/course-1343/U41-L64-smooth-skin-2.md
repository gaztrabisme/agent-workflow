# Lesson 64 · Smooth Skin 2

Anchor: 1343 · U41 · L64 · 11:40 · https://www.domestika.org/en/courses/1973-course-4-retouching-portraits/units/6463-smooth-skin#course_lesson_19502

## Prepare the second portrait and clean larger blemishes

Anchor: 1343 · U41 · L64 · 00:00–01:38

This second technique involves more steps than the first, but that does not make it difficult. The teacher shows both because they produce different results and each teaches something different. He starts a new layer with Shift+Command+N, or Shift+Control+N on Windows, calls it “Clean up,” zooms in, and holds Spacebar to reposition the image. With the Healing Brush, he holds Alt/Option (the captions misrender this as “Alt-Ruption”) and clicks to sample nearby skin, then removes the larger marks.

He says he would also clone out stray flyaway hairs (the captions garble this as “cloning They still fly with their hairs out”), but leaves them for this lesson. There are a few more small bumps he could remove, but he is satisfied with the cleanup for the demonstration.

![1343 · U41 · L64 · 00:31](frames/U41L64-F0031.00.jpg)

On screen: “Photography Course London” [rest omitted]  
Shows: The second portrait open in Photoshop, with the model in a burgundy headband and orange sweater.

![1343 · U41 · L64 · 01:13](frames/U41L64-F0113.00.jpg)

On screen: “Clean up” / “Aligned” / “Sample: Current & Below” [rest omitted]  
Shows: The Healing Brush cursor on the close portrait and the Clean up layer above the background.

## Build separate skin-tone and skin-texture layers

Anchor: 1343 · U41 · L64 · 01:39–03:59

Create a composite layer with Shift+Option+Command+E, or Shift+Control+Alt+E on Windows. Convert it to a Smart Object by right-clicking an empty area of the layer row and choosing Convert to Smart Object. Name it “Skin tones.” Duplicate it with Command/Control+J and name the copy “Skin texture.” Hide Skin texture for now so the skin-tone layer is visible.

Apply Filter > Blur > Surface Blur. Unlike Gaussian Blur (the captions misrender the name as “Gorsham Blur”), Surface Blur tries to preserve texture at edges and lines. Threshold controls how much detail stays: a lower threshold keeps more detail, while a higher threshold keeps less. Radius controls the amount of blur. Raise the radius and try a slightly higher threshold, aiming to blend the skin tones as in the previous technique. The example dialog shows 13 pixels for radius and 19 levels for threshold. The image may look strange at this stage, but some original skin texture can remain in places; change radius and threshold if you want to remove more. The blur itself is not meant to be the finished result. As with Gaussian Blur, the goal is to blend the tones, then reveal them through a mask and lay skin texture back over them.

![1343 · U41 · L64 · 02:21](frames/U41L64-F0221.00.jpg)

On screen: “Skin texture” / “Skin tones” [rest omitted]  
Shows: The two Smart Object layers arranged above Clean up and the background.

![1343 · U41 · L64 · 03:19](frames/U41L64-F0319.00.jpg)

On screen: “Surface Blur” / “Radius: 13 Pixels” / “Threshold: 19 levels” [rest omitted]  
Shows: The Surface Blur dialog over the close portrait preview.

## Reveal the softened skin gradually through a black mask

Anchor: 1343 · U41 · L64 · 04:00–05:57

Add a black layer mask by holding Alt/Option while clicking the layer-mask icon. Select the Brush with B, set white as the foreground color, and paint into the mask. An opacity and flow of 30% each work well. Lower values tend to give more accurate results; if there is time, reduce both to 20% or slightly less. Gradual painting makes the result more controlled.

The Smart Object also lets the teacher use a Smart Filter and change its settings later: double-click the Surface Blur filter rather than stepping backward through the history. Zoom in or out with Command/Control+1 to judge the result. The full-strength softening looks a little fake, so he plans to lower the layer opacity to 50%, as in the previous lesson. Before doing that, he will restore skin texture on a separate layer.

![1343 · U41 · L64 · 04:10](frames/U41L64-F0410.00.jpg)

On screen: “Layer Mask” / “Select and Mask...” / “Color Range...” / “Invert” [rest omitted]  
Shows: The black mask selected on Skin tones with the mask Properties controls open.

![1343 · U41 · L64 · 05:41](frames/U41L64-F0541.00.jpg)

On screen: “Skin texture” / “Skin tones” / “Surface Blur” [rest omitted]  
Shows: The softened close portrait with the Skin tones mask and Surface Blur Smart Filter visible in the Layers panel.

## Restore texture with High Pass and group both layers

Anchor: 1343 · U41 · L64 · 05:58–08:52

Turn on Skin texture. Softening removes texture, so this technique brings the original texture back and overlays it on the softened skin. Apply Filter > Other > High Pass; the captions render “Other” as “out there.” This uses the same approach as the earlier course’s image-sharpening lesson to extract skin texture. Zoom to 100% with Command/Control+1. The High Pass dialog also has a small window with a 100% magnification preview, but he prefers to zoom the whole image. Choose a radius where the original skin texture is just visible. About 1.5 pixels works here, and the Smart Object keeps that setting editable. Change the blend mode to Overlay.

Select Skin texture and Skin tones together and group them with Command/Control+G. Name the group “Skin soften” (the captions render this as “skin soft and”) and start it at 50% opacity (the captions garble this as “as a sailor starts”). The group keeps the layers organized and lets one opacity setting control both the skin texture and softened tones.

The teacher catches a mistake and points it out: the texture is being applied to the entire image. Select the texture layer, right-click its empty area, and choose Create Clipping Mask. This attaches the texture layer to the one below, so it no longer affects the whole image. Compare before and after.

![1343 · U41 · L64 · 06:33](frames/U41L64-F0633.00.jpg)

On screen: “Skin texture” / “Skin tones” [rest omitted]  
Shows: The full portrait with the Skin texture layer selected before applying High Pass.

![1343 · U41 · L64 · 07:27](frames/U41L64-F0727.00.jpg)

On screen: “High Pass” / “Radius: 1.5 Pixels” [rest omitted]  
Shows: The gray High Pass texture preview and its radius setting.

![1343 · U41 · L64 · 08:31](frames/U41L64-F0831.00.jpg)

On screen: “Skin soften” [rest omitted]  
Shows: The portrait with the grouped layers and their Smart Filters visible.

![1343 · U41 · L64 · 08:43](frames/U41L64-F0843.00.jpg)

On screen: “Overlay” [rest omitted]  
Shows: The texture layer set to Overlay within the Skin soften group.

![1343 · U41 · L64 · 08:47](frames/U41L64-F0847.00.jpg)

On screen: “Skin soften” / “Skin texture” / “Skin tones” [rest omitted]  
Shows: The clipped Skin texture layer indented above Skin tones in the Skin soften group.

## Compare the two finishes and choose for the image

Anchor: 1343 · U41 · L64 · 08:53–11:40

The Surface Blur result looks natural, though it may take a few attempts to get used to the technique. The teacher raises the group opacity to about 75% and likes the result. At that setting, the example looks quick to create once the steps are familiar.

![1343 · U41 · L64 · 09:31](frames/U41L64-F0931.00.jpg)

On screen: “Opacity: 75%” / “Skin soften” / “Skin texture” / “High Pass” / “Skin tones” / “Surface Blur” / “Clean up” [rest omitted]  
Shows: The finished Surface Blur portrait with the clipped Skin texture layer and the Skin soften group at 75% opacity.

The group opacity controls the overall effect; adjust the texture and tone layers individually to change their balance.

He switches back to the previous portrait to compare it with the Gaussian Blur method. Gaussian Blur adds noise but does not put the original skin texture back. It can be useful when the original texture is unwanted, such as texture in a backdrop or another surface. It can also reduce shine: the cheek looks slightly less shiny, giving a matte effect.

Overall, he prefers Surface Blur, although it takes more steps and more knowledge. If the original skin texture is desirable, he recommends this method over Gaussian Blur. Both methods have advantages, which is why he showed both. Another method, frequency separation, is more complex and will be covered in the next course. Having learned how to smooth skin in a picture (the captions say “smear the skin”), the next lesson moves on to making the subject stand out in the image.

![1343 · U41 · L64 · 09:47](frames/U41L64-F0947.00.jpg)

On screen: “Opacity: 50%” / “Add Noise” [rest omitted]  
Shows: The earlier portrait with the Gaussian Blur result visible while the teacher compares techniques.

![1343 · U41 · L64 · 10:31](frames/U41L64-F1031.00.jpg)

On screen: “Opacity: 50%” / “Add Noise” [rest omitted]  
Shows: The earlier portrait and the Gaussian Blur layer’s Add Noise Smart Filter as the teacher points out reduced shine on the cheek.
