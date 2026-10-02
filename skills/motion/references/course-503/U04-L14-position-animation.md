# Lesson 14 · Position animation

Anchor: 503 · U4 · L14 · 6:22 · https://www.domestika.org/en/courses/503-introduction-to-motion-design-and-animation-curves-in-after-effects/units/2012-creating-our-basic-library-of-movement#course_lesson_7411

## Duplicate the composition and plan a diagonal position move

Anchor: 503 · U4 · L14 · 00:00–00:56

This lesson is about position animation (*animación de posición*), using what we learned about animation curves (*curvas de animación*). It is the second animation in the series. In the After Effects project, duplicate the previous composition with Command/Control+D and rename it. I usually change the colors so I can tell which composition I am working in; for this one, I change them to red. Delete the previous animated element and keep the background. This time the position animation will travel diagonally so it uses the square format. Create a circular Shape Layer by double-clicking, name it, and set its color.

## Set up the circle, palette colors, and position keyframes

Anchor: 503 · U4 · L14 · 00:56–02:28

Sometimes the bounding box and its scale controls disappear when you select a layer. If that happens, hover over the button below the Composition panel; its tooltip reads “Toggle Mask and Shape Path Visibility.” Click it to turn the bounding box back on so you can scale in the Preview window. Keep the color palette in view. Each composition or animation should use the same palette, but use different colors. I will make this background violet and give the circle another color. Changing colors across the compositions will make the mini reel more interesting visually. Remember your character: how it moves, how it behaves, and the attributes you defined. Press P to reveal Position and set a keyframe here. Place it approximately by eye; we can refine it later. Set the end of the animation at another position, then check the timing.

![503 · U4 · L14 · 01:11](frames/U04L14-F0111.00.jpg)

On screen: “Toggle Mask and Shape Path Visibility” [rest omitted]  
Shows: The cursor hovers over a Composition panel button, displaying its tooltip.

![503 · U4 · L14 · 01:17](frames/U04L14-F0117.00.jpg)

On screen: "Eastwood_position"  
Shows: A selected violet circle centered on a red square, with transform handles around it.

![503 · U4 · L14 · 01:47](frames/U04L14-F0147.00.jpg)

On screen: [none]  
Shows: A dark gray circle fills most of a violet square.

![503 · U4 · L14 · 02:11](frames/U04L14-F0211.00.jpg)

On screen: "Position" / "540.0" / "540.0" [rest omitted]  
Shows: A selected dark circle centered on violet, with transform handles and a central anchor point.

## Separate and move both position curves together

Anchor: 503 · U4 · L14 · 02:28–03:48

With the keyframes selected, press F9 to apply easing (*suavizado*). Open the Graph Editor (*editor de gráficos*) and fit the curves in the view. We need to separate the dimensions: with Position, the value graph (*gráfico de valores*) cannot be edited directly until X and Y are separated. This is the one property where we need to do that. When editing the position curves, a single click selects one curve: red is X and green is Y. We do not want the two curves to be different. Previewing that makes the movement follow a strange curve. Instead, click and drag to select both curves and work on them together. Preview with the spacebar. Now the movement is more or less right: it takes time to start, then moves decisively until it almost reaches the edge.

![503 · U4 · L14 · 02:47](frames/U04L14-F0247.00.jpg)

On screen: "Edit Value Graph" / "Edit Speed Graph" [rest omitted]  
Shows: A Graph Editor context menu is open over the descending position curve.

![503 · U4 · L14 · 03:06](frames/U04L14-F0306.00.jpg)

On screen: "X Position" / "Y Position" [rest omitted]  
Shows: The selected circle and diagonal path appear above separate red and green position curves.

## Increase the apparent travel distance

Anchor: 503 · U4 · L14 · 03:48–04:25

To make the circle seem to travel farther, make it smaller. Reposition the first position keyframe, then do the same at the end. This makes the distance feel greater and the animation more forceful.

![503 · U4 · L14 · 03:58](frames/U04L14-F0358.00.jpg)

On screen: [rest omitted]  
Shows: A large dark circle sits at the lower-right end of a diagonal motion path, above an eased position curve.

![503 · U4 · L14 · 04:08](frames/U04L14-F0408.00.jpg)

On screen: [none]  
Shows: The smaller dark circle sits at the lower-right end of the diagonal path, which reaches toward the upper-left.

## Slow the start and refine the timing

Anchor: 503 · U4 · L14 · 04:25–05:48

As in the scale animation, use the Pen tool to add a keyframe and make the first part slower. The problem is that this selects only one of the two curves, so repeat the operation for the other curve and reposition it. Alternatively, undo with Control/Command+Z and make two keyframes in this area. When you return to the curve, the bounding box (captions: *banding box*) can make it difficult to reach the part you need. Select the starting handles and scale them horizontally to the right in time. That lengthens the opening part of the animation. Adjust the curves so this section is more parallel and the movement starts much more gently. Preview it, make any small corrections, and deselect the other point if it gets in the way. For me, this now reads as Clint Eastwood. The position curves have a few peculiarities, but once we understand them, they are just as easy to edit.

![503 · U4 · L14 · 05:40](frames/U04L14-F0540.00.jpg)

On screen: [rest omitted]  
Shows: The circle and diagonal path appear above red and yellow position curves; one curve stays nearly flat before descending sharply.

## Apply the character’s attributes to your animation

Anchor: 503 · U4 · L14 · 05:48–06:22

Now make your own position animation based on your character. Think carefully about its attributes and how it should behave. We now have two animations in our library. In the next lesson, we will animate position with stretch (*estiramiento*).
