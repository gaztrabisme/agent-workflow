# Lesson 16 · Designing in After Effects 2

Anchor: 3762 · U5 · L16 · 19:51 · https://www.domestika.org/en/courses/3762-animated-infographics-with-illustrator-and-after-effects/units/15362-animating-the-artwork-from-static-to-dynamic#course_lesson_48596

## Moving from the Negroni to the Dry Martini

Anchor: 3762 · U5 · L16 · 00:00–02:24

You can export at any point to get more control over the project. We will cover exporting at the end of the final project.

For object 3, the soda, there is no need to add keyframes between seconds 3 and 4 because it stays off screen during that interval.

![3762 · U5 · L16 · 00:30](frames/U05L16-F0030.00.jpg)

On screen: [none]  
Shows: The composition preview with the small outlined ingredient positioned above the cocktail artwork.

Return to the Illustrator file to see the next scene: the transition from the Negroni to the Dry Martini (captions: *Dre Martini*). The two cocktails differ in several ways: one ingredient is removed, the shapes change size, and the angle of the upper shape changes. Make these changes on the individual elements, as before.

In After Effects, go to second 6 and copy and paste the keyframes so the elements do not move during this interval. Then go to second 7 and enter the new values for the fourth cocktail. Replace the reference image with the Dry Martini and lock it. For this morph, change the dimensions of the shape layer. The captions also record the aside “Who dies first?” here. Make sure the keyframes are at second 6, then enter the new values: the shape needs to be 760 × 140 pixels with 50-pixel rounded corners. The morph will happen only during this interval; the earlier frames will not change.

![3762 · U5 · L16 · 00:49](frames/U05L16-F0049.00.jpg)

On screen: "Boulevardier" / "Negroni" / "Dry Martini" / "White Lady" / "Margarita" [rest omitted]  
Shows: Illustrator reference board with the ingredient shapes and recipe columns for several cocktails.

![3762 · U5 · L16 · 02:19](frames/U05L16-F0219.00.jpg)

On screen: [none]  
Shows: Dry Martini arrangement in the composition at the second-six keyframe, with shape properties and keyframes open.

## Animating ingredients that leave or change shape

Anchor: 3762 · U5 · L16 · 02:24–04:19

Apply the size change to the third element too, enlarging it. Use the reference image to place the elements correctly. Then animate the ingredient that is no longer part of the cocktail so that it exits the scene. Move it upward with a slight rotation (*rotazione*), while the other elements gather toward the center for a harmonious effect.

![3762 · U5 · L16 · 03:32](frames/U05L16-F0332.00.jpg)

On screen: [none]  
Shows: The cocktail shapes changing size and position on the way into the Dry Martini arrangement.

You can add a secondary animation by changing the shape’s dimensions. Set a size keyframe and reduce its height. This makes the animation more dynamic: as the object moves, it changes shape too.

## Setting up the next cocktail transition

Anchor: 3762 · U5 · L16 · 04:19–07:48

Return to Illustrator for the next scene. This scene has a morph and a color change, and an element that left the frame will re-enter. Animate the angle of this shape in relation to the other one, as well as its size and color.

Allow two seconds for the secondary movement and move to second 9 to inspect the scene change. One element is off screen, so it does not need another keyframe. Shape 02 and Shape 04 need keyframes for position, rotation and size. Add a keyframe for Shape 03 as well, since it is the soda animated earlier.

Move to second 10, replace the reference image, then hide and lock it. Watch the movement carefully: keep the transitions between the cocktails consistent. After changing the sizes, use the reference layer to set the positions of the cocktail shapes. For the black outline, change its size too. Select that layer and set a new size keyframe. Animate the corner roundness as well.

![3762 · U5 · L16 · 04:38](frames/U05L16-F0438.00.jpg)

On screen: "Tequila Sunrise" / "Mimosa" [rest omitted]  
Shows: Illustrator board with the cocktail sequence and the individual artwork panels used as references.

![3762 · U5 · L16 · 07:30](frames/U05L16-F0730.00.jpg)

On screen: "05_WhiteLady.jpg" / "White Lady" / "Size" / "760.0,480.0" / "Roundness" / "50.0" [rest omitted]  
Shows: White Lady reference with its large outlined square over the colored shapes and the corner-roundness property open.

## Straightening the path of the traced element

Anchor: 3762 · U5 · L16 · 07:48–09:24

This establishes the transition from the first cocktail to the fifth. The outlined element has a small movement in position and a slight rotation. To improve that movement, select its null object (*oggetto nullo*), move to the previous keyframe, and paste the previous position and rotation. At the keyframe just before the main animation, move the object to a more upright position and increase its rotation.

The element enters differently from the previous one, and the path it follows is wavy.

![3762 · U5 · L16 · 08:56](frames/U05L16-F0856.00.jpg)

On screen: "Null 4" / "04" / "Null 3" / "03" / "Null 2" / "02" / "Null 1" / "01" [rest omitted]  
Shows: The outlined element’s curved motion path before changing the spatial interpolation.

Select all the layers and press P to show their Position (*posizione*) properties. Select all the position keyframes, right-click, and change Spatial Interpolation (*interpolazione spaziale*) to Linear. The keyframes will then follow straight paths rather than curved ones.

![3762 · U5 · L16 · 09:14](frames/U05L16-F0914.00.jpg)

On screen: [rest omitted]  
Shows: The outlined element’s motion path after changing the position keyframes to Linear spatial interpolation.

## Changing solid fills to gradients

Anchor: 3762 · U5 · L16 · 09:24–12:15

Return to Illustrator to check the color arrangement. In the transition from the Dry Martini to the White Lady, an element changes color and changes from a solid fill to a gradient (*gradiente*). In After Effects, select the object and apply a linear gradient instead of a solid fill. Change the colors and adjust the gradient’s start and end points.

