# Lesson 66 · Sharpening

Anchor: 1343 · U43 · L66 · 16:15 · https://www.domestika.org/en/courses/1973-course-4-retouching-portraits/units/6466-sharpening#course_lesson_19423

## Sharpening a portrait and preparing the composite layer

Anchor: 1343 · U43 · L66 · 00:11–03:15

In this lesson, I’ll sharpen a portrait selectively. I usually pay more attention to the eyes than to the skin, and I sharpen backgrounds much less than garments. Selective sharpening can feel counterintuitive when a portrait has a shallow depth of field, but I’ll show how to control where it is applied. I’ll begin with my favourite sharpening method, then use another sample where I missed focus. Sharpening cannot refocus an image, although it may help rescue a picture enough to make it usable instead of deleting it.

The first picture has no layers, so I would normally duplicate the Background. To demonstrate a workflow for a layered image, imagine that we have several layers with some cloning and a Curves adjustment. A common mistake is to make a composite of all the layers without first switching off adjustment layers. If the adjustments in the image are quite subtle, you might not notice this straight away. I can create the composite with Shift+Option+Command+E on a Mac, or Shift+Alt+Control+E on Windows.

If I forget to hide Curves, its effect is included in the composite as well as remaining on the original adjustment layer. That doubles the curve, so the image becomes brighter. The History panel calls the composite “Stamp Visible.” To avoid that, hide Curves and any other adjustment layers, select the topmost active layer, and create the composite. On a Mac, use Shift+Option+Command+E; on Windows, use Shift+Control+Alt+E (captions: *Shift+Option+Command+E on Windows*). If the layer beneath is empty, the composite can take over that layer. If it already contains something, such as a clone, that content remains intact when I make the composite.

I rename the composite Sharpen and convert it to a Smart Object so I can change the values later. Converting for Smart Filters does the same thing: it converts the layer to a Smart Object, so I can work with Smart Filters and adjust their settings later (captions: *great at math*; intended wording unclear).

![1343 · U43 · L66 · 01:02](frames/U43L66-F0102.00.jpg)

On screen: [none]  
Shows: A child resting on a grey cushion in a portrait open in Photoshop.

![1343 · U43 · L66 · 02:13](frames/U43L66-F0213.00.jpg)

On screen: "Stamp Visible" / "Curves 1" [rest omitted]  
Shows: The brightened portrait with the History panel open and a Curves adjustment layer above the composite.

![1343 · U43 · L66 · 03:02](frames/U43L66-F0302.00.jpg)

On screen: "Spot Healing Brush" / "Layer 1" [rest omitted]  
Shows: The portrait with a cloned spot; Curves 1, Layer 1 and Background are visible in the Layers panel before the new composite is made.

## Applying High Pass sharpening

Anchor: 1343 · U43 · L66 · 03:15–05:01

To sharpen, I go to Filter, Other, and choose High Pass, which you may have used before. I zoom to 100% with Command+1 or Control+1 and inspect an area that is already in focus. Although the filter dialog has a small preview at 100%, I find it easier to zoom the whole image. I choose a radius that reveals the texture and details. On this portrait, about three pixels works. A lower radius gives a subtler effect; a higher radius gives a stronger one.

There is some colour in the High Pass layer, and that affects the final edit, so I prefer to remove it. I use Image, Adjustments, Hue/Saturation and remove the colour. The difference may be hard to see at first, but increasing the value shows how much colour is present. Because this is a Smart Object, the Hue/Saturation adjustment appears as a Smart Filter.

I change the layer’s blend mode to Overlay. Soft Light gives a subtler result, but Overlay is probably the most commonly used choice. Comparing before and after, the detail comes through clearly. The same sharpening is also being applied to the cushion, the hair and everything else, however, so I’ll use a mask to control it.

![1343 · U43 · L66 · 03:55](frames/U43L66-F0355.00.jpg)

On screen: "High Pass" / "Radius: 2.9 Pixels" [rest omitted]  
Shows: The portrait rendered as a grey High Pass layer, with the radius set to 2.9 pixels.

![1343 · U43 · L66 · 04:25](frames/U43L66-F0425.00.jpg)

On screen: "Hue/Saturation" / "Saturation: -100" [rest omitted]  
Shows: The Hue/Saturation dialog set to remove colour from the High Pass layer.

![1343 · U43 · L66 · 04:51](frames/U43L66-F0451.00.jpg)

On screen: "Overlay" [rest omitted]  
Shows: A close view of the child’s eye and surrounding skin with the sharpening layer visible.

## Controlling the effect with a layer mask

