# Lesson 33 · Power of RAW 2

Anchor: 1343 · U23 · L33 · 17:05 · https://www.domestika.org/en/courses/1972-course-3-retouching-environmental-images/units/6058-power-of-raw#course_lesson_19490

## Adjust color, tone, and profiles in Camera Raw

Anchor: 1343 · U23 · L33 · 00:00–04:20

There is probably a little noise here. I will zoom in further and add noise reduction; you can see how it is taken out. It is working well.

The Color Mixer adjusts HSL, which stands for Hue, Saturation, and Luminance. It also lets us work by color. I find the Color view more logical than HSL. For example, if I want to work with orange, I can select orange in Color view and then adjust its hue, saturation, and luminance. HSL shows hue, saturation, and luminance controls for all colors. They do the same thing through a different layout: if I change orange's hue in Color view, that change appears in HSL as well, and the same is true for saturation.

There is also a target adjustment tool. Select it, place the cursor over the image, and click and drag. Camera Raw samples the color under the cursor. When I drag over this area, it moves both red and orange because both colors are present there.

Split toning was traditionally used on black-and-white images in the darkroom. It can still be used on black-and-white images in the raw converter, but people now use it on color images too. For example, I can add a warm orange tone to the highlights and a cooler cyan-blue tone to the shadows. The before-and-after shows the effect. Some people use split toning to color-grade an image and give it a look like a filter.

At the top is a profile control. If I want a black-and-white image, I recommend making that conversion in Photoshop with a Black & White adjustment layer, because it gives more control over color separations. If you will stay in the raw converter, perhaps when processing a large batch, making it black and white here can be useful. The default profile is Adobe Color. That differs from the camera's rendering, which is why a RAW image can look different when it first appears in the raw converter. Choose another profile from the menu or browse the full set. Adobe RAW profiles and camera-matching profiles are available if you want a starting point similar to what your camera produced. There are also black-and-white and artistic choices. I think of the artistic choices more as filters than profiles; profiles are generally for correction or for giving an image a certain look. Experiment with them. To leave the profile browser, click the back arrow.

![1343 · U23 · L33 · 00:22](frames/U23L33-F0022.00.jpg)

On screen: "Sharpening 40" / "Noise Reduction 0" / "Color Noise Reduction 27" / "Basic" / "Curve" / "Detail" / "Color Mixer" / "Split Toning" / "Optics" / "Geometry" / "Effects" / "Calibration" [rest omitted]  
Shows: A 300% close-up of the dark rooftop in the Manhattan waterfront photo, with the Detail panel open during noise reduction.

![1343 · U23 · L33 · 00:40](frames/U23L33-F0040.00.jpg)

On screen: "Color Mixer" / "Adjust" / "HSL" / "Color" / "Hue" / "Saturation" / "Luminance" / "All" / "Reds 0" / "Oranges 0" / "Yellows 0" / "Greens 0" / "Aquas 0" / "Blues 0" / "Purples 0" / "Magentas 0" [rest omitted]  
Shows: The Manhattan skyline image with Color Mixer open and the HSL/Color layout menu expanded.

![1343 · U23 · L33 · 01:16](frames/U23L33-F0116.00.jpg)

On screen: "HOLLYWOOD" / "Color Mixer" / "Adjust" / "HSL" / "Color" / "Hue -21" / "Saturation -16" / "Luminance 0" [rest omitted]  
Shows: Three Buddhist monks in red robes beneath the Hollywood sign; the orange channel is selected in Color Mixer.

![1343 · U23 · L33 · 01:48](frames/U23L33-F0148.00.jpg)

On screen: "Reds −7" / "Oranges −18" / "Yellows 0" / "Greens 0" / "Aquas 0" / "Blues 0" / "Purples 0" / "Magentas 0" [rest omitted]  
Shows: A close-up of the red robe in the monk photograph beside the HSL color controls.

![1343 · U23 · L33 · 02:18](frames/U23L33-F0218.00.jpg)

On screen: "Highlights" / "Hue 42" / "Saturation 16" / "Balance 0" / "Shadows" / "Hue 209" / "Saturation 0" [rest omitted]  
Shows: The monk photograph with warm highlights, before saturation is added to the cyan-blue shadow tone.

![1343 · U23 · L33 · 02:33](frames/U23L33-F0233.00.jpg)

