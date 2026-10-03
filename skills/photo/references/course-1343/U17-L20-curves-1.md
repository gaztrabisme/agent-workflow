# Lesson 20 · Curves 1

Anchor: 1343 · U17 · L20 · 13:04 · https://www.domestika.org/en/courses/1971-course-2-retouching-fundamentals/units/6423-curves#course_lesson_19379

## Curves as a visual language

Anchor: 1343 · U17 · L20 · 00:00–01:38

I’m going to teach you probably the most important tool in Photoshop: Curves. We use it for many things, primarily brightness, contrast, and colour. When I first started using Curves, I thought it was a rubbish tool because it seemed to ruin the quality of my images. That was because I did not understand it properly. It is important to understand what the curve does and how it affects the tonal range.

I have prepared screenshots of the curve to show the basic adjustments and what they do. Curves is almost like a language: you should be able to look at a curve and understand what it will do to the image, rather than switching it on and off to compare before and after. Once you can read the curve, you will be able to do much more. That is why I want to begin with screenshots of the curves instead of first showing their effect on an image.

![1343 · U17 · L20 · 00:58](frames/U17L20-F0058.00.jpg)

On screen: "Curves" / "Preset: Default" / "RGB" / "Input:" / "Output:" [rest omitted]  
Shows: Photoshop’s Curves properties panel with the default straight line and no added points.

## Reading tones and changing brightness

Anchor: 1343 · U17 · L20 · 01:39–02:54

In the first screenshot, the curve is at its default, with no points on it. We add points to change the curve’s shape. The scale along the left and bottom runs from black at the bottom left to white at the top right. If you follow a point on the curve to the left or down, you can identify the tone it represents. The middle represents the midtones.

If you put a point in the middle and pull it up, the image becomes brighter. In this example, the curve is above the original line, so it brightens the whole tonal range. If you do the opposite and pull a middle point down, it darkens the whole tonal range.

![1343 · U17 · L20 · 02:28](frames/U17L20-F0228.00.jpg)

On screen: "Brighter" / "Input: 100" / "Output: 154" [rest omitted]  
Shows: A middle point lifted above the original diagonal curve.

![1343 · U17 · L20 · 02:48](frames/U17L20-F0248.00.jpg)

On screen: "Darker" / "Input: 159" / "Output: 106" [rest omitted]  
Shows: A point lowered below the original diagonal curve.

## Using Curves for contrast

Anchor: 1343 · U17 · L20 · 02:55–04:41

Contrast is the difference between the brightest and darkest tones. Increasing contrast makes bright tones brighter and dark tones darker. In the curve shown here, the upper point brightens the tonal range because it is above the original line. The lower point darkens the range because it is below the line.

I would always choose Curves for contrast because it offers more control than the basic Brightness/Contrast tool. Brightness/Contrast is a good, simple way to increase contrast, but Curves is better when you need something more specific: in Curves, you can control highlights and shadows independently. If applying contrast makes the highlights too bright, you can pull that point back. With a basic tool, you would have to reduce the overall effect. You can also add another point lower on the curve to make the blacks even darker.

![1343 · U17 · L20 · 02:58](frames/U17L20-F0258.00.jpg)

On screen: "Contrast" / "Input: 87" / "Output: 66" [rest omitted]  
Shows: An S-shaped curve with one point above and another below the original line.

## Adjusting colour channels

Anchor: 1343 · U17 · L20 · 04:42–05:41

Curves can also change colour. In this example I have selected the red channel. By default, RGB combines red, green, and blue; together they determine luminosity, or brightness. Selecting an individual colour channel lets you change the colours in the image.

To add a colour, you would typically put a point in the middle of the curve and pull it up. In the red channel, that adds red. Because Photoshop works with light, adding a colour also adds brightness, so sometimes you need to compensate in the RGB channel. Removing red can be thought of as adding cyan; reducing the amount of red light also darkens the image.

![1343 · U17 · L20 · 04:58](frames/U17L20-F0458.00.jpg)

On screen: "Red" / "Red + Brighten" / "Input: 99" / "Output: 153" [rest omitted]  
Shows: The red-channel curve raised above its original line.

![1343 · U17 · L20 · 05:28](frames/U17L20-F0528.00.jpg)

On screen: "Red" / "Cyan + Darken" / "Input: 162" / "Output: 108" [rest omitted]  
Shows: The red-channel curve lowered below its original line.

## Choosing an image and adding a Curves layer

Anchor: 1343 · U17 · L20 · 05:42–07:43

Now let’s apply this to an image. I came across this stock photograph. Stock images are already finished images: their brightness and colours have been created or corrected before they are uploaded. Brightness and colour are subjective and can be artistic choices. The photographer considered this image finished, but I would personally change its colours and contrast, and perhaps adjust its brightness slightly.

