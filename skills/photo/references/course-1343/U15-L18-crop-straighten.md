# Lesson 18 · Crop & Straighten

Anchor: 1343 · U15 · L18 · 14:35 · https://www.domestika.org/en/courses/1971-course-2-retouching-fundamentals/units/6421-crop-straighten#course_lesson_19377

## Cropping options and preserving pixels

Anchor: 1343 · U15 · L18 · 00:00–02:36

In this lesson, I’ll show how to use Photoshop’s Crop tool to choose an aspect ratio, fit an image to a paper size, straighten it, and use the Perspective Crop tool. Press **C** to select the Crop tool. Before cropping, look at its options. You can choose a ratio; I’ll leave that blank for now and return to it shortly. The next two boxes are related to the ratio. The next control is the **Straighten** tool (captions: *straight and tall*). The crop guide overlay can show the rule of thirds, a grid, or a golden spiral. Those guides can help when recomposing or straightening an image.

The **Delete Cropped Pixels** option is important. By default, I believe it is switched off, so Photoshop keeps the pixels outside the crop. This makes the crop non-destructive: you can bring those pixels back later. The trade-off is a larger file. If you are sure you want to commit to a crop, turn this option on. **Content-Aware** fills areas outside the original canvas with a content-aware fill instead of leaving blank pixels.

![1343 · U15 · L18 · 01:08](frames/U15L18-F0108.00.jpg)

On screen: "Ratio" / "Clear" / "Straighten" / "Delete Cropped Pixels" / "Content-Aware"  
Shows: A landscape photograph of a child under the active crop boundary. The magnified inset shows Clear, Straighten, and the crop-guide overlay control; Delete Cropped Pixels and Content-Aware appear in the small options bar at the top.

## Remove distractions and straighten a tilted image

Anchor: 1343 · U15 · L18 · 02:36–04:39

The first kind of crop removes unwanted objects. It is rare that you will want to restore pixels removed for this purpose, so I turn on **Delete Cropped Pixels**. In this photograph, an arm at the left edge interferes with the image. Pull the crop boundary in to remove most of it. I can leave a little sleeve to keep as much of the photograph as possible; that small remnant is easy to remove with the Clone tool. I could also use the Spot Healing Brush: enlarge it slightly with the square bracket keys next to **P**, then paint over the sleeve.

![1343 · U15 · L18 · 03:05](frames/U15L18-F0305.00.jpg)

On screen: [none]  
Shows: A rule-of-thirds overlay inside a crop boundary, with part of an adult’s sleeve at the left edge of a child’s photograph.

![1343 · U15 · L18 · 03:19](frames/U15L18-F0319.00.jpg)

On screen: "Crop Preview" [rest omitted]  
Shows: The child photograph in Crop Preview, with the cropped area bright and the area outside it darkened.

Another common use is to level a photograph that is leaning, or to correct a building whose top is slanted. The Crop tool’s **Straighten** control is useful for this. Its icon looks a bit like a handbag, but it represents a spirit level. Select it, place the cursor along the edge you want to level—in this case, the water’s edge—and drag along that line. Photoshop shows an angle of negative three degrees.

![1343 · U15 · L18 · 04:18](frames/U15L18-F0418.00.jpg)

On screen: "-3.0°" [rest omitted]  
Shows: A lake photograph inside the active crop boundary as the Straighten tool is dragged along the waterline, with the -3.0° angle readout beside the cursor.

Photoshop rotates the image when you release the mouse. Press **Enter** or **Return**, or click the check mark in the options bar, to commit the crop.

![1343 · U15 · L18 · 04:35](frames/U15L18-F0435.00.jpg)

On screen: "Crop Preview" [rest omitted]  
Shows: A lake photograph in Crop Preview, with a rule-of-thirds grid and the rotated image visible beyond the crop boundary.

## Reframe for a precise print size

Anchor: 1343 · U15 · L18 · 04:39–07:20

This next photograph is landscape, and I think it works well that way, but a portrait crop could also fit a frame. To crop to a specific size—say, a 10-by-8-inch frame—you can enter an exact size or choose a ratio. A ratio gives you the shape, but not the physical size. For an exact size, select **W x H x Resolution**; Photoshop then provides fields for the resolution as well.

