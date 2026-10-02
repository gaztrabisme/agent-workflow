# Lesson 82 · Delivering Files to a Client 2

Anchor: 1343 · U54 · L82 · 13:38 · https://www.domestika.org/en/courses/1974-course-5-final-touches-and-useful-tips/units/6480-delivering-files-to-a-client#course_lesson_19507

## Soft-proof vivid colors for print

Anchor: 1343 · U54 · L82 · 00:00–02:58

When an image is going to print, color matters, especially when it has very vivid colors and will be printed somewhere other than a standard inkjet printer. For example, if an image is going to be printed on a postcard (captions: “going wrong, On a postcard”), that is offset printing, which often produces much less saturated color. I chose this picture because of its bright red. If you send it straight to a printer for a postcard or business card, you may expect the vivid red to represent you well as a photographer, then get back something that looks nothing like you expected. Converting an image to the right color profile can be important.

Before converting, make a soft proof. In Photoshop, find Proof Colors in the View menu, but first set up the proof from View, Proof Setup, Custom. Choose the profile for the output. A good photographic lab will typically provide its own custom profile for download from its website; install it in Photoshop and use it for soft proofing. A postcard printer may not use the most advanced printers, and when I have called and asked which profile to use, they have not always known what I meant. A photographic print shop should know about profiles.

The most commonly used CMYK profile for offset printing in Europe at the moment is Coated FOGRA39 (ISO 12647-2:2004), though this changes over time and may differ in the United States. Do not simply take my word for it; I will use Coated FOGRA39 as the example here.

![1343 · U54 · L82 · 00:40](frames/U54L82-F0040.00.jpg)

On screen: [none]  
Shows: Woman in a vivid red dress standing against a dark wall.

![1343 · U54 · L82 · 01:30](frames/U54L82-F0130.00.jpg)

On screen: “View / Proof Setup / Custom... / Proof Colors / ⌘Y” [rest omitted]  
Shows: View menu and Proof Setup submenu open over the red-dress portrait.

![1343 · U54 · L82 · 02:40](frames/U54L82-F0240.00.jpg)

On screen: “Custom Proof Condition / Device to Simulate / Coated FOGRA39 (ISO 12647-2:2004)” [rest omitted]  
Shows: Custom Proof Condition dialog with the profile list open over the red-dress portrait.

## Compare the proof and adjust the reds

Anchor: 1343 · U54 · L82 · 02:58–07:55

After selecting Coated FOGRA39, turn on Proof Colors from the View menu. Command-Y on a Mac or Control-Y on Windows toggles the proof. The shortcut is useful because, when you use the menu, you look at the menu instead of the image as its appearance changes. Compare the original colors with the soft proof: the reds look much more faded. Soft proofing is mainly a way to manage expectations. If the result no longer looks as good but you are happy with it, that may be fine. If it does not represent the image’s colors well, make adjustments.

Selective Color is one adjustment for working with color. It is intended for this kind of editing, though using it for color is not necessarily wrong. Its color groups are Reds, Yellows, Greens, Cyans, Blues, Magentas, Whites, Neutrals, and Blacks. These controls work with how colors are made up from a CMYK perspective. Removing cyan gives more red; reducing cyan makes the red more vivid. Adding magenta makes red pinker, while removing magenta shifts it toward orange or yellow. Reducing yellow makes the red pinker; adding yellow makes it darker and more orange. Black can intensify or slightly fade the color. With the adjustments here, the red is more vivid and suited to CMYK printing rather than the RGB colors we usually see while editing in Photoshop.

![1343 · U54 · L82 · 03:24](frames/U54L82-F0324.00.jpg)

On screen: [rest omitted]  
Shows: View menu open with Proof Colors checked over the red-dress portrait.

![1343 · U54 · L82 · 03:40](frames/U54L82-F0340.00.jpg)

On screen: [rest omitted]  
Shows: Red-dress portrait with the proof profile shown in the document tab.

![1343 · U54 · L82 · 04:26](frames/U54L82-F0426.00.jpg)

On screen: “Selective Color / Reds / Yellows / Greens / Cyans / Blues / Magentas / Whites / Neutrals / Blacks / Layers / Selective Color 1 / Background” [rest omitted]  
Shows: Selective Color color-group list expanded beside the red-dress portrait.

![1343 · U54 · L82 · 05:40](frames/U54L82-F0540.00.jpg)

On screen: “Preset: Custom / Colors: Reds / Cyan: -31% / Magenta: +2% / Yellow: +11% / Black: +17% / Relative / Absolute” [rest omitted]  
Shows: Selective Color controls and the red-dress portrait with the Reds values displayed.

