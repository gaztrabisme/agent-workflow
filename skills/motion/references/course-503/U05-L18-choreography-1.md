# Lesson 18 · Choreography 1

Anchor: 503 · U5 · L18 · 18:46 · https://www.domestika.org/en/courses/503-introduction-to-motion-design-and-animation-curves-in-after-effects/units/2013-next-level-choreographic-animations#course_lesson_7415

## Organising the project and creating a composition

Anchor: 503 · U5 · L18 · 00:00–01:23

This time I am going to make a more complex animation that simulates a user-interface environment in a very simplified graphic way. I will establish cause-and-effect relationships in a sequence that is more complicated and therefore needs some planning. Let’s see it.

For our first choreographic animation, I will first tidy up our After Effects project. I put the simple animations inside their folder, move that folder out of the way, and create another folder called “Choreographic animations.” Remember to use colours to your advantage. I make the folders I am not working in a less visible colour and set the folder I am using to red. Then I duplicate one of the compositions with Command or Control+D, drag it into this folder and rename it “Choreography 1.” I make that red too, so I know I am working on it. This gives me a composition with the width and height I need, and I may be able to reuse its coloured background. I will remove this element, but I now have a composition ready to work in.

## Planning the sequence with three shapes

Anchor: 503 · U5 · L18 · 01:23–03:25

I am going to switch to Adobe Photoshop for a moment. You can use paper and pencil, which is what I always recommend; it is much more relaxing. I am using Photoshop to plan the animation. Since this is a choreographic animation, I need to take more care to be clear about what I am going to make. I am roughly drawing three elements on a new layer: a triangle, more or less a circle, and a square.

The action will be a more complicated swipe (*arrastre*) like the one we made earlier. The circle will become a little smaller; as I always tell you, this is a good time to name the layers. It will then move upwards and drag the square with it. The square will disappear above the frame, and the triangle will appear from below and take the square’s former position. The circle will return to its dragging position and pull again: the triangle will go up and another square will come from below. That gives us a loop. Make a little storyboard or notes on paper, in whatever form helps you plan.

Back in After Effects, I create the three elements from the plan: a triangle, the circle that will do the dragging, and a square.

![503 · U5 · L18 · 02:34](frames/U05L18-F0234.00.jpg)

On screen: [none]  
Shows: A rough storyboard with a circle, square and triangle arranged on a white page.

![503 · U5 · L18 · 03:20](frames/U05L18-F0320.00.jpg)

On screen: “triangulo” [triangle] / “circulo” [circle] / “cuadrado” [square] / “fondo” [background] [rest omitted]  
Shows: The After Effects composition with the purple background, yellow square, dark circle and red triangle.

## Animating the circle’s swipe

Anchor: 503 · U5 · L18 · 03:25–06:34

Before animating, I arrange the shapes in their starting positions. The circle will drag, while the triangle sits just outside the composition so it is not visible. This is the initial state, so I set a keyframe (*fotograma clave*). I animate the circle first and move it to the top.

To make the work easier, I can lock the other layers and unlock them when I need them. As we saw in the previous lesson, the element that makes the swipe should first get smaller and then drag the other shape. I reduce the circle, press P for Position and start moving it upwards. Now I can work on the curves.

I am in the curve editor. To work with Position in the value graph, I need to separate X and Y; I have already separated them. Since this animation goes only upwards, along Y, I remove the X keyframes. I also use the eye control to show only the properties I have selected, instead of every animated property. That lets me choose what I see. Now I can animate the position. I fit the view and shape the curve so the circle is reluctant to start, then gathers speed and shoots upwards like a bolt. When it stops, though, I do not want it to stop abruptly. I slow it down. This is the “Clint Eastwood” feel (captions: *Cleanish Boot*): reluctant at the beginning, then quick once the movement gets going.

I subdivide this part of the curve with the pen tool, G, which we used in the lesson on animation curves. I pull the point out carefully without letting it go below the value; otherwise the circle would bounce. I preview the result. I like it, but the circle needs to travel higher. To keep it from leaving the composition, I should make it even smaller. This is a matter of correcting the animation as we go, and previewing often is important. I move it further up and adjust the keyframe directly in the preview window. I want this part to travel higher too, so I adjust the cursor downward a little. This is fine-tuning. Now I am happy with the swipe.

