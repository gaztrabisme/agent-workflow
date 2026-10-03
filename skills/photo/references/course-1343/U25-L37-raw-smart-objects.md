# Lesson 37 · RAW Smart Objects

Anchor: 1343 · U25 · L37 · 16:14 · https://www.domestika.org/en/courses/1972-course-3-retouching-environmental-images/units/6438-raw-smart-objects#course_lesson_19395

## Why open RAW images as Smart Objects

Anchor: 1343 · U25 · L37 · 00:00–02:44

In this lesson, I’ll show how to open RAW files in Photoshop as Smart Objects. The benefit is that we can access the RAW data after we have left the RAW converter. In a previous lesson, I briefly showed how to open images as Smart Objects and how to set the workflow options; here I’ll explain why opening as a Smart Object can be useful.

The example is a landscape photo with a very bright sky. Before opening it in Photoshop, I make a few Camera Raw adjustments: lower the exposure a little, open the shadows, darken the highlights and blacks, add some texture and dehaze, and make the colours slightly more vibrant. In the workflow options at the bottom, I check that the bit depth is 16 bits per channel. The option to open in Photoshop as a Smart Object is not checked here. If you don’t want that to be the default, hold Shift: the Open Image button changes to Open Object. Click it, and the image opens as a Smart Object.

Double-clicking the layer thumbnail opens the RAW converter again, so you can continue editing the RAW data. For example, I slightly increase Vibrance and Dehaze, click OK, and Photoshop updates the image. This access to the RAW converter is especially useful with high-contrast landscape photos, where a very bright sky can be difficult to darken while recovering detail.

![1343 · U25 · L37 · 00:58](frames/U25L37-F0058.00.jpg)

On screen: [none]  
Shows: RAW photo of a ship on the water, with a bright overcast sky.

![1343 · U25 · L37 · 01:35](frames/U25L37-F0135.00.jpg)

On screen: "Exposure" "-0.25" / "Highlights" "-33" / "Shadows" "+6" / "Blacks" "-17" / "Texture" "+8" / "Clarity" "+15" / "Dehaze" "+8" / "Vibrance" "+17" [rest omitted]  
Shows: The harbor photo and Camera Raw adjustments.

![1343 · U25 · L37 · 01:59](frames/U25L37-F0159.00.jpg)

On screen: "Workflow Options" / "Color Space" / "Space: Adobe RGB (1998)" / "Depth: 16 Bits/Channel" / "Open in Photoshop as Smart Objects" [rest omitted]  
Shows: Workflow Options dialog over the harbor photo; the Smart Objects checkbox is unchecked.

![1343 · U25 · L37 · 02:11](frames/U25L37-F0211.00.jpg)

On screen: "Open Object" [rest omitted]  
Shows: The Camera Raw Open Object button at the bottom of the window.

![1343 · U25 · L37 · 02:22](frames/U25L37-F0222.00.jpg)

On screen: "Smart Object thumbnail" [rest omitted]  
Shows: The Photoshop layer thumbnail with its Smart Object badge.

![1343 · U25 · L37 · 02:38](frames/U25L37-F0238.00.jpg)

On screen: "Dehaze" "+10" / "Vibrance" "+20" / "Saturation" "0" [rest omitted]  
Shows: Camera Raw with a slight increase to Dehaze and Vibrance.

## Why separate Smart Object copies

Anchor: 1343 · U25 · L37 · 02:44–05:51

To show the problem with ordinary adjustments, I add a Curves adjustment layer and try to darken the sky. I have to push the curve very hard before I recover anything, and the rest of the image becomes very dark. I delete that layer and try an Exposure adjustment instead; darkening the exposure simply makes the whole image go gray. Being able to return to the RAW converter is useful here. I also want to make these changes on separate layers so that I can use layer masks.