Before this, the scenes used a uniform tint. Now open Contents > Rectangle > Gradient to edit the colors. Set a keyframe for the gradient. At the previous keyframe, make the gradient’s two colors identical so it looks like a solid color. Move to the middle of the movement and advance this keyframe. The change from a flat tint to a gradient will then happen gradually during the movement.

The shape, corner roundness and color have changed while the original design remains recognizable. The following elements repeat parameters already used, keeping the original design consistent. For the Tequila Sunrise, there are two outlined elements. You can create another element, link it to a null object, and have it enter the scene smoothly. Now that we have seen how to use these settings, apply the same approach to the remaining cocktails.

Once all the elements are set, the animation will be 25 seconds long. Press N or move the work-area marker to set the preview from zero to 25 seconds, then press Space to view the full animation. In this example, one-second animations are followed by two-second pauses.

![3762 · U5 · L16 · 10:42](frames/U05L16-F1042.00.jpg)

On screen: [none]  
Shows: The White Lady reference shape with a pink-to-purple gradient, and its gradient start and end properties open below.

![3762 · U5 · L16 · 11:39](frames/U05L16-F1139.00.jpg)

On screen: "15cl" [rest omitted]  
Shows: Illustrator references for the Tequila Sunrise and Mimosa, with their outlined elements and ingredient shapes.

## Adjusting keyframe speed and keeping the movement consistent

Anchor: 3762 · U5 · L16 · 12:15–14:49

![3762 · U5 · L16 · 12:15](frames/U05L16-F1215.00.jpg)

On screen: [none]  
Shows: The assembled 25-second animation range on the timeline, with the Dry Martini shapes in preview.

The keyframes currently move at a constant speed, from one keyframe to the next throughout the sequence. Take layer 02 as an example: its shape and properties change in a straight, constant way. Select its Position keyframes, right-click, and open the speed panel. Change the influence (*influenza*) value, which controls the speed coming into and leaving an animation, to 85% for both parameters. Apply the same change to Rotation, Size and Roundness.

![3762 · U5 · L16 · 13:32](frames/U05L16-F1332.00.jpg)

On screen: [none]  
Shows: Cocktail shapes in After Effects with position, rotation, size and roundness keyframes visible across the timeline.

Press Space to preview the movement. The object no longer moves linearly; it makes sharper movements, with an initial acceleration. Apply the same influence to the other properties, except color. Changing the speed of all these keyframes makes the transitions between shapes faster rather than linear.

As you review the movement, check that the rotation and position are set correctly. All the elements follow a deliberate order, and they move uniformly together. During a rotation, an object can make a counter-movement as it rises, or it can keep rotating clockwise as it changes from one cocktail to the next.

![3762 · U5 · L16 · 14:14](frames/U05L16-F1414.00.jpg)

On screen: [none]  
Shows: The cocktail shapes at a point in the sequence where the outlined element and the colored shapes rotate together.

## Organizing the layers and colors

Anchor: 3762 · U5 · L16 · 14:49–16:09

Also check the layer order in the timeline. Put the elements with masked gradients above the other elements, as you would in Illustrator, so their changes remain visible and fit together. To move an element in the timeline, select that layer and its null object, then move them below the other layers. Here, the strokes (*tracce*) must stay particularly clear and visible, while the element with a gradient connected to the structure beneath it goes on layer 1.

For a clearer project file, rename the elements and number them in sequence: this becomes layer 1, that becomes layer 2, followed by the other layers, including layer 4 and layer C. You can also assign colors to the layers. For example, make the selected outlined elements green so they are easier to find. This gives you a clear view of the timeline and of the difference between a solid shape layer and a stroke.

![3762 · U5 · L16 · 15:49](frames/U05L16-F1549.00.jpg)

On screen: "[Palette.ai]" / "01_Americano.jpg" / "Null 1" / "03" / "Null 3" / "05" / "Null 2" / "04" / "Null 4" / "02" / "Null 1" / "BG" [rest omitted]  
Shows: After Effects timeline with the shape and null layers arranged in sequence.

## Adding secondary movement and a loop

Anchor: 3762 · U5 · L16 · 16:09–19:45

The main movements are in place. Now add secondary movements by animating Position and Rotation on the objects linked to the null objects. Start with layer 1. Press 1 to show its Size and Roundness keyframes. Select a null object to see the main movement: the object holds its position for a while, then changes again, and so on. Select the layer and set a Position and Rotation keyframe.

No new keyframe is needed until second 1, so move the Position and Rotation values directly at second 1. This object will move upward. At second 3, increase its rotation and raise it. Set those keyframes at second 4, then at second 6 rotate it farther and move it down. The object will keep floating and moving through the space during those intervals.

To keep the object from stopping and then starting again, you do not need pairs of duplicate keyframes. Keep the movement balanced and work at the midpoint of the change as the sequence moves from one cocktail to the next. To make a loop (*loop*), restore the starting Position and Rotation at the final keyframe. The object will continue moving over time, even when its null object has no keyframes.

Apply the same logic to the other elements. These secondary movements make the shapes appear to float. The null object provides the initial movement, which becomes the main movement; the shape properties add a secondary movement.

![3762 · U5 · L16 · 17:33](frames/U05L16-F1733.00.jpg)

On screen: [none]  
Shows: The secondary movement with the lower shape selected and Position and Rotation keyframes open.

![3762 · U5 · L16 · 18:50](frames/U05L16-F1850.00.jpg)

On screen: [none]  
Shows: Clean preview of the overlapping cocktail shapes after their movements have been set.

We have established the movements and animation logic, adding treatments and gradients to make the shapes more dynamic. The cocktail shapes are animated. In the next lesson, we will work on the decorations and typography.
