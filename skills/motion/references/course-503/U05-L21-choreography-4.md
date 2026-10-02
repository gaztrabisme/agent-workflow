# Lesson 21 · Choreography 4

Anchor: 503 · U5 · L21 · 17:26 · https://www.domestika.org/en/courses/503-introduction-to-motion-design-and-animation-curves-in-after-effects/units/2013-next-level-choreographic-animations#course_lesson_7418

## From a still poster to a choreographed sequence

Anchor: 503 · U5 · L21 · 00:00–03:16

Let’s make another choreographic animation (*animación coreográfica*) with several moving elements. This is the fourth one we have made together. Afterward, I want you to make three more at your own pace, bringing your series to twelve animations. This one will be a little more playful. Here is the storyboard I have prepared. I always recommend paper and pencil, a sketchpad (captions: “blog”). That lets you step away from the computer for a while and relax.

The sequence was inspired by an image on the board I share with you, Domestika1, on my Pinterest profile. Let me find it: this poster here. It uses a fairly common visual device. It suggested that the square could run along this kind of diagonal track, from the bottom left to the top right. That was the starting point for this animation. Even static images can suggest animations or sequences. Look closely at static references: when you look at them with an animator’s mindset, they can give you very good ideas for your animation exercises.

I’ll explain the storyboard quickly, then we’ll start animating. In the first panel, we refer to the design we just saw. The square comes from down here, follows the arrow to the upper right, and turns into a circle as it finishes moving. This is a rough storyboard, the kind we make for ourselves. When we prepare storyboards for clients, the unwritten rule is to make them as polished, attractive, and beautiful as we can. For our own work, rough sketches are fine; for something we will show a client, we should make it look good.

In the second panel, the circle is pressed and a triangle appears from the left, settling at the top. The triangle then falls and bounces. In the fourth stage, a rectangle appears in the center, opens, and pushes the other two elements sideways until they leave the frame or composition. In the fifth stage, the central rectangle turns 45 degrees so that it ends exactly as it began. The rectangle appears in this position, making a perfect loop (*bucle*); the storyboard marks the connection between this moment and the opening moment.

![503 · U5 · L21 · 01:18](frames/U05L21-F0118.00.jpg)

On screen: “CLUB / BERL / IN” [Club Berlin] / “11.08.2013” / [illegible] [rest omitted]  
Shows: A Pinterest pin with a geometric party poster in pink, blue, yellow, and turquoise; a row of related design pins appears below it.

![503 · U5 · L21 · 02:09](frames/U05L21-F0209.00.jpg)

On screen: “CUAD. SE TRANSFORMA / EN CÍRCULO.” [Square transforms into a circle] / “LOOP” / “LOOP” / “PULSA” [Press] / “PULSA” [Press] / “CAE Y REBOTA” [Falls and bounces] / “ABRE” [Opens] / “GIRA 45°” [Turns 45°] / “aparece” [appears]  
Shows: Six storyboard panels with arrows for the square’s diagonal path, the circle presses, the triangle falls and bounces, the center opens and pushes the other shapes outward, and the rectangle turns toward the loop.

## Animate the square along its track

Anchor: 503 · U5 · L21 · 03:16–05:59

For the first stage, based on the design we liked, I have prepared a square that I call the track (*pista*). Name your layers in a way that makes sense to you. I have also created a null object (*objeto nulo*) and parented, or linked, the two layers to it. That gives me a simple way to change the size of both elements for aesthetic reasons, even while they are animated.

![503 · U5 · L21 · 03:20](frames/U05L21-F0320.00.jpg)

On screen: “posición escala animación 1” [position scale animation 1] / “cuadrado - círculo” [square - circle] / “pista” [track] / “fondo” [background] [rest omitted]  
Shows: The After Effects composition with a purple square at the lower end of a yellow diagonal track; its layer list is visible below.

Let’s animate. I’ll set a position keyframe (*fotograma clave*) for the square at two seconds and put it up here. I’ll zoom in with the magnifying glass so I can place it more precisely, right at the corner. Now we have the route the square will take along the track. Let’s adjust the animation curves a little. I have recommended using the value graph (*gráfico de valores*), but try the speed graph (*gráfico de velocidad*) too. It is fine to switch between them now and then, so you can get a feel for each one.

![503 · U5 · L21 · 04:36](frames/U05L21-F0436.00.jpg)

On screen: [none]  
Shows: The purple square at the upper end of the yellow track, with a curved graph open below the composition.

I like the animation as it is now. Always remember “CleanEastBoot” (unclear in the captions); here we have our “Cleanest Boot.” I’ll mark the preview area with the N key. It starts lazily, accelerates decisively, and has a very subtle easing (*suavizado*) at the end, but then stops quite sharply.

Let’s look at the storyboard again. As the square is finishing its movement, or at some point while it is moving quickly, it will turn directly into another shape.

![503 · U5 · L21 · 05:06](frames/U05L21-F0506.00.jpg)

On screen: [rest omitted]  
Shows: The storyboard returns to its first panel, where the diagonal square turns into a circle.

