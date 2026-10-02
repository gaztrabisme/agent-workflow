# Lesson 39 · Vibrance and Hue/Saturation 2

Anchor: 1343 · U26 · L39 · 10:36 · https://www.domestika.org/en/courses/1972-course-3-retouching-environmental-images/units/6439-vibrance-and-hue-saturation#course_lesson_19492

## Select the color of the water

Anchor: 1343 · U26 · L39 · 00:10–01:49

When I took this photograph, the ocean had an amazing turquoise, greenish-blue color. In this lesson I’ll select a color and add those pixels to the picture so I can enhance that specific color. Earlier I used Hue/Saturation to target colors; here I’ll copy pixels and work with them. We can use any selection tool, but I want to show how to select a particular color in an image.

From the Select menu, choose Color Range. The dialog shows a preview of the selection. The Selection Preview is currently set to None, so the image itself does not show the selection. To see it over the image, we can choose Quick Mask, with its red overlay, or a white or black matte. Grayscale is useful as a larger version of the small preview: white means selected, black means deselected, and gray means partially selected. For most things I prefer None and look at the image itself.

![1343 · U26 · L39 · 00:40](frames/U26L39-F0040.00.jpg)

On screen: [none]  
Shows: The original beach photograph, with turquoise water, a sandy shore, distant mountains, and a boat.

## Sample the water and refine the selection

Anchor: 1343 · U26 · L39 · 01:49–03:26

We can click different colors in the image. If I click the sand, it starts appearing as selected in the preview. The Fuzziness slider controls how much of a color is selected: a lower number selects less of the color, while a higher number includes related colors. Start with a low value and increase it.

I’ll sample the turquoise-green water, and often I click a few different areas to see what works best for the image. We can inspect the result in grayscale or Quick Mask. After choosing the color, increase Fuzziness. Some sky appears in this selection; that may not matter for this image. If it does, we can handle it later with the layer mask. A Fuzziness value of 23 looks good for this selection, so I’ll click OK.

![1343 · U26 · L39 · 02:53](frames/U26L39-F0253.00.jpg)

On screen: "Color Range" / "Fuzziness: 16" / "Selection Preview" / "None" / "Grayscale" / "Black Matte" / "White Matte" / "Quick Mask" [rest omitted]  
Shows: The Color Range dialog over the beach image, displaying the sampled water in grayscale with the selection-preview choices open.

![1343 · U26 · L39 · 03:24](frames/U26L39-F0324.00.jpg)

On screen: "Color Range" / "Select: Sampled Colors" / "Fuzziness: 23" / "Selection Preview: None" [rest omitted]  
Shows: The water selection preview with Fuzziness set to 23.

## Correct the selection after it lands on the wrong mask

Anchor: 1343 · U26 · L39 · 03:26–04:34

I made a mistake: the selection was added to the layer mask of the previous layer. We can learn from mistakes in Photoshop, and I include them so I can show how to correct them. We all make mistakes. Here it would be easy to go back in History, undo Color Range, and repeat the selection. It was not difficult to make, and it went into the mask because that mask was selected when I opened Color Range. I should have selected the Background layer first.

If redoing the selection would take extra work, we can reuse it.

![1343 · U26 · L39 · 04:11](frames/U26L39-F0411.00.jpg)

On screen: "Open" / "Color Range" / "Deselect" / "New Vibrance Layer" / "Modify Vibrance Layer" / "Layer Visibility" / "Layer Visibility" / "Color Range" [rest omitted]  
Shows: The beach image with the History panel open and Color Range entries visible.

## Restore a white mask and keep the copied water

Anchor: 1343 · U26 · L39 · 04:34–06:24

Command-click on Mac or Control-click on Windows gives a dotted selection cursor. Clicking loads a luminosity selection, which is basically the selection we had in the dialog. I can then select the Background layer and use Command-J or Control-J to copy those pixels onto a new layer.

The old layer still has the wrong mask, so I’ll make it white. We can fill that mask with white through Edit and Fill. Another option is to delete the mask: no mask has the same effect as a white mask. For simplicity, I can add a new mask and choose Reveal All. That option is available when we create a new mask; it is no longer available when an existing mask is selected. With the Background temporarily switched off, we can see that the copied layer contains the turquoise-green water and a little sky.

