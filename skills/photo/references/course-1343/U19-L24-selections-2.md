# Lesson 24 · Selections 2

Anchor: 1343 · U19 · L24 · 15:56 · https://www.domestika.org/en/courses/1971-course-2-retouching-fundamentals/units/6426-selections#course_lesson_19485

## Tools for a more accurate cutout

Anchor: 1343 · U19 · L24 · 00:00–02:02

For a more accurate selection to cut out the sneaker, I would not use the ordinary Lasso tool. I want to show the Magnetic Lasso because many people use it, but I do not recommend it: it is slow and not very good. The Polygonal Lasso can give a cutout the particular look of scissors, but I rarely use it; occasionally it is useful. Avoid the Magnetic Lasso.

The Object Selection tool is relatively new. Draw a rectangle around the subject and Photoshop tries to select it. It has done a fairly good job on most of this sneaker, though some areas are not quite right. Its options bar has the familiar selection-mode symbols, so it can select more than one object, and its mode can be changed from Rectangle to Lasso. I deselect with Command or Control+D and move on to the Quick Selection tool.

![1343 · U19 · L24 · 00:59](frames/U19L24-F0059.00.jpg)

On screen: "Lasso Tool" / "Polygonal Lasso Tool" / "Magnetic Lasso Tool" [rest omitted]  
Shows: The three Lasso tool choices in the Photoshop toolbar beside the sneaker on a white background.

![1343 · U19 · L24 · 01:22](frames/U19L24-F0122.00.jpg)

On screen: "Mode: Rectangle" / "Object Subtract" / "Select Subject" / "Select and Mask..." [rest omitted]  
Shows: The sneaker surrounded by a selection, with the Object Selection options bar visible.

## Refine the sneaker with Quick Selection

Anchor: 1343 · U19 · L24 · 02:02–05:48

The Quick Selection tool has the same selection modes as the other tools except Intersect. Its plus and minus icons make Add to Selection and Subtract from Selection easier to read. Because it is a brush tool, it has controls for size, hardness, spacing and roundness. I generally recommend checking Sample All Layers and Enhance Edge. The options bar also gives access to Select and Mask. Select Subject uses the same technology as Object Selection and gives a similar result; here it has done a slightly better job in one area, but missed the tip of the shoelace.

![1343 · U19 · L24 · 03:20](frames/U19L24-F0320.00.jpg)

On screen: "Sample All Layers" / "Enhance Edge" [rest omitted]  
Shows: The Select Subject result around the sneaker, with an enlarged inset showing the missed tip of the shoelace.

I can make the brush smaller with the square-bracket keys beside P, zoom in with Command or Control plus, and reposition with the Spacebar. Then I paint over the missed areas. The selection is mostly good, though the heel could use a little more painting. To remove an unwanted area, I could choose Subtract from Selection in the options bar, but holding Alt or Option temporarily changes the plus to a minus, which is faster. Photoshop processes the edge when I release the mouse. Enhance Edge usually gives a better result; I would turn it off only if it slows the computer. I make the brush smaller again and hold Alt or Option to subtract where needed.

After zooming out with Command or Control+0, I can copy the selected sneaker to a new layer with Command or Control+J. The Layers panel shows the sneaker on its own layer against transparency.

![1343 · U19 · L24 · 04:43](frames/U19L24-F0443.00.jpg)

On screen: [none]  
Shows: A close view of the sneaker's heel loop, with the selection edge visible around the narrow opening and fabric.

![1343 · U19 · L24 · 05:37](frames/U19L24-F0537.00.jpg)

On screen: "Layer 1" / "Background" [rest omitted]  
Shows: The sneaker on the canvas with its copied layer above the background in the Layers panel.

## Feather a broad foreground selection

Anchor: 1343 · U19 · L24 · 05:48–08:01

I like this forest photograph, but the two people are getting lost near the middle of the wide, light image. I want to darken the image gradually rather than darkening everything and then removing the effect from this area. The foreground is bright and draws a lot of attention; some of the background trees could also be darker.

The Rectangular Marquee is a simple, useful selection tool. I drag out a selection of the foreground. The options bar again offers Add, Subtract and Intersect. An adjustment on this sharp-edged selection would have a hard edge, so I use Select and Mask, choose Overlay and raise Feather until the boundary blends away. Marching Ants are a poor way to judge a selection like this because they do not show its soft edge.

