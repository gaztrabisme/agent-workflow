# Lesson 48 · Creative Effects 1

Anchor: 1343 · U31 · L48 · 13:31 · https://www.domestika.org/en/courses/1972-course-3-retouching-environmental-images/units/6449-creative-effects#course_lesson_19406

## Introducing Blend If and finding Layer Style

Anchor: 1343 · U31 · L48 · 00:00–01:04

1343 · U31 · L48 · 00:00–01:04

In this lesson, I’ll show how to add a warm tone, backlight and sun flare to an image. To make the most of Photoshop, it is important to understand the different ways to blend images and layers. We have already used opacity, blend modes and layer masks. Now I’ll introduce **Blend If**, which is in the Layer Style dialog. The quickest way to open Layer Style is to double-click the empty area beside a layer’s name. The dialog also contains blend modes, opacity, fill opacity and other advanced options.

## Blend If with the underlying layer

Anchor: 1343 · U31 · L48 · 01:04–04:33

1343 · U31 · L48 · 01:04–04:33

Blend If is divided into **This Layer** and **Underlying Layer**. I still find the names a little confusing, so I’ll explain them with two color bands: a solid orange strip and a gradient strip. The solid orange strip is selected. First, look at **Underlying Layer**. Its sliders run from 0 to 255; whenever you see that scale, it refers to the tonal range.

Moving a slider removes visibility of the current layer at the tones you specify. Pulling the black end in makes the selected orange layer disappear from the blacks and dark grays. At one setting it is no longer visible from 0 to 45. Pulling the slider toward the middle removes it around the midtones; around 128 is the midpoint. You can also pull in the white end to remove the color from the highlights.

By default, the change has a hard edge. Hold Alt or Option and split a slider to make the transition gradual. For example, if the black side is set to 30, the layer is invisible from 0 to 30, then gradually becomes solid between 30 and 128, from dark gray toward mid-gray. That is Blend If with the underlying layer.

The name can suggest that you are changing the layer underneath, but you are still changing the current layer. The result is based on the tones of the underlying layer. In the band example, splitting the black slider creates a smooth transition instead of an abrupt disappearance.

![1343 · U31 · L48 · 01:34](frames/U31L48-F0134.00.jpg)

On screen: "Blend If: Gray" / "This Layer: 0 255" / "Underlying Layer: 0 255" [rest omitted]  
Shows: A solid orange strip and an orange-to-black gradient over a grayscale band, with the Layer Style dialog open.

![1343 · U31 · L48 · 04:03](frames/U31L48-F0403.00.jpg)

On screen: "This Layer: 0 255" / "Underlying Layer: 30 / 128 / 200 / 255" [rest omitted]  
Shows: The orange strip fades at both ends of the grayscale band, with both ends of the underlying-layer slider split.

## This Layer and a practical use

Anchor: 1343 · U31 · L48 · 04:33–07:04

1343 · U31 · L48 · 04:33–07:04

Reset the settings and choose **This Layer**. It refers to the tonal range within the current layer. With a solid color, moving this slider does little until it reaches the color’s tone; then the color disappears. Splitting the slider only makes that solid color partly transparent. The gradient makes the effect easier to see: moving the slider removes its darkest tones, and splitting it creates a gradual transition. Because the gradient is not solid white, it does not disappear all at once; pulling the slider toward the middle also makes it disappear from the light end. With **Underlying Layer**, the gradient is removed according to the tones underneath it, as in the earlier example.

This is useful when you add color to an image but do not want the whites to take on that color. For example, if you want only the midtones colored while leaving highlights or shadows alone, use the Blend If sliders to control which tones receive the color. I’ll now use the image called *Sunflare* to show this with an actual photograph.

![1343 · U31 · L48 · 05:57](frames/U31L48-F0557.00.jpg)

On screen: "This Layer: 28 115" / "Underlying Layer: 0 255" [rest omitted]  
Shows: The darkest part of the gradient layer fading out through a split This Layer slider.

![1343 · U31 · L48 · 06:27](frames/U31L48-F0627.00.jpg)

On screen: "Underlying Layer: 71 255" [rest omitted]  
Shows: The gradient layer fading according to the underlying grayscale tones.

## Warming the family photograph