Photoshop also has a Gamut Warning, which I used to look at but eventually stopped using. It puts a gray overlay on colors that are out of the printer's gamut—that is, colors without the right saturation for that printer (captions: “calorie”). I used to think this was useful, but the warning does not show how far out of gamut a color is: even a color that is only 1% out of gamut turns gray. Use it to get an idea of which colors may not print well, but take that indication with a pinch of salt because it cannot tell you exactly how the image will print. I recommend using Proof Colors; Gamut Warning can give you an additional idea.

![1343 · U54 · L82 · 06:36](frames/U54L82-F0636.00.jpg)

On screen: [rest omitted]  
Shows: Gray Gamut Warning overlay across the dress, with the Selective Color controls visible.

A soft proof is called “soft” because a hard proof is a print you can look at. A soft proof on screen (captions: “software”) is not as accurate as a hard proof. When you are happy with the soft proof, convert the file to the profile. Proofing alone does not convert the colors; it only previews them.

## Convert the file to the print profile and size it

Anchor: 1343 · U54 · L82 · 07:55–10:48

Choose Edit, Convert to Profile. The destination space shown here is currently sRGB, which is what was used to convert the file before; you do not really save it as a preset. sRGB is a useful default because it is a simplified profile and colors are represented fairly accurately in almost any application, including the internet. It does not have as vivid or as wide a color range as Adobe RGB, for example, but it is the profile I prefer as my default. For this print example, choose Coated FOGRA39.

For conversion settings, I typically recommend Relative Colorimetric (captions: “calorimetric”), Use Black Point Compensation, and Use Dither. I do not recommend Flatten Image to Preserve Appearance. Flattening may give a better result in some cases, but it removes the layers. Keeping the layers lets me edit the Selective Color adjustment if I am not happy after sending the file to print. If the conversion looks strange, undo it and try it again, then flatten the image if needed. Before doing that, save a version that preserves the Selective Color changes. After confirming the conversion, the file is in the CMYK profile and can be sent to print.

Before sending it to print, size the image in Photoshop. Even if a print service lets you choose the size, set it in Photoshop so the printer only prints the file instead of processing it in a way you cannot control.

![1343 · U54 · L82 · 08:00](frames/U54L82-F0800.00.jpg)

On screen: “Edit / Convert to Profile...” [rest omitted]  
Shows: Edit menu open over the red-dress portrait with Convert to Profile visible.

![1343 · U54 · L82 · 08:40](frames/U54L82-F0840.00.jpg)

On screen: “Destination Space / Profile: Working RGB - sRGB IEC61966-2.1” [rest omitted]  
Shows: Convert to Profile dialog with the destination-profile list open.

![1343 · U54 · L82 · 09:50](frames/U54L82-F0950.00.jpg)

On screen: “Conversion Options / Intent: Relative Colorimetric / Use Black Point Compensation / Use Dither / Flatten Image to Preserve Appearance” [rest omitted]  
Shows: Convert to Profile dialog with the print profile and conversion options displayed.

![1343 · U54 · L82 · 10:10](frames/U54L82-F1010.00.jpg)

On screen: [rest omitted]  
Shows: Red-dress portrait and its adjustment and background layers in Photoshop.

## Save the working file and delivery copy

Anchor: 1343 · U54 · L82 · 10:48–13:38

For the actual save, I save to my computer. Keep the working file with its layers as a Photoshop document. The list of formats is shorter after conversion to CMYK because some formats do not support that color space. PNG is not in this list, and it would not be the format I would choose for printing anyway. The main formats here are Photoshop, JPEG, PDF, and TIFF; all support CMYK.

TIFF is the optimum file, particularly when the recipient may make changes such as resizing. If you send a file to print and nothing will be changed—the printer will simply print it—you can send a JPEG at the highest quality, level 12. For any output, whether print or web, choose the right profile and size. If you are sending a file to a client, I would typically choose a highest-quality JPEG in sRGB unless the client specified something else. The best option is also to send TIFF files, but you are in for a much longer delivery time (captions: “buy Urim”) because TIFF is much larger than a JPEG.

That is how I think you should deliver files to a client. In the next lesson, we will look at finishing touches for pictures and make a photo logo from your own signature, which has become quite popular.

![1343 · U54 · L82 · 11:11](frames/U54L82-F1111.00.jpg)

On screen: “Format / Photoshop / JPEG / Photoshop PDF / TIFF” [rest omitted]  
Shows: Save As dialog with the format menu open over the red-dress portrait.
