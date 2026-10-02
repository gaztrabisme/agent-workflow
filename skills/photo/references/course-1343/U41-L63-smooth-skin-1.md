# Lesson 63 · Smooth Skin 1

Anchor: 1343 · U41 · L63 · 15:57 · https://www.domestika.org/en/courses/1973-course-4-retouching-portraits/units/6463-smooth-skin#course_lesson_19420

## Set up a separate cleanup layer and test Spot Healing

Anchor: 1343 · U41 · L63 · 00:00–02:33

The teacher introduces a few simple, effective ways to soften skin in portraits. Photoshop has no magic filter that produces perfect skin, but careful editing can get close to very good skin. For a fair comparison, he opens two pictures of the same woman in the same light. Skin softening belongs near the end of a retouching workflow.

He begins with ordinary skin cleanup. Create a new layer with Shift+Command+N, or Shift+Control+N on Windows, and name it “Clean up” or another clear name. Zoom to 100% with Command/Control+1, then hold Spacebar to reposition the canvas. The Spot Healing Brush is quick and often gives good results, but watch the image as you work. Reduce brush size with the square bracket keys. Because “Clean up” is an empty layer, enable Sample All Layers in the options bar; without sampling across layers, the tools will not work on this blank layer. Working on a duplicate background has advantages.

The first Spot Healing result on the skin is poor. That is a limitation of the tool: it can work well against a simple background but fail against complex skin. Undo the marks with Command/Control+Z.

![1343 · U41 · L63 · 00:55](frames/U41L63-F0055.00.jpg)

On screen: [none]  
Shows: The portrait open in Photoshop, with two document tabs for the same model.

![1343 · U41 · L63 · 01:35](frames/U41L63-F0135.00.jpg)

On screen: “Clean up” / “Sample All Layers” [rest omitted]  
Shows: The portrait on a blank Clean up layer, with the Spot Healing Brush options visible.

![1343 · U41 · L63 · 02:07](frames/U41L63-F0207.00.jpg)

On screen: [rest omitted]  
Shows: Close view of the portrait during the Spot Healing Brush attempt.

## Finish cleanup before softening skin

Anchor: 1343 · U41 · L63 · 02:34–04:13

Switch to the Healing Brush, set its sample to Current & Below, and enable Aligned. Hold Alt/Option and click to sample nearby skin; the result looks much better. The teacher is demonstrating rather than completing a full retouch, so he does not remove every small mark. For a paid job, he would remove every bump that does not belong in the image. A skin-softening filter does not replace clone work. He recommends doing the softening as the final step in the workflow. For example, if the subject’s teeth need a little cleanup or bleaching, do that first; he briefly demonstrates teeth whitening here.

![1343 · U41 · L63 · 02:37](frames/U41L63-F0237.00.jpg)

On screen: “Aligned” / “Use Legacy” / “Sample: Current Layer” [rest omitted]  
Shows: The Healing Brush options before the teacher changes the sample setting and enables Aligned; both checkboxes are off.

![1343 · U41 · L63 · 03:02](frames/U41L63-F0302.00.jpg)

On screen: [rest omitted]  
Shows: The Healing Brush cursor over a small blemish on the model’s chin.

## Whiten the teeth with a masked Hue/Saturation adjustment

Anchor: 1343 · U41 · L63 · 04:14–07:42

The teeth look yellow, so create a Hue/Saturation adjustment layer to bleach them. The teacher names the layer “Teeth whiten” (the captions misrender this as “Peace Monaghan”). Photoshop’s target adjustment tool can select a color range: clicking the teeth first selects Yellows, but that uses the default yellow range. The eyedropper samples the specific yellow in the teeth, so it is different from the target adjustment tool. After sampling, the range bar centers around the clicked color.

To avoid affecting nearby colors, use the subtract eyedropper and click the small flesh-colored areas. This narrows the color range and makes masking easier, although the mask is still necessary. The goal is to remove the yellow color, like bleaching, rather than change it to a different color. Lower saturation; about −30 looks reasonable. Lighten the teeth slightly as well. At this stage the whole selected yellow range is affected, including skin, so the skin looks bleached until it is masked.

