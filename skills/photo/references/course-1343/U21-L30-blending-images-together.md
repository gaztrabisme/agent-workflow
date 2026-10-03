# Lesson 30 · Blending Images Together

Anchor: 1343 · U21 · L30 · 16:27 · https://www.domestika.org/en/courses/1971-course-2-retouching-fundamentals/units/6433-blending-images-together#course_lesson_19390

## Ways to blend two images

Anchor: 1343 · U21 · L30 · 00:00–01:07

In this lesson, the teacher demonstrates blending images with layer masks, introduces Photoshop’s gradient tool, and looks at blend modes, texture, and other image effects. Photoshop offers several ways to blend images. The example document has a portrait above a beach. One option is to reduce the portrait layer’s opacity, which blends it with the beach and can create a dreamlike effect. Another common method is to use a gradient in a layer mask.

![1343 · U21 · L30 · 00:09](frames/U21L30-F0009.00.jpg)

On screen: "LESSON 9" / "Blending Two Images Together" / "PHOTOSHOP FOR PHOTOGRAPHY / COURSE 2"  
Shows: Lesson title card.

![1343 · U21 · L30 · 00:43](frames/U21L30-F0043.00.jpg)

On screen: "Opacity: 100%" / "Portrait" / "Beach" [rest omitted]  
Shows: A portrait of a woman on a bridge, with the Portrait and Beach layers in the Layers panel.

![1343 · U21 · L30 · 00:46](frames/U21L30-F0046.00.jpg)

On screen: [rest omitted]  
Shows: The beach-at-sunset image by itself.

![1343 · U21 · L30 · 00:59](frames/U21L30-F0059.00.jpg)

On screen: "Opacity: 53%" [rest omitted]  
Shows: The portrait and beach blended at reduced opacity, with both images visible together.

## Extend the canvas and fade with a gradient mask

Anchor: 1343 · U21 · L30 · 01:07–03:42

First, restore the portrait layer’s opacity to 100% and zoom out with Command or Control plus the minus key. The teacher wants more room for the portrait above the beach, so he extends the canvas with the Crop tool. The Canvas Size dialog, shown in another lesson, is another way to extend a canvas; the Crop tool is useful when you want to see visually how much space you are adding. Press C to choose the Crop tool, pull the canvas edge outward, then press Enter or Return to commit the crop. Choose the Move tool with V and shift the portrait to the left.

Pixel layers do not have a layer mask by default. Add one from the Layer menu or click the rectangle-with-a-circle icon at the bottom of the Layers panel.

![1343 · U21 · L30 · 02:17](frames/U21L30-F0217.00.jpg)

On screen: "Add layer mask" [rest omitted]  
Shows: The bottom of the Layers panel, magnified, with the Add layer mask icon under the pointer.

Clicking it adds a white mask; Alt or Option-clicking it creates a black mask. Choose the Gradient tool with G. The gradient is currently set to foreground-to-background, black to white, so press X to swap the foreground and background colors. A white mask reveals the layer and a black mask hides it; gray values between them hide it gradually.

Place the cursor next to the model and drag. The area to the left of the cursor becomes white and remains visible. Beyond the point where you release, the mask becomes black and hides the portrait; the grayscale between those areas creates a gradual fade. Hold Shift while dragging to keep the gradient in a straight line. This is another example of using a layer mask to hide pixels.

![1343 · U21 · L30 · 01:58](frames/U21L30-F0158.00.jpg)

On screen: [rest omitted]  
Shows: The portrait shifted right, with transparent canvas space added at the left.

![1343 · U21 · L30 · 03:36](frames/U21L30-F0336.00.jpg)

On screen: [rest omitted]  
Shows: The portrait on the left fading into the beach on the right, with the portrait layer mask selected.

## Screen blend mode and additive RGB light

Anchor: 1343 · U21 · L30 · 03:42–06:33

Another way to blend images is with blend modes. In a prepared document, red, green, and blue circles sit on top of each other. The red circle appears white because its blend mode is Screen. Set it back to Normal and the circle looks red again.