![1343 · U15 · L18 · 05:40](frames/U15L18-F0540.00.jpg)

On screen: "Ratio" / "W x H x Resolution" / "Original Ratio" / "1 : 1 (Square)" / "4 : 5 (8 : 10)" / "5 : 7" / "2 : 3 (4 : 6)" / "16 : 9" / "Front Image" / "4 x 5 in 300 ppi" / "8.5 x 11 in 300 ppi" / "1024 x 768 px 92 ppi" / "1280 x 800 px 113 ppi" / "1366 x 768 px 135 ppi" / "New Crop Preset..." / "Delete Crop Preset..." [rest omitted]  
Shows: A landscape photograph of a child under the crop boundary, with the Crop tool’s size and ratio menu open.

For this crop, I do not want to delete the cropped pixels in case I change the crop later. Set the width to **8 in** and the height to **10 in**. For print, set the resolution to **300** and make sure the unit is pixels per inch, not pixels per centimetre. Move the crop frame to fit the photograph, then press **Enter** or **Return** to commit.

![1343 · U15 · L18 · 06:18](frames/U15L18-F0618.00.jpg)

On screen: "8 in" / "10 in" / "300" / "px/in" [rest omitted]  
Shows: The child photograph inside a portrait crop, with the width, height, and resolution fields set in the Crop tool.

After applying a crop without deleting pixels, Photoshop may rename the Background layer **Layer 0**.

![1343 · U15 · L18 · 06:50](frames/U15L18-F0650.00.jpg)

On screen: "Layer 0" [rest omitted]  
Shows: A portrait crop of a child with a magnified Layers panel showing the layer name Layer 0.

That is because a normal Background layer cannot retain hidden pixels. If I select the Crop tool again, the original image is still visible beyond the crop boundary because I left **Delete Cropped Pixels** off.

![1343 · U15 · L18 · 07:17](frames/U15L18-F0717.00.jpg)

On screen: "Delete Cropped Pixels" [rest omitted]  
Shows: The portrait crop active again, with the original landscape photograph visible outside its crop boundary.

## Keep a series consistent with the original dimensions

Anchor: 1343 · U15 · L18 · 07:20–10:07

A crop like this may not matter for a single image. With a series, though, you do not want one photograph to end up a different shape or size when you print the images or put them on a website. You can crop back to the image’s original size; Photoshop will return the crop to those original dimensions. One way is to enter its original dimensions as a specific size. Use **Option+Command+I**, or **Alt+Control+I** on Windows, to open Image Size. When I switch the units to inches or centimetres, this lake photograph measures **56.9 by 37.93 centimetres**.

![1343 · U15 · L18 · 08:20](frames/U15L18-F0820.00.jpg)

On screen: "Image Size" / "Dimensions: 6720 px × 4480 px" / "Fit To: Original Size" / "Width: 6720 Pixels" / "Height: 4480 Pixels" / "Resolution: 300 Pixels/Inch" [rest omitted]  
Shows: An Image Size dialog over the lake photograph, with the original pixel dimensions and resolution visible.

You could enter that original size in the Crop tool’s size-and-resolution fields. Or select **Front Image** from the menu. That saves you from writing down the dimensions: Photoshop enters the exact image size for you, using pixels because they are the most accurate unit. I can then select the Straighten tool, drag along the shoreline, and commit the crop. The Image Size dialog confirms that the image is still 56.9 by 37.93 centimetres, with the pixel dimensions that Photoshop inserted into the Crop tool. This is useful when cropping an image that belongs in a series.

![1343 · U15 · L18 · 09:05](frames/U15L18-F0905.00.jpg)

On screen: "Front Image" [rest omitted]  
Shows: The Crop tool menu open over the lake photograph, with Front Image highlighted.

![1343 · U15 · L18 · 09:12](frames/U15L18-F0912.00.jpg)

On screen: "6720 px" / "4480 px" [rest omitted]  
Shows: A lake photograph under the active crop boundary, with the Crop tool’s width and height fields showing the original pixel dimensions.

![1343 · U15 · L18 · 09:49](frames/U15L18-F0949.00.jpg)

