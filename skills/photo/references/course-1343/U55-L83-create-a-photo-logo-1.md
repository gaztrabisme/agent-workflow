# Lesson 83 · Create a Photo Logo 1

Anchor: 1343 · U55 · L83 · 14:12 · https://www.domestika.org/en/courses/1974-course-5-final-touches-and-useful-tips/units/6482-create-a-photo-logo#course_lesson_19439

## Choose how to use a scanned signature

Anchor: 1343 · U55 · L83 · 00:00–01:29

In this lesson I’ll show you how to make a logo from your signature and add it to photographs. It is popular at the moment and fairly easy to do, and it can replace a watermark. I signed a piece of paper and scanned it; you can follow along with your own signature or practise with my scribble.

There are a few ways to use the logo. You can use the scanned signature as it is, create a brush from it, draw a signature in Photoshop, or turn it into a shape. The difference between a shape and a brush is that a shape is vector-based. It is independent of resolution, so its quality does not depend on its size.

![1343 · U55 · L83 · 01:06](frames/U55L83-F0106.00.jpg)

On screen: "[illegible]"  
Shows: A handwritten signature scan centered on a white page.

## Clean and darken the scan

Anchor: 1343 · U55 · L83 · 01:29–04:11

First I’ll clean the scan a little by zooming in. I can add a Curves adjustment above everything to darken the marks and make them easier to see. Some paper texture is visible, but it probably will not be a problem. I’ll use the Spot Healing Brush directly on the Background layer to remove anything that stands out. I watch the result as I work because the tool is automatic, even though it is useful.

![1343 · U55 · L83 · 01:48](frames/U55L83-F0148.00.jpg)

On screen: [none]  
Shows: The scanned signature enlarged to 200% while the Spot Healing Brush is being used.

Once the scan looks good, I make a rough selection around it, open Select and Mask, and feather the edge to soften it. After clicking OK, I invert the selection and fill it with white. Pressing D restores the default colours, which gives me pure white as the background colour; I use Command+Backspace on a Mac or Control+Delete on Windows to fill. I deselect. The small amount of texture left is fine because the signature will not be this dark. I delete the temporary Curves layer.

![1343 · U55 · L83 · 02:40](frames/U55L83-F0240.00.jpg)

On screen: [none]  
Shows: A rough selection surrounds the scanned signature.

Next I want to darken the signature itself. I choose Select > Color Range and select Midtones. Midtones does not include the black parts, so I lower the range until the selection covers them too. The resulting selection looks good, so I add a Curves adjustment and darken the signature slightly.

![1343 · U55 · L83 · 03:50](frames/U55L83-F0350.00.jpg)

On screen: "Color Range" / "Select: Midtones" / "Range: 105 150" [rest omitted]  
Shows: The Color Range dialog set to Midtones, with the signature selection preview.

## Make a reusable signature layer

Anchor: 1343 · U55 · L83 · 04:11–05:18

I’m making two versions: one that keeps the look of a pen, and another that looks more like a digital logo.

![1343 · U55 · L83 · 04:20](frames/U55L83-F0420.00.jpg)

On screen: [none]  
Shows: The darkened signature on its white scan background.

I put the current result on its own layer. Flattening the image would prevent me from changing it later, so I stamp the visible result onto a new layer instead: Shift+Option+Command+E on Mac, or Shift+Alt+Control+E on Windows. I call the layer Signature.

I copy it to the other two images with Duplicate Layer: right-click the empty area of the layer and choose the other image as the destination. I repeat that for the third image. The signature is quite large in each image, but I can resize it.

## Place the scanned signature on photographs

Anchor: 1343 · U55 · L83 · 05:18–07:47

I’ll use blend modes to put the signature on the photographs. The white background is still on the image (captions: *the YTM*). On the dark image, I change the blend mode to Screen. At first it has the opposite effect from what I want, but inverting the layer with Command+I or Control+I makes the signature white.

![1343 · U55 · L83 · 05:47](frames/U55L83-F0547.00.jpg)

On screen: "Screen" / "Signature" [rest omitted]  
Shows: An oversized white signature crossing the forehead of a dark portrait before it is resized.

I’ll use Command+T or Control+T to resize it and place it in the bottom-right corner. A very large logo can interfere with a photograph, so I prefer a smaller one.

In recent versions of Photoshop, holding Shift while resizing allows distortion; it used to constrain proportions. I have been used to holding Shift to keep proportions, so the change feels strange. I like that proportions are constrained by default, but I would rather use a different key to remove the constraint. I press Enter or Return to commit the resize.

