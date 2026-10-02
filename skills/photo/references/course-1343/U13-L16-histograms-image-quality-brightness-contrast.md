# Lesson 16 · Histograms & Image Quality, Brightness & Contrast

Anchor: 1343 · U13 · L16 · 12:43 · https://www.domestika.org/en/courses/1971-course-2-retouching-fundamentals/units/6057-histograms-image-quality-brightness-contrast#course_lesson_18304

## Set up the histogram to read tonal range

Anchor: 1343 · U13 · L16 · 00:00–01:55

In this course, I’m going to teach you the fundamentals of retouching. There is a lot to cover, so we’ll start with one of the most important subjects: the histogram and image quality. We’ll also learn about brightness and contrast and understand how to use them properly in your editing. Let me show you.

Before making adjustments to an image, take a closer look at the histogram and consider what makes a good exposure. By default, Photoshop shows the colors in the histogram. In this lake-and-mountain image, blue is by far the brightest color. Color information can sometimes be useful to read, but for now we can simplify the display and use an RGB composite, which shows the tonal range. Open the options in the Histogram panel and choose the expanded view. Photoshop displays the colors; changing the channel to RGB gives a composite of all the colors, which is easier to work with in most cases. There are quite a lot of numbers below the graph, and we do not need them for this explanation. After changing the value and setting the channel to RGB, we can return to the compact view. If you prefer a slightly larger histogram, keep the expanded view.

![1343 · U13 · L16 · 01:11](frames/U13L16-F0111.00.jpg)

On screen: "Lake Garda, Italy.tif @ 100% (RGB/16#)" / "Bonnie on the beach.tif @ 100% (RGB/16#)" / "Joanie and car boot.tif @ 100% (RGB/16#)" / "Luca in the woods.tif @ 100% (RGB/16#)" / "colour&brightness.sif @ 69.8% (RGB/8#)" / "Histogram" / "Navigator" [rest omitted]  
Shows: The lake, mountains, and water beside overlapping red, green, and blue histogram peaks.

![1343 · U13 · L16 · 01:36](frames/U13L16-F0136.00.jpg)

On screen: "Source: Entire Image" / "Mean: 143.11" / "Std Dev: 44.17" / "Median: 145" / "Pixels: 6096000" / "Level:" / "Count:" / "Percentile:" / "Cache Level: 1" [rest omitted]  
Shows: The lake photo beside a white composite histogram and an enlarged histogram data readout.

## A middle-heavy histogram can still be correctly exposed

Anchor: 1343 · U13 · L16 · 01:55–02:59

Most tutorials I have seen say that a histogram should peak in the middle when an image is correctly exposed. Unfortunately, that is not true in general. It is true only when the image is dominated by mid-tones, as this particular image is. Its histogram is almost empty on the left and on the right. That means the image has no pure white and no pure black, or any dark shadows for that matter. It does not mean the exposure is bad: I would call this the correct exposure. The image has no blacks because it was a humid day, and the only shadows are in the distance, where they become slightly faded.

![1343 · U13 · L16 · 02:27](frames/U13L16-F0227.00.jpg)

On screen: [rest omitted]  
Shows: The lake-and-mountain photo beside a white histogram with a broad mid-tone spread and little at either end.

## Read a bright image and check the highlight edge

Anchor: 1343 · U13 · L16 · 02:59–03:57

Now consider another image. Most of its tones are on the right-hand side of the histogram, where the bright tones are. The taller the graph is, the more of that particular tone it represents (the captions read “time”). By default, an exclamation mark indicates that Photoshop has not generated the true histogram from the entire image. To save processing power, it usually calculates the histogram from a thumbnail version. Click the small triangle to generate the histogram from the entire image. This image is correctly exposed even though most of its tones are in the highlights.

![1343 · U13 · L16 · 03:40](frames/U13L16-F0340.00.jpg)

On screen: [rest omitted]  
Shows: A woman standing at the water’s edge, seen from behind, beside a histogram concentrated toward the bright end.

## A dark background can dominate the histogram

Anchor: 1343 · U13 · L16 · 03:57–05:16

Here is another image, with a wide spread of tones. Its histogram has a tall peak on the left, and the image shows why: the background is very dark; it is the boot of a car, so this dominant tone makes the peak very tall. The tones also spread toward the right-hand side. I’ll click the triangle to see the true histogram; it does not change very much. Notice the small gap between the histogram and its right edge. That means the image has captured all the tones in the highlights. This matters when taking pictures as well as when working in Photoshop. When you take a picture, you can analyze the histogram to see whether you captured the tones. In particular, check the right-hand side to make sure you have kept detail in the highlights.

![1343 · U13 · L16 · 04:31](frames/U13L16-F0431.00.jpg)

On screen: [rest omitted]  
Shows: A red-haired child against a dark car interior, with the histogram showing a tall shadow peak and a smaller spread toward the highlights.

## Use a selection to inspect a small part of an image

Anchor: 1343 · U13 · L16 · 05:16–06:44

Here is one more example: an image dominated by dark tones. Its histogram is primarily on the left-hand side, and at first it seems to show nothing in the highlights, even though the exposure is quite good. The bright tones occupy such a small portion of the image that they barely appear in the full-image histogram.

Photoshop can show the histogram for just part of an image. If you crop the image or make a selection, the histogram updates to show that area. To check the boy’s face, draw a small box with the Rectangular Marquee tool. The histogram now shows many tones in that selection. A histogram can be a little misleading when very bright or very dark tones occupy only a small part of the image. Deselect with Command-D on a Mac or Control-D on Windows.

![1343 · U13 · L16 · 05:31](frames/U13L16-F0531.00.jpg)

