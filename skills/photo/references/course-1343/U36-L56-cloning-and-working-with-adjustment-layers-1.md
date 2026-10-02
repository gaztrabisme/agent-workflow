# Lesson 56 · Cloning and Working With Adjustment Layers 1

Anchor: 1343 · U36 · L56 · 15:33 · https://www.domestika.org/en/courses/1973-course-4-retouching-portraits/units/6059-cloning-and-working-with-adjustment-layers#course_lesson_18329

## Why use a separate cloning layer

Anchor: 1343 · U36 · L56 · 00:00–02:10

Welcome to this fourth course on retouching portraits. We will cover many new topics, including smoothing skin, fixing wrinkles, sorting out skin tones and removing redness from skin. In this lesson, we will work with cloning layers alongside adjustment layers. It is important to keep the work editable and the layers in the right order. You will learn where cloning and adjustment layers belong in the stack, and we will introduce layer groups to keep the work organized and easy to edit.

So far, we have mostly used duplicated Background layers for cloning and retouching. This is simple to understand and lets you use all of Photoshop's tools. The Patch tool is one of the tools we have used, and it will not work unless you are working on a duplicate. It would work directly on the Background, but you should never edit directly on the Background. I will duplicate it and rename the new layer Clone. With the Patch tool, I can circle a blemish and drag the selection to an area to use as the replacement.

One benefit of cloning on a duplicate is that adjustments placed above it affect the cloning too.

![1343 · U36 · L56 · 01:50](frames/U36L56-F0150.00.jpg)

On screen: “Clone” / “Background”  
Shows: A portrait of a woman with the Patch tool selection over a blemish near her chin; two layers are visible.

## Why repeated background copies become awkward

Anchor: 1343 · U36 · L56 · 02:10–04:42

As you become more advanced, you may want several cloning layers. Duplicating the Background more than once makes the file very large. The document-size readout is at the bottom left of the workspace. You can change what it displays by clicking its arrow; I recommend leaving it set to Document Sizes unless you need something else. The original image size here is 9.22 MB and the current document size is 18.4 MB. Duplicating the Background doubles the image's pixels. If I make more copies with Command-J on Mac or Control-J on Windows, the document has three layers and is three times the original size.

Another drawback is that the work is not separated: everything still has to be on one layer. I will patch a few more areas, then switch off both layers to compare them. I did some cloning on the first layer and added more on the second. I could return to the earlier layer, switch off or delete the later one, and continue there. What I could not do cleanly is keep the edit on the upper layer while restoring the earlier work from the lower one; that would require strange, confusing edits.

![1343 · U36 · L56 · 02:50](frames/U36L56-F0250.00.jpg)

On screen: “Doc: 9.22M/18.4M” [rest omitted]  
Shows: The woman's portrait, a duplicate layer, and the document-size readout.

![1343 · U36 · L56 · 03:27](frames/U36L56-F0327.00.jpg)

On screen: “Doc: 9.22M/27.7M” [rest omitted]  
Shows: Three portrait layers and the document-size readout.

![1343 · U36 · L56 · 03:48](frames/U36L56-F0348.00.jpg)

On screen: [rest omitted]  
Shows: The portrait and three-layer stack, with the pointer at a Clone layer's visibility control.

## Working on blank layers and setting sampling

Anchor: 1343 · U36 · L56 · 04:42–07:58

My usual approach is to work on blank layers. They add only the new pixels needed and keep the file smaller. There are other benefits too. I will delete the two duplicate layers, add a blank layer with the plus icon at the bottom of the Layers panel, and name it Clone. If I try to use the Patch tool on it, Photoshop reports that the selected area is empty. The Patch tool needs a duplicated Background or a composite of all the layers; we will cover that composite workflow later.

The Healing Brush, Clone Stamp and Spot Healing Brush can work across layers. However, sampling an area with Alt or Option and painting on an empty layer does nothing, and Photoshop gives no warning. Adobe should add a warning for this. These tools sample only the current layer by default. In the options bar, change the sample setting to Current & Below or All Layers. Current & Below uses the active layer and any layers beneath it; All Layers also includes layers above it. I usually choose Current & Below. Some tools, including the Spot Healing Brush, only offer All Layers. A symbol in the options bar indicates that adjustment layers will be ignored; that is what I recommend when cloning.

With the sample setting changed, I try the Healing Brush again: I hold Alt or Option to sample an area and paint on the blank layer. This time it works. I then check the settings for the other tools: set the Spot Healing Brush to sample all layers, and set the Clone Stamp to Current & Below. There are reasons to use Current Layer even when you are not cloning onto a Background duplicate, but we will cover those later.

![1343 · U36 · L56 · 05:19](frames/U36L56-F0519.00.jpg)

On screen: “Could not use the patch tool because the selected area is empty.” / “OK” [rest omitted]  
Shows: Photoshop's error dialog over the portrait and the empty Clone layer.

![1343 · U36 · L56 · 06:43](frames/U36L56-F0643.00.jpg)

On screen: “Current Layer” / “Current & Below” / “All Layers” [rest omitted]  
Shows: The Healing Brush sampling menu open over the portrait.

![1343 · U36 · L56 · 07:05](frames/U36L56-F0705.00.jpg)

