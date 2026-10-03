# Lesson 29 · Layer Masks 3

Anchor: 1343 · U20 · L29 · 12:25 · https://www.domestika.org/en/courses/1971-course-2-retouching-fundamentals/units/6430-layer-masks#course_lesson_19489

## Adjust only the fox’s color

Anchor: 1343 · U20 · L29 · 00:00–02:46

The fox’s color looks a little faded, and the image is flat because it does not have enough contrast. I will first increase the saturation and make the fox a little redder. In Hue/Saturation I choose Yellows and use the eyedropper to sample the fox. The sampled color falls between yellow and red. I move Hue slightly toward red, then increase Saturation a little.

The before-and-after view shows that the adjustment affects the whole image, including the background. To limit it to the fox, I click the mask and invert it from the Properties panel, or press Command-I on Mac or Control-I on Windows. I select the Brush tool with B, remove its hardness for a soft edge, and make it a little smaller.

There is a common mistake here, and it is not only a beginner’s mistake. I blame Adobe: please add a close button to this window. The way to close it is to click outside it, but if I click on the image, I am using the brush. The mark appears on the layer mask. It may be harmless if I notice, but otherwise it could appear in a later print or publication. I undo with Command-Z or Control-Z.

![1343 · U20 · L29 · 00:32](frames/U20L29-F0032.00.jpg)

On screen: [none]  
Shows: The original fox photograph, before the saturation and contrast adjustments.

![1343 · U20 · L29 · 01:23](frames/U20L29-F0123.00.jpg)

On screen: "Yellows" / "Hue: -6" / "Saturation: +10" / "Lightness: 0" [rest omitted]  
Shows: The Hue/Saturation adjustment on the fox photograph before the mask limits it to the animal.

![1343 · U20 · L29 · 02:07](frames/U20L29-F0207.00.jpg)

On screen: "Size: 105 px" / "Hardness: 0%" [rest omitted]  
Shows: The brush settings window over the fox photograph while the soft brush is being set.

![1343 · U20 · L29 · 02:33](frames/U20L29-F0233.00.jpg)

On screen: "Layer Mask" / "Density: 100%" / "Feather: 0.0 px" / "Hue/Saturation 1" / "Background" [rest omitted]  
Shows: The mask displayed by itself, with the small white brush mark left by clicking the image.

## Paint and inspect the fox mask

Anchor: 1343 · U20 · L29 · 02:46–04:49

Another common mistake is to start painting and see nothing happen. I have the right layer and mask selected, and there is no no-entry symbol, but the foreground color is black. I am painting black onto a black mask. When nothing happens, check that the brush color is right.

I press X to make white the foreground color, start with a slightly larger brush using the square brackets next to P, and brush over the fox. I am not concerned about the grass stems crossing him yet. Once I have the edge, I use a larger brush to fill the middle. It is hard to tell from the image whether I have filled the whole fox, but it is obvious when I inspect the mask: hold Alt or Option and single-click its thumbnail. Here, there are areas I missed. Get into the habit of checking, then Alt- or Option-click again to leave the mask view.

The before-and-after now shows the fox’s color adjustment. This is similar to the earlier apple example, but next I will add contrast to the fox while using only one mask.

![1343 · U20 · L29 · 04:15](frames/U20L29-F0415.00.jpg)

On screen: [rest omitted]  
Shows: The fox mask displayed by itself, with a white painted shape on black; missed areas are visible.

## Share one mask across adjustments in a group

Anchor: 1343 · U20 · L29 · 04:49–07:06

I can put adjustment layers into a group and use one mask for them together. I drag the Hue/Saturation layer to the group symbol. Its indent shows that it is inside the group. I name the group Fox, then drag the mask from the Hue/Saturation layer to the group. When the group has a blue outline, I release the mask there. The Hue/Saturation layer no longer has its own mask; the mask is on the group.

A mask on a group applies to everything inside that group. I can still add another mask to an individual layer, but its effect cannot extend beyond the area allowed by the group mask. This makes it easy to add a Curves adjustment for contrast while keeping it restricted to the fox. Because the curve is inside the Fox group, I can name it Contrast; without the group I would call it something like Contrast on Fox. Although the curve’s own mask is white everywhere, the group mask still limits the result to the fox. Toggle the adjustment or the group to compare.