On screen: [rest omitted]  
Shows: A boy riding a bicycle on a wooded path beside a histogram with most of its area toward the shadows.

![1343 · U13 · L16 · 06:20](frames/U13L16-F0620.00.jpg)

On screen: "W: 78 px" / "H: 139 px" [rest omitted]  
Shows: A rectangular selection around the cyclist’s face, with a magnified view of the selection and its dimensions.

![1343 · U13 · L16 · 06:40](frames/U13L16-F0640.00.jpg)

On screen: "Histogram" / "Navigator" [rest omitted]  
Shows: The wooded path and cyclist beside a histogram with a broad spread of tones.

## Set a target before adjusting the tonal range

Anchor: 1343 · U13 · L16 · 06:44–08:10

Now I want to show how to edit brightness and contrast with the histogram as a guide, rather than judging only by looking at the image. This is a more scientific way to work and aims to make the adjustment correctly rather than treating it as a creative choice. The histogram here is quite short at both the highlights and the shadows.

Highlights do not necessarily have to reach the far right of a histogram. A bright color in an image does not always have to become pure white or bleached-out white. A light source, a reflection of a light source, or the sun will always bleach out; there is nothing we can do about that. If the image has no such light source, as this one does not, the histogram should typically end just before the edge.

![1343 · U13 · L16 · 07:16](frames/U13L16-F0716.00.jpg)

On screen: [rest omitted]  
Shows: A green-tinted portrait of a young man centered on the Photoshop canvas.

## Make a working copy and enable the legacy dialog

Anchor: 1343 · U13 · L16 · 08:10–09:23

As we continue through the course, we will start using adjustment layers, but I do not want to confuse you with complex adjustments yet. We will use the simplest way of working: make a copy of the Background layer, apply image adjustments to that copy, and use the basic tools. Duplicate the Background with Command-J on a Mac or Control-J on Windows, then rename the new layer “Adjustments.” Go to Image > Adjustments > Brightness/Contrast.

Brightness/Contrast used to let you push an image very far. I liked the old tool because it helped you properly understand what brightness and contrast meant, and that is what I want to show here. To use the old version, check “Use Legacy.” Do that now. Normally we would not use the legacy version, but I want you to use it so you can properly understand brightness and contrast.

![1343 · U13 · L16 · 09:22](frames/U13L16-F0922.00.jpg)

On screen: "Brightness/Contrast" / "Brightness: 0" / "Contrast: 0" / "Use Legacy" / "Adjustments" / "Background" [rest omitted]  
Shows: The Brightness/Contrast dialog with Use Legacy checked over the portrait; the Adjustments copy sits above Background in the Layers panel.

## Brightness moves the histogram

Anchor: 1343 · U13 · L16 · 09:23–10:30

As you make adjustments, watch the histogram. If you move the brightness slider to the right, the histogram moves to the right. If you reduce brightness, the histogram moves to the left. Understanding what a histogram should look like gives you a target before you start adjusting.

For this image, there is probably a black, or at least a very near-black, and we want the histogram to come almost all the way over to the right-hand side. As I change the brightness, I change the histogram’s position. I shift it with the brightness slider until it is roughly centered, which is a good starting point.

![1343 · U13 · L16 · 10:21](frames/U13L16-F1021.00.jpg)

On screen: "Brightness/Contrast" / "Brightness: -20" / "Contrast: 0" / "Use Legacy" / "Histogram" / "Navigator" [rest omitted]  
Shows: The portrait with the Brightness/Contrast dialog set to brightness -20 and contrast 0, beside the histogram.

## Contrast expands or compresses the tonal range

Anchor: 1343 · U13 · L16 · 10:30–12:43

Next I use the contrast slider. As you can see, the contrast slider (the captions read “Contra”) either expands or compresses the histogram. I combine contrast and brightness to shift the histogram. I am not even looking at the image while I do this; I am adjusting the sliders with the histogram as my guide. I tweak brightness and increase contrast a little, then move it down.

![1343 · U13 · L16 · 10:42](frames/U13L16-F1042.00.jpg)

On screen: "Brightness: -30" / "Contrast: -25" [rest omitted]  
Shows: The portrait under a low-contrast brightness adjustment, with the two slider values shown in the dialog.

![1343 · U13 · L16 · 10:54](frames/U13L16-F1054.00.jpg)

On screen: "Brightness: -23" / "Contrast: 43" [rest omitted]  
Shows: The portrait under a stronger contrast adjustment, with the histogram spread wider and the slider values visible.

Remember, we want the histogram to start very close to the edge, but we do not want it stuck on the edge. We also want to keep a gap on the right-hand side because the whites or highlights in this image should not be bleached-out white. I increase contrast slightly. Now the histogram starts on the left-hand side and finishes close to the edge. That is the kind of range we are looking for when editing the image’s tones. Here I am using Brightness/Contrast, but other tools can make similar adjustments.

![1343 · U13 · L16 · 11:50](frames/U13L16-F1150.00.jpg)

On screen: "Brightness: -24" / "Contrast: 49" [rest omitted]  
Shows: The portrait with the final brightness and contrast values and a broad histogram that stops short of the right edge.

Click OK to apply the adjustment. In the Layers panel, toggle the Adjustments layer off and on to compare the before and after. The histogram now has a much better spread than the original. I hope you have a better understanding of the histogram and how to work with brightness and contrast in your images. In the next lesson, you will learn how to balance colors in your images and do some creative coloring.

![1343 · U13 · L16 · 12:07](frames/U13L16-F1207.00.jpg)

On screen: [rest omitted]  
Shows: The adjusted portrait with the Adjustments layer visible above Background in the Layers panel.