I have previously shown how to add an adjustment layer from Layer > New Adjustment Layer > Curves. Here is another, quicker method that I prefer: click the black-and-white circle at the bottom of the Layers panel. It opens the adjustment layers and fill layers; choose Curves.

Technically, the adjustments can be made in any order. For the workflow, I recommend starting with brightness. Until brightness is right, you will not see the true colours. Until brightness and colour are right, you will not see the true contrast. Doing them in a different order may mean returning to earlier adjustments later.

![1343 · U17 · L20 · 06:18](frames/U17L20-F0618.00.jpg)

On screen: [none]  
Shows: The original stock photograph of red planes flying above a forested landscape.

![1343 · U17 · L20 · 06:49](frames/U17L20-F0649.00.jpg)

On screen: "Layer" / "New Adjustment Layer" / "Curves..." [rest omitted]  
Shows: Photoshop’s Layer menu open to the Curves adjustment-layer command.

## Setting brightness first

Anchor: 1343 · U17 · L20 · 07:44–09:06

I rename this layer Brightness. If you are new to Curves, call it Brightness Curve so it is clear that it is a curve. The layer thumbnail may show a curve icon, but that depends on its size: with medium thumbnails, as I have here, the icon is usually visible; with smaller thumbnails, you may see only the small circle that identifies an adjustment layer.

For brightness, I usually add one point in the middle and pull it up to brighten or down to darken. I prefer this image slightly darker. I’ll zoom in on the preview: the adjustment is small, but it still affects the image. To compare before and after, toggle the visibility using the eye icon; clicking the eye here does the same thing as clicking the one in the Layers panel.

![1343 · U17 · L20 · 08:40](frames/U17L20-F0840.00.jpg)

On screen: "Brightness Curve" / "Input: 134" / "Output: 127" [rest omitted]  
Shows: The plane photograph with a slight darkening curve on the Brightness Curve layer.

## Warming the image with a colour curve

Anchor: 1343 · U17 · L20 · 09:07–10:06

After brightness, I add another curve for colour and rename it Colour Curve. The default channel is RGB; to edit colour, switch to an individual channel. I choose Blue because I want to remove some blue from the picture. I add a point in the middle and pull it down. Removing blue makes the image more yellow. I compare before and after, and I think it looks a little better.

![1343 · U17 · L20 · 09:56](frames/U17L20-F0956.00.jpg)

On screen: "Blue" / "Input: 135" / "Output: 123" [rest omitted]  
Shows: The plane photograph with the Blue channel lowered on the Colour Curve layer.

## Shaping highlights and shadows for contrast

Anchor: 1343 · U17 · L20 · 10:07–12:04

Next I add a curve for contrast. I’ll show a useful shortcut. As far as I know, it works only on a Mac: hold Option, the equivalent of Alt on Windows, and click the black-and-white circle. Who knows, Adobe may update this soon; it is a very useful shortcut. When I choose Curves, a dialogue appears with the default name already selected, so I can type Contrast Curve instead of double-clicking the title.

To adjust contrast, I usually add one point in the highlights and pull it up. At this stage, the whole curve is above the original line, so I have only brightened the image. I then add a point in the shadows and pull it down below the line. The upper section is now brightening and the lower section darkening; together, that gives us contrast. I toggle the preview to compare before and after.

Another useful shortcut is to Option-click the eye beside the background layer. This shows only that layer, giving a quick comparison between the original and the image with all adjustments.

![1343 · U17 · L20 · 10:48](frames/U17L20-F1048.00.jpg)

On screen: "New Layer" / "Name:" / "Curves 1" / "OK" / "Cancel" [rest omitted]  
Shows: The New Layer dialogue with the default name, Curves 1, selected for the new adjustment layer.

![1343 · U17 · L20 · 11:18](frames/U17L20-F1118.00.jpg)

On screen: "Contrast Curve" / "Input: 179" / "Output: 191" [rest omitted]  
Shows: The plane photograph with the contrast curve and its histogram enlarged in an inset.

## Reviewing and refining the adjustments

Anchor: 1343 · U17 · L20 · 12:05–13:04

Looking at the original and adjusted image, I now find it slightly green. This can happen during editing: after adding a couple of adjustments, you may start to notice something you did not see earlier. Naming the layers makes it easy to return to the right adjustment. To edit the colour, rather than adding another adjustment layer, I return to the Colour Curve and select the Green channel to reduce some of the green.

![1343 · U17 · L20 · 12:15](frames/U17L20-F1215.00.jpg)

On screen: "Input: 75" / "Output: 67" [rest omitted]  
Shows: The plane photograph and the contrast curve while the background layer’s visibility control is used for comparison.

![1343 · U17 · L20 · 12:55](frames/U17L20-F1255.00.jpg)

On screen: "Green" / "Input: 110" / "Output: 141" [rest omitted]  
Shows: The plane photograph with the Green channel selected and the Brightness Curve, Colour Curve, and Contrast Curve layers visible.