![1343 · U20 · L29 · 05:24](frames/U20L29-F0524.00.jpg)

On screen: "Fox" [rest omitted]  
Shows: The Fox group is outlined in blue as the Hue/Saturation mask is being dragged onto it.

![1343 · U20 · L29 · 05:27](frames/U20L29-F0527.00.jpg)

On screen: [rest omitted]  
Shows: The fox photograph with the Hue/Saturation adjustment inside a Fox group, whose mask isolates the animal.

![1343 · U20 · L29 · 07:04](frames/U20L29-F0704.00.jpg)

On screen: [rest omitted]  
Shows: The Fox group contains a mask, a Curves adjustment named Contrast, and Hue/Saturation 1.

## Use a mask to replace part of a photograph

Anchor: 1343 · U20 · L29 · 07:06–08:35

We began by using a layer mask to hide or reveal pixels in a cutout. I will now use one in a way similar to cloning. In this field photograph, I want to remove the person. I could use the Clone Stamp or Content-Aware Fill, but matching elements on a diagonal can sometimes be easier with this method. It is also useful when there is only a limited area available to clone from.

![1343 · U20 · L29 · 08:27](frames/U20L29-F0827.00.jpg)

On screen: [none]  
Shows: The field photograph with the person still present and a loose selection around the area to use as a replacement.

## Position and warp a replacement patch

Anchor: 1343 · U20 · L29 · 08:35–10:20

I use the Lasso tool to make a generous selection around the person, going a little above and below him and pulling out a small square. It is fine if the selection is too large; the important thing is to include enough material. Command-J or Control-J copies it to a new layer. With the Move tool, V, I place it where it can replace the person and nudge it with the arrow keys.

Free Transform, Command-T or Control-T, is where this method differs from the Clone Stamp. I can scale, skew, or warp the patch. Right-click for more options. If a line does not match, choose Warp. In the options bar, choose a 3 × 3 grid. The grid boxes let me move a small part of the image so that the lines line up. Press Enter or Return to commit the transform.

![1343 · U20 · L29 · 09:38](frames/U20L29-F0938.00.jpg)

On screen: "Grid" / "Warp: Custom" / "Default" / "3 x 3" / "4 x 4" / "5 x 5" [rest omitted]  
Shows: The field photograph with the selected patch positioned over the person and Warp’s 3-by-3 grid options open.

## Reveal the patch through a mask

Anchor: 1343 · U20 · L29 · 10:20–11:50

I add a layer mask to the patch. With the layer toggled, it does not look good yet: the edges are sharp and there is too much patch showing. I choose Layer > Layer Mask > Hide All to create a black mask, which hides the whole patch layer. Then I use a soft-edged brush at 100% opacity and paint white over the person. The brush seems to paint the person away, but what it actually does is reveal the replacement layer.

Without the mask, the patch looks poor. With it, I only need the patch to look right where it covers the person. This can be more useful than cloning when I need to match lines or very sharp edges.

![1343 · U20 · L29 · 10:27](frames/U20L29-F1027.00.jpg)

On screen: "Layer 1" / "Background" [rest omitted]  
Shows: The person has been removed from the field, with the copied patch on Layer 1.

![1343 · U20 · L29 · 10:39](frames/U20L29-F1039.00.jpg)

On screen: "Layer" / "Layer Mask" / "Hide All" / "Layer 1" / "Background" [rest omitted]  
Shows: The Layer > Layer Mask submenu is open over the field photograph, with Hide All highlighted.

## Keep practicing with masks

Anchor: 1343 · U20 · L29 · 11:50–12:25

By now you should have a better understanding of layer masks, but do not worry if the idea is still difficult. We will return to it throughout the course. Masks are among the most important things to understand properly in Photoshop. The next lesson is about blending images together, including how to do that with layer masks.

![1343 · U20 · L29 · 11:56](frames/U20L29-F1156.00.jpg)

On screen: [rest omitted]  
Shows: The completed field photograph with the person removed and the masked patch layer selected.

### Key points (derived)

- Check both the image and the mask when painting; black hides and white reveals.
- A group mask can constrain several adjustment layers to the same subject.
- A transformed patch with a soft mask can replace a subject when cloning is difficult.
- Inspect masks for missed areas and unintended brush marks.
