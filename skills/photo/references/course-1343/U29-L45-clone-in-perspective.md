# Lesson 45 · Clone in Perspective

Anchor: 1343 · U29 · L45 · 19:07 · https://www.domestika.org/en/courses/1972-course-3-retouching-environmental-images/units/6446-clone-in-perspective#course_lesson_19403

## Why ordinary cloning fails in perspective

Anchor: 1343 · U29 · L45 · 00:11–03:18

In this lesson, I’ll show a way to clone in perspective. Perspective has to stay correct when we move something from three-dimensional space onto a two-dimensional surface; otherwise, its size will look wrong. We’ll also use the Vanishing Point filter.

Suppose we want to extend this jetty. I first duplicate the background with Command/Control+J and rename the new layer **Clone**. With the Clone Stamp selected, I hold Alt/Option to sample part of the jetty and try to align it. The boards look too large, and when I move to the other side they do not fit. That is why we sometimes need Vanishing Point, which lets us clone in perspective.

![1343 · U29 · L45 · 00:48](frames/U29L45-F0048.00.jpg)

On screen: [none]  
Shows: A short wooden jetty in a mountain lake.

![1343 · U29 · L45 · 01:08](frames/U29L45-F0108.00.jpg)

On screen: "Clone" / "Background" [rest omitted]  
Shows: A first Clone Stamp attempt beside the jetty, with the copied boards out of alignment.

I undo the attempt, open **Filter > Vanishing Point**, and use the tools in its toolbox. There is a Create Plane tool, a Clone Stamp, and a brush for painting in perspective. To make a plane, I look for straight lines that show perspective clearly. On the jetty, I place the first points along the second plank rather than the first: if the first plank is at a slight angle, it can cause a problem. I click on the opposite side, follow the plank lines at the top, and close the plane. A red outline means Photoshop has not accepted the perspective. If one point is slightly out, the whole plane can fail, so I move the point until the lines turn blue and the grid appears. I can then drag the plane outward along the jetty’s edges.

![1343 · U29 · L45 · 03:00](frames/U29L45-F0300.00.jpg)

On screen: "Vanishing Point" / "Grid Size: 100" / "Angle:" / "Click+drag to adjust the plane. Line up the grid with perspective content in the image."  
Shows: A blue perspective grid fitted to the jetty planks, with an inset close-up of the plane.

## Cloning the jetty and correcting its edge

Anchor: 1343 · U29 · L45 · 03:18–06:48

In Vanishing Point, the Clone Stamp has hardness and opacity controls. There is no separate Healing Brush here, but the Clone Stamp has a **Heal** setting. When duplicating or extending something like this jetty, I turn healing off; otherwise Photoshop tries to blend the copy with what is underneath.

I hold Alt/Option and click to sample the jetty. The sample appears on the brush, which I align with the boards. I zoom in with Command/Control+Plus and reposition with the spacebar to use the hand tool. Then I paint. The boards match. A larger brush might have made the job quicker, but even if I go slightly over the edge, I can fix it after returning to Photoshop.

![1343 · U29 · L45 · 04:39](frames/U29L45-F0439.00.jpg)

On screen: "Diameter: 100" / "Hardness: 50" / "Opacity: 100" / "Heal: Off" / "Aligned" [rest omitted]  
Shows: Cloned boards on the jetty inside a green perspective plane.

After clicking **OK** to leave Vanishing Point, I zoom in and see that I missed part of the edge. If this were a finished job, I would return and redo that part.

![1343 · U29 · L45 · 04:48](frames/U29L45-F0448.00.jpg)

On screen: [none]  
Shows: A 200% close view of the jetty's angled left edge and surrounding water, with the brush cursor over the edge.

The grid remains when I reopen Vanishing Point, so I do not have to create the whole plane again.

![1343 · U29 · L45 · 05:01](frames/U29L45-F0501.00.jpg)

On screen: "Click+drag to reposition the plane." [rest omitted]  
Shows: The original jetty plane still displayed with its blue perspective grid after reopening Vanishing Point.

To remove the extra edge of the board, I use the Polygonal Lasso. When closing a lasso selection, I can double-click instead of returning to the first point; Photoshop closes it by the shortest route. Pixel layers do not have a mask by default, so I choose **Layer > Layer Mask > Hide Selection**. Photoshop adds a layer mask and puts black where I made the selection. I have still missed a little area. The jetty may not be perfectly straight after all; lens curvature could be causing it, so I make a few more clicks to follow the edge.

![1343 · U29 · L45 · 05:27](frames/U29L45-F0527.00.jpg)

