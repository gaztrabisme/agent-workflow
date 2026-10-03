# Lesson 77 · Frequency Separation 2

Anchor: 1343 · U51 · L77 · 18:35 · https://www.domestika.org/en/courses/1974-course-5-final-touches-and-useful-tips/units/6475-frequency-separation#course_lesson_19505

## Make the action pause for an image-specific blur choice

Anchor: 1343 · U51 · L77 · 00:13–02:12

When you use the action, remember that you still need to judge how much to blur each image. The action currently applies a 5-pixel Gaussian Blur, but the right value varies. To make yourself choose rather than accept 5 pixels automatically, double-click the Gaussian Blur step and set a very low default, such as 0.1 pixels. Click the small dialog toggle beside the step. Photoshop will then stop at the Gaussian Blur dialog while the action runs, so you can choose the image-specific value. Delete the two layers or the whole group and play the action to see it pause there. Choose the value, click OK, then follow the reminder to set the Clone Stamp to Current Layer and continue.

The Clone Stamp itself was not part of the action, and I quite like that. To make it the tool left active at the end, select another tool, record again, then select the Clone Stamp. Its sample setting does not get recorded, though, so set Sample to Current Layer yourself.

![1343 · U51 · L77 · 01:10](frames/U51L77-F0110.00.jpg)

On screen: "Gaussian Blur" / "Radius: 0.1 pixels" / "Frequency separation" [rest omitted]  
Shows: The Gaussian Blur step is expanded in the Actions panel with the 0.1-pixel radius and its dialog-toggle control visible.

![1343 · U51 · L77 · 01:25](frames/U51L77-F0125.00.jpg)

On screen: "Gaussian Blur" / "Radius: 0.1 Pixels" [rest omitted]  
Shows: The frequency-separation action is paused at the Gaussian Blur dialog so an image-specific radius can be chosen.

## Paint color over the strap line

Anchor: 1343 · U51 · L77 · 02:12–05:01

On the woman’s image, a red line from her strap has pressed into the skin. As in the previous image, where I added a little color to hide some shine, I’ll work with color here. The strap line belongs to Low frequency, so it is a color problem rather than texture. One way to work with the color is to use the regular Brush. Make the brush larger, hold Alt or Option to sample from the image, and paint directly on the Low frequency layer. To keep the work separate and editable, first make a new layer. With the Brush, Alt or Option samples a color from the image; make sure the sampling option is not Point Sample.

The Brush is convenient because you do not need to manage a moving source point: you are painting with color. Keep sampling different nearby colors so the result does not become a flat patch. Raise the opacity to 20% and let the line fade gradually while also evening out the tan line. To blend it, work up and down rather than sweeping left and right across the whole area. Zoom out to compare before and after; it is not quite finished, but the texture has not changed. Name the separate layer strap line. If you want some of the original color back, lower that layer’s opacity. The same approach can even out the paler patches higher on the skin.

![1343 · U51 · L77 · 02:36](frames/U51L77-F0236.00.jpg)

On screen: "Sample: Current Layer" [rest omitted]  
Shows: A close view of the woman’s back and arm with the red strap line pressed into the skin; it is visible near the strap in the main view and in the zoomed inset, where the cursor marks a sample point.

![1343 · U51 · L77 · 04:30](frames/U51L77-F0430.00.jpg)

On screen: "Mode: Normal" / "Opacity: 20%" / "Flow: 100%" [rest omitted]  
Shows: The woman’s back and arm during the low-frequency color-painting pass.

## Even color with the Mixer Brush or a feathered selection

Anchor: 1343 · U51 · L77 · 05:01–09:23

For the paler patches, I’ll show a different method. Duplicate the layer before working directly on it if you want a more editable version. Use the Mixer Brush, which you may remember from an early lesson where we copied a red rose as an oil painting; it is also used in high-end retouching. Brush presets do not always work with every Mixer Brush, so choose one that behaves as needed. Set it to clean after each stroke and lower Flow to 10%. Each stroke samples the color and blends the colors together. The change may be subtle, so compare before and after or zoom out to see the more even skin tone. It can look odd if only one area is evened out while the rest is not. Some people prefer this technique; others prefer the regular Brush. The Mixer Brush cannot work on a blank layer or across layers, so use a duplicate of Low frequency.

