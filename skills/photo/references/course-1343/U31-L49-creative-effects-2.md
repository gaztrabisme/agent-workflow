# Lesson 49 · Creative Effects 2

Anchor: 1343 · U31 · L49 · 16:49 · https://www.domestika.org/en/courses/1972-course-3-retouching-environmental-images/units/6449-creative-effects#course_lesson_19497

## Reviewing Match Color and copying a color layer

Anchor: 1343 · U31 · L49 · 00:00–01:30

1343 · U31 · L49 · 00:00–01:30

Here is the family photograph before and after using Match Color to copy its color from another image. I do not tend to use Match Color because it is destructive and a little basic for my taste, so I’ll show another method. Cancel the dialog and go to the sunset image. You can drag a layer to the other image’s tab, as in earlier lessons, or right-click the empty area of the layer and choose **Duplicate Layer**. Name it **Sunset colouring**, choose **Sun flare** as the destination document and click OK. The copied layer now appears in the family photograph.

![1343 · U31 · L49 · 00:21](frames/U31L49-F0021.00.jpg)

On screen: "Match Color" / "Destination Image" / "Target: Sun flare.jpg (Colouring, RGB/8)" / "Image Options" / "Luminance 78" / "Color Intensity 56" / "Fade 48" / "Preview" / "Neutralize" / "Source: Sunset.jpg" / "Layer: Background" [rest omitted]  
Shows: The family photograph with the Match Color result and its source settings.

![1343 · U31 · L49 · 00:56](frames/U31L49-F0056.00.jpg)

On screen: "Sunset.jpg @ 25% (RGB/8)" [rest omitted]  
Shows: The separate vertical photograph of orange and blue sunset clouds.

## Blending and blurring the sunset color

Anchor: 1343 · U31 · L49 · 01:30–04:49

1343 · U31 · L49 · 01:30–04:49

Set the copied sunset layer to **Soft Light**, probably the most common way to blend color into an image. The cloud shapes remain visible through the layer, so blur it. First return to Normal so you can see what you are doing. Choose **Filter > Blur > Gaussian Blur**, then find a radius that blends the colors very smoothly. You should still see differences in lightness and darkness and perhaps a hint of blue. Increase the value a little if needed, then click OK. Soft Light now gives a much smoother result.

There is another option. Return in History to before changing the blend mode, then choose **Filter > Blur > Average**. Photoshop finds the average color of the layer, which you can use as the coloring. Compare before and after. If you like the colors, warmth or coolness in an image, crop it to focus on those particular colors, apply a heavy Gaussian Blur, use Average, and set the result to Soft Light. That can give you interesting results.

![1343 · U31 · L49 · 02:24](frames/U31L49-F0224.00.jpg)

On screen: "Gaussian Blur" / "Radius: 117.8 Pixels" / "Preview" [rest omitted]  
Shows: The sunset image blurred into a smooth field of warm and cool colors.

![1343 · U31 · L49 · 03:35](frames/U31L49-F0335.00.jpg)

On screen: "Filter" / "Blur" / "Average" / "Sunset colouring" [rest omitted]  
Shows: The family-photo document with the copied sunset-color layer active and Filter > Blur > Average highlighted.

![1343 · U31 · L49 · 03:40](frames/U31L49-F0340.00.jpg)

On screen: [none]  
Shows: The average-color result as a flat warm brown layer.

![1343 · U31 · L49 · 04:10](frames/U31L49-F0410.00.jpg)

On screen: "Soft Light" [rest omitted]  
Shows: The flat sunset color blended over the family photograph in Soft Light.

## Creating a composite layer for the flare

Anchor: 1343 · U31 · L49 · 04:49–06:42

1343 · U31 · L49 · 04:49–06:42

Now I’ll add a sun flare. Some people like sun flares and some try to avoid them, but it is still useful to know how to make one, in case someone you work for wants it in a picture.

Before adding the flare, create a composite layer containing all the current layers. It is like flattening the image, except the flattened result is placed on a separate layer above the others. You can still return to the original layers underneath. There is no menu command for this, so use **Shift-Option-Command-E** on Mac or **Shift-Alt-Control-E** on Windows. The new composite is a combination of the three layers. Turning off the layers underneath makes no difference while the composite remains visible.

I strongly suggest converting a layer to a Smart Object before applying filters. This keeps the filters editable so you can change them later. Rename the composite **Sun flare**, right-click beside the layer name and choose **Convert to Smart Object**. You can also choose **Convert for Smart Filters** in the Filter menu; those two commands do the same thing.

![1343 · U31 · L49 · 05:40](frames/U31L49-F0540.00.jpg)

On screen: "Layer 1" [rest omitted]  
Shows: The composite family photograph on a new top layer above the sunset-color and original image layers.

## Positioning and applying Lens Flare

Anchor: 1343 · U31 · L49 · 06:42–08:15

1343 · U31 · L49 · 06:42–08:15

To add the flare, choose **Render > Lens Flare**. By default it uses a zoom lens, brightness at 100%, and places the flare near the middle of the image. Move it to the sun, then compare the lens choices: 35mm Prime, 105mm Prime, Movie Prime and 50–300mm Zoom. They look fairly similar. I’ll choose 50–300mm Zoom and leave the brightness as it is. Click OK to apply it.

![1343 · U31 · L49 · 07:31](frames/U31L49-F0731.00.jpg)

On screen: "Lens Flare" / "Brightness: 100%" / "Lens Type" / "50-300mm Zoom" / "35mm Prime" / "105mm Prime" / "Movie Prime" [rest omitted]  
Shows: The Lens Flare dialog over the family photograph, with 50–300mm Zoom selected.

## Masking the unwanted flare

Anchor: 1343 · U31 · L49 · 08:15–09:49