On screen: "Highlights" / "Hue 42" / "Saturation 16" / "Balance 0" / "Shadows" / "Hue 209" / "Saturation 28" [rest omitted]  
Shows: The monk photograph with warm highlights and cooler cyan-blue shadows applied in Split Toning.

![1343 · U23 · L33 · 04:06](frames/U23L33-F0406.00.jpg)

On screen: "Profile" / "Adobe Vivid" / "Adobe Landscape" / "Adobe Neutral" / "Adobe Portrait" / "Adobe Standard" / "Camera Matching" / "Faithful" / "Landscape" / "Neutral" / "Portrait" / "Artistic" / "B&W" / "Modern" / "Vintage" [rest omitted]  
Shows: The profile browser over the monk photograph, with Adobe profiles, camera-matching profiles, and profile groups visible.

## Inspect and correct optical problems

Anchor: 1343 · U23 · L33 · 04:20–07:21

The next section is Optics, which begins with Remove Chromatic Aberration. When I first heard the term, I did not know what it meant, so here is an example. I zoom in to 300%; that is how I check for the problem. You might not notice it at first, but if you later push the image hard in Photoshop by adding contrast or sharpening, the problem can become more pronounced. Look for it at high magnification, especially along sharp, high-contrast edges and in backlit areas. In this image there is a small halo along the staircase edge and a reddish halo on the flagpole.

Often, simply selecting Remove Chromatic Aberration does a good job. Compare the before and after at this high magnification. At 100%, the red line on the flagpole should no longer be visible.

Defringe offers more manual control over chromatic aberration, but the automatic option is often enough.

Distortion and vignetting can also be adjusted manually. Profile corrections use the camera and lens metadata to apply corrections for distortion and vignetting. Open the profile details to see the camera and lens and the separate Distortion and Vignette amounts. If I like the distortion correction but do not want the vignette correction, I can adjust one without the other; I can also reduce the distortion and keep the vignette correction. The preview makes it possible to compare these choices.

![1343 · U23 · L33 · 05:11](frames/U23L33-F0511.00.jpg)

On screen: "51 SPRING ST." / "Remove chromatic aberration" / "Use profile corrections" / "Defringe" [rest omitted]  
Shows: A 300% crop of a New York storefront awning and high-contrast edges, with Optics controls open.

![1343 · U23 · L33 · 05:56](frames/U23L33-F0556.00.jpg)

On screen: "Remove chromatic aberration" / "Use profile corrections" / "Defringe" [rest omitted]  
Shows: The New York street photograph after chromatic aberration removal at 100% zoom.

![1343 · U23 · L33 · 06:15](frames/U23L33-F0615.00.jpg)

On screen: "Use profile corrections" [rest omitted]  
Shows: The New York street photograph before the camera and lens profile corrections are applied; the checkbox is unchecked.

![1343 · U23 · L33 · 06:29](frames/U23L33-F0629.00.jpg)

On screen: "Remove chromatic aberration" / "Use profile corrections" / "Distortion 100" / "Vignette 100" [rest omitted]  
Shows: The full New York street photograph with the camera and lens profile corrections enabled.

## Straighten the image, then review effects and calibration

Anchor: 1343 · U23 · L33 · 07:21–09:51

Geometry is where we transform the image and straighten verticals. There are several automatic options, and I will demonstrate Guided. One edge of this building leans, while another looks fairly straight. That may be because my camera was tilted. Guided correction follows straight lines in the picture: I draw one line along one edge of the building and a second along the other edge. With two or more lines, Photoshop straightens them. This crops quite a lot from the image. I can add more lines, but the extra ones do not seem to change the result. We can add horizontal lines too. As more guides are placed, Photoshop corrects the image. Moving a line after placing it accidentally can be tricky, so I cancel this attempt. Try the feature yourself. The automatic options can also straighten the image, and in this example the result works quite well.

Effects has controls for adding grain or a vignette, with more options behind the arrows. Photoshop gives us more options for those edits. And if you like grain (captions: *rain*), maybe you should shoot film. Calibration is less creative and more corrective. If the shadows have a green or magenta tint, Calibration provides controls to correct it.

![1343 · U23 · L33 · 08:13](frames/U23L33-F0813.00.jpg)

