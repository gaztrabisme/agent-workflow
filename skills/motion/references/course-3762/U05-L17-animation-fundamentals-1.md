# Lesson 17 · Animation Fundamentals 1

Anchor: 3762 · U5 · L17 · 17:51 · https://www.domestika.org/en/courses/3762-animated-infographics-with-illustrator-and-after-effects/units/15362-animating-the-artwork-from-static-to-dynamic#course_lesson_48416

## Masking gradients inside the cocktail shapes

Anchor: 3762 · U5 · L17 · 00:00–03:38

We have seen how to animate the ingredients and move from one cocktail to the next. In this lesson we will work with blending modes (*modalità di fusione*) and compositions (*composizioni*), and animate the typography and decorations of the cocktails.

Once the main shapes and their movement are set, look at the gradients (*gradienti*) within the shapes. You can create more sophisticated effects by working with the strokes (*tracce*). In After Effects, we will use masks (*maschere*).

The two shape layers interact: as in the Illustrator file, part of one shape has a gradient masked inside the shape below it. Set up the movements first and make sure the shape animation works. Then duplicate the underlying shape layer: select it and press Ctrl+D or Command+D. Press Enter to rename it `01 gradient`. This duplicate has the same properties as the layer below. Apply the Set Matte effect (later captions: *Sat Mat*) to it, and set layer 03 as its mask. Put `01 gradient` above layer 03 so it can be seen. At first there is no visible difference because both layers have the same colors. Invert the gradient colors and apply the new color. Adjust the gradient’s starting point until it is masked inside the intended shape. For convenience, set a color on `01 gradient`.

From now on, the orange layers will be gradients hidden inside other shapes. The Illustrator file shows this effect between these two shapes, then again in the Negroni and Dry Martini (captions: *Dremartini*). For the White Lady and Margarita, we will also apply it to strokes. In the Tequila Sunrise, the stroke colors will change too. In the last cocktail, the Spritz, the effect is applied where the Campari bitter and Prosecco intersect.

![3762 · U5 · L17 · 00:53](frames/U05L17-F0053.00.jpg)

On screen: [illegible] [rest omitted]  
Shows: Americano composition with the pink-to-olive gradient crossing into the lower shape.

![3762 · U5 · L17 · 03:03](frames/U05L17-F0303.00.jpg)

On screen: "Boulevardier" / "Negroni" / "Dry Martini" [rest omitted]  
Shows: Illustrator reference board with the cocktail panels and the overlapping areas where the gradients are masked.

## Animating the gradient’s start and end points

Anchor: 3762 · U5 · L17 · 03:38–05:10

Return to After Effects and apply the masking effect to all the shapes. During the animation, the gradient moves upward and becomes invisible in some cases. To fix this, open layer `01 gradient`, go to Gradient Fill, and set keyframes for the gradient’s start and end points. Press U to show only the active keyframes.

Use the null object’s keyframes to locate the main movement. At second 1, position the gradient accordingly. Its start and end points need to move. Give their keyframes the same speed as the earlier keyframes so the gradient moves inside the shapes and lands where it should. At second 3, set new keyframes for both values. When the movement is finished, reposition the gradient where you want it.

## Masking the second cocktail’s gradient

Anchor: 3762 · U5 · L17 · 05:10–07:43

Apply the same effect to the second cocktail. Here, the bourbon (captions: *barbon*) defines the mask for the gradient. Duplicate `01 gradient` and rename the copy `02 gradient`. Reveal the effects applied to the layer. The Set Matte effect that was inside Shape 03 will now be visible, but Shape 02 will be its mask. Change the source in the effect to change which shape acts as the mask. Press U to reveal all the layer’s keyframes (captions: *I*), then select the layer to change its colors. Sample the colors directly from the artwork so they match.

Choose the gradient’s start and end points to create a counter-movement (*contromovimento*) between the two layers. The gradient will then be visible only inside that shape. After copying the keyframes to the new position, change the gradient color. Open Gradient Fill and set a color keyframe. During this transition, the gradient should change at the same time as the color of the shape below it.

The underlying Shape 02 has a Hold keyframe. At second 3, frame 13, the gradient changes. Hold Command or Control and press the left arrow to move back one keyframe. Place the color-change keyframe there so the gradient changes exactly when the color underneath changes. Use this same effect wherever it is needed.

![3762 · U5 · L17 · 05:14](frames/U05L17-F0514.00.jpg)

On screen: "Bourbon or Rye Whiskey" [rest omitted]  
Shows: Boulevardier and Negroni reference panels while the bourbon shape is selected.

## Continuing the masked gradient through the later cocktails

Anchor: 3762 · U5 · L17 · 07:43–10:43

