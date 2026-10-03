# Lesson 19 · Levels

Anchor: 1343 · U16 · L19 · 14:20 · https://www.domestika.org/en/courses/1971-course-2-retouching-fundamentals/units/6422-levels#course_lesson_19378

## Levels and the histogram

Anchor: 1343 · U16 · L19 · 00:11–01:59

In this lesson, I’m going to show you how to work with Levels in Photoshop. We use this tool to set the black and white points and adjust the tonal range of an image. In the previous lesson, we used Brightness and Contrast to edit the tonal range. Now we’re stepping it up a level and adding adjustment layers to the workflow. Choose Layer > New Adjustment Layer > Levels, then click OK.

Levels is dedicated to the histogram and works directly with the image’s tonal range. Its panel displays the histogram; the Histogram panel shows the same information. Move the points to adjust it. The left slider represents the black point and starts at 0. The right slider represents the white point and starts at 255. The middle point is the gamma slider, which starts at 1.0.

![1343 · U16 · L19 · 00:57](frames/U16L19-F0057.00.jpg)

On screen: “Layer” / “New Adjustment Layer” / “Levels...” [rest omitted]  
Shows: The Layer menu and New Adjustment Layer submenu open over the snowy image, with Levels highlighted.

![1343 · U16 · L19 · 01:29](frames/U16L19-F0129.00.jpg)

On screen: “Levels” / “RGB” / “0” / “1.00” / “255” / “Output Levels: 0 / 255” [rest omitted]  
Shows: The Levels panel and histogram beside the snowy landscape, with the black, gamma, white and output values at their defaults.

## Set the white point and correct exposure with gamma

Anchor: 1343 · U16 · L19 · 01:59–05:33

In this snowy image, the black point is already in a good place: the black tones reach the lower-left corner of the histogram, as we want. But the brightest tone is darker than a midtone. The gamma slider is centered at the midtone, and the histogram is nowhere near white. I chose this image to show how incorrectly a camera can expose a scene when everything is white.

To adjust it, move the white point and assign a new white in the image. The original white is slightly darker than a midtone, which is also visible in the histogram. As I move the white-point slider, the image gets brighter and the histogram moves to the right. As in the previous lesson, aim for a small gap at the right. Bring the white point all the way to the right only if the image contains a bleached-out white from a light source or its reflection. This image captured neither, so I leave a gap; this looks like a good setting.

![1343 · U16 · L19 · 03:44](frames/U16L19-F0344.00.jpg)

On screen: “124” [rest omitted]  
Shows: The snowy landscape after the white point has been moved; the Levels input white value is 124, and the histogram has shifted toward the right while retaining a gap.

The gamma slider still reads 1.0 even after the white point has moved. That value describes the relationship between the white and black points: 1.0 places gamma directly between them. To assign more highlights, move gamma to the left. It can seem counterintuitive that dragging toward the darker point makes the image brighter. The reason is that this divides the range into a larger midtone-to-highlight section, giving us more bright tones, and a shorter shadow-to-midtone section. Moving the gamma slider changes its value as well.

![1343 · U16 · L19 · 04:32](frames/U16L19-F0432.00.jpg)

On screen: “1.87” / “124” / “Output Levels: 0 / 255” [rest omitted]  
Shows: The snowy landscape with gamma moved left to 1.87; the histogram has a longer midtone-to-highlight section and a shorter shadow-to-midtone section.

Do not think of this slider as a way to adjust brightness. It is better to think of it as correcting a bad exposure: moving gamma reassigns the image’s midtone. For most adjustments, we do not need to change the midtone, so I restore the default by typing 1 in the box.

## RGB, eyedroppers and output levels

Anchor: 1343 · U16 · L19 · 05:33–08:02

The channel menu is set to RGB. Adjusting red, green and blue together changes what we call luminosity, or the brightness value. You can choose individual channels to make adjustments, but my advice is to leave that alone for now. We’ll use another tool when working with color.

Some people use the eyedroppers to assign a black or white point by clicking something in the image that is meant to be black or white. In my opinion, these tools are destructive and rarely give good results.

![1343 · U16 · L19 · 06:08](frames/U16L19-F0608.00.jpg)

On screen: “Sample in image to set black point (press Opt to display clipping preview)” [rest omitted]  
Shows: The black-point eyedropper selected in the Levels controls, with its tooltip visible beside the three eyedroppers.

For example, choose the white eyedropper and click on part of the snow. Photoshop makes that point pure white. The histogram then shows clipping and is pushed all the way to the right. Undo that command with Command-Z on Mac or Control-Z on Windows.

![1343 · U16 · L19 · 06:38](frames/U16L19-F0638.00.jpg)

On screen: “255” [rest omitted]  
Shows: The snow image after the white eyedropper has been used; the histogram is clipped at the right edge, with an inset over the sampled snow.

The values above the controls are input levels, which directly affect the image. The output levels at the bottom are generally used to communicate with a printer. By default, output black is 0 and output white is 255, so the printer uses the entire tonal range. To limit the range the printer uses, reduce the white point. In printing, white means nothing: a printer does not use white ink; white means revealing the paper. That can leave parts of the print without ink. With a very light image, it can be useful to lower the value even a little, to 252, for example. That forces the printer to put ink down everywhere (captions: *everyone*).

