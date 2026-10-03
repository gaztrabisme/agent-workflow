# Lesson 50 · Panorama

Anchor: 1343 · U32 · L50 · 17:13 · https://www.domestika.org/en/courses/1972-course-3-retouching-environmental-images/units/6451-panorama#course_lesson_19408

## Accessing Photomerge from Bridge

Anchor: 1343 · U32 · L50 · 00:00–01:14

In this lesson I use one of Photoshop’s automated features, Photomerge, to create a panorama from several exposures. In Bridge, I select the photos I want to include, then Shift-click the last one to extend the selection. From Tools > Photoshop > Photomerge, I can open the merge dialog directly. If Bridge is not installed, I can do the same thing from Photoshop, although Bridge is my preferred way to start a panorama.

![1343 · U32 · L50 · 00:57](frames/U32L50-F0057.00.jpg)

On screen: "Tools" / "Photoshop" / "Photomerge..." / "Panorama_2672.dng" / "Panorama_2671.dng" / "Panorama_2670.dng" [rest omitted]  
Shows: Three landscape exposures selected in Bridge, with the Photoshop submenu open.

## Prepare and synchronise the source exposures

Anchor: 1343 · U32 · L50 · 01:14–02:38

I open the images in the raw converter. I have already made a few basic adjustments. In Lens Corrections, I remove chromatic aberration and enable Profile Corrections. A panorama works better when the source images have little distortion or vignetting, so I apply those corrections.

In the filmstrip menu, I choose Select All, or press Command or Control+A, then choose Sync Settings. This works best when the panorama was shot in manual mode: I can leave the settings checked and click OK. If the light changed between exposures, or the camera was not in manual mode, I may need to make further adjustments after synchronising. I click OK, then open the images in Photoshop.

![1343 · U32 · L50 · 02:16](frames/U32L50-F0216.00.jpg)

On screen: "Lens Corrections" / "Synchronize" / "Default" / "Chromatic Aberration" / "Lens Profile Corrections" / "Lens Manual Distortion" / "Lens Manual Vignetting" [rest omitted]  
Shows: Three panorama exposures in Camera Raw, with the Synchronize dialog open and lens corrections visible.

![1343 · U32 · L50 · 02:37](frames/U32L50-F0237.00.jpg)

On screen: "Open Images" [rest omitted]  
Shows: Three exposures selected in Camera Raw, with the Open Images button and its tooltip visible.

## Choose a challenging panorama example

Anchor: 1343 · U32 · L50 · 02:38–03:16

I chose this subject to test Photoshop. Very sharp lines running across an image can make a panorama difficult; here there are pylons and power lines. Movement can also cause problems: the water is moving, and a few birds cross the scene. The usual advice is to photograph the sequence from left to right. I deliberately started on the right and worked left; it should not make much difference, but left to right is the recommendation.

![1343 · U32 · L50 · 03:08](frames/U32L50-F0308.00.jpg)

On screen: [none]  
Shows: A source exposure of the river, with power lines, pylons, clouds, and moving water.

## Set up and run Photomerge

Anchor: 1343 · U32 · L50 · 03:16–04:39

In Photoshop, I go to File > Automate > Photomerge. The dialog is the same, or very similar, to the one in Bridge. I choose Auto for the layout. If the source photos are already open, I click Add Open Files; otherwise, I can use Browse to locate them. I recommend enabling Vignette Removal and Geometric Distortion Correction.

When I click OK, Photoshop analyses the images and puts them together. If the source images have not been saved on the computer, Photoshop says it cannot work with them. I save the files and repeat the process.

![1343 · U32 · L50 · 03:59](frames/U32L50-F0359.00.jpg)

On screen: "Layout" / "Auto" / "Source Files" / "Use" / "Files" / "Browse..." / "Add Open Files" / "Blend Images Together" / "Vignette Removal" / "Geometric Distortion Correction" / "Content Aware Fill Transparent Areas" [rest omitted]  
Shows: Photomerge with Auto selected, three source files listed, and vignette removal and geometric distortion correction enabled.

## Review the merged panorama

Anchor: 1343 · U32 · L50 · 04:39–05:19

Photoshop has done a good job of combining the exposures. The images have not actually been merged into one flattened layer: Photoshop has arranged them as layers and is using masks. If part of an image has been excluded or the merge does not quite work, I can inspect and adjust the masks. I made this panorama handheld, without a tripod, to show that it can work. A tripod is still better because it leaves fewer parts of the image missing.

![1343 · U32 · L50 · 04:46](frames/U32L50-F0446.00.jpg)

On screen: [none]  
Shows: The wide river panorama assembled from three layers, each with a layer mask; transparent gaps remain along the edges.

## Make a tight crop with a selection

Anchor: 1343 · U32 · L50 · 05:19–06:30

