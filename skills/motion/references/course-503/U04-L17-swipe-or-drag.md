# Lesson 17 · Swipe or drag

Anchor: 503 · U4 · L17 · 8:20 · https://www.domestika.org/en/courses/503-introduction-to-motion-design-and-animation-curves-in-after-effects/units/2012-creating-our-basic-library-of-movement#course_lesson_7414

## Define a swipe and study references

Anchor: 503 · U4 · L17 · 00:00–01:58

In this lesson we’ll make a swipe or drag animation (*arrastre*), which simulates a user interacting with content. Let’s see it. You caught me; give me a moment while we go into After Effects.

To make this animation we need two elements. I have a circle and this square—sorry, this is the background, this square here. I lock the background so I can no longer select it; now I can select only the circle and the square, the two elements I’m going to animate.

The best way to understand a swipe is to look at examples. Dribbble (captions: *Dribble.Com*) is a good place to find references for micro-animations or short animations. It’s a social network that we may talk about at the end of the course. Remember, the name has three Bs—I always get it wrong: T-R-I-B-B-B-L-E. I’ve searched for “swipe” and selected a few examples to show you.

![503 · U4 · L17 · 01:09](frames/U04L17-F0109.00.jpg)

On screen: "dribbble" / "swipe" [rest omitted]  
Shows: Dribbble search results for “swipe” appear in a grid of animation projects.

Here’s a swipe by Jardson Almeida (captions: *Yardson Almeida*). At its simplest, a swipe is one element dragging another. Another example makes that even clearer: we need at least two elements, one that drags and one that is dragged. Here is another example of simplified UI prototyping. It’s interesting because, when one element swipes, the dragged element has a slight delay; it is reluctant to follow the movement of the element doing the dragging.

After seeing these examples, it’s as simple as this: we have a circle that will drag the other element, and a square. Let’s get to it and start animating.

![503 · U4 · L17 · 00:38](frames/U04L17-F0038.00.jpg)

On screen: "Círculo" [circle] / "Cuadrado" [square] / "fondo" [background] [rest omitted]  
Shows: The After Effects composition contains a dark circle inside a purple square on a red background.

![503 · U4 · L17 · 01:20](frames/U04L17-F0120.00.jpg)

On screen: "Page Scrolling" / "by Jardson Almeida" [rest omitted]  
Shows: A Dribbble project page for a yellow page-view indicator animation, with three dots and a magenta strip at the right edge.

![503 · U4 · L17 · 01:34](frames/U04L17-F0134.00.jpg)

On screen: "Swiping off" / "by Morten Niklasson" [rest omitted]  
Shows: A Dribbble project page shows a drawn hand moving toward an orange shape on a turquoise field.

![503 · U4 · L17 · 01:45](frames/U04L17-F0145.00.jpg)

On screen: "Swipe Studio" / "by MDS in InVision Studio" [rest omitted]  
Shows: A red-and-white interface prototype displays overlapping cards and a small dark circle on the front card.

![503 · U4 · L17 · 01:51](frames/U04L17-F0151.00.jpg)

On screen: [rest omitted]  
Shows: The same prototype shows two red cards side by side, with a dark circle on the left card.

## Animate both objects and tune their position curves

Anchor: 503 · U4 · L17 · 01:58–04:15

I set a keyframe at the starting position on both layers. I move forward a little, then zoom in on the timeline at the one-second mark, for example. We can adjust the timing or speed later. I move both layers at once. The animation is there. I press N to set the preview area and launch it with the space bar. It disappears. You may think it looks terrible. Don’t worry: animations usually look bad at first, and we improve them by adjusting the keyframes and especially the curves. Don’t get discouraged at the beginning.

I press F9 to give the keyframes curves for acceleration and deceleration. I open the Graph Editor (*editor de gráficos*). Remember that we need to work in the value graph (*gráfico de valores*) and separate X and Y. I select both layers and use one of our favorite buttons in the Graph Editor to separate X and Y. Since I’m animating only the two objects moving sideways, I’m using only X. I click the Y stopwatch to remove it; that deletes all keyframes connected to that value, leaving only X. The U shortcut is also useful because it shows only properties with keyframes.

I fit the curves in the view so I have more room to work. Make sure both layers are selected, because we want to give both objects the same curve so they move together. I select both curves by dragging and pull their handles. Keep your character in mind: mine is Clint Eastwood. His swagger is shown by the reluctance or delay at the start, so this part of the curve has much more easing. At the end he arrives more abruptly. I preview it. It could work, although we’ll refine it.

![503 · U4 · L17 · 02:02](frames/U04L17-F0202.00.jpg)

