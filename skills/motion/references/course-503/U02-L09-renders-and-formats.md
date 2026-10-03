# Lesson 09 · Renders and formats

Anchor: 503 · U2 · L09 · 10:56 · https://www.domestika.org/en/courses/503-introduction-to-motion-design-and-animation-curves-in-after-effects/units/2010-cheering-in-after-effects-with-style#course_lesson_7406

## Render types and their purposes

Anchor: 503 · U2 · L09 · 00:08–01:05

503 · U02 · L09 · 00:08–01:05

In this lesson, we’ll see how to launch a render (*renderizado*) from After Effects. For the optimized renders I always use Adobe Media Encoder. While it renders, I can keep animating in After Effects.

Rendering means generating the file that contains our animation, in whichever format we choose: QuickTime or an image sequence (*secuencia de imágenes*). I’ll pause these two before they distract you. There are two types of render: Master renders (*renders master*), which have no loss of quality and can serve as the source for later optimized renders (*renders optimizados*), and optimized renders, which we can make directly for social media, for example.

![503 · U2 · L09 · 00:37.90](frames/U02L09-F0037.90.jpg)

On screen: "1920 x 1080" / "1080 x 1080" [rest omitted]  
Shows: The wide master composition with a woman in pink and a man in blue dancing.

## Framing guides for different formats

Anchor: 503 · U2 · L09 · 01:05–03:25

503 · U02 · L09 · 01:05–03:25

Here’s a small trick for working with compositions (*composiciones*) or projects in multiple formats. Imagine a 1920 × 1080 composition whose name matches its dimensions; this is the master format. We make the animation in it, with Phil dancing. If we later want a square 1080 × 1080 version for Instagram, we can import the master animation into that composition, but the sides will be cropped and we will lose a lot of information.

![503 · U2 · L09 · 01:38.00](frames/U02L09-F0138.00.jpg)

On screen: [rest omitted]  
Shows: The square composition displays the central portion of the selected wide dancing clip; the layer bounds extend beyond the square frame at both sides.

To see what would be cropped in the Instagram format, I recommend making a framing guide (*referencia de encuadre*) in the master composition. Create a shape layer (*capa de forma*) with a rectangle, double-click it, and rename the layer `frame`. In the rectangle settings, set the size to exactly 1080 × 1080, remove the fill, and add a stroke about six pixels thick. Choose a more visible color. This gives you a framing reference.

Select the layer, right-click, and choose Guide Layer (*capa guía*). The guide stays visible while you work, but it will never appear in the render. When the master composition is nested inside the Instagram composition, the guide no longer appears there either. If you know a project will need several formats—Twitter, Instagram, Dribbble, or other social networks—I recommend working in the largest master format and adding framing guides for the other formats. Turning the shape layers into guide layers keeps them out of the render and lets you see which parts will fall inside or outside each crop.

![503 · U2 · L09 · 02:33.30](frames/U02L09-F0233.30.jpg)

On screen: "frame" / "Rectangle Path 1" / "Size" / "1080.0,1080.0" / "Stroke 1" [rest omitted]  
Shows: A purple square framing guide over the wide dancing clip.

![503 · U2 · L09 · 02:44.90](frames/U02L09-F0244.90.jpg)

On screen: "Guide Layer" [rest omitted]  
Shows: The right-click menu with Guide Layer highlighted beside the square guide over the wide composition.

## Set the render area and add the composition to the queue

Anchor: 503 · U2 · L09 · 03:25–04:47

503 · U02 · L09 · 03:25–04:47

Now for Master renders, or renders without loss. First define the area to render, just as when setting the preview area: the part between these endpoints is what will render. I often use the markers to show where the render ends. I move an endpoint while holding Shift, and it snaps to the marker so I can set the render area exactly where I need it.

Next, add the current composition and this defined area to the render queue (*cola de render*): choose Composition, then Add to Render Queue. The queue panel may seem to take over the timeline, but the composition tabs are still there. The right side is where we create the final file. We hardly ever need to change Best Settings under Render Settings, so leave those settings alone. The important part is Output Module (*módulo de salida*), which is currently set to Lossless.

