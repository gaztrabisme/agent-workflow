# Lesson 76 · Frequency Separation 1

Anchor: 1343 · U51 · L76 · 17:19 · https://www.domestika.org/en/courses/1974-course-5-final-touches-and-useful-tips/units/6475-frequency-separation#course_lesson_19432

## What frequency separation divides

Anchor: 1343 · U51 · L76 · 00:11–01:35

I’m going to teach you how to use frequency separation in Photoshop. It is a powerful retouching tool, but it can be difficult to understand. I’ll break down how it works and what the numbers mean. It takes time to get used to, so I’ll also show how to create an action from the technique; first I’ll explain the idea and show how to create and use the separation.

An image contains two frequencies. High frequencies hold the grain and texture; low frequencies hold color and light. Separating them lets you clone texture without bringing in color, or change color without disturbing texture. It is a different, somewhat complicated way to work, and it takes practice to understand both the separation and how to make it.

![1343 · U51 · L76 · 01:01](frames/U51L76-F0101.00.jpg)

On screen: [none]  
Shows: The original portrait of a seated man in a gray suit against a dark paneled wall.

## Build the low- and high-frequency layers

Anchor: 1343 · U51 · L76 · 01:35–04:54

Start by making two copies of the Background with Command-J on a Mac or Control-J on Windows. Name the lower copy Low frequency and the upper copy High frequency; you could instead call them colors and texture. Put the two copies in a group named Frequency Separation. Open the group, switch off the upper layer so it does not cover the lower one, and select the lower layer.

Choose Filter, Blur, Gaussian Blur and zoom to 100% with Command-1 or Control-1. Use a low radius that removes most of the texture and pixel structure. The goal is not to blur the image; it is to remove the texture. The right radius changes from image to image, so do not apply one fixed value to every photograph.

![1343 · U51 · L76 · 02:31](frames/U51L76-F0231.00.jpg)

On screen: "Gaussian Blur" / "Radius: 12.0 Pixels" / "Frequency separation" / "High frequency" / "Low frequency" [rest omitted]  
Shows: The Gaussian Blur dialog previews the man's portrait with the radius set to 12.0 pixels.

Turn on and select the High frequency layer. Choose Image, Apply Image. Apply Image combines two images or layers and offers several blend modes. Here, use the Low frequency layer as the source rather than Merged. The high-frequency layer currently contains both color and texture. Subtract the Low frequency layer to remove the color from it, leaving texture.

Set Scale to 2, the highest setting, and Offset to 128. A value of 128 is midway between black and white, so the color being subtracted becomes mid-gray. Linear Light removes that mid-gray. Click OK, then set the layer’s blend mode to Linear Light. The lower layer now holds color and the upper layer holds texture. If you hide the Background and Low frequency layers, you can see the high frequencies by themselves.

![1343 · U51 · L76 · 04:35](frames/U51L76-F0435.00.jpg)

On screen: "Layer: Low frequency" / "Blending: Subtract" / "Opacity: 100%" / "Scale: 2" / "Offset: 128" [rest omitted]  
Shows: The Apply Image dialog sits over the gray texture-only rendering of the portrait.

![1343 · U51 · L76 · 04:54](frames/U51L76-F0454.00.jpg)

On screen: "Linear Light" / "High frequency" / "Low frequency" [rest omitted]  
Shows: The portrait is visible again with the Frequency Separation group open and the high-frequency layer selected.

## Retouch texture and reduce shine

Anchor: 1343 · U51 · L76 · 04:54–10:09

On the High frequency layer, use the Clone Stamp (S) and set its sample menu to Current Layer. If you sample Current and Below, the tool can pull color from the layer underneath and put it into the texture layer, creating a strange result. Since color and texture have been separated, sample only the current layer. In the preview, the sample copies the gray texture; when I apply it, it does not bring the sampled color across and keeps the darker tone below. Zoom in on the man’s skin and clone away marks without having to match their tones. Normally the Clone Stamp needs a good color and tone match. It gives a better-quality result than the Healing Brush, but is harder to use; frequency separation makes it easier to work with.

I chose this photograph by James Ross partly because of its bright highlights. I do not think they are a problem in this image, but shiny highlights on a face can be difficult to remove with cloning or healing brushes. To reduce one, select Low frequency and paint on the image itself. For a non-destructive result that you can control with opacity, create a new layer called Shine. Choose the Brush (B), reduce opacity and flow—press 3 for 30% opacity and Shift-1 for 10% flow—and make the brush larger. Sample a fairly bright color and paint over the highlight.

If you can see the brush stroke, the settings are probably too high. Undo it. Use 20% opacity, keep sampling new colors as you move across the area, and do not paint it all with one color; varying the sampled colors keeps the result more dynamic. Twenty percent still looks too strong here, so lower it a little more. This changes the color without changing the texture. Toggling the layer off shows that the original texture remains.