Anchor: 1343 · U31 · L48 · 07:04–08:52

1343 · U31 · L48 · 07:04–08:52

We’ll look at how to create sun flares. Some people really like them; others do everything to avoid them. You may or may not like the effect, but we’ll do some coloring here too. There are many ways to color an image; I’ll show a few. A Photo Filter gives us a warming filter by default. The earlier solid orange strip was orange so that you could relate it to this example. The filter warms the family photograph, although the effect is subtle at first. Increase its density for a stronger result. In the before-and-after, the little girl’s dress changes color, and the shadows also take on the warmth.

![1343 · U31 · L48 · 08:24](frames/U31L48-F0824.00.jpg)

On screen: "Photo Filter" / "Warming Filter (85)" / "Density: 70%" / "Preserve Luminosity" [rest omitted]  
Shows: A family walking at sunset with a warming Photo Filter applied.

## Restricting the filter color to selected tones

Anchor: 1343 · U31 · L48 · 08:52–11:20

1343 · U31 · L48 · 08:52–11:20

To remove some of the Photo Filter from part of the tonal range, open Blend If again. Set the sliders to exclude the shadows and highlights. The result looks strange at first because there are no transitions, just as with the earlier gradient example. Adobe does not make the way to split the sliders obvious: hold Alt or Option to split them. Move the dialog so you can see the highlights in the sky, then split that end to make a softer transition. Split the shadow slider as well. You can exaggerate the change by moving the split points farther.

Before and after, the difference is subtle, but it is visible in the darker shadows. With the split points adjusted, the original color remains in the shadows while the filter affects most of the tonal range. Clicking OK applies the change. The coloring remains through most tones; it has been removed from the highlights and shadows. A Photo Filter is one way to color an image. I’ll delete it before showing another method.

![1343 · U31 · L48 · 10:49](frames/U31L48-F1049.00.jpg)

On screen: "Underlying Layer: 51 / 83 / 142 / 204" [rest omitted]  
Shows: The family photograph with the Layer Style dialog open and split underlying-layer sliders for shadows and highlights.

## Matching color from another photograph

Anchor: 1343 · U31 · L48 · 11:20–13:31

1343 · U31 · L48 · 11:20–13:31

![1343 · U31 · L48 · 11:30](frames/U31L48-F1130.00.jpg)

On screen: "Sunset.jpg @ 25% (RGB/8) *" [rest omitted]  
Shows: The separate sunset photograph, including its dark strip along the bottom.

![1343 · U31 · L48 · 11:37](frames/U31L48-F1137.00.jpg)

On screen: [none]  
Shows: The family photograph after the Photo Filter layer has been removed.

I have not shown the sunset source image yet. To copy its color into the family photograph, first crop the bottom of the source image: we do not want to copy its blacks. Use the Crop tool to remove that part.

![1343 · U31 · L48 · 11:55](frames/U31L48-F1155.00.jpg)

On screen: [none]  
Shows: The crop boundary excludes the dark strip along the bottom of the sunset source image.

Return to the family photograph and duplicate the Background with Command-J on Mac or Control-J on Windows. Call the duplicate **Colouring**.

There are a couple of different ways to copy the color from another image. One is **Image > Adjustments > Match Color**. This dialog does not work with Smart Objects: if you convert a layer to a Smart Object, you cannot use Match Color. I do not know why. The source control is at the bottom of the dialog; I think it would make more sense at the top, but choose the sunset image there. Photoshop copies its coloring into the family photograph. You can then edit the values above. **Fade** works a little like opacity.

![1343 · U31 · L48 · 12:45](frames/U31L48-F1245.00.jpg)

On screen: "Match Color" / "Destination Image" / "Target: Sun flare.jpg (Colouring, RGB/8)" / "Source: None" / "Layer: Colouring" [rest omitted]  
Shows: The family photograph in the Match Color dialog before the sunset source is selected.

![1343 · U31 · L48 · 13:16](frames/U31L48-F1316.00.jpg)

On screen: "Image Options" / "Luminance 100" / "Color Intensity 66" / "Fade 0" / "Source: Sunset.jpg" / "Layer: Background" [rest omitted]  
Shows: The sunset source selected in Match Color and its warm color transferred to the family photograph.