Anchor: 1343 · U43 · L66 · 05:01–07:21

I like to sharpen the whole image, even if it is a little soft, but I want more control over the amount in different areas. I add a mask and fill it with 50% grey. Grey has the same effect as setting the sharpening layer to 50% opacity: it gives half the sharpening effect across the image. I use Edit, Fill, or Shift+F5 (captions: *shift, At five?*), and set the contents to 50% gray. When I compare before and after or switch the layer on and off, sharpening is still present, but it is reduced across the image.

I set my brush opacity and flow to 30%. With a white brush, I paint over the eye to bring the sharpening up to its full effect there. Where I want less sharpening, I paint with black; X swaps the foreground and background colours. For example, I can paint over the cushion. Working at reduced opacity gives me control over how much sharpening I remove. I rarely remove it completely: I prefer to leave some sharpening across the image and apply more to the eyes, lips and similar areas. In this picture the lips are out of focus, so adding more sharpening to them would not make sense. I can turn the Curves layer back on or delete it, since it was not really part of the image. Sharpening is very important and really brings out the best in images. But, as I said, it should not be confused with correcting an image that is out of focus.

![1343 · U43 · L66 · 05:22](frames/U43L66-F0522.00.jpg)

On screen: "Layer Mask" / "Density: 100%" / "Feather: 0.0 px" [rest omitted]  
Shows: The child’s portrait with a new white layer mask selected.

![1343 · U43 · L66 · 05:40](frames/U43L66-F0540.00.jpg)

On screen: "Fill" / "Layer Mask" [rest omitted]  
Shows: The layer mask after it has been filled with grey, leaving the portrait visible.

![1343 · U43 · L66 · 06:23](frames/U43L66-F0623.00.jpg)

On screen: "Opacity: 30%" / "Flow: 30%" [rest omitted]  
Shows: The black brush cursor over the cushion while the mask is painted to reduce sharpening there.

![1343 · U43 · L66 · 07:01](frames/U43L66-F0701.00.jpg)

On screen: "Sharpen" [rest omitted]  
Shows: The child’s portrait as the sharpening layer is compared on and off.

## Trying to rescue a missed-focus portrait

Anchor: 1343 · U43 · L66 · 07:21–10:36

Sharpening is not the same as bringing an out-of-focus image into focus. I would only try this rescue when I had no other option. For example, I photographed a comedian pulling a particular expression, but I slightly missed focus: his mouth is sharp and his eyes are blurred. It makes the image seem almost useless, but it is the only picture I have of him making that face, and I still want to use it.

I duplicate the Background with Command+J or Control+J and name the layer Smart Sharpen (captions: *Smart Shop*), so I’ll remember that I used this to rescue the image. I convert the layer to a Smart Object, go to Filter, Sharpen, and choose Smart Sharpen. The dialog has a 100% preview, but I zoom the whole image to 100% because it is easier to work that way. When I switch Preview on and off, the effect is applied to the image in the main window, not to the dialog’s small preview. This can be confusing if I watch only the small preview and see no change; I need to look at the main image.

The controls are Amount, Radius and Reduce Noise, along with a choice of what kind of blur to remove: Gaussian Blur (captions: *caution blur*), Lens Blur and Motion Blur. This is lens blur, so I select Lens Blur. Amount controls the strength. It is odd that the control uses a percentage rather than a value: how could I remove 200% of lens blur? It does not really make sense, so I think of Amount as a value. Radius controls how far the sharpening spreads. It is often better to bring the Radius fairly high to start with and then reduce it. Here, the Radius is 2.2 and Amount is close to 400%. The eyes look sharper and clearer, but this is not the same as bringing them back into focus. It may make the photo usable at a smaller size, such as on a website, though probably not for a full-resolution print.

I do not need to settle on a perfect value now because the Smart Object lets me change it later. This was shot in a studio, so there is not much noise to reduce. If noise is present, I can reduce some of it by raising the Reduce Noise slider (captions: *slide*).

![1343 · U43 · L66 · 07:39](frames/U43L66-F0739.00.jpg)

On screen: [none]  
Shows: The comedian’s portrait, from the waist up, against a white background.

![1343 · U43 · L66 · 08:17](frames/U43L66-F0817.00.jpg)

On screen: "Smart Sharpen" [rest omitted]  
Shows: A close view of the comedian’s face, with the eyes less sharp than the mouth.

![1343 · U43 · L66 · 10:10](frames/U43L66-F1010.00.jpg)

On screen: "Amount: 397 %" / "Radius: 2.2 px" / "Reduce Noise: 10 %" / "Remove: Lens Blur" [rest omitted]  
Shows: The Smart Sharpen dialog over the comedian’s face, with the eye preview and sharpening settings visible.