![1343 · U26 · L39 · 06:18](frames/U26L39-F0618.00.jpg)

On screen: "Vibrance: +57" / "Saturation: 0" / "Vibrance 1" / "Layer 1" / "Background" / "Indicates layer visibility" [rest omitted]  
Shows: With the Background hidden, the copied turquoise-green water and a little sky sit over transparency.

![1343 · U26 · L39 · 06:24](frames/U26L39-F0624.00.jpg)

On screen: "Vibrance 1" / "Layer 1" / "Background" [rest omitted]  
Shows: The beach photograph and a Layers panel containing a separate pixel layer above the Background.

## Use Soft Light and soften the edges

Anchor: 1343 · U26 · L39 · 06:24–08:50

We can now choose a blend mode that saturates and enhances the water color. The blend-mode menu contains many options. Recent versions of Photoshop preview them; in older versions, either update the software or try the options one by one. Soft Light works well for this. Overlay and Hard Light can also work in some situations, but they can be too harsh. Toggling before and after shows how the water color has come out.

![1343 · U26 · L39 · 07:24](frames/U26L39-F0724.00.jpg)

On screen: "Soft Light" / "Opacity: 100%" / "Layer 1" [rest omitted]  
Shows: The beach image with a turquoise color enhancement and Soft Light selected for the copied layer.

Some edges look harsh because the selection was not feathered. Some colors also look pixelated and blocky.

To fix that, we can blur the copied layer slightly. Go to Filter, Blur, Gaussian Blur. Gaussian Blur is useful for a basic blur. Click in the image to see a preview in the small window.

![1343 · U26 · L39 · 08:24](frames/U26L39-F0824.00.jpg)

On screen: "Gaussian Blur" / "Radius: 9.5 Pixels" / "100%" / "Preview" / "OK" / "Cancel" [rest omitted]  
Shows: The Gaussian Blur dialog with a 9.5-pixel radius over the beach photograph.

Because the layer is on a transparent background, it can be hard to see the blur there, so look at the image itself. Raise the value until the harshness disappears; do not go so far that the image itself looks blurred. Click OK and compare before and after. This is a useful way to enhance one color in an image.

![1343 · U26 · L39 · 08:42](frames/U26L39-F0842.00.jpg)

On screen: "Fill: 100%" [rest omitted]  
Shows: The beach photograph after the selected water color has been blended and softened, with the Layers panel open.

## Make an existing red stand out

Anchor: 1343 · U26 · L39 · 08:50–10:36

For another example, I’ll use a Warner Brothers fire department truck. It already has a vivid red, so it can be difficult to make it stand out more. Red draws our attention, and when a color is already very saturated, we may not be able to bring it out further. Instead, we can reduce the saturation of the other colors.

I’ll add a Hue/Saturation adjustment layer. Since red is the color I want to emphasize, I’ll leave Reds alone and reverse the process: remove the color from Yellows, Greens, Cyans, Blues, and Magentas. That can create an interesting effect by itself. Here I’ll use the layer opacity to fine-tune it. Start with the opacity all the way down, then raise it gradually to reduce the other colors in the image.

![1343 · U26 · L39 · 09:21](frames/U26L39-F0921.00.jpg)

On screen: "Stage / 6" / "3rd Street" / "FIRE DEPT." [rest omitted]  
Shows: A red fire department truck parked on a studio street between tan buildings.

![1343 · U26 · L39 · 10:33](frames/U26L39-F1033.00.jpg)

On screen: "Magentas" / "Saturation: -100" / "Opacity: 35%" [rest omitted]  
Shows: The fire truck remaining red as the surrounding colors are reduced, with the adjustment layer opacity at 35%.

### Key points (derived)

- Color Range creates a pixel selection from sampled colors; check the selection preview and refine Fuzziness before applying it.
- Soft Light can strengthen a selected color, and a slight Gaussian Blur can soften harsh selection edges. To emphasize an already vivid color, reduce other colors and adjust the layer opacity.