On screen: “Turn on to ignore adjustment layers when healing” [rest omitted]  
Shows: The Healing Brush options bar with the adjustment-layer-ignore icon's tooltip open; a loupe magnifies the symbol.

![1343 · U36 · L56 · 07:27](frames/U36L56-F0727.00.jpg)

On screen: [none]  
Shows: The portrait with a freshly healed spot visible in the loupe while the Healing Brush is active.

![1343 · U36 · L56 · 07:36](frames/U36L56-F0736.00.jpg)

On screen: “Sample All Layers” [rest omitted]  
Shows: Spot Healing Brush options over the portrait; the Sample All Layers checkbox is visible and unchecked.

## Choosing how many cloning layers an image needs

Anchor: 1343 · U36 · L56 · 07:58–09:10

For this portrait, where almost the entire image is the woman's face, I would probably need only one layer to clean up the skin, so duplicating the Background would not be a major problem. Compare it with another image that has a strip of floor at the bottom. I would put cloning on the floor on its own layer. I would also keep work on the man's teeth separate from flyaway hairs, marks or creases on his shirt, and marks on a backdrop. If you use duplicated Backgrounds for all those tasks, the file becomes very large.

![1343 · U36 · L56 · 09:01](frames/U36L56-F0901.00.jpg)

On screen: [none]  
Shows: A full-length portrait of a man against a white studio background, including the floor at the bottom.

## Make the main adjustments before cloning

Anchor: 1343 · U36 · L56 · 09:10–12:54

The order of work matters. It is tempting, especially when you are new to retouching, to start with cloning because it feels more exciting than Levels, Curves and similar adjustments. That can mean doing unnecessary work: once the image is brighter and its colour and contrast are corrected, some flaws may no longer be visible. Do the main adjustments first, such as Levels and Curves for colour and tonal range, and then clone.

There is a pitfall to watch for. I will start with Levels. Clipping highlights is generally bad, but a white studio backdrop is an exception: if you want to bleach it out completely, you want the histogram to reach the right edge. The blacks are not quite black, so I will bring in the black point. To see the clipping, hold Alt or Option while dragging the black-point slider; this is called threshold mode. The image turns white, and the areas that begin to appear show the clipped parts. I do not want to clip any part of the subject. I pull the slider back until clipping just begins, which confirms a true black, and check the small creases at the bottom of the image by toggling Alt or Option. I leave the black point at 4.

I will add a Curves adjustment called Brightness and make the already bright image just a little brighter. Then I will add one called Colours: the man's skin looks slightly yellow, so I will add a hint of blue and take out a tiny bit of red.

![1343 · U36 · L56 · 10:49](frames/U36L56-F1049.00.jpg)

On screen: “Levels 1” / “0” / “1.00” / “255” [rest omitted]  
Shows: Levels controls and the histogram over the portrait against the white studio background.

![1343 · U36 · L56 · 11:46](frames/U36L56-F1146.00.jpg)

On screen: “4” [rest omitted]  
Shows: The image in threshold view, with the black-point value set to 4.

![1343 · U36 · L56 · 12:27](frames/U36L56-F1227.00.jpg)

On screen: “Colours” / “Brightness” [rest omitted]  
Shows: The portrait with the Colours, Brightness and Levels adjustment layers in the stack.

## Correct the brush selection and finish the cloning example

Anchor: 1343 · U36 · L56 · 12:54–15:33

This is a common mistake, and I like to show mistakes as well as correct methods. If you learn how to fix a mistake, you are more likely to recover than to jump back through History or start again. The normal workflow is to make the tonal-range, brightness and colour adjustments first, then clone on a blank layer. I will add one and call it Clone, zoom to 100% with Command-1 or Control-1, and try to remove a couple of marks on the man's neck with the Healing Brush. Press J to select it, use the square brackets next to P to make the brush smaller, and hold Alt or Option to sample.

I accidentally selected the Spot Healing Brush. Adobe should use different icons for the Spot Healing Brush and Healing Brush. The J shortcut selects the Healing Brush, but it can also select the Spot Healing Brush unless you have edited the shortcuts. Press Shift-J to toggle between the available tools. To customize them, choose Edit Toolbar at the bottom of the toolbar. For example, I can remove the Spot Healing Brush, Patch tool, Content-Aware tool and Red Eye tool, then click Done. Now J selects only the Healing Brush. That is my preference.

I will try again with a smaller brush, sample with Alt or Option, and cover a few marks. It does not matter which marks I choose here; I am showing how the method works.

![1343 · U36 · L56 · 13:39](frames/U36L56-F1339.00.jpg)

On screen: [rest omitted]  
Shows: A close view of the man's neck and shirt with the Spot Healing Brush cursor over the skin.

![1343 · U36 · L56 · 14:49](frames/U36L56-F1449.00.jpg)

On screen: “Customize Toolbar” [rest omitted]  
Shows: The Customize Toolbar dialog open over the man's portrait.

![1343 · U36 · L56 · 15:06](frames/U36L56-F1506.00.jpg)

On screen: [none]  
Shows: The man's neck and shirt after the toolbar dialog has closed.

![1343 · U36 · L56 · 15:17](frames/U36L56-F1517.00.jpg)

On screen: “Source: Sampled” / “Diffusion: 5” [rest omitted]  
Shows: The Healing Brush cursor over the man's neck; the Clone layer is selected.
