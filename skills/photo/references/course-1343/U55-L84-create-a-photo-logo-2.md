# Lesson 84 · Create a Photo Logo 2

Anchor: 1343 · U55 · L84 · 12:44 · https://www.domestika.org/en/courses/1974-course-5-final-touches-and-useful-tips/units/6482-create-a-photo-logo#course_lesson_19508

## Compare the pen signature with a logo trace

Anchor: 1343 · U55 · L84 · 00:00–00:49

I’ll remove the white signature layer from the previous example. (It remains visible on screen.) The scanned signature has the look of an actual pen: some parts are faded, other parts are see-through, and the edge is a little jagged. If you want a more logo-like look instead of a real signature, trace it.

![1343 · U55 · L84 · 00:17](frames/U55L84-F0017.00.jpg)

On screen: [illegible] / "Actions" / "Workflow" / "Dodge & Burn" / "Frequency Separation" / "Colour grade" / "White Signature" / "Black Signature" [rest omitted]  
Shows: A white signature at the lower-right of a dark portrait, with the Actions panel open.

![1343 · U55 · L84 · 00:41](frames/U55L84-F0041.00.jpg)

On screen: [rest omitted]  
Shows: A close view of the black signature on a light portrait, with a magnified detail inset.

## Set up a smooth brush trace

Anchor: 1343 · U55 · L84 · 00:49–03:35

I close the Actions panel and create a new layer with Shift+Command+N on Mac or Shift+Control+N on Windows. I call it Signature Trace. I press B for the Brush tool and choose a hard brush. I set opacity and flow to 100%. I normally advise against smoothing for natural brushwork, but here I want a very smooth-looking logo, so smoothing will help.

In Brush Settings, I remove the spacing. Photoshop saves processing time and energy by leaving gaps between the marks in a brush stroke. If I increase the spacing, a stroke is just dots placed next to each other, which can make a bumpy line. This saves computer processing power, but for this trace I bring spacing down to its lowest value. I paint in black and adjust the brush size to fit the original pen strokes.

![1343 · U55 · L84 · 02:10](frames/U55L84-F0210.00.jpg)

On screen: "Brush Settings" / "Spacing" / "48%" [rest omitted]  
Shows: The signature on a white canvas beside the brush-spacing control and its stroke preview.

The trace does not match the original perfectly, but that is fine. I also add the little dots.

![1343 · U55 · L84 · 03:21](frames/U55L84-F0321.00.jpg)

On screen: [none]  
Shows: The black trace crossing the lighter scanned signature on a white canvas.

## Add a changeable background and refine the trace

Anchor: 1343 · U55 · L84 · 03:35–05:22

To make a white background, I use a Solid Color layer rather than filling a layer with white pixels. I can change a Solid Color later, and it saves file size because pixels take up space while this type of layer does not.

If I were preparing the signature properly, I would use Liquify and work to smooth it as much as possible. It is not easy to do on a computer, even with my own signature; the main thing is to understand the approach rather than finish it here. I click OK. I would also turn the trace into a Smart Object before Liquify so I could change it later. The crooked line is visible, but that is okay for now.

![1343 · U55 · L84 · 04:12](frames/U55L84-F0412.00.jpg)

On screen: "Liquify (signature scan.tif @ 100%)" [rest omitted]  
Shows: The signature on a transparent canvas in Photoshop’s Liquify window.

![1343 · U55 · L84 · 04:48](frames/U55L84-F0448.00.jpg)

On screen: "signature trace" / "Color Fill 1" [rest omitted]  
Shows: The traced signature on a white Solid Color background, with its layers visible.

## Turn the trace into a brush and try it on a photograph

Anchor: 1343 · U55 · L84 · 05:22–06:25

To select the signature, I Command-click its layer thumbnail, or Control-click on Windows. I use the menu option Define Brush Preset and name the brush Signature. The signature selection is now the brush. I create a new layer and make a single click to place it. I can use any size that seems appropriate, but making it larger than the original introduces distortion. Scan the signature at a fairly high resolution. If I want to use it very large, a brush will not work because it is based on pixels.

![1343 · U55 · L84 · 06:00](frames/U55L84-F0600.00.jpg)

On screen: "Layer 1" / "signature scan" [rest omitted]  
Shows: A black brush signature at the lower-left of a dark portrait, with the white signature remaining at the lower-right from the previous lesson.