![503 · U2 · L09 · 04:07.10](frames/U02L09-F0407.10.jpg)

On screen: "Work Area Duration" [rest omitted]  
Shows: The composition with its work area marked on the timeline.

![503 · U2 · L09 · 04:18.10](frames/U02L09-F0418.10.jpg)

On screen: "Composition" / "Add to Render Queue" / "Ctrl+M" [rest omitted]  
Shows: The Composition menu with Add to Render Queue highlighted.

## Choose a master-render format

Anchor: 503 · U2 · L09 · 04:47–05:54

503 · U02 · L09 · 04:47–05:54

The Output Module dialog lists the file types for the render. In general, Master renders are image sequences, even if that seems a little strange at first. I usually choose a TIF sequence; there is also a PNG sequence. Never use JPGs here, because we want no quality loss. The three formats we normally use for Master renders are TGA, TIFF, and PNG. We can import these sequences into After Effects later and quickly make optimized renders from them. Master renders can also be a delivery format—for example, for television or another broadcast medium.

If we want the image sequence to include transparency, we have to set that here. Then click OK and use the render button to generate the sequence. That gives us the Master render, in this example as PNG.

![503 · U2 · L09 · 05:29.00](frames/U02L09-F0529.00.jpg)

On screen: "Output Module Settings" / "Format: PNG Sequence" / "JPEG Sequence" / "PNG Sequence" / "TIF Sequence" / "Targa Sequence" [rest omitted]  
Shows: The Output Module format menu open with the sequence formats listed.

![503 · U2 · L09 · 05:40.90](frames/U02L09-F0540.90.jpg)

On screen: "Channels: RGB + Alpha" [rest omitted]  
Shows: Output Module settings for a PNG sequence, with RGB + Alpha selected for transparency.

![503 · U2 · L09 · 05:47.50](frames/U02L09-F0547.50.jpg)

On screen: "Render" / "Custom: PNG Sequence" [rest omitted]  
Shows: The render queue with the PNG sequence ready to render.

## Open Adobe Media Encoder for optimized renders

Anchor: 503 · U2 · L09 · 05:54–06:45

503 · U02 · L09 · 05:54–06:45

Now suppose this is our Instagram format and we want to make a render suited to that platform. These are optimized or delivery formats, for example, for social media. The useful way to make this kind of render is to send it to Adobe Media Encoder. Click the button and wait a little for the program to open. It works alongside After Effects and Adobe Premiere, and it can take a moment.

![503 · U2 · L09 · 06:38.70](frames/U02L09-F0638.70.jpg)

On screen: "Adobe Media Encoder CC 2018" / "1080 x 1080" / "H.264" / "Vimeo HD 1080p" [rest omitted]  
Shows: Adobe Media Encoder open with the square composition in its queue.

## Select presets and queue several outputs

Anchor: 503 · U2 · L09 · 06:45–08:07

503 · U02 · L09 · 06:45–08:07

Adobe Media Encoder is open with our 1080 × 1080 composition. Enlarge the view and look at the presets (*ajustes preestablecidos*) in the lower-left panel. For social media, look under Video Web. There are many profiles: Facebook 720 and 1080, a smaller Twitter format and its larger, higher-resolution format, and Vimeo 4K and HD. These formats are generally based on the settings recommended by the platforms themselves.

Another useful thing is that I can drag several presets onto the same composition. When I press Play, Media Encoder makes several different videos. Suppose I also need YouTube HD: drag that preset in too. It will make the first version, then the YouTube version, and then the Vimeo version, giving me two videos in different formats in one go. On the right, click to choose the output folder and file name. To change a preset’s settings, click its name—for example, YouTube HD 720.

![503 · U2 · L09 · 07:25.30](frames/U02L09-F0725.30.jpg)

On screen: "Redes sociales" [Social networks] / "Facebook 720p HD" / "Facebook 1080p HD" / "Twitter 640x360 (1 Mbps)" / "Twitter 720p HD (6 Mbps)" / "Vimeo HD 720p" / "Vimeo HD 1080p" / "Vimeo 4K 2160p" [rest omitted]  
Shows: The expanded social-network preset list in the lower-left panel.