Invert the layer mask from the Properties panel or press Command/Control+I. Select the Brush with B and reset the foreground/background colors with D to pure black and white. Set brush opacity to 50% by pressing 5. Paint white over the teeth; at reduced opacity, go over them a few times to build the effect. The narrower color range makes the mask easier: a little spill onto lips or other fleshy tones is acceptable as long as the brush does not touch the skin. The before-and-after shows an easy, subtle tooth bleach (the captions render “after” as “often”).

![1343 · U41 · L63 · 04:32](frames/U41L63-F0432.00.jpg)

On screen: “Hue/Saturation” / “Teeth whiten” [rest omitted]  
Shows: The close portrait with the Hue/Saturation adjustment layer selected.

![1343 · U41 · L63 · 04:43](frames/U41L63-F0443.00.jpg)

On screen: “Hue/Saturation” / “Preset: Default” / “Yellows” / “Hue: 0” / “Saturation: 0” / “Lightness: 0” [rest omitted]  
Shows: The default Yellows range selected after the target adjustment tool is used on the teeth, with an inset of the controls.

![1343 · U41 · L63 · 05:17](frames/U41L63-F0517.00.jpg)

On screen: “Yellows” [rest omitted]  
Shows: The sampled yellow range and eyedropper controls beside the portrait.

![1343 · U41 · L63 · 05:45](frames/U41L63-F0545.00.jpg)

On screen: [rest omitted]  
Shows: The narrowed Yellows range in the Hue/Saturation controls.

![1343 · U41 · L63 · 06:05](frames/U41L63-F0605.00.jpg)

On screen: “Hue/Saturation” / “Custom” / “Yellows” / “Hue: 0” / “Saturation: -29” / “Lightness: 0” [rest omitted]  
Shows: The Hue/Saturation adjustment affecting the close portrait before its mask is inverted.

![1343 · U41 · L63 · 06:32](frames/U41L63-F0632.00.jpg)

On screen: “Select and Mask...” / “Color Range...” / “Invert” / “Invert layer mask” [rest omitted]  
Shows: The layer-mask Properties controls and the Invert layer mask tooltip.

![1343 · U41 · L63 · 07:32](frames/U41L63-F0732.00.jpg)

On screen: “Opacity: 50%” [rest omitted]  
Shows: A brush cursor on the teeth with the black adjustment mask selected.

## Make a composite layer before applying the blur

Anchor: 1343 · U41 · L63 · 07:43–09:23

Before softening, hide adjustment layers. The teeth adjustment is not affecting skin in this example, but the teacher shows the step so the workflow is clear. Select the uppermost active layer: because “Teeth whiten” is not active, “Clean up” is the uppermost active layer. Create a composite from all visible, active layers with Shift+Option+Command+E, or Shift+Alt+Control+E on Windows. This places the visible image on one layer while retaining the layers underneath, similar to flattening without losing the separate layers. Name the new layer “Skin soften” so its purpose is clear.

![1343 · U41 · L63 · 08:02](frames/U41L63-F0802.00.jpg)

On screen: [rest omitted]  
Shows: The portrait with the Teeth whiten adjustment mask above the Clean up layer.

![1343 · U41 · L63 · 08:32](frames/U41L63-F0832.00.jpg)

On screen: [rest omitted]  
Shows: The Clean up layer selected above the background while the teacher prepares the composite.

![1343 · U41 · L63 · 09:23](frames/U41L63-F0923.00.jpg)

On screen: “Skin soften” [rest omitted]  
Shows: The new Skin soften layer selected above Clean up and the background.

## Choose the lowest useful Gaussian Blur value

Anchor: 1343 · U41 · L63 · 09:23–10:48

Apply Filter > Blur > Gaussian Blur to the composite layer. The dialog opens with the last-used value, about 340 pixels, which is far too high here. Zoom the image to 100% with Command/Control+1. Although the dialog has a 100% preview if you click the image, the teacher prefers to zoom the canvas itself. Raise the blur only until the skin tones blend together, keeping the value as low as possible. In this image, about 9 pixels is enough. The right value depends on the image size and what the retoucher plans to do. After applying it, the result is too strong.

