# Lesson 80 · Colour Grading & Batch Processing

Anchor: 1343 · U53 · L80 · 13:58 · https://www.domestika.org/en/courses/1974-course-5-final-touches-and-useful-tips/units/6479-colour-grading-batch-processing#course_lesson_19436

## Color grading with lookup tables

Anchor: 1343 · U53 · L80 · 00:11–03:00

In this lesson, I’ll show you how to color grade images and batch process them. Color grading is an important finishing step: it can bring a set of images together so they look coherent, as if they were taken by the same photographer. Batch processing lets us apply the same settings to many images with very little effort. There are several popular ways to color grade, and I’ll show you a few.

A color lookup table, or LUT, comes from the film industry, where a color grade is often applied at the end of the editing process. This gives a film a coherent look and feel, so that as a viewer you feel you are watching the same thing throughout. Photoshop includes a few lookup tables; you can install more, and there are ways to create your own. In the Properties panel, one option gives the image a warm look. In this example it also adds some contrast, which sharpens the image. Other options try to reproduce film stocks, including Fujifilm and Kodak. Teal and orange is another popular film color combination. I find this version a little too cold for my taste. These options are generally strong on purpose, so you can choose how much of the effect to use. A good starting point is 50%, then increase or decrease it to suit your preference. Here is the before and after: the image now has a more distinct look.

![1343 · U53 · L80 · 01:35](frames/U53L80-F0135.00.jpg)

On screen: "Color Lookup" / "Color Lookup 1" / "Load 3D LUT..." / "Crisp_Warm.look" / "Fuji ETERNA 250D Fuji 3510 (by Adobe).cube" / "Kodak 5205 Fuji 3510 (by Adobe).cube" / "TealOrangePlusContrast.3DL" / "Surf Your Limits" [rest omitted]  
Shows: The man in a blue sweatshirt against a concrete wall, with Photoshop's lookup table list open.

![1343 · U53 · L80 · 01:47](frames/U53L80-F0147.00.jpg)

On screen: [rest omitted]  
Shows: The same portrait after a warm lookup table has been applied.

![1343 · U53 · L80 · 02:05](frames/U53L80-F0205.00.jpg)

On screen: [rest omitted]  
Shows: The lookup table list scrolled to Kodak and Fujifilm film-stock options, with a Kodak/Fuji option selected on the portrait.

![1343 · U53 · L80 · 02:26](frames/U53L80-F0226.00.jpg)

On screen: [rest omitted]  
Shows: The portrait with a strong teal-and-orange lookup table applied.

![1343 · U53 · L80 · 02:34](frames/U53L80-F0234.00.jpg)

On screen: "Opacity: 50%" [rest omitted]  
Shows: The same portrait with the lookup-table layer opacity set to 50%.

Another example is a photograph by the great photographer Simon Irwin, shot on Sunset Boulevard. In its current state it does not convey the warm sunset feeling we might expect from the image.

![1343 · U53 · L80 · 03:00](frames/U53L80-F0300.00.jpg)

On screen: "MODELS" / "AGENCY | SOCIAL CLUB" [rest omitted]  
Shows: The ungraded Sunset Boulevard street photograph, with palm trees, traffic, pedestrians, and the sun low in the sky.

## Gradient maps and blend modes

Anchor: 1343 · U53 · L80 · 03:00–05:41

Another popular way to color grade is with a gradient map. By default, applying one turns the image black and white. A gradient map maps the image’s tones to a new gradient: the default black-to-white gradient puts black in the shadows, white in the highlights, and gray in the mid-tones. You can change it by clicking the gradient and opening the Gradient Editor, which offers a variety of choices, including blues, pinks, purples, and reds. The result may look strange at first, but bear with me: I’ll choose a warm-looking gradient.

At first the gradient seems back to front. The left side is mapped to black and the right side to white, so I reverse it. Now yellow is added to the whites and highlights, while red or orange is added to the shadows. That still does not quite work, but there are several ways to work with it. We can use blend modes; recent versions of Photoshop preview the different modes. They can produce interesting effects. Soft Light is a popular mode for coloring, which we have already used in this course. Overlay also works, but it is strong. You can use Multiply or another mode that suits your needs. I’ll leave this on Soft Light. We can keep coloring by other methods, and we can adjust the opacity as well.

![1343 · U53 · L80 · 03:15](frames/U53L80-F0315.00.jpg)

On screen: "Gradient Map" / "Dither" / "Reverse" / "Gradient Map 1" [rest omitted]  
Shows: The street photograph with the default black-to-white gradient map applied.