On screen: "Image Size" / "Image Size: 86.1M" / "Dimensions: 6720 px × 4480 px" / "Fit To: Original Size" / "Width: 56.9 Centimeters" / "Height: 37.93 Centimeters" / "Resolution: 300 Pixels/Inch" / "Resample: Automatic" / "Cancel" / "OK" [rest omitted]  
Shows: An Image Size dialog over the lake photograph, with its original pixel dimensions and size in centimetres visible.

## Correct perspective on an angled photograph

Anchor: 1343 · U15 · L18 · 10:07–11:45

The **Perspective Crop Tool** lets you crop an object photographed from an angle and make it square-on. Here, a framed photograph on a wall is tilted in the scene. If I crop only that photograph with the normal Crop tool, its perspective will still be wrong, so I use the Perspective Crop Tool.

![1343 · U15 · L18 · 11:02](frames/U15L18-F1102.00.jpg)

On screen: "Show Grid" [rest omitted]  
Shows: A framed black-and-white portrait on a wall above two chairs, as seen within Photoshop.

Position the cursor at the photograph’s bottom-right corner and zoom in to make the work easier. Click to place a point, then drag out a line. As you add the remaining corners, the perspective plane appears. Keep the lines straight; the grid helps you align them. Press **Enter** or **Return**, or click the check mark in the options bar. The result keeps only a small part of the original scene.

![1343 · U15 · L18 · 11:38](frames/U15L18-F1138.00.jpg)

On screen: "Commit current crop operation" [rest omitted]  
Shows: A four-corner perspective crop grid fitted to the framed portrait.

## Remove a tiny edge with Canvas Size

Anchor: 1343 · U15 · L18 · 11:45–14:35

After a perspective crop, a tiny line can be difficult to trim with the Crop tool. Zoom in very close to see how much needs removing. The pixel grid helps: at the top there are about two or three pixels of a very light line and a hint of blue. The bottom looks fine, and so does the right side; the Navigator is useful for checking those edges. Zoom out with **Command+0** on Mac or **Control+0** on Windows.

![1343 · U15 · L18 · 12:04](frames/U15L18-F1204.00.jpg)

On screen: [none]  
Shows: The cropped black-and-white portrait by itself, after perspective correction.

![1343 · U15 · L18 · 12:16](frames/U15L18-F1216.00.jpg)

On screen: "1200%" [rest omitted]  
Shows: The photograph’s top edge at 1200%, with the pixel grid and a thin light and bluish line visible.

Instead of using the Crop tool for such a tiny strip, open the **Image** menu and choose **Canvas Size** (captions: *Canva size*). Enter a negative value of **3 pixels** for both width and height. Anchor the document at the bottom-right corner so Photoshop removes pixels from the left and the top. When you click **OK**, Photoshop warns that the new canvas will be smaller and some clipping will occur. I usually check **Don’t show again**, though you may want to leave it unchecked for now, then click **Proceed**.

![1343 · U15 · L18 · 13:30](frames/U15L18-F1330.00.jpg)

On screen: "Canvas Size" / "Width: -3 Pixels" / "Height: -3 Pixels" / "Relative" / "Anchor" [rest omitted]  
Shows: The Canvas Size dialog over the portrait, with both dimensions set to -3 pixels and the bottom-right anchor selected.

![1343 · U15 · L18 · 13:46](frames/U15L18-F1346.00.jpg)

On screen: "The new canvas size is smaller than the current canvas size; some clipping will occur. / Don't show again / Cancel / Proceed" [rest omitted]  
Shows: Photoshop’s clipping warning over the Canvas Size dialog and portrait.

The result is subtle. Open the History panel and zoom in to compare before and after (captions: *and often*). A hint of the bluish-purple line remains, but this works well for our purposes. That wraps up the Crop tool lesson. You should now have a better understanding of how to crop images and why to use certain ratios. In the next lesson, I’ll teach you how to use Levels.

![1343 · U15 · L18 · 14:08](frames/U15L18-F1408.00.jpg)

On screen: "History" / "Open" / "Perspective Crop" / "Canvas Size" [rest omitted]  
Shows: A close-up of the portrait with the History panel open and the Canvas Size step selected.