On screen: "Feather: 0 px" / "Anti-alias" / "Select and Mask..." [rest omitted]  
Shows: A polygonal selection over the water just above the jetty.

For this second selection, **Layer > Layer Mask** no longer offers **Hide Selection**. It would be useful to keep hiding within the mask, but here I fill the selection with black instead.

![1343 · U29 · L45 · 06:13](frames/U29L45-F0613.00.jpg)

On screen: "Layer" / "Layer Mask" / "Hide Selection" [rest omitted]  
Shows: The Layer Mask submenu open with Hide Selection greyed out while an area above the jetty is selected.

The menu command is **Edit > Fill...** (captions: *Edit Film*), then I choose black. I can also use Command/Control+Backspace or Delete. I deselect with Command/Control+D and zoom out. Apart from a small missed edging line, it looks good. Here is the original, and here is the version with the additional cloning.

![1343 · U29 · L45 · 06:25](frames/U29L45-F0625.00.jpg)

On screen: "Edit" / "Fill..." [rest omitted]  
Shows: The Edit menu open with Fill highlighted while an area above the jetty is selected.

![1343 · U29 · L45 · 06:48](frames/U29L45-F0648.00.jpg)

On screen: [none]  
Shows: The extended jetty with its Clone layer mask selected.

## Building a perspective plane from the wall’s lines

Anchor: 1343 · U29 · L45 · 06:48–09:08

Here is another example: extending a wall. A regular Clone Stamp gives us the same problem as before. With a hard brush, I copy and try to match the bricks. At first it looks almost right, although the match with the sky is not perfect and could be fixed later. But at the second set of bricks, the pattern no longer matches. I undo with Command/Control+Z and open Vanishing Point.

This is trickier because the wall does not give us four defined corners. We can use other lines in the image; the plane does not have to follow four visible corners of an object. I zoom in and try to place the points accurately. I can move them later, but accurate placement at the start makes it easier. I put one point above and one below, follow the brick lines, and close the plane by following a line toward the top. Because I paid attention to the lines, the grid turns blue straight away. If it turns red, I reposition the points so Photoshop can find the perspective. I extend the plane upward, sample with Alt/Option, move the copy out, and align it. After clicking **OK**, the wall has been extended in perspective. Look for straight lines or edges when four corners are not defined.

![1343 · U29 · L45 · 06:56](frames/U29L45-F0656.00.jpg)

On screen: [none]  
Shows: A brick house facade with a projecting bay window and roofline.

![1343 · U29 · L45 · 07:18](frames/U29L45-F0718.00.jpg)

On screen: [none]  
Shows: The brick façade and bay window, with the copied courses no longer aligned at the second set of bricks.

![1343 · U29 · L45 · 08:47](frames/U29L45-F0847.00.jpg)

On screen: [rest omitted]  
Shows: A green perspective plane fitted across the house’s brick wall.

![1343 · U29 · L45 · 08:51](frames/U29L45-F0851.00.jpg)

On screen: [none]  
Shows: A close view of the brick wall and bay window after cloning.

## Extending the dock while keeping the woman

Anchor: 1343 · U29 · L45 · 09:08–13:17

The last example is similar to the first. I want to extend this jetty but keep the woman where she is. I can clone the dock and then use a layer mask to bring her back. I duplicate the background with Command/Control+J and call the layer **Jetty extension**. In Filter, I choose Vanishing Point again.

I zoom in with Command/Control+Plus and reposition with the spacebar. I find the edge and drag across it. Again, I use the second board in rather than the edge so I do not introduce an alignment problem. The plane looks right, so I extend it and pick up the Clone Stamp. I hold Alt/Option to sample along the edge, zoom in a little more, and reposition with the spacebar. I intentionally paint over the woman slightly. I can paint across her to just above her knees, and I make sure to cover the dock’s edge completely. It is all right if I go too far; I will clean it up with a mask later.

I resample farther out. If the Clone Stamp stops painting, the plane may need extending to the right. That may be what happened in the first example when I lost the jetty’s edging. I like to share these mistakes because you can learn from them. With the Edit Plane arrow, I select the middle handle to extend the plane. Selecting a corner would move it and alter the plane; I only want to extend it. Then I return to the Clone Stamp and sample the edge again.

The water is darker nearer the foreground. I can mask that area later, or, if I need it, use a Curves adjustment to brighten it. I deliberately paint slightly over the woman and beyond the desired edge. It is better to paint a little too far and clean it up with a mask in Photoshop. Vanishing Point can use more memory and processing, so there can be a lag. I zoom out to check the result. I want the dock to end just above her knee, so I click **OK**.

![1343 · U29 · L45 · 09:34](frames/U29L45-F0934.00.jpg)