On the other image, I want to remove the white and keep the black, so I use Multiply. Blend If could also remove the white, but I prefer the blend mode. I transform the signature again and move it to the bottom-right corner. This time I remember not to hold Shift, and I make the version a little smaller. That is the manual way to add the signature to these images.

![1343 · U55 · L83 · 06:58](frames/U55L83-F0658.00.jpg)

On screen: "Screen" / "Signature" [rest omitted]  
Shows: A white signature placed at the lower-right of a dark portrait.

![1343 · U55 · L83 · 07:40](frames/U55L83-F0740.00.jpg)

On screen: "Multiply" / "Signature" [rest omitted]  
Shows: A black signature placed at the lower-right of a light portrait.

## Save the scan for an action

Anchor: 1343 · U55 · L83 · 07:47–09:00

If you need to add the signature to many photographs, write an action. An action can place a file into an image. I delete the signature layers from the working images, then save the signature scan on my computer. I put it in my Pictures folder, though it could be anywhere because the action will work anywhere. I save without compression and click OK. Including layers makes the file larger, but this file is small, so I am not concerned.

## Record and test the white-signature action

Anchor: 1343 · U55 · L83 · 09:00–12:26

I open the Actions panel. It is already in editing mode; if it is not, exit button mode to get to the editing view. I name the action White Signature because I will use it on a dark image, and the other action will be for a light image. I assign a colour; blue does not matter, and I consider yellow as a light colour. Then I click Record.

![1343 · U55 · L83 · 09:32](frames/U55L83-F0932.00.jpg)

On screen: "Actions" / "Retouching" / "Workflow" / "Dodge & Burn" / "Frequency Separation" / "Colour grade" / "New Action" / "Name: White Signature" / "Set: Retouching" / "Record" / "Cancel" [rest omitted]  
Shows: The New Action dialog with White Signature as its name.

I choose File > Place Embedded, select the signature scan, and click Place. Photoshop places it as a Smart Object by default, which means I can change its size later without losing the original quality. I resize it. I start to hold Shift out of habit, then let go and set it roughly to the size I want. I click the checkmark in the options bar; the layer now has the Smart Object symbol.

![1343 · U55 · L83 · 11:16](frames/U55L83-F1116.00.jpg)

On screen: "Place" [rest omitted]  
Shows: The placed signature as a Smart Object over the portrait, before it is aligned.

With the Move tool, the options bar gives me ways to place a layer in the image. They are unavailable until I tell Photoshop what to align to. I think it would be nice if, by default, they were based on the size of the image. I select the whole image with Command+A or Control+A. I align the signature to the bottom edge and right side, then deselect. I change the blend mode to Screen. It is quite an interesting effect; we get see-through text there. But I want to invert the signature. Since this is a Smart Object, the inversion becomes a Smart Filter; if I decide I prefer the earlier look, I can change it back.

I stop recording and test the action. I delete the layer, select the action title, and press Play. Photoshop places the signature. The Actions panel also shows the recorded placement, alignment, and inversion steps.

![1343 · U55 · L83 · 12:23](frames/U55L83-F1223.00.jpg)

On screen: "Set Selection" / "Align current layer" / "Align current layer" / "Set Selection" / "Set current layer" / "Invert" [rest omitted]  
Shows: The white-signature action steps beside the portrait with the white signature at lower right.

## Record and test the black-signature action

Anchor: 1343 · U55 · L83 · 12:26–14:12

On the light image, I record a second action for the black signature (the captions read “plaque signature”). I give it the same yellow colour so the two actions stay together. I record, choose File > Place Embedded, select the signature scan, and click Place.

I resize without holding Shift. If I want both signatures to be exactly the same size, I can type 40% for each one.

![1343 · U55 · L83 · 13:21](frames/U55L83-F1321.00.jpg)

On screen: "Black Signature" / "W: 40" / "H: 40.00%" [rest omitted]  
Shows: The signature placed on the light portrait, with the width set to 40% for resizing.

I click OK, select all, and use the Move tool to align the signature to the bottom and right. I deselect with Command+D or Control+D, change the blend mode to Multiply, and stop recording. I test the action in button mode. Applying the signature is now very quick.

![1343 · U55 · L83 · 13:54](frames/U55L83-F1354.00.jpg)

On screen: "Black Signature" [rest omitted]  
Shows: A black signature at the lower-right of a light portrait, with the Actions panel open.
