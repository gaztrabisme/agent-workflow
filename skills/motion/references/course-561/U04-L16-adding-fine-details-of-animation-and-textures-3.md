# Lesson 16 · Adding fine details of animation and textures 3

Anchor: 561 · U4 · L16 · 14:30 · https://www.domestika.org/en/courses/561-creation-of-animated-infographics/units/5653-animation#course_lesson_17136

## Bringing Illustrator text into After Effects

Anchor: 561 · U4 · L16 · 00:00–02:30

561 · U04 · L16 · 00:00–02:30

We will continue with the second part of detailed animation. Four precompositions (*precomposiciones*) are already animated, so I enter the next one. I brought its text from Illustrator and created it in After Effects so I could use animation presets (*ajustes preestablecidos*). In After Effects these are text effects for animating an entrance, and they can save a lot of animation time. I go to the illustration in Illustrator, copy all the text, return to After Effects, choose New, Text, and press Control + V. This creates the text just as it was in Illustrator; I only arrange it. I did this with all the text in this precomposition.

I apply an entrance effect. This one, for example, writes one character at a time. Set whatever speed you want and try the different effects; some are very interesting, although some are too extravagant, so I try to use simple effects. I can apply an effect to every layer. I press U again to see the keyframes (*fotogramas clave*), select them and shorten their duration so they do not take so long. I can offset each layer by one frame so they enter at different speeds. Usually this has to be done manually. If I have a plugin (*complemento*), I can do it all at once, which can save a lot of time. Here I select all the layers, set them two frames apart, and the plugin does it automatically. We can see them all enter at different times. We can separate them by more frames, too. If I have animated something, I should lock it so it does not get in the way of the other work. We will go part by part.

![561 · U4 · L16 · 00:25](frames/U04L16-F0025.00.jpg)

On screen: "50.658" / "COCHES PRODUCIDOS EN 2005" [cars produced in 2005] / "500.000" / "PLANEA PRODUCIR EN 2019" [plans to produce in 2019] [rest omitted]  
Shows: The Tesla infographic grid with a plug symbol and production figures.

![561 · U4 · L16 · 00:43](frames/U04L16-F0043.00.jpg)

On screen: "NATURAL" [natural] / "RESERVA" [reserve] / "ECONOMICO" [economic] / "ECOLOGICO" [ecological] / "SUSTENTABLE" [sustainable] / "ALMACENAMIENTO" [storage] / "TESLA" / "300.000" / "CLIENTES" [customers] / "900" / "EUROS DE ENTRADA" [euros down payment] / "+270" / "MILLONES DE EUROS" [million euros] / "123 KM/H" [rest omitted]  
Shows: Illustrator view of the Tesla infographic with its grid, labels, and brand title.

![561 · U4 · L16 · 02:02](frames/U04L16-F0202.00.jpg)

On screen: "Frames: 2" / "Execute" [rest omitted]  
Shows: The SequenceLayers panel set to a two-frame offset beside repeated text groups at different animation stages.

## Animating the loading bars and line

Anchor: 561 · U4 · L16 · 02:30–05:53

561 · U04 · L16 · 02:30–05:53

I will start down here. I will animate this loading bar with Scale (*escala*). I move its anchor point (*punto de anclaje*) over here, unlink the two scale values, and then it will scale from this side so it looks as if it is loading. I start at zero and give it a couple of seconds. It reaches the end—or, rather, the middle, because the value here is 50 percent. I set the keyframes, apply Easy Ease (the Spanish interface calls it *Desaceleración suave*; F9), and can adjust the dotted line. I convert it to a vector shape and animate the lines using the path offset. I set a keyframe at the beginning, go to the end while holding Shift, move farther along, and leave it there.

Now that this is animated, I lock it and animate these bars using the same principle. Since I have the plugin I showed you, I can select all the anchor points and move them down together. They will take about four seconds. I set a Scale keyframe, go to the beginning, unlink the values so only the Y axis scales, and now they all scale together. I offset them so they load at different times, then press F9. The bars are loading. I select and lock everything, zoom in with the mouse, and check it all.