I delete the Exposure adjustment layer, then show what happens if I duplicate the layer. I right-click the empty area of the layer and choose Duplicate Layer. I name it “copy,” double-click it to reopen the RAW converter, lower the exposure, and click OK. Photoshop updates the Smart Object, but it also applies the same adjustment to the original Smart Object. I undo that change.

This time I right-click the empty layer area and choose New Smart Object via Copy. Smart Objects created this way work independently. I double-click this copy and make an adjustment while looking at the sky. After I click OK, I can switch the copy off and see the original underneath. The key is to use New Smart Object via Copy instead of simply duplicating the layer.

![1343 · U25 · L37 · 03:09](frames/U25L37-F0309.00.jpg)

On screen: "Curves..." [rest omitted]  
Shows: The adjustment-layer menu with Curves highlighted.

![1343 · U25 · L37 · 03:30](frames/U25L37-F0330.00.jpg)

On screen: "Curves" / "Input: 177" / "Output: 107" [rest omitted]  
Shows: A steep Curves adjustment that darkens the whole harbor photo.

![1343 · U25 · L37 · 03:56](frames/U25L37-F0356.00.jpg)

On screen: "Exposure" "-2.03" [rest omitted]  
Shows: The whole harbor image darkened by the Exposure adjustment.

![1343 · U25 · L37 · 04:10](frames/U25L37-F0410.00.jpg)

On screen: "Duplicate Layer" / "Duplicate: IMG_2633" / "As: cop" / "Document: IMG_2633-1" [rest omitted]  
Shows: Duplicate Layer dialog while the copy name is being entered.

![1343 · U25 · L37 · 04:21](frames/U25L37-F0421.00.jpg)

On screen: "Exposure" "-1.75" / "Highlights" "-33" [rest omitted]  
Shows: The darkened image in Camera Raw while adjusting the duplicated Smart Object.

![1343 · U25 · L37 · 04:30](frames/U25L37-F0430.00.jpg)

On screen: "copy" [rest omitted]  
Shows: The harbor photo darkened after editing the duplicated Smart Object; both the copy and original layers are visible.

![1343 · U25 · L37 · 04:50](frames/U25L37-F0450.00.jpg)

On screen: "New Smart Object via Copy" [rest omitted]  
Shows: The layer context menu open with New Smart Object via Copy listed.

![1343 · U25 · L37 · 05:29](frames/U25L37-F0529.00.jpg)

On screen: "Exposure" "-1.00" / "Highlights" "-49" / "Dehaze" "+23" [rest omitted]  
Shows: Camera Raw adjustments to the sky on the independent Smart Object copy.

![1343 · U25 · L37 · 05:38](frames/U25L37-F0538.00.jpg)

On screen: "IMG_26331" [rest omitted]  
Shows: The original harbor photo after the adjusted Smart Object copy is switched off, with the original layer visible underneath.

## Select and mask the darker sky

Anchor: 1343 · U25 · L37 · 05:51–08:34

To mask the sky, a simple starting point is the Quick Selection tool; I can refine its selection afterward. I make the selection on the layer below because its contrast is greater. I paint across the sky and don’t worry if the ship’s masts are selected too; I can fine-tune the selection later.

![1343 · U25 · L37 · 06:00](frames/U25L37-F0600.00.jpg)

On screen: [rest omitted]  
Shows: Two Smart Object layers in the Layers panel before the sky selection.

A small tower is selected as well, so I make the brush smaller with the left bracket key beside P. Instead of changing tools in the options bar, I hold Alt or Option to get a minus sign and subtract from the selection. I could add that area back, but it will not make much difference. The selection is good enough as a starting point.

I zoom out with Command- or Control-minus (captions: “Commander Control. See you, rome.”). I don’t want a razor-sharp edge, so I open Select and Mask. The edge is very sharp, so I add just a little feathering to create a transition, then click OK.

I activate the layer above, which contains the darker sky. The icon at the bottom of the Layers panel adds a layer mask, but I recommend using the Layer menu because it offers more options: Reveal Selection or Hide Selection. Here I choose Reveal Selection so the darker sky on this layer shows through.