The brush strokes looked poor because I had the brush at 100% hardness. You could reduce the hardness and start again, or soften the edges of the strokes with Filter, Blur, Gaussian Blur. This blur works like the soft edge of a brush: keep the strokes visible but soften their edges. Zoom back out to 100% and check the result. The shine is reduced, and you can lower the layer opacity further to control it. Bright spots draw attention, so reducing this kind of shine can remove a distraction.

![1343 · U51 · L76 · 06:40](frames/U51L76-F0640.00.jpg)

On screen: "Sample: Current Layer" / "Linear Light" / "High frequency" / "Low frequency" [rest omitted]  
Shows: A close view of the man's face with the Clone Stamp cursor on his cheek and the frequency layers visible.

![1343 · U51 · L76 · 09:37](frames/U51L76-F0937.00.jpg)

On screen: "Gaussian Blur" / "Radius: 8.0 Pixels" / "Shine" [rest omitted]  
Shows: A Gaussian Blur dialog is open over the man's face; the Shine layer is selected.

![1343 · U51 · L76 · 09:43](frames/U51L76-F0943.00.jpg)

On screen: "Frequency separation" / "High frequency" / "Shine" / "Low frequency" [rest omitted]  
Shows: The full portrait with the Shine layer selected and the reduced highlights visible on the man's face.

## Record and repair a reusable action

Anchor: 1343 · U51 · L76 · 10:09–17:19

Now repeat the setup on another image and make an action, because the process has several steps. When an image already has retouching, account for it: duplicating the Background would leave that work out. The example layer is called Clone (captions: “Clown”). Set the Clone Stamp’s Sample to Current Layer; otherwise it will not work. In an action that must work with different layer setups, make a blank layer and stamp a composite of the visible image into it. Use Shift-Option-Command-E on Mac or Shift-Control-Alt-E on Windows. That way the action can include existing clone layers as well as an untouched background.

Open the Actions panel and leave button mode. Create a new action called Frequency Separation, choose violet as its color, and click Record. Make the composite, duplicate that layer with Command-J or Control-J, name the lower layer Low frequency and the upper one High frequency, and put them in a Frequency Separation group. Open the group, select Low frequency and switch off High frequency. Choose Filter, Blur, Gaussian Blur and zoom to 100%. Use only enough blur to remove texture; this second image is a little larger, so its radius is slightly higher. About 5 pixels looks good here.

Select and turn on High frequency. Choose Image, Apply Image and change the source layer to Low frequency. Photoshop retains the settings used earlier, so there is nothing else to change. Click OK and change the blend mode to Linear Light (captions: “linear line”).

In the Actions panel menu, choose Insert Stop. The label is confusing; “Insert Message” would make more sense. A stop lets you show a message to yourself or another person who uses a shared action. Enter a reminder to set the Clone Stamp to Current Layer, and allow the action to continue after the message. If you forget this setting, the technique will not work. Remember to click Stop to finish recording.

To share actions, use Load or Save in the Actions panel menu. Save Actions is disabled until you select an action. In Photoshop 2020 you can save only a whole folder of actions, not one action by itself. To share one action, put it in its own folder, save that folder, then load it on another computer.

Test the action by reverting the image, deleting the layers, selecting the action and pressing Play. Photoshop reports that the command “Merge Visible” is not currently available. The action does not work and produces a strange result. This is a useful way to catch a mistake. If there are layers in the image, use Merge Visible—the Shift-Option-Command-E shortcut—to include them. If there are no layers, the Merge Visible or Stamp Visible command is unavailable. Start by adding a blank layer.

To fix the action, record again and add a layer. Stop recording, then drag Make Layer from the bottom of the action list to the top. Make Layer must happen first; then Merge Visible can work. Delete the failed result and try the action again. The reminder appears—set the Clone Stamp to Current Layer—then you can continue.

![1343 · U51 · L76 · 10:41](frames/U51L76-F1041.00.jpg)

On screen: [none]  
Shows: The second working portrait, a woman looking over her shoulder against a pale background.

![1343 · U51 · L76 · 14:21](frames/U51L76-F1421.00.jpg)

On screen: "Record Stop" / "Remember to set clone stamp to Current Layer" [rest omitted]  
Shows: The action’s Record Stop message dialog is open over a close view of the woman’s portrait.

![1343 · U51 · L76 · 15:42](frames/U51L76-F1542.00.jpg)

On screen: "The command “Merge Visible” is not currently available." / "Retouching" / "Workflow" / "Dodge & Burn" / "Frequency Separation" [rest omitted]  
Shows: Photoshop’s error dialog appears over the woman’s image while the Frequency Separation action is selected.

![1343 · U51 · L76 · 15:59](frames/U51L76-F1559.00.jpg)

On screen: "Linear Light" / "Opacity: 100%" / "Frequency separation" / "High frequency" [rest omitted]  
Shows: A strongly overexposed, posterized orange rendering of the woman appears after the action fails.

![1343 · U51 · L76 · 16:42](frames/U51L76-F1642.00.jpg)

On screen: "Merge Visible" / "Layer Via Copy" / “Select layer "Layer 1"” / "Set current layer" [rest omitted]  
Shows: The existing action steps are expanded in the Actions panel beside the woman’s portrait.