Another option is the Lasso. Set it to the first selection mode and add 10 pixels of feather so the selection does not have a sharp edge. Circle a blotchy patch of skin on the arm, then use Filter, Blur, Gaussian Blur—about 8 pixels here. The first lasso option automatically clears the previous selection as you begin the next one, so you do not have to deselect by hand. Circle another area and apply the previous filter with its last-used setting. Photoshop shows that filter at the top of the Filter menu. In older Photoshop versions, Command-F or Control-F applied the last filter; in newer versions that shortcut opens search, so use Option-Command-F or Alt-Control-F instead. Deselect with Command-D or Control-D. Keep circling areas and applying the blur, but do not raise it too much or the skin will look fake.

![1343 · U51 · L77 · 05:41](frames/U51L77-F0541.00.jpg)

On screen: "Wet Media Brushes" / "KYLE's Real Oils Round Flex Wet" [rest omitted]  
Shows: The Mixer Brush preset panel is open with a wet-media brush selected.

![1343 · U51 · L77 · 06:17](frames/U51L77-F0617.00.jpg)

On screen: "strap line" [rest omitted]  
Shows: The woman’s back after the color pass, with the separate strap-line layer visible in the layer stack.

![1343 · U51 · L77 · 08:17](frames/U51L77-F0817.00.jpg)

On screen: "Feather: 10 px" / "Anti-alias" [rest omitted]  
Shows: A feathered lasso selection circles a patch of skin on the woman’s arm and back.

## Shape the portrait with Liquify

Anchor: 1343 · U51 · L77 · 09:23–12:29

In the last image, some work is already done. The original is shown alongside skin-tone corrections and notes. The blue lines mark where Liquify can shape the image, and that is typically where I suggest starting. Get approval from the client or the person you work for before making large changes with Liquify, especially substantial slimming of arms or legs. Small adjustments, such as fixing clothing or trimming something slightly, do not need the same sign-off.

Switch off the notes and adjustment layers for a moment. Duplicate the image layer, name it Liquify, then right-click in an empty area and make it a Smart Object; alternatively, choose Filter, Convert for Smart Filters. Photoshop shows a warning dialog. I usually check the box but leave it unchecked here. Choose Filter, Liquify.

To change the jawline, the woman’s hand has created an awkward shape at her chin. Push it out slightly with the Forward Warp tool. Make the brush smaller and use fairly high Density to move the area together. Work gradually, pushing some parts in and others out. Press P to preview. Keep the suggestion that the skin is pushed in, but make it less extreme.

To slim or push the arm, use the Push Left tool (which I call the “Push Pixel” tool). Make the brush smaller. Painting from bottom to top pushes left; painting from top to bottom pushes right. Paint from the top down to push the arm in, and use P to compare. Then paint from the bottom up where you want to push left. Keep the change small: because the arm is closer to the camera, it looks a little larger than it would in real life. Click OK and compare before and after.

![1343 · U51 · L77 · 09:32](frames/U51L77-F0932.00.jpg)

On screen: "Darken" / "Notes" / "Adjustments" [rest omitted]  
Shows: An annotated portrait of a blonde woman in a black dress, with colored marks on her face and arm and green lines around the figure.

![1343 · U51 · L77 · 10:30](frames/U51L77-F1030.00.jpg)

On screen: [none]  
Shows: The blonde woman’s original portrait against a dark gray background, before the Liquify adjustments.

![1343 · U51 · L77 · 12:16](frames/U51L77-F1216.00.jpg)

On screen: "Liquify" / "Size: 250" / "Density: 50" [rest omitted]  
Shows: Photoshop’s Liquify workspace is zoomed in on the woman’s bent arm and dress, with brush options at the right.

![1343 · U51 · L77 · 12:22](frames/U51L77-F1222.00.jpg)