![503 · U5 · L18 · 04:25](frames/U05L18-F0425.00.jpg)

On screen: “Position” / “Scale” [rest omitted]  
Shows: The circle and square in the composition with the selected position curve visible in the graph editor.

![503 · U5 · L18 · 05:49](frames/U05L18-F0549.00.jpg)

On screen: “X Position” / “Y Position” [rest omitted]  
Shows: The dark circle has moved to the top of the yellow square.

## Making the square follow the circle

Anchor: 503 · U5 · L18 · 06:34–08:31

Next I will animate the square that the circle drags. I unlock its layer so I can work comfortably. With the animated circle selected, I press U to see where its animation is. I zoom in on the timeline. The circle’s position animation starts here and ends here. I animate the square’s position so it begins where it was and, when the swipe ends, it is outside the composition. I move this keyframe to the point where the square should leave the frame.

At the moment the result is poor. The circle, the dragger, must lead the movement, and the square should follow it. The curves will give us that delay. I open the curve editor, separate the dimensions again, remove the X animation because I do not need it, and take time to adjust the curves. This means refining both the curves and the timeline. Little by little, I get the first swipe interaction to a point I like.

## Bringing in the triangle

Anchor: 503 · U5 · L18 · 08:31–10:01

Now I unlock the triangle. It has to appear from where it is, below, while the square travels upwards. As a consequence of the swipe, the triangle should rise and occupy the square’s former position. I select the square and press U to see where it rises, then press P to animate Position. I give the triangle a little delay and keep its position animation roughly in sync with the square’s.

I bring up the rulers with Command or Control+R so I can align the triangle with the square’s earlier position. I place it neatly where the previous element was. Then, as we have done many times, I adjust the curves in the curve editor. I will work on that for a moment. Now I have an animation I like quite a lot.

![503 · U5 · L18 · 09:38](frames/U05L18-F0938.00.jpg)

On screen: [rest omitted]  
Shows: The dark circle sits above the red triangle as the triangle rises into the yellow square’s former position.

## Returning the circle and shaping the second beat

Anchor: 503 · U5 · L18 · 10:01–12:39

Let’s think about the next step. The circle that made the swipe needs to return to the centre and to its initial size. It goes up, then comes back down to the centre at this size. I find the circle layer’s keyframes and copy the initial Scale keyframe to a later point. I do the same with the initial Position keyframe. Then I preview it.

There is a small problem: the circle changes during the time when we want it to stay up here, at this scale and position. I copy this state and paste a keyframe further along so the position does not change across this interval. I do the same with Scale. Now I adjust the keyframe timing and curves. I will make this happen in two beats rather than having the circle move and grow at the same time. That did not look right. First it should move into the centre, then it should grow. I place the keyframes accordingly.

I will shape the scale with our “Clint Eastwood” timing: it is reluctant at the start and then finishes with a punch. The position moves first, and then the circle grows as if it were about to punch you. Although we know Dirty Harry was more likely to shoot first and ask questions later. I preview the animation at a wider range. We now have the opening change, the return, and the start of what we need for a loop.

![503 · U5 · L18 · 10:14](frames/U05L18-F1014.00.jpg)

On screen: [rest omitted]  
Shows: The dark circle overlaps the upper part of the red triangle on the purple composition.

![503 · U5 · L18 · 12:14](frames/U05L18-F1214.00.jpg)

On screen: [rest omitted]  
Shows: The dark circle overlaps the top of the red triangle during the return movement.

## Building the loop with a square from below

Anchor: 503 · U5 · L18 · 12:39–14:40

To complete the loop, the circle needs to become small again, swipe upwards, and bring in a square from below that matches the first one. It should end exactly like the initial state. I add a Scale keyframe where there is no change, then make the circle small again as before. I copy the earlier keyframes so this part of the animation behaves symmetrically and uses the same timing. I copy the two keyframes that make the circle large and paste them at the return point. The circle now repeats the same animation. I still need to animate a square appearing from below, taking its place, while the triangle rises. Then the loop will be complete.