For the Dry Martini, Shape 02 defines the gradient. Duplicate Shape 02 and move the copy upward to create the effect. Name it `02 gradient`, set its color to orange, and apply Set Matte. Shape 03 will act as its mask. Rename the next layer `03 gradient`, set its color to orange, and apply Set Matte as well. For `03 gradient`, set layer 03 as the mask. Apply a linear gradient and adjust its colors to match the established artwork.

In Contents > Rectangle > Gradient Fill, set keyframes for the start and end points. Position the gradient where it is needed, then animate these values so the gradients move and create a dynamic effect. As the shapes float during their secondary movement, the gradient can follow them, wrap around the shape, and reposition itself. From second 9 to second 10, change the start and end points again, and change the gradient colors. Select all the keyframes and set their influence to 85%.

![3762 · U5 · L17 · 07:50](frames/U05L17-F0750.00.jpg)

On screen: "Set Matte" [rest omitted]  
Shows: Dry Martini shapes in After Effects with the Set Matte effect and gradient keyframes visible.

## Keeping the White Lady’s stroke intact

Anchor: 3762 · U5 · L17 · 10:43–12:27

The White Lady has a gradient in the square that also has a stroke. To recreate this in After Effects, duplicate the object. Shape 05 will be the mask. Rename the duplicate `01 mask`, set it to cyan, and add a fill. Set its stroke to zero. The filled shape layer now works like the stroked one. Place it below layer 05, which has the stroke, so the fill shows through without changing the stroke thickness. Hide this layer for now.

Select Shape 03 and duplicate it. Rename the copy `04 gradient`, place it with the other gradients, set its color to orange, and apply Set Matte. In this case, `01 Mask` is the mask for the shape layer. Adjust the start and end points precisely. Here the gradient should run in the opposite direction, contrasting with the colors in the shape layer and its mask.

![3762 · U5 · L17 · 10:43](frames/U05L17-F1043.00.jpg)

On screen: "White Lady" / "Margarita" [rest omitted]  
Shows: White Lady and Margarita reference panels; the White Lady has a gradient-filled shape beneath its black square stroke.

## Changing the Tequila Sunrise strokes

Anchor: 3762 · U5 · L17 · 12:27–14:54

In the Tequila Sunrise, the strokes change color inside the tequila. To apply this in After Effects, duplicate the two Stroke layers and move the copies above the originals. Set them to purple and rename them `01-bar` and `02 stroke pair` (captions: *02 tratto par*). These copies have purple strokes instead of black. Apply Set Matte to one of them, using Shape Layer 02 as the mask. The tequila now animates vividly inside the stroke. Copy the effect by pressing E and apply it to the other layer.

Keep the duplicated strokes purple only inside the shape, rather than across the other elements in the project. Use the null object’s keyframes to mark the exact moments when the color changes, so the strokes stay synchronized. Select the two purple layers and press Shift to make a precise cut. Delete the frames to the right of the cut. Do the same in reverse at a frame before the tequila intersects the other element: delete the frames before that point. The purple layers will then appear only where they intersect the tequila, during this interval.

![3762 · U5 · L17 · 12:27](frames/U05L17-F1227.00.jpg)

On screen: "Tequila Sunrise" / "Mimosa" [rest omitted]  
Shows: The Tequila Sunrise reference with its overlapping outlined squares and the adjacent Mimosa shape.

## Finishing the Spritz and grouping the gradients

Anchor: 3762 · U5 · L17 · 14:54–17:31

The last cocktail, the Spritz, already has a gradient in its stroke, on layer `04 gradient`. As with the tequila, go back and duplicate the layer. Cut it in half and remove the later part. We do not want this element filled with a gradient. Layer `03 gradient` represents the gradient inside this volume and shows its internal changes.

Set a keyframe for the gradient colors, then change them according to the plan: use yellow and its opposite color, red. Set keyframes at the beginning and end for the required gradient. Select all the gradient layers, one at a time or by selecting their shared color label. Lock the group so you can select the layer you need. We have seen how to animate the gradients’ start and end points. You can apply the same animation to the shape layers created earlier to add depth to them. This shape layer can also have animated start and end points.

![3762 · U5 · L17 · 14:54](frames/U05L17-F1454.00.jpg)

On screen: "Take Matte From Layer" / "17.02" [rest omitted]  
Shows: The yellow Spritz shape and its black outline with the Set Matte controls open.

![3762 · U5 · L17 · 16:17](frames/U05L17-F1617.00.jpg)

On screen: [rest omitted]  
Shows: Yellow and red gradients crossing through the overlapping cocktail shapes, with their color keyframes visible.

## Bringing the shapes together

Anchor: 3762 · U5 · L17 · 17:31–17:43

Masks let us place gradients inside other shapes. Here, the effect integrates the shapes: they are no longer separate shape layers, but one object moving through space.

![3762 · U5 · L17 · 17:31](frames/U05L17-F1731.00.jpg)

On screen: [rest omitted]  
Shows: The red, pink and olive shapes integrated into one cocktail form in the composition.