![1343 · U53 · L80 · 03:41](frames/U53L80-F0341.00.jpg)

On screen: "Gradient Editor" / "Pinks" / "Reds" / "Oranges" / "Name: Blue_03" [rest omitted]  
Shows: The street photograph under a blue gradient preview, with the Gradient Editor open and gradient presets visible.

![1343 · U53 · L80 · 04:29](frames/U53L80-F0429.00.jpg)

On screen: "Multiply" [rest omitted]  
Shows: The sunset street photograph with a warm gradient-map treatment and the blend-mode list open.

## Combining a color layer with Blend If

Anchor: 1343 · U53 · L80 · 05:41–07:20

We can combine effects. I’ll add a Solid Color layer and choose a fairly saturated orange. I can then change its blend mode. Soft Light or Multiply can be interesting, although Multiply looks strange in the highlights, so I’ll set the layer to Soft Light.

We can also control where the color is added. Double-click the empty area to the right of the layer name to open Blend If. If we do not want the color in the shadows, move the slider to remove it. The shadows then return to their normal appearance. Without a transition this looks strange, so hold Alt or Option and pull the slider apart to create a transition. You can also let the effect reach the shadows while reducing it a little in the darkest blacks. Preview the adjustment to compare the original with the changed image. We can combine the gradient map with a color layer; if the combined effect is too strong, reduce its value. Alt- or Option-click the background layer’s eye to compare the original, where the sun is setting but the colors are very cold, with the adjusted image, which looks very warm.

![1343 · U53 · L80 · 05:43](frames/U53L80-F0543.00.jpg)

On screen: "Soft Light" / "Opacity: 100%" / "Color Fill 1" / "Gradient Map 1" [rest omitted]  
Shows: The street image with the orange Color Fill layer set to Soft Light above the Gradient Map layer.

![1343 · U53 · L80 · 06:09](frames/U53L80-F0609.00.jpg)

On screen: "Layer Style" / "Blend Mode: Soft Light" / "Opacity: 100%" / "Blend If: Gray" / "This Layer: 0 255" / "Underlying Layer: 52 255" [rest omitted]  
Shows: The Layer Style dialog open on Blend If, with the underlying-layer slider moved to keep the color out of some shadows.

![1343 · U53 · L80 · 06:38](frames/U53L80-F0638.00.jpg)

On screen: "This Layer:" / "Underlying Layer: 0 / 81 255" [rest omitted]  
Shows: The Blend If underlying-layer slider split into two halves to create a gradual transition.

![1343 · U53 · L80 · 07:09](frames/U53L80-F0709.00.jpg)

On screen: "Indicates layer visibility" [rest omitted]  
Shows: The original, cool-toned street photograph as the adjustment layers are hidden for comparison.

## Building and reusing a color grade with curves

Anchor: 1343 · U53 · L80 · 07:20–10:29

I’ll show one more color-grading option. Curves are my personal favorite because they give us many options. I’ll also show how to apply a curve to several images, although we could do that with any of the options already covered. I add a Curves adjustment layer and call it “color grade,” so it is not confused with other coloring I have done in the image. This example has no other layers, but if it were part of my workflow, that is how I would name the curve.

For the popular orange-and-teal look, we add warmth to the highlights and a cooler tone to the shadows. I start in the red channel, adding a little red to the highlights and subtracting some from the shadows. I can pull the lower point in to limit the effect further; here I pull the bottom down a little. In the green channel, I take some green out of the highlights, which gives magenta, and add a little green to the shadows. Then I go to the blue channel and remove a little blue from the highlights to get yellow there, and add a little blue to the shadows. That is the before and after. To make the effect stronger, pull the lines a little further. Here is the before and after again. I can also combine the color grade with a contrasting curve. Here is the before and after (captions: “often”).

Curves can be saved as a preset. Open the curve’s menu in the Properties panel and choose to save the curve as a preset; I call it “colorGrade.” It now appears among the presets. I showed how to create a preset in an earlier lesson, so this is a reminder. To apply the same type of coloring to another image, pick that preset. You may need to make a few tweaks, but it is a good starting point.

![1343 · U53 · L80 · 07:40](frames/U53L80-F0740.00.jpg)

On screen: [none]  
Shows: The woman in a dark suit standing among parked cars, before the curves-based color grade.

![1343 · U53 · L80 · 08:48](frames/U53L80-F0848.00.jpg)

On screen: "Curves" / "Preset: Custom" / "Green" / "Input: 199" / "Output: 194" / "Colour grade" [rest omitted]  
Shows: A green-channel curve adjustment on the woman’s portrait; the sky has shifted toward magenta.

