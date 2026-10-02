# Lesson 34 · Local Edits in the RAW Converter 1

Anchor: 1343 · U24 · L34 · 15:13 · https://www.domestika.org/en/courses/1972-course-3-retouching-environmental-images/units/6436-local-edits-in-the-raw-converter#course_lesson_19393

## Plan the edit before opening Camera Raw

Anchor: 1343 · U24 · L34 · 00:10–05:03

I’m going to show the local editing tools in Adobe Camera Raw. They are useful when you want to bring out specific areas, such as very dark shadows or very bright highlights. I’ll also show how to open a RAW file straight into Photoshop as a smart object and then bring it back into the RAW converter after opening it in Photoshop.

Before returning to the RAW converter, I want to explain how I plan an edit. I find it easier to visualize this in Photoshop. Before I start working on an image, I think about the final picture I want. Planning the edit helps straight away.

I divide an image into general sections. In this beach photograph, the sections are the sky, the beach and the water. I often try to even out the tonality so that no one part of the image is much brighter than another. The image is easier on the eye, and this also helps bring out detail. Brightening shadows reveals more detail in them; darkening highlights reveals more detail there. This is something I always aim to do in the RAW converter, bringing the tones closer together.

When I take the image back into Photoshop, I can push those tones apart again, making the shadows darker and the highlights brighter. That may seem counterintuitive: first darken highlights and brighten shadows, then later brighten highlights and darken shadows. The point in the RAW converter is to bring out detail. If I then brighten highlights or darken shadows in Photoshop and lose detail, masking makes it easy to bring the detail back. I think of the RAW converter as the place to bring out image quality and detail, and Photoshop as the place for creative editing.

After looking at the broad sections, I look at individual areas. The large bright area on the beach draws more attention than I want, so I would darken it. I would also darken the bright area higher up to even it out, even though there are a couple of people there whom I might want to draw attention to. I would do the same on the left. I would brighten the rocks to bring out detail. I might brighten another patch of beach not to reveal detail but to even its tonality. The middle of the image is darker than the rest, so I would brighten it to balance the picture.

I would also try to give the boats more definition. As I’ve shown you before, Clarity can work wonders on slightly faded things like these. Dehaze is available too, but it is so strong that I often prefer Clarity. After these edits, the image might look like the example here. Compared with the original, the beach is more even in tonality. The front part and some other parts are still brighter than the rest, but the tones are closer together, which makes the picture easier to look at.

![1343 · U24 · L34 · 01:11](frames/U24L34-F0111.00.jpg)

On screen: "General tonal range" / "Water" / "Beach" / "Sky" / "Darken" / "Darken Beach Left" / "Darken Beach Right" / "Darken Beach front" / "Lighten" / "Lighten Beach Middle" / "Lighten Beach Left" / "Lighten Rocks" [rest omitted]  
Shows: The beach photograph in Photoshop, with its sky, sea, and beach areas and the Layers panel grouping tonal adjustments.

![1343 · U24 · L34 · 03:41](frames/U24L34-F0341.00.jpg)

On screen: [rest omitted]  
Shows: Red and blue dashed adjustment outlines mark several beach, rock, and shoreline areas in the photograph.

![1343 · U24 · L34 · 04:41](frames/U24L34-F0441.00.jpg)

On screen: [rest omitted]  
Shows: The beach photograph after the planned tonal adjustments, displayed with its Photoshop layer groups.

## Camera Raw 12.3 and the adjustment brush

Anchor: 1343 · U24 · L34 · 05:03–07:35

Now I’ll show how to make local edits in Adobe Camera Raw. As I mentioned in the previous lesson, I am re-recording these first two lessons because Adobe has just released a major Camera Raw update. The latest version at the time of this recording is 12.3. One of the main changes is the interface. I generally like it and think Adobe did a great job, although it is missing a couple of important features that I hope will be added in later versions.

On the right is a list of tabs. The first is Edits, which is a great improvement over the old interface, where it was difficult to find your edits after entering a local editing tool. The other tabs include Crop and Clone. I do not think you should crop or clone in the RAW converter if you plan to continue working in Photoshop. I would use those tools here if I were staying in the RAW converter and exporting, for example, to JPEG. The tools are not as good as their Photoshop equivalents, but they are useful if you are not going into Photoshop.

The first tool is the Adjustment Brush. It lets you brush an effect into the image. Photoshop’s brush tools are much better, but the image data is better while the picture is still in RAW format than it is after it goes into Photoshop. This is a balance to consider: the RAW converter’s tools are not as good, but the quality of the result can be better.

![1343 · U24 · L34 · 06:24](frames/U24L34-F0624.00.jpg)

On screen: "Camera Raw 12.3" [rest omitted]  
Shows: Camera Raw displays the sculpture photograph, a filmstrip of other photographs, and the right-side adjustment panel.

## Brush controls, first stroke, and preview

Anchor: 1343 · U24 · L34 · 07:35–11:01

First, open the arrow beside the brush settings. I think Adobe should have left these settings open by default so that people discover them instead of later finding out that important controls were hidden.

