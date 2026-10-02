# Lesson 19 · Animation Fundamentals 3

Anchor: 3762 · U5 · L19 · 12:38 · https://www.domestika.org/en/courses/3762-animated-infographics-with-illustrator-and-after-effects/units/15362-animating-the-artwork-from-static-to-dynamic#course_lesson_48595

## Staggering the decoration pattern

Anchor: 3762 · U5 · L19 · 00:00–01:29

In the timeline, isolate the elements with the yellow label by using Solo. Check that their order follows a precise, consistent pattern; here, the elements form diagonals. Select all the layers with Command+A on Mac or Ctrl+A, then exclude the first layer. Deselect it with Shift-click or by dragging a selection. Move the elements in the two frames on the right later in the timeline. This staggers the animation: it begins in the upper-left corner and continues across as one progression.

Some layers have no content before the movement begins. Select all layers and extend their content earlier so every element is already visible at second zero. Apply the same adjustment to the other elements.

![3762 · U5 · L19 · 00:40.70](frames/U05L19-F0040.70.jpg)

On screen: [none]  
Shows: A diagonal arrangement of yellow decoration elements in the composition, with their layers visible in the timeline.

## Animating Margarita decorations in a separate composition

Anchor: 3762 · U5 · L19 · 01:29–02:48

Margarita needs its own composition (*composizione*), 03_OTHER_MARG. Create a new precomposition (*precomposizione*) folder inside 01_COMP and put the precomposition there. After importing the layers, their anchor point (*punto di ancoraggio*) is shared, but it needs to be centered on each individual element. A quick way to do this is Layer > Transform > Center Anchor Point in Layer. Each element will then have a centered anchor point.

The Margarita animation starts at second 12 and enters between seconds 12 and 13. Reveal Scale (*scala*) by pressing S. Set every element's scale to 0 at second 12 and to 100% at second 13. Repeat this at second 15, then return the scale to 0 at second 16. The circles enter and then disappear. Keep their speed consistent with the other elements.

![3762 · U5 · L19 · 02:20.50](frames/U05L19-F0220.50.jpg)

On screen: "03_OTHER_MARG" [rest omitted]  
Shows: Lavender decoration elements in inner and outer circles in the Margarita composition.

## Grouping and rotating Margarita elements

Anchor: 3762 · U5 · L19 · 02:48–05:59

Select the inner circle of the drawing and fill all its elements a vivid pink. Choose the fuchsia label and align its elements on the same plane. This creates two distinct groups: one for the inner circle and one for the outer circle. Create a null object (*oggetto nullo*) and place it at the center of the elements. Duplicate it for the blue label. Parent all the fuchsia elements to the first null object and all the blue-labeled elements to the second.

![3762 · U5 · L19 · 03:27.70](frames/U05L19-F0327.70.jpg)

On screen: [rest omitted]  
Shows: The Margarita composition with a pink inner circle of elements and a larger outer ring of white elements.

Use the null objects to animate rotation. Add a rotation keyframe at the beginning and another at the end of the animation. Rotate the first null object by 90° and the second by −90°. You can also animate each null object's scale so the elements start much smaller and grow outward. They grow outward during the exit too. Apply the same speed to these keyframes.

Insert the Margarita precomposition in 03_OTHER. Its elements will appear with the cocktail and then disappear, leaving room for the other decorations. In Main, insert the 03_OTHER decoration composition. Expand the layer controls to set its blending mode (*metodo di fusione*) to Difference (*differenza*). The decorative animation will then interact with the already animated cocktail shapes, adding another visual effect. The cocktail shapes and a composition of decorations now move together.

![3762 · U5 · L19 · 05:22.30](frames/U05L19-F0522.30.jpg)

On screen: [rest omitted]  
Shows: The composition with the red and magenta cocktail forms and the black outlined square.

## Setting up the cocktail text

Anchor: 3762 · U5 · L19 · 05:59–08:19

Finish the animation by adding text in composition 02_TXT. Set the composition background to white in Composition Settings. Add the visual's key, then create a text layer. Selecting a different text layer lets you change its wording and formatting. Choose a color and font. You can also copy text directly from Illustrator: use Command+C or Ctrl+C, then paste into the selected text layer with Ctrl+V on Windows or Command+V on Mac. The text keeps its size and formatting.

Set each text layer's anchor point at its lower-left corner. Use the reference screens to find the exact position or reuse the coordinates from Illustrator. Duplicate a selected text layer with Ctrl+D or Command+D. Press R to reveal its Rotation control and rotate it 90° as needed. Do this for all four text elements to establish the typographic layout.

![3762 · U5 · L19 · 07:41.10](frames/U05L19-F0741.10.jpg)

On screen: "Boulevardier"  
Shows: The first cocktail title on the white text composition.

![3762 · U5 · L19 · 08:03.10](frames/U05L19-F0803.10.jpg)

On screen: [rest omitted] / "Bourbon or Rye Whiskey 45ml" [rest omitted]  
Shows: The Boulevardier text layout over the colored cocktail forms, with ingredient labels around the composition.

## Building a continuous text loop

Anchor: 3762 · U5 · L19 · 08:19–11:45

Begin with the Boulevardier and make cyclic text animations so the loop (*ciclo*) runs smoothly. The text takes one second to enter. At second 1, set a Position (*posizione*) keyframe for all the text layers, then return to second 0. Move the cocktail title 500 pixels to the left. Apply the same movement along the axis to the other text. During the first second, all the elements will move into their proper positions.

The text stays still until second 3, so add another Position keyframe there. Move to second 4 to create a short exit animation, shifting the cocktail title 500 pixels to the right and doing the same for the other text. At second 3, between frames 9 and 10, select all layers and use Shift+D to split them; delete the right-hand portions. Set the speed on all keyframes. This produces a short entrance, a pause while the titles are visible, and an exit.

Select and duplicate all the layers, then set the duplicates to start at second 3. As the first text moves out, a new one will enter. Duplicate the opening text layers and position them below the Boulevardier. Make the keyframes meet at the end so the animation loops continuously. Repeat by duplicating layers and replacing the text with the final wording. Once all the text is in place, the ingredients for each cocktail form a text loop.

## Assembling and trimming the animation

Anchor: 3762 · U5 · L19 · 11:45–12:38

Return to the Main composition and place the text composition below the decorations. Move to second 25 and right-click the work area (*area di lavoro*) to trim the composition at that point. The result is a cycle in which the shapes change size to fit the cocktail ingredients. The decorations blend with the shapes and typography through the Difference blending mode, creating a unified animation. The animation is ready; the next lesson covers exporting it with Media Encoder.

![3762 · U5 · L19 · 11:58.30](frames/U05L19-F1158.30.jpg)

On screen: "Americano" / "Bitter Campari" / "30ml" / "Sweet Red Vermouth" / "30ml" / "A splash of soda water" [rest omitted]  
Shows: The Americano composition with its cocktail shapes, decoration points and ingredient labels.