On screen: [none]  
Shows: A woman seated on a wooden dock facing a lake and mountains.

![1343 · U29 · L45 · 10:18](frames/U29L45-F1018.00.jpg)

On screen: [rest omitted]  
Shows: A blue perspective plane extending the dock behind the seated woman.

![1343 · U29 · L45 · 11:18](frames/U29L45-F1118.00.jpg)

On screen: [rest omitted]  
Shows: A close view of the plane’s right edge beside the woman and dock.

## Cutting the dock edge and selecting the woman

Anchor: 1343 · U29 · L45 · 13:17–16:50

![1343 · U29 · L45 · 13:21](frames/U29L45-F1321.00.jpg)

On screen: "Jetty extension" / [rest omitted]  
Shows: The extended dock with the seated woman before the edge is masked.

First I cut the dock edge. I zoom in and switch the extension layer off to locate the top of her knee. If I want the dock edge just above the knee, I use this board; if I want it just below, I use a few boards lower. The edge looks too sharp, so I remove some of it with the lasso. Because of the lens curvature, I make a few clicks to keep the curve going. I also remove a dark area, then double-click to close the selection. I choose **Layer > Layer Mask > Hide Selection** to create the edge. I could tidy it more, but it looks fine for now.

When I temporarily hide the extension, one knee is slightly above the edge and the other is slightly below. Rather than painting blindly to find the edge, I hide the layer and select the shape I want. When I turn the layer back on, I can fill that selection into its layer mask.

I use the Quick Selection tool. If **Sample All Layers** is not switched on, this can cause problems, so I make sure it is enabled and make the brush a little smaller. I select the woman’s knee and part of the arm, then do the same on the other side. Turning the layer on shows that I need a little more of the arm but do not need anything at another part of the selection.

Now I want to refine the edge. **Select and Mask** is greyed out; in older Photoshop versions the same dialog is called **Refine Edge**. The menu command is greyed out too.

![1343 · U29 · L45 · 15:56](frames/U29L45-F1556.00.jpg)

On screen: "Select" / "Select and Mask..." [rest omitted]  
Shows: The Select menu open with Select and Mask greyed out.

The reason is that the extension layer is switched off. If I turn it on, Select and Mask becomes available. But I want to see the woman’s legs on the background, so I select the Background layer; now Select and Mask is available.

When cutting something out, I must not select beyond its edge, or I may get an unwanted halo. Zoomed in very close, I can see that the selection is slightly outside the edge. I hold Alt/Option to subtract from it, which improves the selection.

![1343 · U29 · L45 · 16:28](frames/U29L45-F1628.00.jpg)

On screen: "Sample All Layers" / "Enhance Edge" / "Select Subject" [rest omitted]  
Shows: A selection outline around the woman’s body and knees, with an inset close-up of the edge.

## Refining the mask and checking the result

Anchor: 1343 · U29 · L45 · 16:50–19:01

A useful trick when the cutout must not include any background is to choose **Select > Modify > Contract**. We specify how far to contract the selection; typically one pixel is enough. It moves the selection slightly inward. Before continuing, I turn on the extension layer to see whether anything else needs masking. If it does, I can enlarge the selection.

I hide the layer again and open Select and Mask. I set the preview to a white background and raise its opacity all the way, then zoom in. The selection looks rough at first, so I smooth it. I add a little feathering, but not enough to make a soft edge; it helps make the edge more uniform. If the edge becomes too soft, I add contrast to crisp it up.

I activate the layer above and select its mask. I fill the selection into the mask with Command/Control+Backspace or Delete, then deselect to see the result. There may still be things to tidy, but overall it looks convincing. I can compare it with the original by holding Alt/Option and clicking the Background layer’s eye: that shows the original, and switching back shows the extended jetty.

Keeping perspective in mind is important when cloning. In the next lesson, I’ll show how to replace a sky for more dramatic impact in an image.

![1343 · U29 · L45 · 17:20](frames/U29L45-F1720.00.jpg)

On screen: [rest omitted]  
Shows: A close view of the selection around the woman’s knee and sleeve.

![1343 · U29 · L45 · 17:59](frames/U29L45-F1759.00.jpg)

On screen: "Smooth: 12" / "Feather: 1.2 px" / "Contrast: 0%" / "Shift Edge: 0%" [rest omitted]  
Shows: The Select and Mask preview of the selected figure against white.

![1343 · U29 · L45 · 18:50](frames/U29L45-F1850.00.jpg)

On screen: "Density: 100%" / "Feather: 0.0 px" [rest omitted]  
Shows: The woman on the extended dock with the Jetty extension mask selected.
