# Lesson 20 · Choreography 3

Anchor: 503 · U5 · L20 · 12:26 · https://www.domestika.org/en/courses/503-introduction-to-motion-design-and-animation-curves-in-after-effects/units/2013-next-level-choreographic-animations#course_lesson_7417

## Planning a cause-and-effect choreography

Anchor: 503 · U5 · L20 · 00:00–01:25

Now that we are moving along, I will add more elements and interaction to make a more complicated choreography. I am in Photoshop to plan the animation. As I always say, take paper and pencil; it is the most relaxing and pleasant way to do it. I will explain it in Photoshop, using material from our earlier design exploration, and set out what we are going to do in animation.

I want to use this third choreography to explore masks (*máscaras*) further. This shape will start where it is and stretch as it moves upwards. It will rise to fill this whole area. The parts that overlap the circle will have different colours from the parts outside the circle. To do that, we will split the layer into three and use the “Set Matte” effect (*mate*), as in the previous choreography. To finish the loop, when the shape moves out above, a yellow square will appear from below again. This time we will make a perfect loop. Now let’s go to After Effects and animate it.

![503 · U5 · L20 · 00:37](frames/U05L20-F0037.00.jpg)

On screen: [none]  
Shows: Six square designs from the earlier exploration arranged in two rows.

![503 · U5 · L20 · 01:24](frames/U05L20-F0124.00.jpg)

On screen: [none]  
Shows: Two storyboard panels: a circle and coloured squares, with a drawn upward arrow over the second panel.

## Setting up the shape animation

Anchor: 503 · U5 · L20 · 01:25–02:22

I have made a composition with a similar design to the one we had before. There is a circle and three squares. One is called “Hero Squares”; it is this shape that will rise, turn into a rectangle, and show three colours divided by the circle. Since it will change shape as it rises, I will use the stretch method we learned when animating Position. I right-click and convert it to a closed path (*trazado cerrado*). Now I can animate the shape of the vector itself. I make this rough setup and start animating.

Instead of animating this piece’s Position and then its Scale, I will do the whole animation with a morphing (*morfín*) of the shape. I search for “path” (*trazado*; captions: *paz*) and find the shape property. I set a keyframe (*fotograma clave*) and move it to the beginning; this is the starting position. Then I set the end position so the shape covers the screen.

![503 · U5 · L20 · 01:39](frames/U05L20-F0139.00.jpg)

On screen: “cuadrado 3” [square 3] / “cuadrado 2 HERO” [square 2 HERO] / “cuadrado 1” [square 1] / “circulo 1” [circle 1] / “fondo” [background] [rest omitted]  
Shows: The initial composition with a coral rectangle, dark circle and three small coloured squares along its lower edge.

## Stretching the shape and refining its movement

Anchor: 503 · U5 · L20 · 02:22–04:33

We left these guides from before, so I remove them using View > Clear Guides and place a new guide here. I lock it, because otherwise I could move it accidentally. I want this part to line up exactly with the edge of the other squares so that the geometric design looks orderly and makes sense to the eye. I hide the guide and check the result. It looks good.

The movement is very basic so far. I want it to feel more elastic: as it rises, the bottom should stay in place and then gather back in. I add another guide below. The top part should move upwards while the bottom part stays here. In View, I can turn on snapping so that the layer snaps to the guides. That makes this operation easier. The setup is in place and the shape gathers back in, but I need to adjust the curves and timing. I will work on that, as we have done in earlier lessons.

Here is the animation I made. It rises and then stops quite forcefully. There is a very subtle ease (*suavizado*) after that, but most of the movement starts reluctantly and then reacts strongly. That is the character we have been using. You can give your animation a different character, of course. We do not all get up on the same side of the bed. Today Clint Eastwood is in a gentler mood, so this reaction is a little more subtle.

![503 · U5 · L20 · 02:45](frames/U05L20-F0245.00.jpg)

On screen: “Path” / “matte” / “Set Matte” [rest omitted]  
Shows: The yellow shape has stretched into a vertical bar across the circle in the coral composition.

![503 · U5 · L20 · 04:00](frames/U05L20-F0400.00.jpg)

On screen: [rest omitted]  
Shows: The shape animation is being previewed in the composition.

## Using the circle as a trigger

Anchor: 503 · U5 · L20 · 04:33–06:31

Next, I think we need a trigger (*disparador*; captions: *tríer*) for the movement. What could it be? The circle could shrink like a button being pressed, creating a cause-and-effect animation. When the button is pressed, the other animation begins.

First I change the circle’s colour so it is easier to distinguish. I give the animation a little more room at the beginning, then use the circle layer as our button. I animate its Scale so that it passes into the next action. I press S to show Scale, set one keyframe for its unpressed size, then another for the size it reaches when pressed. After that, it should return to the same size it had at the beginning. I set the second keyframe by eye and adjust the curves until the effect feels right. I will move ahead and come back when I have worked on it.

I think the button press works. Next, I will synchronise the button animation with the other shape’s upward morph. It should feel like cause and effect: pressing the button starts the second animation. If you watch it now, the second animation begins a little late, so I move it earlier. I adjust it again until our brains tell us visually that the relationship is right.

