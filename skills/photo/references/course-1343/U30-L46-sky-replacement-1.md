# Lesson 46 · Sky Replacement 1

Anchor: 1343 · U30 · L46 · 11:24 · https://www.domestika.org/en/courses/1972-course-3-retouching-environmental-images/units/6447-sky-replacement#course_lesson_19404

## Replacing a flat sky with a new image

Anchor: 1343 · U30 · L46 · 00:11–01:12

*Course 1343 · U30 · L46 · 00:11–01:12*

In this lesson I’ll show how to replace the sky in an image. Doing so can make the image more impactful, especially when its sky is bleak or uninteresting. In the first photograph, a colorful street leads toward the center of the frame beneath a pale, plain sky. I’ll add a new sky to give the scene more interest.

![1343 · U30 · L46 · 00:42](frames/U30L46-F0042.00.jpg)

On screen: “Background” [rest omitted]  
Shows: A colorful street with a pale, plain sky.

First I bring in one of the new skies. I drag its layer onto the photograph’s tab and then into the image. Before releasing the mouse, I hold Shift so Photoshop places the layer in the center of the frame. That is often a useful starting position.

![1343 · U30 · L46 · 00:58](frames/U30L46-F0058.00.jpg)

On screen: [none]  
Shows: The replacement sky photograph, with blue sky, clouds, sea, and beach.

## Selecting the sky and refining the edges

Anchor: 1343 · U30 · L46 · 01:12–04:55

*Course 1343 · U30 · L46 · 01:12–04:55*

I hide the new sky layer while I select the area where it will show, then I’ll apply a mask to the sky layer. I rename the layer “Sky.” I choose the Quick Selection tool with W. If that selects another tool in the same group, holding Shift toggles between the tools. I enlarge the brush with the square bracket keys beside P. The first selection is already a good start.

In the options bar I have Sample All Layers checked. The sky layer is selected but switched off. Many tools will not work on a hidden layer, but Quick Selection works when Sample All Layers is on. I zoom in with Command or Control plus and hold the space bar to use the Hand tool temporarily while I inspect the edges. Where I have missed an area or selected too much, I make the brush smaller. I can choose the minus option in the options bar to subtract from the selection, but I prefer to hold Alt or Option to get the subtract brush.

![1343 · U30 · L46 · 02:01](frames/U30L46-F0201.00.jpg)

On screen: “Sample All Layers” / “Enhance Edge” / “Select Subject” / “Select and Mask...” / “Sky” [rest omitted]  
Shows: A Quick Selection outline follows the tops of the buildings; the cursor is in the pale sky.

There are small details, such as the pole, that I’m not going to bother including in the selection. I’ll show a way to bring missed details back later. Sometimes it is better to leave out something that is very close in color to the background, because it can look strange when the sky is replaced. I reduce the brush and paint where needed. I forgot to hold Alt or Option once, so I undo with Command or Control Z, hold Alt or Option, and paint again. The selection does not need to be absolutely perfect, though I’m trying to make it as good as I can.

![1343 · U30 · L46 · 02:48](frames/U30L46-F0248.00.jpg)

On screen: [none]  
Shows: A 200% close-up of the selection around the distant building roofs.

The Alt or Option key gives me the subtract brush while I paint, so I can remove missed areas from the selection.

![1343 · U30 · L46 · 03:03](frames/U30L46-F0303.00.jpg)

On screen: [none]  
Shows: The selection follows the roofline while the subtract brush cursor is over a rooftop; an enlarged inset shows the brush at the selection edge.

To use Select and Mask, I first select the active Background layer. I open Select and Mask and smooth the selection slightly. I do not want a very soft edge; I want to remove jaggedness.

![1343 · U30 · L46 · 04:29](frames/U30L46-F0429.00.jpg)

On screen: “Smooth: 3” / “Feather: 0.5 px” / “Contrast: 0%” / “Shift Edge: 0%” [rest omitted]  
Shows: The refined sky selection in Select and Mask, with its edge settings visible.

Then I click OK. I zoom out with Command or Control zero, switch the sky layer on, and activate it.

## Masking the sky and adjusting its brightness

Anchor: 1343 · U30 · L46 · 04:55–07:03

*Course 1343 · U30 · L46 · 04:55–07:03*

From Layer, I choose Layer Mask. Here I want to reveal the selection, so Photoshop hides everything else and reveals the sky through the selected area. The result looks artificial at first because the original sky was almost nonexistent and the replacement is deep blue.