Here is a small trick: I duplicate the square layer and call the copy “Square 1.” I move it above the other square. When the circle makes this swipe upwards, I want the new square already to be in position by the time the swipe ends. I place it below the circle. I remove its existing keyframes and extend its layer. It should begin outside the frame and finish centred. I set the end keyframe, then move the square outside the composition at the start. I turn off the triangle so it will not get in the way; I will animate it afterwards.

![503 · U5 · L18 · 14:21](frames/U05L18-F1421.00.jpg)

On screen: “cuadrado 2” [square 2] [rest omitted]  
Shows: A duplicate square is positioned in the composition beneath the circle.

## Easing the square and removing the triangle

Anchor: 503 · U5 · L18 · 14:40–16:07

Now I adjust the square’s animation curves. I press the view-fit button so I can work more comfortably, select the keyframes and convert them to curved keyframes. Here I do not want as much “Clint Eastwood” as a quick appearance while it is dragged, followed by a gradual slowdown as it reaches its final position. I preview it. The square arrives too soon, so I will work on it for a moment.

This is looking good. I used the pen tool again to subdivide the curve, then adjusted it carefully, as I always tell you, so it does not cross below the value. If it does, it bounces. I exaggerate the curve so you can see the bounce caused by going below the value, then pull it back. Now the animation looks quite good.

![503 · U5 · L18 · 15:35](frames/U05L18-F1535.00.jpg)

On screen: [rest omitted]  
Shows: The graph-editor curve drops below its baseline while the dark circle sits near the top of the purple composition.

We are nearly finished, and the lesson is getting a little long. But believe me: if you make this animation, you will be fantastic at animating with keyframes. When the circle drags upwards, the triangle needs to leave the composition. I select the triangle’s Position, set its keyframe at the point where the upward drag begins, and move it out of the frame. I will adjust the curves calmly.

![503 · U5 · L18 · 15:43](frames/U05L18-F1543.00.jpg)

On screen: [rest omitted]  
Shows: The dark circle sits high over the yellow square while the position curve is adjusted below.

## Synchronising the elements and checking the loop

Anchor: 503 · U5 · L18 · 16:07–18:46

I also need to sync the square that enters; it is arriving a little early. I press U to show its keyframes and move them back slightly in time. Almost there. It feels good when the animation starts to line up. I delay it a little more. The circle should also feel more energetic and faster as it moves upwards. I find where that ascent happens and adjust the timing. This leaves everything a little behind, so I tweak the timing again. This one appears too early; I move it later.

Sometimes it helps to turn off an element that makes it hard to see clearly. If we try to see all three elements at once, we will not be able to judge the animation properly. We will get the square choreography right, then continue with the triangle. It may feel tedious, but finishing will be very satisfying. The square is a little late, so I move it forward a touch. That is right for me. Now I turn the triangle layer visible again. It is late and moving oddly, so it needs to begin earlier and have less hesitation at the start. Almost there. Perhaps it should respond to the movement a little later, and then leave sooner. For me, that is right.

Now I check whether the loop works. The animation starts here and ends here, more or less. I press N to set the end of the work area and play it. So far, so good. When the loop comes around again (captions: *Luke*), it is perfect: a three-element choreographic loop with a swipe. We have made our first choreography. In the next lesson we will raise the difficulty a little for the second choreography.

![503 · U5 · L18 · 17:13](frames/U05L18-F1713.00.jpg)

On screen: [rest omitted]  
Shows: The dark circle is near the top of the purple composition as a yellow square enters from below.

![503 · U5 · L18 · 18:34](frames/U05L18-F1834.00.jpg)

On screen: [rest omitted]  
Shows: The dark circle overlaps the upper edge of a yellow square within the purple composition.

### Key points (derived)

- Plan a multi-element animation with a small storyboard, then build it from clear starting positions.
- Let the circle lead each swipe; delay the square and triangle so each follows the cause of its movement.
- Preview and adjust curve handles and timing as you go. Avoid curves that pass below the value and create a bounce.
- Reuse matching keyframes to make repeated motion symmetrical, then check the start and end of the loop together.