I can also work on this loading line. I convert it to a vector shape and add the effect called Trim Paths (*Recortar trazados* in the Spanish version). I set a keyframe here and move the end value. Again, it looks as though it is loading. I will make a small loop (*bucle*) with the plug by copying and pasting these keyframes. If I hold Alt and click the stopwatch, this arrow appears. In Properties, I choose Loop here. It is code—programming languages can be a little complicated—but After Effects can do it automatically without my having to look for the code or know how to program. Now this animation will repeat by itself, and it looks quite interesting.

![561 · U4 · L16 · 03:22](frames/U04L16-F0322.00.jpg)

On screen: "RECARGABLE" [rechargeable] / "50%" / "177 KM" [rest omitted]  
Shows: A half-filled progress bar with the percentage and distance beneath it.

![561 · U4 · L16 · 04:22](frames/U04L16-F0422.00.jpg)

On screen: "+" / "900" / "EUROS DE ENTRADA" [euros down payment] / "=" / "+270" / "MILLONES DE EUROS" [million euros] / "209" / "KILOMETROS DE AUTONOMIA" [kilometers of range] / "254 M" / "396 M" / "74 M" / "294 M" / "889 M" / "575 M" / "2011" / "2012" / "2013" / "2014" / "2015" / "2016" [rest omitted]  
Shows: The infographic's bar chart with six labeled yearly values and the adjacent totals.

![561 · U4 · L16 · 05:10](frames/U04L16-F0510.00.jpg)

On screen: [none]  
Shows: A glowing plug icon in a circular progress outline, selected in After Effects.

![561 · U4 · L16 · 05:34](frames/U04L16-F0534.00.jpg)

On screen: “Property” / “loopOut(type = "cycle", numKeyframes = 0)” [rest omitted]  
Shows: The expression menu open on the highlighted loopOut option for the Position property.

## Animating the dials, text, and timing

Anchor: 561 · U4 · L16 · 05:53–09:08

561 · U04 · L16 · 05:53–09:08

We have that, and now we can work on these dials. Go to the end and work on Position (*posición*); everything can start at zero or near zero. I can bring one over here, copy its position, and paste it onto all of them so they all start from the same place. Then I offset them so they reach their destinations at different times. Press F9. If you watch this with the normal keyframes, it is more boring and linear. Remember to apply F9 to the keyframes; then they appear in the graph. I can adjust the speed graph a little here and make the animation look different and much more pleasant.

Now we will animate these texts. Sometimes you cannot click what you want. In this example, I want to click the text but cannot. I click and see what is above it: this layer is in the way. Now I can select all these elements. If I select them one by one while holding Shift, then press Control + X and Control + V, they are ordered in the same sequence in which I selected them. I had all these text layers out of order; now I can select them from first to last and apply an animation. Again, I adjust the keyframes, press F9, and change the speeds. In this case the graph shows that the text comes in quickly and eases out at the end—very smoothly. I offset the layers by two frames, then by four, which is easier to see.

This glow (*brillo*) still remains hanging there. You can see how each detail adds something to the animation: while the text animates, the bars fill, the line draws, the plug moves back and forth, and these other elements move. When there is a lot happening, you cannot see everything at real speed. You can keep rendering, checking the speeds, and rendering again. We will move on to the next composition, which uses more of what we have already tried.

![561 · U4 · L16 · 06:25](frames/U04L16-F0625.00.jpg)

On screen: [none]  
Shows: Five yellow squares and five white horizontal dials, each with a circular marker.

![561 · U4 · L16 · 08:04](frames/U04L16-F0804.00.jpg)

On screen: "Escala" [scale] / "Opacidad" [opacity] [rest omitted]  
Shows: The speed graph for the animated elements, with the Scale and Opacity properties visible.

![561 · U4 · L16 · 08:49](frames/U04L16-F0849.00.jpg)

On screen: "1.000.000" / "PLANEA PRODUCIR EN 2020" [plans to produce in 2020] / "30" / "MINUTOS DE CARGA" [minutes of charging] / "209" / "KILOMETROS DE AUTONOMIA" [kilometers of range] / "254 M" / "396 M" / "74 M" / "294 M" / "889 M" / "575 M" / "2011" / "2012" / "2013" / "2014" / "2015" / "2016" [rest omitted]  
Shows: The completed Tesla infographic with its charging bar, labels, dial rows, and six-year bar chart.

## Masking and animating the SpaceX scene