![503 · U2 · L09 · 07:58](frames/U02L09-F0758.00.jpg)

On screen: "Guardar como" [Save as] / "Nombre:" [Name:] / "1080 x 1080.mp4" / "Tipo:" [Type:] / "Archivos de video (*.mp4)" [Video files (*.mp4)] / "Guardar" [Save] / "Cancelar" [Cancel] [rest omitted]  
Shows: The output Save As dialog with the filename field selected and the Save and Cancel buttons.

## Match preset dimensions to the composition

Anchor: 503 · U2 · L09 · 08:07–08:40

503 · U02 · L09 · 08:07–08:40

For a square composition of 1080 × 1080, remember that presets come with their own width and height. It is very important to click Match Source. After that, the settings show 1080 × 1080. That way the output will be in the Instagram format; otherwise, it would not be. Let’s look in the social-network list: in this case I don’t have an Instagram preset.

![503 · U2 · L09 · 08:23.30](frames/U02L09-F0823.30.jpg)

On screen: "Ajustes de exportación" [Export settings] / "Formato: H264" [Format: H264] / "Ajuste preestablecido: YouTube HD 720p" [Preset: YouTube HD 720p] / "Coincidir con origen" [Match Source] [rest omitted]  
Shows: The export settings panel with Match Source available for the square composition.

## Adjust the social preset and bitrate

Anchor: 503 · U2 · L09 · 08:40–09:30

503 · U02 · L09 · 08:40–09:30

Although there is no Instagram preset here, Facebook 1080 works very well. Drag it into the queue, open its properties, and click Match Source. That changes it from 1920 × 1080 to 1080 × 1080.

If you want to adjust the preset, you can change the target bitrate (*velocidad de destino*) and maximum bitrate with their sliders. The panel estimates the final file size below. The target bitrate is the setting that affects quality the most. For example, the estimate is 22 megabytes; if I lower the slider, the file gets smaller, but the quality also goes down.

![503 · U2 · L09 · 08:46.90](frames/U02L09-F0846.90.jpg)

On screen: "YouTube HD 720p" / "Vimeo HD 1080p" [rest omitted]  
Shows: Two queued output rows with YouTube HD 720p and Vimeo HD 1080p presets.

![503 · U2 · L09 · 09:18.90](frames/U02L09-F0918.90.jpg)

On screen: "Velocidad de destino (Mbps)" [Target bitrate (Mbps)] / "Velocidad máxima (Mbps)" [Maximum bitrate (Mbps)] / "Tamaño de archivo estimado: 18 MB" [Estimated file size: 18 MB] [rest omitted]  
Shows: The export settings panel with target and maximum bitrate sliders and an estimated file size.

## Start the renders and keep working

Anchor: 503 · U2 · L09 · 09:30–09:54

503 · U02 · L09 · 09:30–09:54

Click Accept, then check where the render will be saved and what name it has. Click Play to generate the files. Another advantage is that I can launch renders from Adobe Media Encoder and keep working in After Effects at the same time. Look how happy Phil is.

## Recap: master and optimized delivery

Anchor: 503 · U2 · L09 · 09:54–10:56

503 · U02 · L09 · 09:54–10:56

We have two kinds of render. Master renders have no loss; they can be a delivery format for broadcast, or we can save them and import them into our project to make more optimized renders. We work with image sequences for the Master render: TIFF, PNG, or TGA. Optimized or delivery renders have some loss in quality and are already suited to social networks or other media that need specific optimized settings.

We’ve seen how to render our videos and animations. In the next lesson, we’ll add context so we understand what we mean by designing movement.

![503 · U2 · L09 · 09:59.00](frames/U02L09-F0959.00.jpg)

On screen: [none]  
Shows: Phil dancing in the square composition.

### Key points (derived)

- Keep a lossless Master render as the source for delivery versions; use TGA, TIFF, or PNG image sequences.
- For multiple aspect ratios, build guides in the largest composition and mark them as guide layers so they do not render.
- Use Media Encoder presets for platform-specific delivery, match preset dimensions to the source, and adjust bitrate when file size or quality needs to change.