## Completing the morph before applying Set Matte

Anchor: 503 · U5 · L20 · 06:31–08:29

Remember the design: the rectangle needs to be divided into three colours based on the circle underneath it. We will do that with Set Matte, as in the previous lesson. Before dividing it, though, it is important to finish the animation. First the rectangle rises and takes this position through a shape morph. Then it must move upwards again so that it can reappear from below and complete the loop.

I add another keyframe. The top part rises a little, and then the bottom part gathers in until it disappears completely. Now I adjust the timing and curves, giving the movement the personality of our character. One important point: when we animate paths, the graph is always the speed graph (*gráfico de velocidad*), even if we are working in the value graph (*gráfico de valores*). That is a small flaw in After Effects. We can use the Bézier handles (*controladores Bézier*) to make a smoother curve; where the slope is steep, the animation will move faster. I will add a little subtlety to the ending. I add a keyframe and move the final part to test it. That first attempt is not subtle enough. I try another adjustment. If it does not convince us, we can leave it as it was. This version could work.

![503 · U5 · L20 · 07:30](frames/U05L20-F0730.00.jpg)

On screen: [rest omitted]  
Shows: The yellow rectangle extends vertically through the circle while its shape path is selected.

![503 · U5 · L20 · 07:45](frames/U05L20-F0745.00.jpg)

On screen: [rest omitted]  
Shows: The graph editor displays several sharp peaks in the selected path’s speed curve while the vertical yellow shape appears in the composition.

## Dividing the shape and simplifying the design

Anchor: 503 · U5 · L20 · 08:29–10:46

Now that the rectangle’s animation is complete, I will duplicate it so we have the layers for the three colours and the finish we planned. The top section will be grey. Remember that the colours in this drawing are only a visual guide; I have changed them a little. White is not in the palette we are using, because I want everything to be more colourful. I work a little “sloppy,” as the English speakers would say, and improvise. You can instead make your design exploration and final animation exactly match. That discipline throughout the process is very useful on commercial projects, because the client will not get unexpected changes. It is your choice. I am trying to enjoy the work, so sometimes I stray from the plan.

Now we do the operation. I duplicate the layer twice. I select the upper one, go to Effects, and use the search field to find Set Matte. I can drag the effect onto the layer, or double-click it with the layer selected. The effect controls appear in the upper-left panel. I want this upper layer to be visible only over the circle. In “Take Matte From Layer,” I choose the circle. Then I change the colour to check that it is working. Great; I love when these effects work.

At this point I may rethink the design. I like it in two colours, even though I planned three. I make an executive decision and simplify it. I no longer need this extra layer. I rename the remaining ones “Hero 2” and “Hero 1.” The animation now has the design finish I like: using one object to mask another.

![503 · U5 · L20 · 08:56](frames/U05L20-F0856.00.jpg)

On screen: [none]  
Shows: The planning page with two composition sketches and an upward movement arrow.

![503 · U5 · L20 · 09:07](frames/U05L20-F0907.00.jpg)

On screen: [none]  
Shows: The six earlier design studies, including geometric circles, rectangles and diagonal divisions.

![503 · U5 · L20 · 10:42](frames/U05L20-F1042.00.jpg)

On screen: [rest omitted]  
Shows: The vertical shape is coloured purple where it overlaps the circle and yellow below it.

## Finishing the loop and reviewing the choreography

Anchor: 503 · U5 · L20 · 10:46–12:26

If I preview the whole animation, only two things remain. Before the shape starts moving upwards, the button should be pressed again, so that the button press causes the animation to begin as it did at the start. Then, after the shape disappears above, it should reappear below, making a perfect loop that connects to the initial composition. I will do this in fast motion; it is now a matter of placing keyframes and adjusting the timing and curves.

Here is the third choreographic animation. It works as a smooth or perfect loop (captions: *look*): when the playhead reaches the end, at six seconds, it starts again without the eye noticing an abrupt change. That differs from the previous choreography, where we deliberately used a jump because we liked the look it gave the animation.

There are two important things in this choreography. First, make cause-and-effect animations: here, the circle acts like a button and starts the rectangle’s animation. Second, keep your character in mind so your animations have a personality and the whole series of animations feels coherent.

We have finished another choreography. Remember to share your animations on social media with the hashtag #DMSTKH79. In the next lesson we will raise the difficulty a little more.

![503 · U5 · L20 · 11:24](frames/U05L20-F1124.00.jpg)

On screen: [rest omitted]  
Shows: The completed composition returns to its initial arrangement of a coral rectangle, circle and three coloured squares.

### Key points (derived)

- Use a trigger shape to make a cause-and-effect sequence: the circle’s press starts the larger shape’s morph.
- Complete the shape’s full path, including its departure and return, before adding the matte layers.
- Guides help align the geometric design; curve handles control how the shape accelerates and eases.
- Set Matte can colour only the portion of a layer inside another shape. The palette and number of colours can still change during exploration.
- Check the loop at its join and keep the motion style consistent across a series.