I can improve it with an adjustment. If I want to brighten the sky, I choose Curves. If I am ever in doubt, Curves is the tool to use; it is by far the most versatile tool in Photoshop. When I brighten it directly, the whole image becomes brighter. Image adjustments can affect just the selected layer, but they are permanent, so I could not change that adjustment later. Instead, I use a clipping mask. The clipping symbol in the Properties panel clips the adjustment to the layer underneath; an arrow then indicates that the curve is clipped. Adjustments now affect that layer only. A strong curve makes a large difference. To change brightness while retaining more of the color, I set the blend mode to Luminosity. Luminosity tries to keep the color values while changing brightness. Comparing the history states shows the image in Normal and then Luminosity.

![1343 · U30 · L46 · 05:18](frames/U30L46-F0518.00.jpg)

On screen: [none]  
Shows: The street photograph with the replacement blue sky revealed through a layer mask.

![1343 · U30 · L46 · 06:11](frames/U30L46-F0611.00.jpg)

On screen: “Input: 87” / “Output: 157” [rest omitted]  
Shows: The curve brightens the entire street image before it is clipped to the sky layer.

![1343 · U30 · L46 · 07:01](frames/U30L46-F0701.00.jpg)

On screen: “Create Clipping Mask” / “Blending Change” / “Luminosity” [rest omitted]  
Shows: The street and replacement sky after the curve is clipped and its blend mode is changed.

## Repairing missed areas in the mask

Anchor: 1343 · U30 · L46 · 07:03–09:28

*Course 1343 · U30 · L46 · 07:03–09:28*

When I zoom in, I can see small bits I missed. I can continue with Quick Selection on the mask, but I zoom in close and make the brush very small. Photoshop quickly selected the whole layer mask, so I go back to the Background layer and deselect with Command or Control D. I hide the sky layer for a moment to identify the spot I need beside the chimney, then make a small selection.

I can view the mask by holding Alt or Option. The black area is hidden; painting or filling it with white reveals it. I use Command or Control Backspace or Delete to fill the selected area with the background color. Here my background color is white; if I wanted to use the foreground color, I would press Alt or Option Backspace or Delete. When I inspect the result, the edge does not have the same softness as the rest, so I undo with Command or Control Z, open Select and Mask, and add a little smoothing and the same half-pixel feather. After clicking OK, I fill with the white background color again. The missing part now shows through the mask.

![1343 · U30 · L46 · 07:28](frames/U30L46-F0728.00.jpg)

On screen: [none]  
Shows: A 500% close-up of the selection beside the chimney and the edge of the neighboring building.

![1343 · U30 · L46 · 08:50](frames/U30L46-F0850.00.jpg)

On screen: “Select” [rest omitted]  
Shows: The mask displayed in black and white while Select and Mask is opened from the Select menu.

![1343 · U30 · L46 · 09:17](frames/U30L46-F0917.00.jpg)

On screen: [none]  
Shows: The mask with the small selected area beside the chimney filled white.

## Moving the sky, testing blend modes and grouping

Anchor: 1343 · U30 · L46 · 09:28–11:24

*Course 1343 · U30 · L46 · 09:28–11:24*

The link icon connects the sky pixels and the mask. If I want to move the sky without moving the mask, I click the link to unlock them. I choose the Move tool with V. I first move the mask by mistake because the mask thumbnail is still selected. I undo with Command or Control Z, select the sky layer thumbnail so the mask is no longer selected, and move the sky within the mask.

Some parts of the scene have been cut off. With a very light background, Multiply can bring small details back. The Normal and Multiply versions show the difference. Replacing a sky often involves trial and error. Rather than applying a new mask every time, I can put the relevant layers into a group by selecting them and dragging them onto the group symbol at the bottom of the Layers panel.

![1343 · U30 · L46 · 09:50](frames/U30L46-F0950.00.jpg)

On screen: “Sky, Layer Mask/8” [rest omitted]  
Shows: The street composite with the Sky layer mask thumbnail selected while the Move tool is used on the canvas.

![1343 · U30 · L46 · 10:44](frames/U30L46-F1044.00.jpg)

On screen: “Normal” / “Multiply” [rest omitted]  
Shows: The blend mode menu is open with Multiply highlighted while the street image remains in Normal mode.

![1343 · U30 · L46 · 10:53](frames/U30L46-F1053.00.jpg)

On screen: “Opacity: 100%” [rest omitted]  
Shows: A 200% close-up of the roofline with the Multiply blend mode active and the History panel open.

![1343 · U30 · L46 · 11:12](frames/U30L46-F1112.00.jpg)

On screen: [none]  
Shows: The street photograph with the replacement sky and a curve inside the layer stack.

### Key points (derived)

- A selection and layer mask let the replacement sky show through while preserving the buildings.
- Clip Curves to the sky layer; use Luminosity when changing brightness while retaining color.
- Keep the mask separate from the sky pixels when repositioning, and use a group mask when testing several skies.