![1343 · U25 · L37 · 06:37](frames/U25L37-F0637.00.jpg)

On screen: "Sample All Layers" / "Enhance Edge" / "Select Subject" / "Select and Mask..." [rest omitted]  
Shows: The Quick Selection tool making a selection across the sky.

![1343 · U25 · L37 · 07:28](frames/U25L37-F0728.00.jpg)

On screen: [none]  
Shows: A zoomed-in view of the brick building, its narrow spires, and the sky behind them.

![1343 · U25 · L37 · 07:51](frames/U25L37-F0751.00.jpg)

On screen: "Feather" "2.7 px" [rest omitted]  
Shows: Select and Mask with a small feather applied to the skyline selection.

![1343 · U25 · L37 · 08:21](frames/U25L37-F0821.00.jpg)

On screen: "Layer Mask" / "Reveal Selection" [rest omitted]  
Shows: The Layer menu’s Layer Mask submenu, with Reveal Selection highlighted.

## Blend the sky and water with gradients

Anchor: 1343 · U25 · L37 · 08:34–14:16

After applying the mask, I compare the result. There’s a useful way to fade it gradually. I edit the layer mask (captions: “mosque”). The default gradient runs from foreground to background, which may mean white to black or black to white. I can choose another gradient in the options bar. These are usually under Basics; if they are not visible at the top, open Basics. I choose Foreground to Transparent and click OK.

I set black as the foreground colour by pressing X. That gives me a black-to-transparent gradient, but I want transparent to black. I prefer to reverse the gradient instead of drawing it in the opposite direction. If I used white-to-black, I would lose the small skyline. With the cursor about halfway down, slightly below that point, I click and drag down while holding Shift to keep the gradient straight. This fades the darker layer gradually into the original sky along the skyline, making the transition more natural. Alt- or Option-clicking the mask thumbnail lets me inspect the mask. I Alt- or Option-click it again to return to the image. In the History panel, I can compare the state before the gradient with the state after it; the transition is smoother.

Right-clicking the layer mask thumbnail gives the option to disable the mask. This lets me see the contents of the masked layer and decide if any other part of the image would benefit from it. The water looks better on this layer too. I can re-enable or disable the mask with Shift-click instead of reopening the menu.

I Alt- or Option-click the layer mask thumbnail (captions: “Leymar’s thumbnail”) to edit it again. This time I want white at the bottom (captions: “Y”) without losing the original skyline, so I turn the reverse option off. I Alt- or Option-click the mask again to leave the mask view (captions: “Mars”), look at the water, press G for the Gradient tool, and drag a straight gradient from about halfway into the water while holding Shift. The effect is too strong: the area above is very bright (captions: “right”) compared with the bottom. I can soften it by painting with gray, since gray on the mask gives a partial effect. The current gray has 50% brightness; to get a value between white and that mid-gray, I enter 75 in the brightness field. I press G again and draw a light-gray-to-transparent gradient as before. The mask is now light gray there and the water effect is milder. The History panel shows the previous gradient and the more subtle one.

![1343 · U25 · L37 · 08:36](frames/U25L37-F0836.00.jpg)

On screen: [none]  
Shows: The darker RAW sky revealed above the original water and skyline.

![1343 · U25 · L37 · 09:16](frames/U25L37-F0916.00.jpg)

On screen: "Gradient Editor" / "Name: Foreground to Transparent" / "Gradient Type: Solid" / "Smoothness: 100%" / "Presets" / "Basics" [rest omitted]  
Shows: Gradient Editor with Foreground to Transparent selected.

![1343 · U25 · L37 · 10:30](frames/U25L37-F1030.00.jpg)

On screen: "Reverse" / "Dither" / "Transparency" [rest omitted]  
Shows: The black-and-white layer mask after drawing the first gradient across the sky.

![1343 · U25 · L37 · 10:41](frames/U25L37-F1041.00.jpg)