1343 · U31 · L49 · 08:15–09:49

I like the little rays of light above the sun, but not the flare artifacts lower in the image. You could use the Clone Stamp to remove them, but I prefer the simpler approach of using a mask. Add a gradient to the Smart Filters mask. Click the mask, choose the Gradient tool with **G**, and make sure it runs from foreground to background. Press **D** for the default colors, then make black the foreground color; press **X** to swap the colors if needed.

Put the cursor where you want the flares removed. To remove them at the bottom and reveal them gradually above, start near the bottom and drag upward, at a slight angle. The gradient is now applied to the filter mask. Move it slightly higher if you want to remove a little more. Compare before and after.

![1343 · U31 · L49 · 08:21](frames/U31L49-F0821.00.jpg)

On screen: "Sun flare" / "Smart Filters" / "Lens Flare" [rest omitted]  
Shows: The applied lens flare over the family photograph, with a large circle and smaller flare artifacts near the bottom.

![1343 · U31 · L49 · 09:05](frames/U31L49-F0905.00.jpg)

On screen: "Filter Mask" / "Density: 100%" / "Feather: 0.0 px" / "Color Range…" / "Invert" [rest omitted]  
Shows: The flare remains near the sun while the selected Smart Filters mask controls are open.

## Adding contrast and darkening the image

Anchor: 1343 · U31 · L49 · 09:49–11:12

1343 · U31 · L49 · 09:49–11:12

To bring the image together, add a little contrast and darken it slightly. Add a Curves adjustment and name it **Contrast**. I do not want to make the highlights much brighter while darkening the whole image. The tonal range here is a little wishy-washy, so use the target tool to choose the tone to darken. Click the back of the man’s shirt or his trousers and pull that tone down. Then deepen the blacks by pulling the bottom point down ever so slightly. Compare before and after.

![1343 · U31 · L49 · 11:10](frames/U31L49-F1110.00.jpg)

On screen: "Curves" / "Preset: Custom" / "RGB" / "Input: 55" / "Output: 43" / "Contrast" [rest omitted]  
Shows: The family photograph with a Curves adjustment lowered to darken a sampled midtone.

## Shaping a vignette around the sunlight

Anchor: 1343 · U31 · L49 · 11:12–14:45

1343 · U31 · L49 · 11:12–14:45

Finally, add a vignette. It does not have to be a perfect oval around the center; shape it to mimic the light from the sun. Choose the Lasso or Polygonal Lasso tool. Start up at the sun, bring the line down and slightly outside the image, then continue around and return to the starting point. Double-click to find and close the starting point; moving around until the closing symbol appears can be frustrating.

![1343 · U31 · L49 · 12:18](frames/U31L49-F1218.00.jpg)

On screen: "Feather: 0 px" / "Anti-alias" / "Select and Mask…" [rest omitted]  
Shows: A lasso outline beginning near the sun and enclosing an irregular area across the family photograph.

The selection should not be hard-edged, so open **Select and Mask**. For a darkening effect, use the **On Black** preview; for a brightening effect, use **On White**. I typically use Overlay, but this selection is for darkening, so use On Black. Feather it heavily, around 200 or 300 pixels, to mimic the light coming from the sun.

![1343 · U31 · L49 · 13:14](frames/U31L49-F1314.00.jpg)

On screen: "Feather: 281.9 px" / "Contrast: 0%" / "Invert" [rest omitted]  
Shows: The irregular selection previewed on black with a broad feather around the central family.

I have selected the opposite of what I want. It is often easier to select the center than the outside, but you can invert the selection here or invert the layer mask later. That is a common mistake; I make it all the time. After creating a Curves adjustment, darken it slightly. You can invert the mask in its Properties panel, return to Select and Mask to edit it further, and add another 100 pixels of feather if you want.

## Refining the vignette and checking the original

Anchor: 1343 · U31 · L49 · 14:45–16:49

1343 · U31 · L49 · 14:45–16:49

Mask density confuses many people, so I’ll show the mask itself: hold Alt or Option and click its thumbnail. Reducing density makes what was black become gray, reducing the effect’s opacity in that part of the mask. For example, at 50% density, a black area becomes mid-gray and gives a 50% effect.

![1343 · U31 · L49 · 15:10](frames/U31L49-F1510.00.jpg)

On screen: "Density: 52%" [rest omitted]  
Shows: The layer mask fills the canvas in grayscale with Density set to 52%.

That is useful if you like the effect but want some of it in the center; you can reduce the density instead of redoing the selection or adding another adjustment layer. At 50%, the center is darkened by half as much as the outside.

I would not normally go as far as 50% here. At a density of 85%, 15% of the effect reaches the center of the image. Finally, compare with the original: Option-click the Background layer’s eye on Mac, or Alt-click it on Windows, for a quick view of the beginning.

![1343 · U31 · L49 · 16:30](frames/U31L49-F1630.00.jpg)

On screen: [none]  
Shows: The original family photograph with the Background layer visible and the edited layers hidden.

The vignette follows the sun rather than forming a regular oval. That is how to add creative effects to an image. In the next lesson, I’ll show how to make panoramic images.

![1343 · U31 · L49 · 15:47](frames/U31L49-F1547.00.jpg)

On screen: "Layer Mask" / "Density: 50%" / "Feather: 112.4 px" [rest omitted]  
Shows: The adjusted vignette with the layer-mask density set to 50%.

![1343 · U31 · L49 · 16:05](frames/U31L49-F1605.00.jpg)

On screen: "Density: 85%" [rest omitted]  
Shows: The family photograph with the mask density reduced to 85%.

![1343 · U31 · L49 · 16:33](frames/U31L49-F1633.00.jpg)

On screen: [none]  
Shows: The finished family photograph with the flare and sun-shaped vignette.