## Make a Work Path from the selected signature

Anchor: 1343 · U55 · L84 · 06:25–07:38

For a vector logo, I repeat the steps used to make the brush. With the signature still selected, I open the Paths panel, choose the menu option, and select Make Work Path. The tolerance controls how closely the path follows the selection: a lower value creates more points. A detailed path is useful, but one pixel, which I believe is the default, makes the line very bumpy. I prefer two or three pixels, so I try two. It is not perfect, but it is okay.

![1343 · U55 · L84 · 06:59](frames/U55L84-F0659.00.jpg)

On screen: "Make Work Path" / "Tolerance: 2.0 pixels" / "OK" / "Cancel" [rest omitted]  
Shows: The signature with the Make Work Path dialog set to 2.0 pixels.

## Save and edit the vector path

Anchor: 1343 · U55 · L84 · 07:38–09:53

Before editing, I change the temporary Work Path into a proper path. A Work Path is temporary and can be lost easily, like working directly on the Background layer. I double-click it and rename it Signature. The crooked angle I pointed out earlier is also present in the vector.

I use the Direct Selection tool to activate a point and change its handles to alter the line. I can also nudge points with the keyboard arrows. To edit a brush version, I can use Liquify or keep painting. To select the vector path, I use the Path Selection tool and click it; another way is to click outside the path in the Paths panel, then select it again.

![1343 · U55 · L84 · 08:08](frames/U55L84-F0808.00.jpg)

On screen: "Save Path" / "Name: Signature" / "OK" / "Cancel" / "Paths" / "Work Path" [rest omitted]  
Shows: The path’s points selected around the signature, with a dialog to save it as Signature.

![1343 · U55 · L84 · 08:30](frames/U55L84-F0830.00.jpg)

On screen: [none]  
Shows: Selected vector points and handles along the signature.

## Define and place a custom shape

Anchor: 1343 · U55 · L84 · 09:53–11:17

With the path selected, I choose Edit > Define Custom Shape. A path must be selected for this command; if the option is greyed out, that is usually the reason. I name the custom shape Signature and click OK.

A custom shape can have a fill and a stroke, or no fill and only a stroke. I choose a white fill and drag the shape out. Shapes do not constrain proportions by default, so I hold Shift to constrain them. Adobe, if you listen to this course, please make Shift the key for constraining proportions, while keeping proportions constrained by default for everything.

![1343 · U55 · L84 · 09:53](frames/U55L84-F0953.00.jpg)

On screen: "Edit" / "Define Custom Shape..." [rest omitted]  
Shows: The Edit menu with Define Custom Shape selected above the signature path.

![1343 · U55 · L84 · 10:18](frames/U55L84-F1018.00.jpg)

On screen: "Shape" / "Fill:" / "Stroke:" / "1 px" [rest omitted]  
Shows: Shape controls above a portrait, including the fill and stroke settings.

## Resize the vector logo and review its uses

Anchor: 1343 · U55 · L84 · 11:17–12:44

Once the custom shape is placed, I can change its colour; a pink signature logo is one example. Its benefit is that it is independent of resolution, so I can make it as large as I want. I use Command+T or Control+T to enlarge it. When I resize the placed shape, proportions are constrained by default; holding Shift now distorts it rather than constraining it. At any size, the image keeps perfect quality. At 100% zoom, the edge is still clean.

I look forward to seeing your logos. You can upload them so I and your fellow students can give you feedback. This is not to everyone’s taste, but it can be a good alternative to a watermark. In the next lesson we will do a practical challenge together, combining the skills learned on this course.

![1343 · U55 · L84 · 11:25](frames/U55L84-F1125.00.jpg)

On screen: "Shape" / "Fill:" / "Stroke:" / "1 px" [rest omitted]  
Shows: The pink custom shape signature placed across the portrait.

![1343 · U55 · L84 · 11:52](frames/U55L84-F1152.00.jpg)

On screen: "Signature 1" [rest omitted]  
Shows: An enlarged pink vector signature across a portrait, inside a transform box.

![1343 · U55 · L84 · 12:05](frames/U55L84-F1205.00.jpg)

On screen: "ged.jpg @ 100% (Signature 1, RGB/8*)" [rest omitted]  
Shows: The pink custom shape signature enlarged across the portrait at 100% zoom.