On screen: "Layer mask thumbnail" [rest omitted]  
Shows: The harbor image after the sky gradient, with the mask thumbnail visible in the Layers panel.

![1343 · U25 · L37 · 10:50](frames/U25L37-F1050.00.jpg)

On screen: "History" / "Layer Visibility" / "Add Layer Mask" / "Gradient" [rest omitted]  
Shows: The History panel lists the layer-visibility state before the first gradient and the gradient state after it.

![1343 · U25 · L37 · 11:17](frames/U25L37-F1117.00.jpg)

On screen: "Disable Layer Mask" [rest omitted]  
Shows: The mask context menu over the harbor image.

![1343 · U25 · L37 · 11:35](frames/U25L37-F1135.00.jpg)

On screen: "Layer mask thumbnail" [rest omitted]  
Shows: The layer mask is disabled, marked with a red cross in the Layers panel.

![1343 · U25 · L37 · 12:26](frames/U25L37-F1226.00.jpg)

On screen: [none]  
Shows: The mask with the first gradient fading above the skyline, before the water gradient is added.

![1343 · U25 · L37 · 13:38](frames/U25L37-F1338.00.jpg)

On screen: "B:" "75" "%" [rest omitted]  
Shows: The foreground Color Picker with brightness set to 75 percent.

![1343 · U25 · L37 · 13:57](frames/U25L37-F1357.00.jpg)

On screen: [rest omitted]  
Shows: The grayscale layer mask after the lighter gray-to-transparent gradient, with a light gray band fading through the water.

![1343 · U25 · L37 · 14:05](frames/U25L37-F1405.00.jpg)

On screen: [none]  
Shows: The harbor image after the lighter, more subtle gradient is added to the water.

![1343 · U25 · L37 · 14:10](frames/U25L37-F1410.00.jpg)

On screen: "Enable Layer Mask" [rest omitted]  
Shows: The History panel with earlier mask states and the successive gradients used for the sky and water.

## Finish with Curves and compare

Anchor: 1343 · U25 · L37 · 14:16–16:14

To finish the picture, I add two global Curves adjustments from the black-and-white circle at the bottom of the Layers panel. I name the first one Brightness and brighten the image very slightly. I add another curve named Contrast. The highlights are already very bright, so I don’t change them much. The tonal range is gentle and almost everything is light, so I keep the adjustment subtle. I add a point farther down the curve to make the very darkest tones a little darker.

I compare the image before and after the brightness and contrast adjustments by clicking and dragging to turn both adjustment layers off together. To see the original, I Alt- or Option-click the background layer’s eye; then I show the version with the adjustments. That finishes the lesson on working with Smart Objects (captions: “smart rules”). I hope it has given you a better understanding of Smart Objects in Photoshop and why they are useful with RAW files. In the next lesson, I’ll teach Vibrance and Hue/Saturation.

![1343 · U25 · L37 · 14:47](frames/U25L37-F1447.00.jpg)

On screen: "Contrast" / "Brightness" [rest omitted]  
Shows: The two Curves adjustment layers named Contrast and Brightness.

![1343 · U25 · L37 · 15:03](frames/U25L37-F1503.00.jpg)

On screen: "Input: 75" / "Output: 70" [rest omitted]  
Shows: A lower point on the Contrast curve.

![1343 · U25 · L37 · 15:20](frames/U25L37-F1520.00.jpg)

On screen: "Input: 20" / "Output: 12" [rest omitted]  
Shows: The harbor photo before the brightness and contrast adjustments, with both Curves adjustment layers disabled.

![1343 · U25 · L37 · 15:34](frames/U25L37-F1534.00.jpg)

On screen: [rest omitted]  
Shows: The original harbor photo with the Background layer visible and the upper layers hidden.

![1343 · U25 · L37 · 15:40](frames/U25L37-F1540.00.jpg)

On screen: [rest omitted]  
Shows: The finished harbor photo with the background layer and both Curves adjustments visible in the Layers panel.