## Revealing Smart Sharpen only around the eyes

Anchor: 1343 · U43 · L66 · 10:36–12:19

I select the Smart Filters mask and invert it, which makes the sharpening disappear. Even when the brush is already selected, I tend to press B rather than check first. I press D for the default pure white and pure black, then X to swap between them. Opacity and flow at 30% each work well here.

I start with a fairly large brush and paint around the eyes and eyebrows. Then I make it smaller and gradually build up the effect with the reduced opacity and flow, so more of it is applied in the centre of the eye. To inspect the mask, I hold Alt or Option and click its thumbnail. The eye areas are close to pure white but not quite there, so I add a few more strokes in the centre and use a smaller brush over the eyelashes to bring the full effect there.

Before and after, the result is still not perfect or properly in focus, but I can probably use the image at a smaller size. If someone saw it for the first time, they wouldn’t even notice that it was shot slightly out of focus.

![1343 · U43 · L66 · 10:47](frames/U43L66-F1047.00.jpg)

On screen: "Filter Mask" / "Invert" / "Invert layer mask" [rest omitted]  
Shows: The comedian’s face at 100% after the Smart Filters mask has been inverted, with the black filter mask selected and the sharpening hidden.

![1343 · U43 · L66 · 11:47](frames/U43L66-F1147.00.jpg)

On screen: "Filter Mask" [rest omitted]  
Shows: The black Smart Sharpen filter mask with soft white areas painted over both eyes.

![1343 · U43 · L66 · 12:11](frames/U43L66-F1211.00.jpg)

On screen: "Smart Sharpen" / "Filter Mask" [rest omitted]  
Shows: The comedian’s face with the sharpening effect revealed around the eyes.

## Adding overall sharpening and judging the result

Anchor: 1343 · U43 · L66 · 12:19–16:15

For overall sharpening, I make another composite with Shift+Option+Command+E on a Mac or Shift+Control+Alt+E on Windows, and call it Sharpen. When Photoshop asks about converting it for Smart Filters, it is saying that the layer will be converted into a Smart Object (captions: *smart field to hear*). I usually tick “Don’t show again” on my own machine, but you can leave that unchecked.

I go to Filter, Other, High Pass (captions: *hide paths*) as before and zoom to 100% with Command+1 or Control+1. This image has the same resolution as the previous one. I choose a slightly lower radius, about two pixels, so I do not emphasize the missed focus. Then I desaturate it with Image, Adjustments, Hue/Saturation, setting Saturation to -100, and use Overlay.

I add a mask and fill it with 50% gray using Shift+F5.

![1343 · U43 · L66 · 13:38](frames/U43L66-F1338.00.jpg)

On screen: "Sharpen" / "Add Layer Mask" / "Layer Mask" [rest omitted]  
Shows: The comedian’s full portrait with the new overall Sharpen layer and its mask selected.

With a white brush, I paint over the eyes and eyebrows, add a little more to the lips, and a tiny bit to the hair. I take the eyes all the way to pure white on the mask. The reason I do not paint at 100% opacity is not that I want less than the full effect; I want to build up to it gradually. Think of painting a wall: three coats are better than one very thick coat, which can become streaky and show edges. Retouching is the same. Bold brush strokes are likely to show (captions: *Late*).

![1343 · U43 · L66 · 14:32](frames/U43L66-F1432.00.jpg)

On screen: "Sharpen" / "Layer Mask" / "Brush Tool" [rest omitted]  
Shows: The completed sharpened portrait with the white marks visible on the selected Sharpen layer mask.

I compare the result before and after sharpening. Holding Alt or Option and clicking the Background eye lets me compare the original with the finished version. There is a little noise in the eyes. I could work on that and be more selective, using a mask just along the edges of the iris and pupil to bring out sharp edges without introducing noise. The method is working well overall.

![1343 · U43 · L66 · 15:02](frames/U43L66-F1502.00.jpg)

On screen: "Sharpen" / "Layer Mask" [rest omitted]  
Shows: A 100% close view of the sharpened portrait, including the eyes, iris edges and pupils.

To judge sharpness on a screen, change the image size to the intended pixel count and view it at 100%. To judge how it will look in print, the best way is to print it. For a soft proof on screen, change the image size to the intended print size and view it at 50%. I find that a good way to judge how sharp it will look in print.

I hope you enjoyed learning how to sharpen parts of your images more than others. In the next lesson, I invite you to a challenge where we will put all the different tools we have learned so far on this course together in a practical assignment.