Curves gives the most control for darkening, although it is not the easiest option. I add a Curves adjustment layer from the black-and-white circle at the bottom of the Layers panel. I strongly recommend naming your layers; I call this one “Foreground” and pull the curve down a little. The change is subtle enough that it may be hard to notice at first; toggling the layer's eye on and off shows that the foreground is darker. The goal is for it to blend into the rest of the photograph, which I think it does.

![1343 · U19 · L24 · 06:17](frames/U19L24-F0617.00.jpg)

On screen: [none]  
Shows: The original forest-path photograph, with an adult and child walking among the trees.

![1343 · U19 · L24 · 07:56](frames/U19L24-F0756.00.jpg)

On screen: "Feather: 243.1 px" [rest omitted]  
Shows: The forest photograph in Select and Mask with a red Overlay over the trees and the foreground left clear by a broad feathered selection.

## Darken the trees while excluding the hikers

Anchor: 1343 · U19 · L24 · 08:01–12:01

Next I select the trees in the background. That selection also includes the two people, so I pick up the Lasso tool and set it to Subtract from Selection. Holding Alt or Option temporarily switches to subtract mode if another option is active. I make a loose outline because I will soften the edge. To follow the natural edge of the slope, I can draw outside the image and come back down; when I release the cursor, Photoshop connects it to the starting point by the most direct route.

In Select and Mask, I apply a heavy feather. It begins to creep into the figures, but that may be acceptable, and I can adjust it later if needed.

![1343 · U19 · L24 · 11:08](frames/U19L24-F1108.00.jpg)

On screen: "Feather: [illegible]" / "Indicates: Masked Areas" [rest omitted]  
Shows: The red Overlay from the heavily feathered tree selection reaches across the foreground and into the two hikers.

I click OK, add another Curves adjustment layer, name it “Trees darken,” and pull the curve down slightly. To compare the result with the original and see the work so far, I can hold Alt or Option and click the background layer's eye.

![1343 · U19 · L24 · 11:33](frames/U19L24-F1133.00.jpg)

On screen: "Trees darken" / "Foreground darken" / "Background" / "Input: 127" / "Output: 127" [rest omitted]  
Shows: The selected Trees darken layer with an unchanged Curves diagonal; its readout is Input 127, Output 127.

## Darken around the hikers

Anchor: 1343 · U19 · L24 · 12:01–13:03

I make another loose selection, this time around the two people, and soften its edge in Select and Mask. Because I outlined the figures but want the adjustment applied to everything else, I invert the selection before clicking OK. I add another Curves layer, call it “Darken minus subject,” and darken the surroundings. The change is fairly subtle, but it contributes to the combined effect.

![1343 · U19 · L24 · 12:35](frames/U19L24-F1235.00.jpg)

On screen: "Feather: 154.4 px" / "Invert" [rest omitted]  
Shows: The red Overlay covers the hikers’ loose selection while the surrounding forest remains clear, with the Invert control visible.

## Add a vignette and finish with contrast

Anchor: 1343 · U19 · L24 · 13:03–15:56

To make a classic vignette, I use the Elliptical Marquee, dragging from the top-left corner to the bottom-right. I open Select and Mask and apply a very heavy feather. Since the centre is selected, I need to invert the selection to affect the outside. I deliberately demonstrate the common mistake of darkening the centre instead. After adding a Curves layer called “Vignette,” I exaggerate the adjustment so it is clear that the centre, not the edges, is getting darker.

There is no need to undo or rebuild the selection. With an adjustment layer, I can click its mask to open the mask properties and choose Invert; the darkening then reaches the image edges. To bring the edits together, I add a global contrast adjustment because so many parts have been changed separately and the small centre area may look odd by comparison. Curves is the best tool for contrast. I name the layer “Contrast,” add a point to brighten the highlights a little, darken the shadows, and pull down the darkest blacks. Finally, I compare the original photograph with the result.

![1343 · U19 · L24 · 13:28](frames/U19L24-F1328.00.jpg)

On screen: "Darken minus subject" / "Feather: 0.0 px" / "Invert" [rest omitted]  
Shows: The forest-path photograph with the centre clear and the surrounding area in red Overlay, before the vignette selection is inverted.

![1343 · U19 · L24 · 14:21](frames/U19L24-F1421.00.jpg)

On screen: "Vignette" [rest omitted]  
Shows: The forest photograph has a darkened centre while its outer edges remain brighter, showing the inverted vignette mistake.

![1343 · U19 · L24 · 15:50](frames/U19L24-F1550.00.jpg)

On screen: "Contrast" [rest omitted]  
Shows: The finished forest photograph and its stack of named Curves adjustment layers.