Anchor: 561 · U4 · L16 · 09:08–14:30

561 · U04 · L16 · 09:08–14:30

In this next composition, the stroke (*trazo*) was made in Photoshop, not Illustrator, so I cannot convert it to a vector and apply effects here. This technique can help with another project: I mask (*enmascarar*) the stroke with a shape from After Effects. I create a circle, remove its fill, give it a white stroke like the circle I already have there, and expand it. I cut the stroke, find this stroke, and paste it underneath. Working from the bottom up, I use it as a mask, so the circle sits above the other stroke. That lets me select the circle and apply the effect we used earlier, Trim Paths. I select End and can choose where the circle starts.

I check the graphs again. Now the line animates using the Photoshop stroke as a mask, with the Alpha Matte set to “Stroke.” I animate these small details. This precomposition lasts only four seconds, so I make the small eclipse begin almost fully visible and become covered as the animation moves forward. I unlock what I animated so it will not get in the way later.

We will recycle an earlier animation. Do you remember the fire on this rocket that we animated in the main composition? I copy it with Control + C, bring it into the composition I am working on, find the rocket, and paste it there. The rocket is rotated, so I set it to zero. If this is the rocket, it would be at layer three. This is the smoke. I lock the layers behind it so I can select it. The smoke was spread across several layers and was taking up space, so I hide it. Now everything follows the rocket. The smoke and rocket are already animated; it does not matter which part it is, everything follows the same path. I adjust Position and move it up a little.

Now I will move the glows and hide them. Here the glow for many objects is on one layer. I duplicate that layer, mask it, and subtract the rocket's glow. This duplicate is the same glow layer, but I mask it so only this glow remains. Then I can move it here and make it follow the rocket. I animate it, and the glow is ready.

I will animate the planets left there. I find the Sun and lock the other layers. I make the Moon's glow follow the Moon, the Moon follow the Earth, and rotate the Earth a lot. Since the Earth is a circle, you will not notice it rotating, but the Moon will rotate around it from the Earth's position. I do the same with the Earth: make it follow the Sun and rotate the Sun. To apply the same thing to Mars, I duplicate the Sun, hide the original, make this one follow Sun 2, and animate its rotation. We had just animated it, so we animate that rotation. And that is it.

![561 · U4 · L16 · 09:39](frames/U04L16-F0939.00.jpg)

On screen: "SPACEX" / "TIERRA" [Earth] / "MARTE" [Mars] [rest omitted]  
Shows: SpaceX wordmark at the center of a star field, with the Earth, Mars, orbit paths, and a rocket.

![561 · U4 · L16 · 10:34](frames/U04L16-F1034.00.jpg)

On screen: "Inicio" [Start] / "0.0%" / "Fin" [End] / "120%" / "Desplazamiento" [Offset] / "0x+66.0°" / "Recortar varias formas" [Trim Multiple Shapes] / "Simultáneamente" [Simultaneously] [rest omitted]  
Shows: The Trim Paths controls for the circle used to reveal the line.

![561 · U4 · L16 · 10:48](frames/U04L16-F1048.00.jpg)

On screen: "FUNDADA 6 DE MAYO DE 2002" [founded May 6, 2002] [rest omitted]  
Shows: The SpaceX logo and orbit diagram with a small rocket, planets, and a glow element near the Moon selected.

![561 · U4 · L16 · 12:12](frames/U04L16-F1212.00.jpg)

On screen: "Cohete" [rocket] / "Posición" [position] / "1275.3,799.2" / "[Humo cohete]" [rocket smoke] [rest omitted]  
Shows: A close view of the SpaceX scene with the animated rocket and fire above the layer timeline.

![561 · U4 · L16 · 13:30](frames/U04L16-F1330.00.jpg)

On screen: [none]  
Shows: A close view of the glowing Sun, inner orbit, Earth, and a red outer planet.

![561 · U4 · L16 · 14:12](frames/U04L16-F1412.00.jpg)

On screen: "SOL 2" / "Rotación" [rotation] / "0x+31.7°" / "SOL" / "Rotación" [rotation] / "0x+25.2°" [rest omitted]  
Shows: The SpaceX wordmark around the Sun, the inner orbit and Earth, a crescent Moon at left, and Mars at upper right.
