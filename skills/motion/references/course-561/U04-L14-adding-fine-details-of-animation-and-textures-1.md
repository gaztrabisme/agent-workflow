# Lesson 14 · Adding fine details of animation and textures 1

Anchor: 561 · U4 · L14 · 8:25 · https://www.domestika.org/en/courses/561-creation-of-animated-infographics/units/5653-animation#course_lesson_17134

## Grouping and animating the first scene

Anchor: 561 · U4 · L14 · 00:00–03:06

Continuing with the animation, we will work scene by scene, adding details to each object in our infographic. I am selecting the elements to apply a small scale change. The easiest way is to link them to a null object (*objeto nulo*). Right-click, choose New Null, and select the elements you want. We will leave out anything that should move on its own: for example, the asteroid and its tail will move separately. Hold Shift or Control while selecting each element. Find the pick whip and link the elements to the null, which I will rename Miscellaneous. Now everything is linked, so we can scale and move it using only two keyframes (*fotogramas clave*), rather than moving every element separately.

I scaled up the glow and now we create the keyframes, one at the beginning and one at the end. Since I have the glow from the fire of one of the rockets I made, we create a mask (*máscara*) and set it to Subtract. We are not going to use it, and we add Easy Ease to the keyframes. We check how it all looks, and that is done.

What remains, in this case, is to rotate each element. Sometimes we cannot select a layer because other layers above it get in the way, so we lock those layers and then rotate the elements in different directions. That makes the scene a little more abstract and less monotonous. The process is to try it, play it back, see how it looks, try again and keep adjusting. With time you will gain experience and it will get easier. I select the layers again and create the rotation keyframe at the beginning. Since everything is simple and subtle, we do not need large values, just a small rotation. It depends a lot on what you are going to design and illustrate. The idea is that, because this is an information-heavy infographic with many items and miscellaneous details, we should not go overboard with the animation. It would distract people and they would not read anything. If our purpose is to inform, animation is a detail. We preview the whole thing. It looks quite good.

![561 · U4 · L14 · 00:47](frames/U04L14-F0047.00.jpg)

On screen: “TESLA” [rest omitted]  
Shows: The starfield infographic with planets, asteroid and tail, glowing points, small brand labels, and many selected objects.

## Linking smoke, animating the asteroid and pulsing glows

Anchor: 561 · U4 · L14 · 03:06–06:58

The smoke we animated earlier is something I will duplicate so I can use it on the other rocket. We move it. Sometimes, when we mask things, the anchor point (*punto de anclaje*) ends up off to one side. If we rotate the element, it rotates around that point on the left. We can move the anchor point, or simply rotate the element and adjust it. I will link the smoke to the other rocket, the fire. Done. Since it is linked, we can move the rocket and the smoke will follow it.

I use shortcuts for keyframes: Alt+Shift+T for Transparency (*transparencia*) and Alt+Shift+P for Position. It is faster; you remember them and use them without thinking. But you can also click the arrow, find the property you want to animate and create a keyframe. In this case, I think the scale is too strong; its value was too high, so I made it subtler.

The asteroid tail is an Illustrator vector. Choose Create, then Create Shape Layer, which converts it to a shape layer (*capa de formas*). We are left with a line; simply hide or delete what remains. Then we animate the asteroid's position along the line. Apply Easy Ease and adjust the speed in the properties. We will add Trim Paths (*recorte de trazados*) to the line and animate its End. That will be our starting keyframe: set it to zero and animate the starting keyframe so the line contracts. Apply Easy Ease and check the animation graphs in that small window. It looks different now. We will adjust the keyframes step by step. Move the asteroid. This is the part where we need to go step by step, sometimes frame by frame. Here we adjust it so it looks like the comet's tail and does not get ahead of it. Sometimes all this is tedious, but it is what really makes the difference in animation. So it does not look as if it is slowing down, I applied opacity to the tip of the comet so it disappears.

With the glows we created, I adjust the opacity so the glow seems to pulse. I will show it visually here; it is simply a matter of creating three keyframes. The first and last are the same, and we change the opacity on the middle one. Then we copy and paste those keyframes to the end of the video. We can see how it is turning out.

![561 · U4 · L14 · 03:17](frames/U04L14-F0317.00.jpg)

On screen: “UNA INFOGRAFÍA DE:” [An infographic by:] / “ELON MUSK” / “DOMESTIKA” / “SPACEX” / “TESLA” / “PAYPAL” [rest omitted]  
Shows: The full infographic with its title, orbit, colored particles, two rocket trails, and selection handles around the second smoke layer.

![561 · U4 · L14 · 04:47](frames/U04L14-F0447.00.jpg)

On screen: “Position” / “304.2,559.0” [rest omitted]  
Shows: A 100% close-up of the infographic title and a selected diagonal motion path with handles.

![561 · U4 · L14 · 05:17](frames/U04L14-F0517.00.jpg)

On screen: “Start” 100.0% / “End” 100.0% / “Offset” 0x+0.0 / “Trim Multiple Shapes” / “Simultaneously” [rest omitted]  
Shows: The speed graph for the asteroid-tail Trim Paths animation, with its controls open.

![561 · U4 · L14 · 05:41](frames/U04L14-F0541.00.jpg)

On screen: “Trim Paths 1” / “Start” 0.0% / “End” 22.4% / “Offset” 0x+0.0 [rest omitted]  
Shows: A zoomed comet trail with its selected endpoint and the Trim Paths controls open.

![561 · U4 · L14 · 06:13](frames/U04L14-F0613.00.jpg)

On screen: “Opacity” / “100%” [rest omitted]  
Shows: A 100% close-up of the infographic with a selected glow layer and its opacity keyframes in the timeline.

## Continuing the animation in the next scene

Anchor: 561 · U4 · L14 · 06:58–08:25

We will move on to the next scene. Remember to save the project, just in case. These programs are not perfect; they often crash and we lose all our work. We apply the same idea as in the previous scene: create a rotation keyframe at the beginning and another at the end. As you can see, the marker labeled 1 marks the end of the scene, so we always animate a little farther, just in case. This scene is quite simple, so there is not much to adjust. We will rotate the rings as in the previous scene, a small turn, not too exaggerated. We keep checking how it looks and feels. We will do the same thing for the glows: three keyframes, Control+C, Control+V, and then we move on to the next scene.

![561 · U4 · L14 · 07:25](frames/U04L14-F0725.00.jpg)

On screen: “PAYPAL” / “FUNDADA EN 1998” [Founded in 1998] [rest omitted]  
Shows: The Scene 2 timeline with marker 1 highlighted in yellow.

![561 · U4 · L14 · 07:47](frames/U04L14-F0747.00.jpg)

On screen: [rest omitted]  
Shows: The second scene with the PayPal wordmark, a dotted orbit, and glowing dollar signs.