On screen: "Smart Filters" [rest omitted]  
Shows: The full portrait after Liquify, with the Liquify Smart Filter listed beneath the selected Liquify layer.

## Place frequency separation in the retouching workflow

Anchor: 1343 · U51 · L77 · 12:29–14:08

When you make the frequency separation, switch off the adjustments first. A composite or Stamp Visible includes every layer that is turned on. Then zoom to 100%, choose the image-specific blur radius—about 4.5 pixels works here—and run the action. When the reminder appears, set the Clone Stamp to Current Layer. The action change has taken effect and has selected the Clone Stamp. Turn the adjustments back on; they can help you spot whether any of them need to be changed to match the retouching.

That is how frequency separation fits into a workflow: make the ordinary layers and adjustments first. Do Liquify either at the beginning, at the bottom of the layer stack, or at the very end. If you have already made frequency separation and other adjustments, you can put a new composite layer above them and Liquify that. This lets Liquify affect the whole result.

![1343 · U51 · L77 · 13:17](frames/U51L77-F1317.00.jpg)

On screen: "Workflow" / "Dodge & Burn" / "Frequency Separation" [rest omitted]  
Shows: The portrait with notes and adjustments hidden, the Liquify layer beneath the frequency layers, and the three action buttons in the Actions panel.

## Remove flyaway hairs and finish the workflow

Anchor: 1343 · U51 · L77 · 14:08–18:35

I’ll also show a couple of tips for flyaway hairs. This work sits outside and above frequency separation, although I would usually do it before frequency separation. Add a new layer called flyaway hairs. Use the Clone Stamp with Sample set to Current and Below and a fairly large, soft brush. Follow the background gradient. The file is a somewhat poor-quality JPEG, so it has noise; the clone will not match perfectly, but that is fine. To start, clone well into the hair, even across the hand. The cloned area looks a little strange at first and is darker than the background.

![1343 · U51 · L77 · 15:17](frames/U51L77-F1517.00.jpg)

On screen: "Fly away hairs" [rest omitted]  
Shows: A close crop of the woman’s portrait as a clone patch extends over the dark gray background beside her hair.

An adjustment layer affects all the layers below it, but this correction should affect only the cloned area. Choose Layer, New Adjustment Layer, Curves and use the dialog to clip it to the flyaway-hair layer. Name it flyaway match. Brighten it a little; if the change is too strong, reduce it until the background is a better fit. Toggle it off and on to check. It may not be perfect, but clipping the adjustment makes the match more seamless.

Add a black layer mask by holding Option or Alt and clicking the layer-mask thumbnail. Use the regular Brush (B); here, Shift-B is needed to switch to the normal brush. Set it to 100% opacity and paint on the mask to remove the flyaways. On a plain white background, this is quick. On a gradient, lower the flow and use broader strokes to connect the retouched area to the rest of the image. If a stroke spills, press X to switch to black and use a slightly harder brush to paint it back. This is a quick, efficient way to handle flyaways, with the clipped adjustment layer matching the background.

For this workflow, make the basic color and tone adjustments first, then Liquify near the bottom of the layer stack, and frequency separation above that. If you have not liquified and need to do it later, put Liquify at the top of the adjustments: make a new blank layer and press Shift-Option-Command-E on Mac or Shift-Control-Alt-E on Windows to stamp the visible result into it. If a layer mask depends on the image beneath it, that image must be liquified too, which is why the composite layer goes above everything. Do not worry if frequency separation has not clicked yet; it takes practice, and the action helps you repeat the steps. In the next lesson I’ll show you how to create perfect-looking lips.

![1343 · U51 · L77 · 16:17](frames/U51L77-F1617.00.jpg)

On screen: "fly away match" [rest omitted]  
Shows: The flyaway-hair mask is selected on the blonde woman’s portrait, with a clipped matching layer above it.

![1343 · U51 · L77 · 17:47](frames/U51L77-F1747.00.jpg)

On screen: "No Properties" [rest omitted]  
Shows: The finished portrait is visible with the Adjustments group collapsed; the clipped fly away match and Fly away hairs layers are listed, and the Properties panel reads “No Properties.”
