# Lesson 15 · Stretch position animation

Anchor: 503 · U4 · L15 · 5:35 · https://www.domestika.org/en/courses/503-introduction-to-motion-design-and-animation-curves-in-after-effects/units/2012-creating-our-basic-library-of-movement#course_lesson_7412

## Find the fast part of the position animation and add stretch

Anchor: 503 · U4 · L15 · 00:00–01:32

We are going to make the animation more complex. To suggest movement and speed, add stretch (*estiramiento*). Duplicate the previous position animation (*animación de posición*) and rename the composition. Reuse that animation, identify the part where the element moves fastest, and stretch it around that point so the form shows the speed of the movement. Stretch is one of the principles of animation.

To do this, we will make a shape morph (*variación de la forma*). In the search field, enter Path (*trazado*). The procedural shape is currently a preset ellipse. Right-click it and convert it to a Bézier path (*trazado Bézier*; captions: *B7*), which we can animate. We can create shape morphs by changing the path itself.

![503 · U4 · L15 · 00:51](frames/U04L15-F0051.00.jpg)

On screen: "Eastwood_position_stretch" / "circulo" [circle] / "fondo" [background] [rest omitted]  
Shows: A dark circle sits on a diagonal position path inside the violet square composition.

![503 · U4 · L15 · 01:08](frames/U04L15-F0108.00.jpg)

On screen: "Path" [rest omitted]  
Shows: The circle layer is expanded to show Ellipse Path 1, Path, and Position in the timeline.

## Edit the path at the fastest point

Anchor: 503 · U4 · L15 · 01:32–02:42

Follow the path editing step by step. Select the Pen tool with G and zoom in. Select the two points on the circular path that you will pull to stretch the form. At the moment when it is moving fastest, it becomes a star-like shape, like a comet, to represent the movement. There is a problem: the shape should be rotated (captions: *rota*). Fit the view and rotate it by minus 45 degrees; then it will line up correctly. Imagine the moment when the movement is fastest and set a keyframe there. At the beginning, the shape should still be round. Adjust the points until it is almost a perfect circle. No one would have noticed that we changed the path (captions: *el 7*).

![503 · U4 · L15 · 01:44](frames/U04L15-F0144.00.jpg)

On screen: "path" / "Path 1" [rest omitted]  
Shows: A close view of the selected circular path with its vertex points and Bézier handles visible.

![503 · U4 · L15 · 01:56](frames/U04L15-F0156.00.jpg)

On screen: [rest omitted]  
Shows: The selected path has been pulled into a long vertical capsule shape.

![503 · U4 · L15 · 02:14](frames/U04L15-F0214.00.jpg)

On screen: "Rotation" / "-45.0°" [rest omitted]  
Shows: The selected dark shape is stretched diagonally along the position path.

## Restore the original shape and prepare the curve view

Anchor: 503 · U4 · L15 · 02:42–03:31

Press U to reveal all the keyframes. At the end, the shape will return to its original form, so copy the shape keyframe from the original form and paste it at the current playhead. Next, adjust the curves so the animation works correctly; the result is uneven at this point. Selecting the whole layer shows all its curves, including position curves that we do not need right now. Change the Graph Editor to show only the selected properties. Select the path property and apply easing. The value graph (*gráfico de valores*) looks unusual for a path animation, but it is equivalent to the speed graph (*gráfico de velocidad*).

![503 · U4 · L15 · 02:55](frames/U04L15-F0255.00.jpg)

On screen: "Copied 1 Keyframe" [rest omitted]  
Shows: The selected stretched shape is at the upper-left of the square; Path, X Position, and Y Position keyframes are visible in the timeline.

![503 · U4 · L15 · 03:31](frames/U04L15-F0331.00.jpg)

On screen: "X Position" / "Y Position" [rest omitted]  
Shows: A circular shape sits near the upper-left of the square while the Graph Editor shows two narrow peaks.

## Refine when the shape stretches and gathers back

Anchor: 503 · U4 · L15 · 03:31–04:30

The path animation’s value graph is strange, but it works like the speed graph. Fit the graph in view and identify what is happening. The movement should take longer to start, so pull the first part to make it wait. Do the same at the other end so the shape gathers back more abruptly. Preview the result and refine it gradually. Narrow the preview area and press the spacebar. Let the shape keep gathering for a little while after it has arrived. Adjust it again if needed so the gathering begins earlier. This is a patient fine-tuning process.

![503 · U4 · L15 · 03:56](frames/U04L15-F0356.00.jpg)

On screen: [rest omitted]  
Shows: The stretched shape is at the lower-right of the square while the Graph Editor shows two high peaks for the morph.

## Check the full timing and finish the exercise

Anchor: 503 · U4 · L15 · 04:30–05:35

Return to the curve editor and look at the full movement: the shape travels, stretches, and gathers back. Adjust the overall timing and make it a little faster so the stretch makes more sense; it has quite a lot of stretch (captions: *que tenga tanto estrecho estiramiento*), and I think it looks good now. I could keep adjusting the curves for ten minutes, but this is enough to explain the exercise. Leave your version much better than mine, and then share it with everyone. We have learned to animate position with stretch. In the next lesson, we will animate rotation and use more tricks.

![503 · U4 · L15 · 05:07](frames/U04L15-F0507.00.jpg)

On screen: [rest omitted]  
Shows: The dark circle is back to its round form near the lower-right corner of the violet square.