Screen treats the layer as a light source. If blue, green, and red light are added at maximum brightness, they combine as white. Removing the red light leaves green and blue, which make cyan (captions: “Sayon”). The teacher says that when working with light or in Photoshop we normally think subtractively: removing red gives cyan. Bringing the red back makes the overlap white again. With the blue circle moved away, the red, green, and blue layers are visible separately. Put red and green together without blue and they make yellow (captions: “Yeah, Laura”). When the circles overlap, red is opposite cyan, blue is opposite yellow, and green is opposite magenta; where all three meet, the result is white. This is how light and Photoshop work. Screen is one of many blend modes; the lesson and the rest of the course introduce more, though photographers do not necessarily use every blend mode.

![1343 · U21 · L30 · 06:20](frames/U21L30-F0620.00.jpg)

On screen: "Screen" / "Red" / "Green" / "Blue" / "Background" [rest omitted]  
Shows: Red, green, and blue circles overlapping to make yellow, magenta, cyan, and white.

## Blend a grayscale texture into a snowy photograph

Anchor: 1343 · U21 · L30 · 06:33–09:55

To demonstrate blend modes (captions: “PlanMods”) on photographs, the teacher opens a snowy-road image and a second image of a floor surface, which he thinks is an anti-slip surface of the kind used in swimming pools. He chose it because it contains white, gray, and black specks, and blend modes use the grayscale. He says they will look at color in another example. He copies the texture into the snowy-road document by dragging its layer onto the document tab. A useful shortcut is to hold Shift before releasing the layer so that it lands centered over the image.

The texture is slightly smaller than the photograph, so he zooms out and uses Free Transform with Command or Control+T to scale it until it covers the image. In Normal mode, the texture simply covers the background. Changing the blend mode changes how it combines with the image underneath. He cycles through modes with the down-arrow key; each gives a different result. The floor texture on the snow changes the photograph’s appearance substantially. In Lighten, it can look as though snow is falling. The teacher says this may not be a perfect improvement, but it is a quick starting point and demonstrates how blend modes change the image. Lighten shows only pixels from the texture that are lighter than the layer below, so most gray pixels and almost all black pixels disappear. Darken does the opposite.

![1343 · U21 · L30 · 07:03](frames/U21L30-F0703.00.jpg)

On screen: [none]  
Shows: The original photograph of a road through a snowy forest.

![1343 · U21 · L30 · 07:35](frames/U21L30-F0735.00.jpg)

On screen: [none]  
Shows: The separate floor texture, covered in white, gray, and black specks.

![1343 · U21 · L30 · 09:35](frames/U21L30-F0935.00.jpg)

On screen: "Lighten" [rest omitted]  
Shows: The snowy-road photograph with the speckled floor texture blended over it in Lighten mode.

## Combine a portrait with night-sky layers

Anchor: 1343 · U21 · L30 · 09:55–13:04

The next document contains a portrait and three night-sky layers. The first is an image of the Northern Lights. The layer blend mode is Normal by default. The teacher cycles through the modes again: Multiply creates an interesting effect that shows both dark and light pixels; Lighten keeps the pixels that are lighter than the layer below. Screen also combines the two layers, like Multiply, but brightens instead of darkening. Overlay, Soft Light (captions: “softline”), and Hard Light are used often in retouching, particularly Overlay and Soft Light. For this portrait, the teacher likes the contrast from Hard Light.

![1343 · U21 · L30 · 11:15](frames/U21L30-F1115.00.jpg)

On screen: [rest omitted]  
Shows: The portrait combined with the Northern Lights in Hard Light, with the blend-mode menu open and Hard Light highlighted.

He switches on another sky layer and tries blend modes to combine it with the portrait and Northern Lights. He likes the effect near the bottom of the image. To confine it there, he adds a layer mask and uses the Gradient tool to fade the effect gradually upward. He wants the gradient to start white and finish black, and redraws it a little longer.

He adds a third layer to the mix and chooses Lighten. Looking back at the sequence, he starts with the portrait, adds the Northern Lights in Hard Light for contrast, adds another sky layer also in Hard Light, then uses a layer mask and gradient to keep that effect at the bottom. Finally, he adds the second sky layer in Lighten. The tab is named “Portrait blend with sky”; the captions mishear “sky” as “Scott.”

![1343 · U21 · L30 · 10:05](frames/U21L30-F1005.00.jpg)