On screen: "Position" [rest omitted]  
Shows: The circle and square are selected in the composition; their Position properties and keyframes are visible in the timeline.

![503 · U4 · L17 · 02:55](frames/U04L17-F0255.00.jpg)

On screen: "Edit Value Graph" [rest omitted]  
Shows: The value-graph menu is open over the position curves, with the circle and square in the composition.

![503 · U4 · L17 · 03:30](frames/U04L17-F0330.00.jpg)

On screen: "X Position" [rest omitted]  
Shows: The circle leads the square toward the left while the X-position curve slopes down in the graph editor.

## Add a delay so the circle leads

Anchor: 503 · U4 · L17 · 04:15–04:55

Next I mark which object leads and which one is dragged by giving the square a little delay. I move its keyframes later and preview repeatedly to find the feeling I want. What I don’t like yet is that the leading object, the circle, is so large that I don’t really feel an interaction. So I’ll add a secondary animation: the circle will get smaller at the beginning, just as it starts to drag the other object. That way, we’ll reinforce the feeling of interaction.

![503 · U4 · L17 · 04:27](frames/U04L17-F0427.00.jpg)

On screen: [rest omitted]  
Shows: The centered circle and square composition is selected; their position keyframes are visible in the timeline.

## Make the leading circle shrink quickly

Anchor: 503 · U4 · L17 · 04:55–06:27

I move both layers to the right to make more room at the beginning for the circle’s scale animation. I press S to show Scale, set a keyframe, go to just before the movement starts, and make the circle smaller. I play it to check the timing without curves. See how it gets smaller? This needs to be much more electric and faster.

I enter the Graph Editor. I have a small problem: the eye is showing me all the animated properties. I turn off that option because I want it to show only the properties I select. I choose “Show Selected Properties.” Now I select the scale animation and convert it from a straight, linear line to a Bézier curve (captions: *unidad. ¿Bézier o con curvas?*). I can adjust the scale animation with only its scale curve available. I’ll give it the Clint Eastwood touch (caption: *Clean as Wood*; later: *Clean Eastwood*). You can give yours the touch of your brother-in-law, your cousin, or whoever you chose as your character. We can see the hesitation at the start and then, when it arrives—samba. It really arrives with a lot of decisiveness.

![503 · U4 · L17 · 05:13](frames/U04L17-F0513.00.jpg)

On screen: "Scale" [rest omitted]  
Shows: The selected circle is centered inside the square; its Scale property and keyframes are visible in the timeline.

![503 · U4 · L17 · 05:21](frames/U04L17-F0521.00.jpg)

On screen: [rest omitted]  
Shows: The circle has shrunk inside the square, with its Scale animation visible in the timeline.

![503 · U4 · L17 · 06:21](frames/U04L17-F0621.00.jpg)

On screen: [rest omitted]  
Shows: The reduced circle appears above its descending eased scale curve in the Graph Editor.

## Make the square react when the circle lands

Anchor: 503 · U4 · L17 · 06:27–08:20

It would also be good to show the moment the circle lands on the square by having the square respond with a scale movement. I set a keyframe on the square’s Scale here, a little after the circle actually stops on it, and make the square smaller. I play it to see how it looks. The keyframes are still linear. It looks a little early, so I adjust the timing and move this keyframe later. Now it’s late. Perhaps the scale change is a bit too large. I’ll change it from 82 to 79, for example; I like that number. It looks something like this.

Next I’ll adjust the curves for this animation. I’ll skip the character-personality part a little here, because I’m representing only the interaction between two elements. We want to see how one responds to the other as soon as it lands. It looks pretty good; the scale change could even be subtler. I’ll leave it—although it pains me—and change 79 to 80, maybe 81. Something very subtle. Let’s see. It looks good.

From here, because I’m fanatical about adjusting curves until the animation is at the point I like, I’ll keep working on it like a madman. I encourage you to do the same and make your animations as perfect as you can—surely even better than mine. Now you have your first animation representing a drag or swipe interaction. We’ve seen how to make a swipe or drag. In the next lesson we’ll start animating choreographies.

![503 · U4 · L17 · 06:39](frames/U04L17-F0639.00.jpg)

On screen: [rest omitted]  
Shows: The reduced circle is centered on the purple square, with both inside a red field; the Scale property is visible.

![503 · U4 · L17 · 07:17](frames/U04L17-F0717.00.jpg)

On screen: [rest omitted]  
Shows: The square’s scale curve descends steeply from its earlier value in the graph editor.

![503 · U4 · L17 · 08:07](frames/U04L17-F0807.00.jpg)

On screen: [rest omitted]  
Shows: The dark circle is centered inside the purple square on the red background, with the timeline keyframes visible.