I will use a different cropping method now. I use it when I need to crop very tightly to the edges. I choose the Rectangular Marquee tool by pressing M. Feather should be zero; I am not using a shape, unless I specifically want to crop to one. I put the cursor where I want the crop to begin, including the corner I need, and drag out a selection. Holding Space temporarily gives me the Move tool so I can reposition the selection before I finish dragging it (captions: “press an old space”).

![1343 · U32 · L50 · 05:45](frames/U32L50-F0545.00.jpg)

On screen: "Feather: 0 px" / "Anti-alias" / "Style: Normal" [rest omitted]  
Shows: The panorama with the marquee options bar showing zero feather and Normal style; no selection has been drawn yet.

## Crop and check the panorama edges

Anchor: 1343 · U32 · L50 · 06:30–08:05

I extend the selection to the bottom-right corner, release the mouse, and choose Image > Crop. I deselect with Command or Control+D. Some parts of the panorama are still missing, so I can crop tighter. There is quite a bit missing at the bottom; I bring the crop in a little because there is nothing important I would lose. I crop again and deselect.

The missing corner is now obvious, but sometimes only a few pixels are visible and it is easy to overlook them. I want to catch that before the image goes to print or onto a website.

![1343 · U32 · L50 · 06:42](frames/U32L50-F0642.00.jpg)

On screen: "Image" / "Crop" [rest omitted]  
Shows: The Photoshop Image menu open over the panorama, with Crop highlighted.

![1343 · U32 · L50 · 07:32](frames/U32L50-F0732.00.jpg)

On screen: [rest omitted]  
Shows: The cropped panorama with narrow empty areas still visible along the upper and lower edges.

## Make missing pixels easy to see

Anchor: 1343 · U32 · L50 · 08:05–08:37

To make small gaps easier to spot, I add a Solid Color layer and choose a bright pink, then click OK and move it underneath all the image layers. The empty parts now stand out, so I can use the layer as a check while I fill the corners. It is much safer to notice a tiny gap now than after a large print has been made. I ask, “Why are we missing bits?” (captions: “Why are we missing Betsy?”). I hide the check layer for a moment before continuing.

![1343 · U32 · L50 · 08:28](frames/U32L50-F0828.00.jpg)

On screen: "Color Fill 1" [rest omitted]  
Shows: A bright pink check layer showing through the empty top and lower corners of the panorama.

## Select and fill the first corner

Anchor: 1343 · U32 · L50 · 08:37–10:33

I pick the Lasso tool, zoom in with Command or Control plus, and reposition with Space. For the upper-left corner, I make a generous selection instead of following the empty area as tightly as possible; I include a little of the surrounding image. I want this layer on top of everything else, so I create a new layer called Corner fills (captions: “Corner fails”), then choose Edit > Content-Aware Fill (captions: “content aware field”). Photoshop shows the original image and marks in green the areas it will sample. The first result works fairly well, although part of it looks a little odd.

If the Content-Aware Fill dialog is not available, the Photoshop version may be out of date. Creative Cloud subscribers can update Photoshop to get it.

![1343 · U32 · L50 · 09:11](frames/U32L50-F0911.00.jpg)

On screen: [rest omitted]  
Shows: A generous lasso selection around the missing upper-left corner, including nearby sky and power lines.

![1343 · U32 · L50 · 09:35](frames/U32L50-F0935.00.jpg)

On screen: "Edit" / "Content-Aware Fill..." / "Corner fills" [rest omitted]  
Shows: The Edit menu open over the selected upper-left corner, with Content-Aware Fill highlighted.

![1343 · U32 · L50 · 10:11](frames/U32L50-F1011.00.jpg)

On screen: "Content-Aware Fill" / "Sampling Area Overlay" / "Sampling Area Options" / "Auto" / "Rectangular" / "Custom" / "Sample All Layers" / "Fill Settings" / "Color Adaptation" / "Default" / "Rotation Adaptation" / "None" / "Scale" / "Mirror" / "Output Settings" / "Output To" / "New Layer" [rest omitted]  
Shows: The Content-Aware Fill workspace with the green sampling area over the selected corner and a preview of the fill.

## Refine the sample and fill settings

Anchor: 1343 · U32 · L50 · 10:33–12:39

The first tool in the options bar has a plus and a minus: plus adds to the area Photoshop samples from, while minus subtracts from it. I paint parts of the sample area away to control what Photoshop uses. I initially identify the lines as pylons, then correct myself to the power cables (captions: “was the power cables rather than the pylons, right?”). Photoshop’s first attempt is a little worse, so I adjust the sample again and give it more to work with. The result changes back and forth; there is some trial and error. A small remaining irregularity would be easy to fix with the Clone tool, so I am happy with the result.