Select the Shape Layer (*capa de forma*), open Add, and apply the Round Corners (*esquinas redondeadas*) effect. When we open it, we can animate the moment when the square becomes a circle. Try doing it suddenly, or animate the corner radius until the square becomes a circle. I’ll make that animation and come back in a moment.

![503 · U5 · L21 · 05:43](frames/U05L21-F0543.00.jpg)

On screen: “Round Corners 1” / “Radius” [rest omitted]  
Shows: A purple circle at the upper end of the yellow track; the Round Corners controls and keyframes are expanded in the timeline.

## Morph the square into a larger circle

Anchor: 503 · U5 · L21 · 05:59–08:56

I like the result. If you look at the keyframes, the shape changes suddenly from square to circle at a point when the animation is moving quickly. I think that works well. The part I do not like is that the figure seems to lose a lot of visual weight when it changes from a square into a circle. I want the circle to take up more space, so I’ll make a sudden scale change at the same time as the shape change, making the circle occupy much more of the frame.

That was not as quick as I expected. It was more complicated than it seemed. This will happen to you too. It is an important lesson, perhaps more important than learning the software: sometimes we approach a task in a technically complicated way. It is fine to go back and try another route. This time, I’ll duplicate the layer. The circle will follow the position animation on the original layer, and at a particular moment we will switch from one layer to the other.

I’ll call the square layer “square master animation” so we can tell what is happening. The second layer will be the circle. Always use names that help you understand what you are doing. Open the second layer, remove its position keyframes, and link it to the square master animation layer. I’ll turn this layer off for a moment. We no longer need the shape transition animated on this layer. Press U to reveal the remaining shape-transition keyframes, then delete them so this layer stays a square; the other layer should stay a circle. Now it is a matter of choosing the moment to switch. There, for example. That looks good.

The circle is at the corner. With Control held down, I double-click here, and now it is centered. We can change the circle’s scale and then adjust its final position without affecting the animation on the other layer. We just need to refine the final position a little, and we have it. We have seen that it is fine to back up and try a different route or technical method when the current one is not working. Let’s look at the storyboard to see what we need to animate next.

![503 · U5 · L21 · 06:36](frames/U05L21-F0636.00.jpg)

On screen: “Position” / “Scale” [rest omitted]  
Shows: An enlarged purple circle over the upper end of the yellow track, with Position and Scale expanded in the timeline.

![503 · U5 · L21 · 08:41](frames/U05L21-F0841.00.jpg)

On screen: “círculo - resolución” [circle - resolution] / “cuadrado - master animación” [square - master animation] [rest omitted]  
Shows: The purple circle on the yellow diagonal track; the circle and square master layer names are visible in the timeline.

## Use the storyboard, then simplify

Anchor: 503 · U5 · L21 · 08:56–10:30

This next part is simple and very similar to the previous choreography. The circle will be pressed. A triangle will appear from the left, and a surface or background will appear with it. When the button is pressed, the yellow track will disappear immediately; the triangle and the colored background will come in from the left.

I have made the animation, and I want to point out that the sequence has changed a little. The circle presses, the yellow track disappears, and the triangle comes in from the left. I removed the element we had planned, where a colored background would also come in from the left and cover half the screen. I prefer it simpler this way. Leave some room for improvisation as you work. This is fine for a personal project. If it were client work (the captions at 10:21 say “personal work”), explain any storyboard changes to the client and why you are making them.

![503 · U5 · L21 · 09:20](frames/U05L21-F0920.00.jpg)

On screen: [rest omitted]  
Shows: The storyboard returns, with the circle press, triangle entrance, and rectangle sequence visible.

![503 · U5 · L21 · 10:14](frames/U05L21-F1014.00.jpg)

On screen: [none]  
Shows: The red triangle and purple circle side by side in the After Effects composition, with the yellow track and proposed background absent.

![503 · U5 · L21 · 10:26](frames/U05L21-F1026.00.jpg)

On screen: [rest omitted]  
Shows: The storyboard returns while the teacher discusses how a change to the planned sequence should be communicated to a client.

## Shape the bounce and its timing

Anchor: 503 · U5 · L21 · 10:30–13:46

Now comes a classic animation exercise: animating a bounce. Here, we will make the triangle bounce. The idea is that the button is pressed, the triangle falls, and it makes one or several small bounces. Animate it however you like. Bounce animation is always a very interesting exercise, whether it is a ball or something else. I’ll work on it and come back in a moment.

One important thing to watch for: I’ll undo and go back. Sometimes After Effects makes a movement like this: when it reaches this point, it does not stop, even though this value and the next value are the same. It continues moving and then comes back. This happens because we are using non-linear position keyframes. To fix the unwanted movement, select the keyframes between which it happens. Go to Animation, Keyframe Interpolation, and change Spatial Interpolation (*interpolación espacial*) from Current Settings to Linear. That removes the movement I did not create, which After Effects seemed to produce out of nowhere.