On screen: "Geometry" / "Draw Guides" / "Clear Guides" / "Loupe" / "Show Guides" / "Constrain crop" / "Manual Transformations" [rest omitted]  
Shows: The New York street image with a vertical guided line placed along a building edge.

![1343 · U23 · L33 · 08:54](frames/U23L33-F0854.00.jpg)

On screen: "Upright" / "Draw guides" / "Clear Guides" / "Loupe" / "Show Guides" / "Constrain crop" / "Manual Transformations" [rest omitted]  
Shows: The guided street correction with guide lines and checkerboard areas at the upper-left and lower-left edges showing the crop.

![1343 · U23 · L33 · 09:02](frames/U23L33-F0902.00.jpg)

On screen: "Geometry" [rest omitted]  
Shows: The street image after applying an automatic straighten option.

## Save and synchronize a useful batch starting point

Anchor: 1343 · U23 · L33 · 09:51–12:42

When several images were made in a similar location, it often makes sense to batch-process them by applying the same settings. Images will not match perfectly, but the same edits can be a good starting point. If you have photographed an event, for example, you may have a thousand images, and processing all of them one at a time would take a long time. Batch processing can speed up the workflow.

On this roadside landscape I darken the highlights, brighten the shadows, make the blacks slightly darker, add clarity and a little dehaze, and make the colors more vivid. Compare the before and after.

![1343 · U23 · L33 · 10:30](frames/U23L33-F1030.00.jpg)

On screen: "White balance" / "As Shot" / "Temperature 5500" / "Tint 0" / "Exposure 0.00" / "Contrast 0" / "Highlights 0" / "Shadows 0" / "Whites 0" / "Blacks 0" / "Texture 0" / "Clarity 0" / "Dehaze 0" / "Vibrance 0" / "Saturation 0" [rest omitted]  
Shows: The California roadside landscape before batch adjustments, with the Basic controls at their default values.

If I want to use these settings on other images, I can save them as a preset. Photoshop includes presets, and I can create my own. Choose Create Preset and choose which settings to include. I would typically exclude Exposure and White Balance unless they are part of the look I am creating. For example, if I raise exposure by one stop, darken highlights and shadows, and build a particular look from those settings, I might include exposure. Otherwise I would leave Exposure and White Balance out.

Choose the settings to include and click OK. I forgot to give this preset a name, so it is called Untitled. To apply it, click it in the preset list. A preview shows how it will look before you select it. Presets such as Desaturated Contrast and Cool Light are also available to try.

If you have a group of images, select the images and click the synchronization symbol. Choose which settings to synchronize, then click OK. The selected images now share those settings. This can make a large difference to the speed of your workflow.

![1343 · U23 · L33 · 10:44](frames/U23L33-F1044.00.jpg)

On screen: "Highlights −41" / "Shadows +25" / "Blacks −16" / "Clarity +21" / "Dehaze +19" / "Vibrance +27" [rest omitted]  
Shows: A hazy California roadside landscape after a set of tonal, clarity, dehaze, and color adjustments.

![1343 · U23 · L33 · 11:32](frames/U23L33-F1132.00.jpg)

On screen: "New Preset" / "Name: Untitled" / "Group: User Presets" / "Profile: Adobe Color" / "White Balance" / "Exposure" / "Contrast" / "Highlights" / "Shadows" / "Whites" / "Blacks" / "Texture" / "Clarity" / "Dehaze" / "Vibrance" / "Saturation" [rest omitted]  
Shows: The New Preset dialog over the California road image, with White Balance and Exposure unchecked and other basic adjustments selected.

![1343 · U23 · L33 · 11:45](frames/U23L33-F1145.00.jpg)

On screen: "User Presets" / "Landscape daytime" / "Untitled" [rest omitted]  
Shows: The User Presets group with the grayed-out Landscape daytime preset above the newly created Untitled preset.

![1343 · U23 · L33 · 12:20](frames/U23L33-F1220.00.jpg)

On screen: "Synchronize" / "Profile: Adobe Color" / "Basic" / "White Balance" / "Exposure" / "Contrast" / "Highlights" / "Shadows" / "Whites" / "Blacks" / "Texture" / "Clarity" / "Dehaze" / "Vibrance" / "Saturation" [rest omitted]  
Shows: The Synchronize dialog over a lifeguard hut photograph, with three of nine selected images in the batch.

## Set workflow options, save files, and open them in Photoshop