On screen: "Sky 2" / "Sky 1" / "Northern Lights" / "Background" [rest omitted]  
Shows: The original monochrome portrait with three sky-layer thumbnails listed above it.

![1343 · U21 · L30 · 10:24](frames/U21L30-F1024.00.jpg)

On screen: "Normal" / "Dissolve" / "Darken" / "Multiply" / "Color Burn" / "Linear Burn" / "Darker Color" / "Lighten" / "Screen" / "Color Dodge" / "Linear Dodge (Add)" / "Lighter Color" / "Overlay" / "Soft Light" / "Hard Light" / "Vivid Light" / "Linear Light" / "Pin Light" / "Hard Mix" / "Difference" / "Exclusion" / "Subtract" [rest omitted]  
Shows: The Northern Lights image alone, with the blend-mode menu open.

![1343 · U21 · L30 · 12:11](frames/U21L30-F1211.00.jpg)

On screen: [rest omitted]  
Shows: The portrait combined with Northern Lights and a pink star field along the lower edge, with a gradient mask on the Sky 1 layer.

![1343 · U21 · L30 · 12:35](frames/U21L30-F1235.00.jpg)

On screen: [rest omitted]  
Shows: The portrait combined with the Northern Lights and two star-field layers.

![1343 · U21 · L30 · 12:42](frames/U21L30-F1242.00.jpg)

On screen: [rest omitted]  
Shows: The original monochrome portrait shown again as the starting image for the recap.

## Clip a landscape into a portrait and combine blend modes

Anchor: 1343 · U21 · L30 · 13:04–15:52

For the final example, the teacher wants an image on top of another layer to show only where that lower layer has image pixels. He has cut out a portrait so it sits on a white background, and has a landscape image. Clipping the landscape to the portrait makes it visible only where the portrait exists.

There are several ways to create the clipping mask: use the Layer menu or right-click the empty area of the layer and choose Create Clipping Mask. The clipped layer displays a small arrow and is offset to the right; the title of the layer it clips to becomes underlined. With the Move tool (V), the teacher moves the landscape within the person’s silhouette. He describes this as a fun way to combine images and make a dreamlike effect.

The clipped landscape can also use blend modes. It starts in Normal, then the teacher chooses Hard Light so that both images show strongly. Hard Light also affects pure white (captions: “hard lights”). To demonstrate, he releases the clipping mask by right-clicking the landscape layer and choosing Release Clipping Mask; the landscape then affects the background too. He prefers the clipped version and undoes the release with Command or Control+Z (captions: “set”).

![1343 · U21 · L30 · 13:28](frames/U21L30-F1328.00.jpg)

On screen: "Landscape" / "Portrait" / "Background" [rest omitted]  
Shows: The cut-out profile portrait on white, with the landscape layer above it.

![1343 · U21 · L30 · 13:49](frames/U21L30-F1349.00.jpg)

On screen: [rest omitted]  
Shows: The separate mountain landscape image.

![1343 · U21 · L30 · 13:53](frames/U21L30-F1353.00.jpg)

On screen: "Create Clipping Mask" [rest omitted]  
Shows: The layer context menu with Create Clipping Mask highlighted.

![1343 · U21 · L30 · 13:58](frames/U21L30-F1358.00.jpg)

On screen: [rest omitted]  
Shows: The mountain landscape clipped inside the profile silhouette.

![1343 · U21 · L30 · 15:18](frames/U21L30-F1518.00.jpg)

On screen: [rest omitted]  
Shows: The portrait-and-landscape composite with Hard Light selected in the blend-mode menu.

![1343 · U21 · L30 · 15:39](frames/U21L30-F1539.00.jpg)

On screen: [rest omitted]  
Shows: The portrait-and-landscape composite filling the canvas after the clipping mask is released.

## Exercise and close

Anchor: 1343 · U21 · L30 · 15:52–16:27

He asks learners to blend two images and upload the result to the Domestika website for him and others to review. He says blending images can be fun and create interesting effects, then introduces the next practical exercise, where learners bring the new skills together in one image.

![1343 · U21 · L30 · 16:05](frames/U21L30-F1605.00.jpg)

On screen: [rest omitted]  
Shows: The clipped portrait-and-landscape composite on white after the release is undone.