Size is the brush size, and Feather is its softness. The brush shows two circles: the inner circle is the main bulk of the brush, and the outer circle shows its softness. Increasing Feather makes the outer circle a larger part of the brush; reducing Feather all the way makes it almost disappear. Flow works as it does in Photoshop: it controls how quickly the effect is applied as you brush. Density is similar to opacity because it limits the total effect. I usually leave Density at 100 and use Flow to control how quickly I apply the effect. Scrolling through the controls is very slow, and I am not sure why.

For example, if I want to brush extra light into part of the sculpture’s wing, I would raise Exposure a little, brighten the shadows, and perhaps add some Clarity. You should be able to see the brushstroke. It is a little heavy-handed for my taste, so if I were working on this image I would reduce Flow. For the demonstration, this is okay.

![1343 · U24 · L34 · 08:38](frames/U24L34-F0838.00.jpg)

On screen: "Brush" / "Size 5" / "Feather 50" / "Flow 10" / "Density 100" / "Auto Mask" / "Overlay" / "Mask Options" [rest omitted]  
Shows: The Adjustment Brush controls are expanded beside the sculpture photograph.

![1343 · U24 · L34 · 10:07](frames/U24L34-F1007.00.jpg)

On screen: "Exposure +0.45" / "Shadows +17" / "Clarity +9" [rest omitted]  
Shows: A brush adjustment is selected on the sculpture’s right wing, with its settings visible in the panel.

The preview is a feature I think Adobe has missed. We used to have a preview button here that showed the before and after of the Adjustment Brush work. The current preview shows the original RAW edit instead. If I had changed the Basic settings or applied a curve, those changes would also be toggled, making it harder to judge what the brush did. I do not know why it works this way, but I hope it changes in a future update.

![1343 · U24 · L34 · 10:25](frames/U24L34-F1025.00.jpg)

On screen: [rest omitted]  
Shows: The preview control in the bottom toolbar is highlighted under the cursor and enlarged in an inset while the original image rendering is shown.

## See the mask and keep strokes in one adjustment

Anchor: 1343 · U24 · L34 · 11:01–13:06

The small node marks an adjustment. Hovering over it displays the mask overlay, which is useful for seeing where I brushed. In this example, it makes a missed patch easy to spot; without the overlay, I might not notice it.

When I make another brushstroke, Camera Raw creates another node and puts a new adjustment on top of the original. More often than not, I want to keep working in the existing adjustment. I’ll delete the extra one by selecting it and pressing Backspace or Delete. Then I’ll click the original node to activate it and continue brushing into that same adjustment.

Keeping the strokes together also lets me return to the settings. If I have added too much, I can change it. When I push the adjustment, the blacks start to fade, so I can compensate by darkening the blacks, brighten the shadows a little more, darken the blacks further, and add some Clarity. Then I can compare before and after. The RAW converter brings out an amount of detail and quality that I simply would not get by doing the same work in Photoshop.

![1343 · U24 · L34 · 11:07](frames/U24L34-F1107.00.jpg)

On screen: [rest omitted]  
Shows: A red mask overlay covers most of the sculpture’s right wing, revealing the area reached by the brush.

![1343 · U24 · L34 · 12:37](frames/U24L34-F1237.00.jpg)

On screen: "Exposure +0.60" / "Shadows +30" / "Blacks -11" / "Clarity +9" [rest omitted]  
Shows: The selected brush adjustment’s tonal and Clarity controls are visible beside the sculpture.

## Erase spill and make a separate adjustment

Anchor: 1343 · U24 · L34 · 13:06–15:13

The plus sign creates a new adjustment, almost like making a new adjustment layer in Photoshop. I would create one only when I want to make a different kind of adjustment. The Brush and Eraser controls are grayed out until an adjustment is selected. To illustrate the Eraser, I will deliberately paint over the edge. The Eraser removes part of that adjustment, and Flow controls how much it removes. The preview shows the part I removed.

Now I’ll make a different adjustment: the foreground rock is quite bright, and I might want to darken it. I can hit the plus icon (captions: bus), then reset all the options with the arrow instead of changing them one by one, and lower Exposure. The two adjustments now do separate things in the image. As I said earlier, the original had very dark shadows and bright highlights; the edits bring those tones closer together. The rock is now closer in tone to the area beside it.

![1343 · U24 · L34 · 13:18](frames/U24L34-F1318.00.jpg)

On screen: "Clarity +25" [rest omitted]  
Shows: The Brush controls, including the plus and Eraser icons, are open beside the sculpture photograph.

![1343 · U24 · L34 · 14:07](frames/U24L34-F1407.00.jpg)

On screen: [rest omitted]  
Shows: A circular eraser cursor sits just beyond the wingtip; the magnified inset shows the sky beside the wing edge.

![1343 · U24 · L34 · 14:37](frames/U24L34-F1437.00.jpg)

On screen: "Exposure -0.50" [rest omitted]  
Shows: The foreground rock is enlarged in the inset while the separate darkening adjustment is selected.

![1343 · U24 · L34 · 15:10](frames/U24L34-F1510.00.jpg)

On screen: [rest omitted]  
Shows: The sculpture photograph with two adjustment nodes visible, including the selected brush area on the wing.