Color Adaptation lets Photoshop adjust colour to match the surrounding image, and the default works well here. Rotation Adaptation lets Photoshop rotate the cloned content to fit better. For example, if a line does not follow the right angle, I can ask Photoshop to try Rotation Adaptation (captions: “Let's Photoshop”). If it is not needed, I leave the setting at None. Normally I would send the result to a new layer, but I already created a repair layer, so I choose Current Layer and click OK. I then deselect.

![1343 · U32 · L50 · 11:23](frames/U32L50-F1123.00.jpg)

On screen: [rest omitted]  
Shows: The refined green sample region and the preview of sky and power cables used to fill the upper corner.

![1343 · U32 · L50 · 12:11](frames/U32L50-F1211.00.jpg)

On screen: "Low" / "Medium" / "High" / "Full" [rest omitted]  
Shows: The Rotation Adaptation menu with its strength options open over the fill preview.

![1343 · U32 · L50 · 12:31](frames/U32L50-F1231.00.jpg)

On screen: "Current Layer" / "Duplicate Layer" [rest omitted]  
Shows: The Output To menu with the current, new, and duplicate layer choices.

## Fill the remaining corners one at a time

Anchor: 1343 · U32 · L50 · 12:39–14:31

I move to the next corner, select it with the Lasso tool, and choose Edit > Content-Aware Fill again. This result looks pretty good, although there is a little repetition that would be easy to clone. I put it on the same layer. If the area were more complex and I wanted to inspect each repair separately later, I would choose New Layer instead.

I deselect and move to another area. Photoshop can fill more than one selection at a time, but I prefer to work one area at a time so I can concentrate on each one. I fill the next corner and inspect it before moving on.

![1343 · U32 · L50 · 13:14](frames/U32L50-F1314.00.jpg)

On screen: [rest omitted]  
Shows: A green sampling region over the riverbank and a Content-Aware Fill preview of the shoreline.

![1343 · U32 · L50 · 13:44](frames/U32L50-F1344.00.jpg)

On screen: [rest omitted]  
Shows: A lasso selection around an unfilled lower-right corner beside the brick building and water.

![1343 · U32 · L50 · 14:15](frames/U32L50-F1415.00.jpg)

On screen: [rest omitted]  
Shows: A lasso selection around a missing upper-right strip of sky above the brick building.

Those clouds should not be complicated to fill. The result looks good, so I click OK.

## Complete the last corner repair

Anchor: 1343 · U32 · L50 · 14:31–15:25

For the final area, I select the corner and remove part of the selection by holding Alt or Option. The selection is tight, but still gives Photoshop enough to work with. I choose Content-Aware Fill. The result looks pretty good. I may need to do a tiny bit of tidying with the Clone tool, but as a starting point it looks great. I click OK and deselect.

![1343 · U32 · L50 · 15:14](frames/U32L50-F1514.00.jpg)

On screen: [rest omitted]  
Shows: The last sky-corner selection covered by the green sampling overlay, with the filled clouds in the preview.

## Check the edges and repair the final gap

Anchor: 1343 · U32 · L50 · 15:25–16:38

I zoom out and turn on the check layer, renaming it so it is clear what it is for. It reveals a tiny area that still needs filling. A check layer helps me catch a gap like this before sending a large print to production. I turn it off again, select the repair layer (captions: “It's like my fill layer”), and choose the Lasso tool by pressing L to make a small selection. I choose Content-Aware Fill (captions: “Constance of where Phil”) once more. Working on small areas separately makes Photoshop zoom into the area being repaired, which makes it easier to focus. I click OK and deselect.

![1343 · U32 · L50 · 15:44](frames/U32L50-F1544.00.jpg)

On screen: "Check Layer" [rest omitted]  
Shows: The full panorama with the check layer turned on; a tiny pink gap remains at the top edge.

![1343 · U32 · L50 · 16:14](frames/U32L50-F1614.00.jpg)

On screen: [rest omitted]  
Shows: The Edit menu open while a small lasso selection is made around the last gap in the sky.

![1343 · U32 · L50 · 16:32](frames/U32L50-F1632.00.jpg)

On screen: [rest omitted]  
Shows: A small green sampling area above the clouds and the close-up preview for the final fill.

## View the finished panorama

Anchor: 1343 · U32 · L50 · 16:38–17:13

I zoom out to inspect the whole image. Pressing F a couple of times switches to a screen that works as a simple presentation view. Command or Control+0 fits the image on screen. This is the finished panorama. I hope you enjoyed the lesson; next I will teach HDR, or high dynamic range, images.

![1343 · U32 · L50 · 16:49](frames/U32L50-F1649.00.jpg)

On screen: [none]  
Shows: The completed panorama in a presentation view.

### Key points (derived)

- Bridge can send selected exposures directly to Photomerge; Photoshop offers the same workflow through File > Automate > Photomerge.
- Correct lens distortion and vignetting consistently across the source exposures, then use Auto layout with vignette removal and geometric distortion correction.
- The merge retains source layers and masks, so inspect masks before flattening or cropping.
- Crop to a clean composition, then use a vivid check layer to reveal small transparent gaps before printing or publishing.
- Content-Aware Fill works best when you control its sample area and repair one small region at a time; inspect the result and clean up with Clone if needed.