Anchor: 1343 · U23 · L33 · 12:42–17:05

The last thing I want to show is Workflow Options. They are available from the line near the bottom or from the top. I prefer Adobe RGB as the color space. I cannot explain everything about color spaces in this lesson, but Adobe RGB is a typical choice; use ProPhoto RGB if you are matching with Lightroom, or sRGB.

Sixteen bits per channel gives an image more tones and better quality, but it also makes a much larger file—twice the size of an 8-bit-per-channel image. This is a choice between quality and file size. I work in 16 bits per channel as much as possible, especially for landscape and environmental images. It may be less important for studio portraits, where you control the light. You can, of course, convert an image from 16 to 8 bits later (captions: *18 bits*). I do not recommend resizing the image here; leave it as it is. I recommend leaving Resolution at 300.

For Output Sharpening, I generally recommend leaving it off, or leaving it on with only a small amount for screen. That applies a small amount of sharpening to each image, and you can sharpen more later in Photoshop. The last option is to open in Photoshop as a Smart Object. That lets you bring the image back into the raw converter after it has been in Photoshop. It is a useful option that I will cover more in another lesson. Click OK to accept the workflow settings.

The Save Image option lets me write files out without sending them into Photoshop. If I do not need to keep working in Photoshop, I can save the images as JPEGs. Choose a new filename and a sequence number, select a format such as JPEG, and click Save. The program stays available while it saves, so, for example, you can continue working while 500 RAW files are being saved as JPEGs in the background.

For JPEGs, sRGB is a typical color space because it works well on the internet. You can also size the images—for a web image, for example, they may not need to be larger than 1,000 pixels—and choose sharpening for the intended use. Then click Save. I will cancel this save example.

Done saves the changes made to the RAW files. If you are finished and do not want to send a particular image into Photoshop, click Done. Otherwise select one or more images and click Open to take them into Photoshop. Because I changed Workflow Options to open a Smart Object, the button says Open Object. Hold Shift to change the default. If you did not set Open as Smart Object as the default, the button changes from Open to Open Object.

I hope you enjoyed working with RAW files and have started to see the power they hold compared with a normal JPEG. In the next lesson, I will show you how to make local edits in an image.

![1343 · U23 · L33 · 13:20](frames/U23L33-F1320.00.jpg)

On screen: "Color Space" / "Space: Adobe RGB (1998)" / "Depth: 16 Bits/Channel" / "Image Sizing" / "Resize to Fit: Default (21.0 MP)" / "Resolution: 300 pixels/inch" / "Output Sharpening" / "Open in Photoshop as Smart Objects" [rest omitted]  
Shows: Camera Raw Workflow preferences over the lifeguard hut image, set to Adobe RGB, 16 bits per channel, and 300 pixels per inch.

![1343 · U23 · L33 · 14:27](frames/U23L33-F1427.00.jpg)

On screen: "Sharpen For: Screen" / "Amount: Standard" / "Open in Photoshop as Smart Objects" [rest omitted]  
Shows: The Workflow preferences with screen output sharpening enabled and the Smart Objects option visible.

![1343 · U23 · L33 · 15:57](frames/U23L33-F1557.00.jpg)

On screen: "Example: California_5744.jpg" / "File Extension: .jpg" / "Format: JPEG" / "Space: sRGB IEC61966-2.1" / "W: 1000" / "H: 1000 pixels" / "Resolution: 300 pixels/inch" / "Sharpen For: Matte Paper" / "Amount: Standard" [rest omitted]  
Shows: Save Options configured for a JPEG with sRGB color, a 1,000 by 1,000 pixel size, and output sharpening.

![1343 · U23 · L33 · 16:17](frames/U23L33-F1617.00.jpg)

On screen: "Highlights −41" / "Shadows +25" / "Blacks −16" / "Clarity +21" / "Dehaze +19" / "Vibrance +27" / "Done" / "Open Object" [rest omitted]  
Shows: The lifeguard hut image in Camera Raw with its adjustments and the Done and Open Object controls.

### Key points (derived)

- Color Mixer can target one color or adjust colors through HSL; the target tool can affect more than one sampled color.
- Use Camera Raw profiles, optics, geometry, presets, and synchronization to build a practical starting point for groups of images.
- Choose workflow options to fit the image's color, bit depth, output size, and next editing step.