![1343 · U16 · L19 · 07:59](frames/U16L19-F0759.00.jpg)

On screen: “252” [rest omitted]  
Shows: The snow image with the output white level lowered to 252.

## Limit output white for print and web

Anchor: 1343 · U16 · L19 · 08:02–10:28

Here is an image with a very bright white. To illustrate the effect, I add some white canvas around it. Zoom out, open Canvas Size with Option-Command-C on Mac or Alt-Control-C on Windows, check Relative, and add 25% to both the width and height. After clicking OK, the edges are barely visible.

![1343 · U16 · L19 · 08:46](frames/U16L19-F0846.00.jpg)

On screen: “Canvas” / “W 4445 px” / “H 5926 px” [rest omitted]  
Shows: The light forest image after white canvas was added; its pale edge is hard to distinguish from the white extension.

Undo that change and add a Levels adjustment layer through Layer > New Adjustment Layer > Levels. I name the layer “Output Levels” to specify what I am doing, then lower the output white to 250. The before-and-after change is just about visible, but it makes a major difference for a printer: the printer is no longer allowed to leave blank areas and is forced to put ink down everywhere. If this image were placed on a pure-white website, the adjustment would also reveal four corners.

If I extend the canvas now, the Levels adjustment is applied to the added canvas too, so the difference is not visible. I flatten the image (captions: *flat an image*) and open Canvas Size again. Now each corner is clearly defined.

![1343 · U16 · L19 · 09:35](frames/U16L19-F0935.00.jpg)

On screen: “250” [rest omitted]  
Shows: The very light, misty forest image with the output white level lowered to 250.

![1343 · U16 · L19 · 10:23](frames/U16L19-F1023.00.jpg)

On screen: [none]  
Shows: A larger white canvas surrounding the light forest image after the image has been flattened and the canvas enlarged again.

## Fade black and restore true black

Anchor: 1343 · U16 · L19 · 10:28–11:48

Here is another use of output levels. This black-and-white car image already has a faded black. The histogram has a large gap, which was done intentionally. To make the same effect, create a Levels adjustment layer and call it “Faded Black.” This time, use the output level. As you move it, the histogram is pushed and the black becomes more faded.

If an image has faded black and you want true black, use the input slider for black and pull it in to where the histogram starts.

![1343 · U16 · L19 · 10:35](frames/U16L19-F1035.00.jpg)

On screen: “CALIFORNIA” / “2LKT840” [rest omitted]  
Shows: The black-and-white Mercedes photograph before the faded-black Levels adjustment.

![1343 · U16 · L19 · 11:28](frames/U16L19-F1128.00.jpg)

On screen: “48” [rest omitted]  
Shows: The faded-black car image with the output black level raised to 48.

![1343 · U16 · L19 · 11:47](frames/U16L19-F1147.00.jpg)

On screen: “48” [rest omitted]  
Shows: The same car image with input black moved to 48, where the histogram starts, restoring a true black.

## Compare product whites and set a true white

Anchor: 1343 · U16 · L19 · 11:48–14:20

The final example uses a product shot of a Sharpie marker and a shot of these earphones (captions: *Airforms*). When we compare the images, we might not see much difference at first. Arrange them with Window > Arrange > Two Up Vertical to compare them side by side. In product photography, it is very important for white to be a true white.

To compare directly, drag the Sharpie layer onto the earphones image and zoom in. There is quite a big difference between the whites in the two images. Delete the Sharpie layer, consolidate all the tabs with Window > Arrange > Consolidate All Tabs, and zoom out with Command-0 on Mac or Control-0 on Windows.

Add a Levels adjustment layer and call it “Output White.” Pull the white input slider in. The histogram moves right up to the edge, which means the white is now pure white. Confirm this using the Info panel: place the cursor over the white, and the reading should start at 255. Here, the values are very close to 255, so I may need to push the slider slightly further. That is how to achieve pure white in an image using Levels.

I hope you enjoyed learning about Levels and how to use it properly. In the next lesson, I’ll show you a close relative of Levels: Curves, and how to use it properly.

![1343 · U16 · L19 · 11:57](frames/U16L19-F1157.00.jpg)

On screen: “pamu” [rest omitted]  
Shows: The earphones in their open charging case against a light background.

![1343 · U16 · L19 · 12:06](frames/U16L19-F1206.00.jpg)

On screen: “Sharpie” / “FINE POINT” / “Permanent Marker” / “AP” [rest omitted]  
Shows: The Sharpie marker product photograph against a white background.

![1343 · U16 · L19 · 12:32](frames/U16L19-F1232.00.jpg)

On screen: [rest omitted]  
Shows: The Sharpie marker and the earphones displayed side by side for comparison.

![1343 · U16 · L19 · 14:00](frames/U16L19-F1400.00.jpg)

On screen: “Output White” / “241” / “R: 239/253” / “G: 240/254” / “B: 242/255” [rest omitted]  
Shows: The earphones with the Output White adjustment and Info panel showing the sampled RGB values before and after the adjustment.