![1343 · U41 · L63 · 09:36](frames/U41L63-F0936.00.jpg)

On screen: “Gaussian Blur” / “Radius: 341.6 Pixels” [rest omitted]  
Shows: The Gaussian Blur dialog with its last-used radius before it is lowered.

![1343 · U41 · L63 · 10:22](frames/U41L63-F1022.00.jpg)

On screen: “Gaussian Blur” / “Radius: 9.1 Pixels” [rest omitted]  
Shows: The portrait preview with Gaussian Blur set to a low radius.

## Add editable noise to bring back a natural texture

Anchor: 1343 · U41 · L63 · 10:49–12:52

Zoom in very close with Command/Control and the plus key to inspect the pixels. Turn off the pixel grid through View > Show > Pixel Grid. With the blur layer off, individual pixels underneath each have a different color; with the blur on, they become a flat color. That flatness explains why Gaussian Blur can get a “plastic” look and a bad reputation. The next step makes the result more natural.

Convert the layer to a Smart Object by right-clicking an empty area of its layer row and choosing Convert to Smart Object. This keeps the filter editable, so its settings can be changed later. Apply Add Noise and aim for texture similar to the original. Uniform and Gaussian distributions render slightly differently; Uniform usually works well. Choose Monochromatic, then raise the amount until the texture is closer to the original, around 1.5 here. Toggle the effect to compare it with the original. Zoom back out to 100% with Command/Control+1 and hold Spacebar to reposition.

![1343 · U41 · L63 · 10:57](frames/U41L63-F1057.00.jpg)

On screen: [rest omitted]  
Shows: A magnified patch of skin with the pixel grid visible.

![1343 · U41 · L63 · 11:15](frames/U41L63-F1115.00.jpg)

On screen: [rest omitted]  
Shows: The original skin texture enlarged to show differently colored pixels.

![1343 · U41 · L63 · 11:52](frames/U41L63-F1152.00.jpg)

On screen: “Embedded Smart Object” [rest omitted]  
Shows: The enlarged, smooth skin tone on the Smart Object layer before noise is applied.

![1343 · U41 · L63 · 12:42](frames/U41L63-F1242.00.jpg)

On screen: “Add Noise” / “Amount: 1.5 %” / “Uniform” / “Monochromatic” [rest omitted]  
Shows: The noise preview over the enlarged skin texture with a 1.5% monochromatic Uniform setting.

## Paint the softening through a black mask and reduce its strength

Anchor: 1343 · U41 · L63 · 12:53–15:57

Zoom back out to 100% and reposition the image. Add a black mask by holding Alt/Option while clicking the layer-mask icon at the bottom of the Layers panel. Select the Brush and lower both opacity and flow: press 3 for 30% opacity and Shift+3 for 30% flow, or set them in the options bar. Paint with white and a soft brush. Increase the brush size slightly and paint only where the skin texture should be reduced.

Follow the direction and shape of the skin as if applying makeup rather than brushing back and forth over the whole image; this tends to look more natural. Do not remove all the texture. The teacher paints only areas that need softening, then reduces the layer opacity to 50% by default because the full-strength effect usually looks too strong. Raise it if more softening is needed or lower it if the effect is still too much. Turn the teeth-whitening layer back on and compare before with after. The skin texture remains, though reduced: at 50% opacity, at least half of the original skin texture remains everywhere in the image. A softer look is possible by increasing opacity, but going too high can look fake.

![1343 · U41 · L63 · 13:54](frames/U41L63-F1354.00.jpg)

On screen: “Opacity: 30%” / “Flow: 30%” [rest omitted]  
Shows: The black mask selected while the soft brush is applied across the portrait.

![1343 · U41 · L63 · 15:54](frames/U41L63-F1554.00.jpg)

On screen: “Opacity: 50%” / “Opacity: 30%” / “Flow: 30%” [rest omitted]  
Shows: The finished portrait with the skin-softening layer at 50% and teeth whitening visible.
