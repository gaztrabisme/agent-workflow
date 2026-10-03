# Lesson 25 · Selections 3

Anchor: 1343 · U19 · L25 · 10:58 · https://www.domestika.org/en/courses/1971-course-2-retouching-fundamentals/units/6426-selections#course_lesson_19486

## Channels and luminosity selections

Anchor: 1343 · U19 · L25 · 00:00–02:31

Hair is one of the hardest things to cut out, and curly hair can be especially tricky. For more complex selections, I use channels. By default, the Channels panel sits beside Layers. It contains the Red, Green and Blue channels, as well as the composite RGB channel. An image is made from three black-and-white transparencies with red, green and blue light added to them. Photoshop displays the channels without their colour because they are mostly useful for making selections.

These are often called luminosity selections: selections based on brightness values. I look for the channel with the greatest separation between the subject and the background, especially at the subject's edges. In this portrait, there is not a great deal of difference between the channels, but Blue gives slightly more contrast than the others. The Select and Mask view uses white for selected pixels, black for deselected pixels and grey for partial selection. Here, the background and her skin are mostly selected, while her hair and clothes are mostly black and therefore deselected.

![1343 · U19 · L25 · 00:36](frames/U19L25-F0036.00.jpg)

On screen: "Layers" / "Channels" / "Paths" [rest omitted]  
Shows: The original colour portrait of a curly-haired woman, with the Channels tab indicated in the Photoshop panel.

![1343 · U19 · L25 · 02:10](frames/U19L25-F0210.00.jpg)

On screen: "Red" / "Green" / "Blue" [rest omitted]  
Shows: The portrait displayed in grayscale with the Blue channel selected; its bright background contrasts with the darker hair and clothing.

## Build contrast in a copied channel

Anchor: 1343 · U19 · L25 · 02:31–04:36

Before changing the channel, I make a copy by dragging it to the plus icon at the bottom of the Channels panel. The copy is called Blue copy. Then I choose Image > Adjustments > Levels. Think back to the tool for changing the brightness of white and the darkness of black: Levels is the one to use.

I can use the histogram to see where the image information begins, but here I want to clip some information. As I move the black point and make parts darker, I zoom in to check the fine strands in the hair. If I move the control too far, those details clump together. I push it as far as I can without losing the fine detail. I do the same with white: zoom in and avoid removing too much detail. Ideally, I would remove the texture in the background without losing the hair texture, but that may not be possible. Then I click OK.

![1343 · U19 · L25 · 03:17](frames/U19L25-F0317.00.jpg)

On screen: "Levels" / "Preset: Custom" / "Channel: Blue copy" / "Input Levels: 33 / 1.00 / 255" / "Output Levels: 0 / 255" [rest omitted]  
Shows: The Blue copy channel in Levels, with the black input value adjusted while the portrait is displayed in grayscale.

![1343 · U19 · L25 · 03:58](frames/U19L25-F0358.00.jpg)

On screen: "Input Levels: 61" [rest omitted]  
Shows: A close-up of the curly hair and the Levels dialog as the black point moves further, making it possible to judge when the fine strands start to clump.

## Load the channel as a selection and correct the mask

Anchor: 1343 · U19 · L25 · 04:36–08:17

I zoom back out with Command or Control+0. The dotted-circle button at the bottom of the Channels panel loads the channel as a luminosity selection: white is selected, black is deselected, and grey is partly selected. I click it, turn the RGB channel back on and return to Layers.

![1343 · U19 · L25 · 05:10](frames/U19L25-F0510.00.jpg)

On screen: [rest omitted]  
Shows: The portrait in the copied Blue channel after Levels, with the subject dark against a nearly white background.

I made a mistake by not duplicating the background first. I want to keep the original image, so I can correct this without starting over. I want to keep mistakes on screen because we learn a lot from them in Photoshop. Rather than starting over, I want to teach how to solve mistakes. Command or Control+J is Layer via Copy, not Duplicate Layer: in the Layer menu, Duplicate Layer has no shortcut, while Layer via Copy uses Command or Control+J. I choose Duplicate Layer and name it “Cut out” (captions: “Cat out”). This duplicates the whole layer, not just the selected content. I demonstrate the difference by using Command or Control+J, then undo it and reload the selection.

![1343 · U19 · L25 · 06:47](frames/U19L25-F0647.00.jpg)

On screen: "Cut out" / "Background" [rest omitted]  
Shows: Marching ants remain around parts of the woman while the Layers panel shows a new Cut out layer above Background.

Now I click Add Layer Mask.

The mask thumbnail matches the earlier Blue channel: white is selected and black is deselected. When I hide the background, I see that the wall has been cut out instead of the model. I invert the mask with Command or Control+I, or use Invert in the Properties panel. Now the model is cut out; the skin on her hand is only partly selected, but the hair is coming through quite nicely. We will look at layer masks more later, so it is all right if this is not clear yet.

![1343 · U19 · L25 · 07:38](frames/U19L25-F0738.00.jpg)

On screen: "Masks" / "Layer Mask" / "Density: 100%" / "Feather: 0.0 px" / "Color Range..." / "Invert" [rest omitted]  
Shows: The wrong result of the mask: the model appears transparent while the wall remains, with the mask controls open in Properties.

## Edit the layer mask directly

Anchor: 1343 · U19 · L25 · 08:17–10:58

It can help to inspect a mask directly. Hold Alt or Option and click the mask thumbnail to view it. I can then fill areas in the mask. For example, I could use the Lasso tool to select the area, taking care to make that edge more accurate, and fill it with white through Edit > Fill by setting Contents to White. I deselect with Command or Control+D.

![1343 · U19 · L25 · 08:34](frames/U19L25-F0834.00.jpg)

On screen: [rest omitted]  
Shows: The corrected cutout of the model against a checkerboard transparency grid, with the background layer hidden.

The Quick Selection tool can also help. I make its brush a little larger with the square brackets beside P and paint in the area, taking care to reach the edge. I avoid painting over the fine detail in the hair; the tool does a good job in this area. I switch to the Lasso tool, set it to Subtract, and draw around the hair to remove that part from the fill. Then I switch to Add to Selection and add the glasses, making sure not to fill the part that should stay open. I use Edit > Fill with Contents set to White, click OK and deselect. Alt- or Option-clicking the mask thumbnail again returns to the image. The cutout is beginning to look good, including the fine detail in the hair.

![1343 · U19 · L25 · 09:25](frames/U19L25-F0925.00.jpg)

On screen: [rest omitted]  
Shows: The layer mask viewed directly as a white silhouette against black, with the hand and glasses retaining grey detail.

![1343 · U19 · L25 · 10:05](frames/U19L25-F1005.00.jpg)

On screen: [rest omitted]  
Shows: A lasso outline over the black-and-white mask around the model's hair and face during the mask cleanup.

![1343 · U19 · L25 · 10:47](frames/U19L25-F1047.00.jpg)

On screen: [rest omitted]  
Shows: The finished colour cutout of the woman on a checkerboard transparency grid, with the fine curly-hair edge retained.