![1343 · U53 · L80 · 09:49](frames/U53L80-F0949.00.jpg)

On screen: "RGB" / "Input: 28" / "Output: 8" / "Opacity: 100%" / "Fill: 100%" [rest omitted]  
Shows: The completed color grade on the woman’s portrait with the composite RGB curve visible.

![1343 · U53 · L80 · 10:04](frames/U53L80-F1004.00.jpg)

On screen: "Save curves in:" / "Save As: Colour" / "Curves" [rest omitted]  
Shows: The save dialog for the new curve preset, over the graded portrait.

![1343 · U53 · L80 · 10:21](frames/U53L80-F1021.00.jpg)

On screen: "Preset:" [rest omitted]  
Shows: The saved Colour grade curve preset selected for the woman’s portrait.

## Recording an action and batch processing images

Anchor: 1343 · U53 · L80 · 10:29–13:58

If you have a whole set of images, you can batch process them using actions. I’ll delete this curve for a moment and create an action that adds that particular curve to an image. In the Actions panel, I switch to edit mode, or leave button mode, and click the plus sign to create a new action. I add the curve, choose my color-grade preset, and press Stop. Whenever I create an action, I test it to make sure it works and that the curve points came out in the curve. I put the curve in the bin, select the action, and press Play (captions: “slave the title”). The curve I created appears.

To apply the curve to a group of images, go to File > Automate > Batch. By default, Batch selects the set and action you last used. In Source, choose the folder of images to process. You can also use open files. Bridge is another source: a selection of images in Bridge can be used here, and the batch can also be run directly through Bridge. I’ll use the images that are open. I’ll leave Destination set to None for now. In a typical batch, I would save the results into a new folder or potentially save and close the original image. After I click OK, Photoshop runs through the images. On the first image, the curve has been added. If I switch off the original color lookup table, I can see the before and after from the curve I created. The curve is also in the layer stack. This image will end up with a duplicate, so I delete that duplicate.

That is a simple way to add a little color as a finishing touch near the end of the workflow. It is about creating a look in the image rather than doing color correction. You can see how it creates a more dynamic-looking image. Batch processing saves a lot of time and effort, so make sure you use it as much as possible. In the next lesson, we’ll talk about delivering files to a client.

![1343 · U53 · L80 · 11:14](frames/U53L80-F1114.00.jpg)

On screen: "Actions" / "Retouching" / "Workflow" / "Dodge & Burn" / "Frequency Separation" / "Make adjustment layer" / "Select RGB channel" [rest omitted]  
Shows: The Actions panel with the color-grading action and its recorded adjustment-layer steps.

![1343 · U53 · L80 · 11:35](frames/U53L80-F1135.00.jpg)

On screen: [rest omitted]  
Shows: The test action’s curve applied to the woman’s portrait.

![1343 · U53 · L80 · 12:05](frames/U53L80-F1205.00.jpg)

On screen: "Batch" / "Set: Retouching" / "Source: Folder" / "Destination: None" [rest omitted]  
Shows: Photoshop’s Batch dialog with the Retouching set and color-grade action selected.

![1343 · U53 · L80 · 12:21](frames/U53L80-F1221.00.jpg)

On screen: "Folder" / "Import" / "Opened Files" / "Bridge" [rest omitted]  
Shows: The Batch dialog’s Source menu, with Folder, Opened Files, and Bridge listed.

![1343 · U53 · L80 · 12:37](frames/U53L80-F1237.00.jpg)

On screen: "None" / "Save and Close" / "Folder" [rest omitted]  
Shows: The Batch dialog’s Destination menu.

![1343 · U53 · L80 · 13:06](frames/U53L80-F1306.00.jpg)

On screen: [rest omitted]  
Shows: The blue-sweatshirt portrait after the batch action, with its color lookup and curve layers visible.

![1343 · U53 · L80 · 13:12](frames/U53L80-F1312.00.jpg)

On screen: [rest omitted]  
Shows: The Sunset Boulevard photograph after the batch color grade, with its adjustment layers and curve visible.

![1343 · U53 · L80 · 13:33](frames/U53L80-F1333.00.jpg)

On screen: [rest omitted]  
Shows: The woman’s portrait after the batch color grade.

### Key points (derived)

- Use LUTs, gradient maps, solid-color layers, and Curves to create a consistent color look; adjust strength and blend behavior to suit the image.
- Save a curve preset for reuse, then record and test an action before using Photoshop Batch to apply it across images.