This is not bad. Do not go overboard with lots of bounces. Here, it hits, rises once, and has a very small second bounce, which is enough. It does not have to be extremely physical or realistic; give it the style you want. We are simulating a fall. In this particular animation, the character is not important. Have fun with the bounce: it is an excellent exercise for learning animation. Let’s review what we have so far. It rises, changes, and then the eye needs a little more time to read the scene. Give it a moment, perhaps a second, before the press takes us to the next stage.

I’ll adjust the keyframes to give this moment more breathing room: let it stop, then press and continue the animation. Now the eye, or rather the brain, has time to register this moment of design and composition. It presses and the triangle appears. Much better. The second press is now out of sync; it should happen a little later, so I’ll delay it. Let’s see. There is a big stretch where nothing happens. I’ll move the keyframes forward a little, maybe a little more. Then I’ll trim the preview area and review the whole animation. Now it is right: it rises, presses, and falls. We are happy with how it has gone so far.

![503 · U5 · L21 · 11:41](frames/U05L21-F1141.00.jpg)

On screen: “Keyframe Interpolation” / “Spatial Interpolation” / “Current Settings” / “Linear” [rest omitted]  
Shows: The Keyframe Interpolation dialog over the composition, with the Spatial Interpolation menu open and Linear listed beneath Current Settings.

![503 · U5 · L21 · 12:07](frames/U05L21-F1207.00.jpg)

On screen: [none]  
Shows: The red triangle near the bottom of the composition and the purple circle near the upper right; the triangle’s selected position path is visible.

![503 · U5 · L21 · 12:22](frames/U05L21-F1222.00.jpg)

On screen: [none]  
Shows: The red triangle at the upper left and the purple circle at the upper right, with the triangle’s selected vertical motion path and keyframes visible.

![503 · U5 · L21 · 13:18](frames/U05L21-F1318.00.jpg)

On screen: [none]  
Shows: The red triangle and purple circle side by side in the composition, with the circle selected and the timeline visible below.

## Choose surprise and make the loop

Anchor: 503 · U5 · L21 · 13:46–16:37

Now let’s look at the storyboard. This may be the easiest part. I am not sure whether to make the circle press the button again so the yellow track appears from the center, first vertically, or to have it appear unexpectedly and grow sideways along X while the circle and triangle move away. I think I’ll choose the second option. If we always follow the same pattern—button or circle presses, then something happens—the viewer can predict it, and that gets a little boring. Let’s add some surprise: the central element will appear suddenly, without warning. I’ll make that animation and come back.

The track animation is ready. We have reused and duplicated the layer we made at the beginning, tuning it a little. We have practically set up the next animation, which will make the loop work at the beginning. First, we have the track appear with the rhythm we want. The rhythm and timing (*temporización*) matter because we need to synchronize the animations of the elements that are pushed off the sides by the central yellow element.

I’m going to change my mind again. I do not like this, even though the animation could be better made. I do not like the effect itself, where the central element pushes the other two away. I think I’ll use something more magical, like the earlier idea: at a particular moment, the circle and triangle stay in place and suddenly disappear. I think that will look better.

Here is how it looks. It may be a little too abrupt, too violent. I’ll add an opacity (*opacidad*) effect or animation to both elements so their disappearance is a little softer. Let’s see. I find it interesting and like how it looks. Then this element should rotate into this position, and the square should appear here. I have the rotation animation mostly prepared, so I’ll finish it and show you the complete sequence in a loop.

![503 · U5 · L21 · 13:51](frames/U05L21-F1351.00.jpg)

On screen: [rest omitted]  
Shows: The storyboard returns, with the press, triangle bounce, outward movement, and 45-degree turn panels visible.

![503 · U5 · L21 · 15:03](frames/U05L21-F1503.00.jpg)

On screen: [none]  
Shows: A tall yellow rectangle crosses the composition between the purple circle at the right and red triangle at the lower left.

![503 · U5 · L21 · 16:12](frames/U05L21-F1612.00.jpg)

On screen: “Opacity” / “100%” [rest omitted]  
Shows: The red triangle and purple circle remain apart in the composition, with opacity properties visible in the timeline.

![503 · U5 · L21 · 16:23](frames/U05L21-F1623.00.jpg)

On screen: [none]  
Shows: The yellow track is diagonal again, with a purple square at its lower-left end.

## Review the completed series

Anchor: 503 · U5 · L21 · 16:37–17:26

Let’s watch the complete loop. The circle presses, the triangle bounces, and the sequence returns to the start. We could still adjust some curves and timing, but we can be happy with what we have made. This was the last choreography we were going to make together. It was a little long, but I hope it was worth it.

We have completed the series of animations I planned to make with you. Now I suggest that you make three more to complete a series of twelve. In the next lesson, I’ll teach you a lot of very useful tricks for making a reel that will do really well on social media.

![503 · U5 · L21 · 17:08](frames/U05L21-F1708.00.jpg)

On screen: [none]  
Shows: The final composition’s yellow diagonal track and purple circle, with the animation timeline below.
