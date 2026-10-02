# Lesson 18 · Animation Fundamentals 2

Anchor: 3762 · U5 · L18 · 13:01 · https://www.domestika.org/en/courses/3762-animated-infographics-with-illustrator-and-after-effects/units/15362-animating-the-artwork-from-static-to-dynamic#course_lesson_48594

## Separating the cocktail decorations

Anchor: 3762 · U5 · L18 · 00:00–01:29

The cocktails are animated, so we can move on to animating their decorations. First, isolate the other elements in the file and show only the decorations. The Americano has two kinds of elements: squares and circles. During the transition to the Boulevardier, only the circles remain; the squares pass through a transition and gradually disappear. In the Negroni, those circles become small diamonds. They stay in the same positions in the Dry Martini, but become distorted circles. The White Lady has no decorations, so we will give them an entrance animation for the Italian market.

Each Margarita element can have its own entrance animation because we will control its position and when it enters and exits. Tequila Sunrise and Mimosa use the Boulevardier decoration, so we can reuse the animation already made for it. Spritz reuses the Negroni animation. At the end, a transition returns to the Americano, turning diamonds back into circles and bringing back the squares. Now we can animate these elements in After Effects.

![3762 · U5 · L18 · 00:15.70](frames/U05L18-F0015.70.jpg)

On screen: [illegible]  
Shows: Illustrator overview board with nine cocktail compositions, a chart, palette swatches and decoration samples.

![3762 · U5 · L18 · 00:26.00](frames/U05L18-F0026.00.jpg)

On screen: "Americano" / "Bitter Campari" / "30ml" / "A splash of soda water" / "Sweet Red Vermouth" / "30ml" [rest omitted]  
Shows: The Americano artboard with yellow squares and red circles arranged across the grid.

![3762 · U5 · L18 · 00:44.10](frames/U05L18-F0044.10.jpg)

On screen: "Bourbon or Rye Whiskey (45ml)" / "Negroni" / "Gin" / "30ml" / "Dry Martini" [rest omitted]  
Shows: Recipe layouts for the Negroni and Dry Martini with ingredient labels and decoration dots.

![3762 · U5 · L18 · 00:51.70](frames/U05L18-F0051.70.jpg)

On screen: "White Lady" / "Gin" / "30ml" / "Fresh lemon juice" / "20ml" / "Triple Sec" / "30ml" / "Margarita" / "Tequila" / "50ml" / "Freshly squeezed lime juice" / "50ml" / "Triple Sec" / "20ml" [rest omitted]  
Shows: The White Lady artboard with no decoration dots beside the Margarita artboard with its small dot pattern.

## Creating the Americano's squares and circles

Anchor: 3762 · U5 · L18 · 01:29–03:27

In After Effects, work in the composition (*composizione*) 03_OTHER, where the decorations will be animated independently. Start with the Americano. Create a square and a circle, each exactly 10 × 10 pixels, using the rectangle tool as before. Center the shape's anchor point (*punto di ancoraggio*). Name the first layer Item-A_01 and assign it a color. Duplicate it as Item-B_01 and give the duplicate an orange color. Use the Roundness control to make the circular element, setting its roundness (*rotondità*) to 5 pixels and adding a keyframe.

Import the palette into the assets folder to finish the setup. Both elements currently have gradients, so change them to solid fills: yellow for the squares and red for the circles. The palette can then be removed.

![3762 · U5 · L18 · 01:38.60](frames/U05L18-F0138.60.jpg)

On screen: "01_Cocktail" / "03_OTHER" [rest omitted]  
Shows: After Effects is open on 01_Cocktail, with 03_OTHER listed in the project panel.

![3762 · U5 · L18 · 02:48.50](frames/U05L18-F0248.50.jpg)

On screen: [rest omitted] / "Item-B_01" / "Item-A_01" [rest omitted]  
Shows: A yellow square and a small group of rounded yellow shapes in the decoration composition.

## Timing the square exit and Negroni diamond transition

Anchor: 3762 · U5 · L18 · 03:27–05:50

Use the cocktail composition as a guide: at second 1, the animation moves to the next cocktail. The decoration composition therefore needs an animation from second 0 to second 1. The squares leave the scene during this transition. Add keyframes for rotation and size so each square rotates by 90° and shrinks to 0 × 0 pixels. Select those keyframes and set the movement speed. The squares will then rotate and shrink as they leave the screen.

The circles do not change when the Americano becomes a Boulevardier. At second 3, begin the Boulevardier-to-Negroni transition by keyframing size, roundness and rotation. Over one second, from second 3 to second 4, reduce the elements from 10 to 7 pixels, set roundness to 0 and rotate them 45° clockwise. Set the speed on these keyframes. In the resulting animation, the circles turn into small diamonds in one second.

![3762 · U5 · L18 · 04:30.10](frames/U05L18-F0430.10.jpg)

On screen: "Size 10.0,10.0" / "Roundness 5.0" [rest omitted]  
Shows: The 10-pixel yellow square and red circle before their transitions, with shape properties expanded in the timeline.

![3762 · U5 · L18 · 05:20.00](frames/U05L18-F0520.00.jpg)

On screen: "Keyframe Velocity" / "Keyframe type: Size" / "Incoming Velocity" / "Lock Dimensions" / "Dimension: X - /sec" / "Influence: 85 %" / "Dimension: Y - /sec" / "Influence: 85 %" / "Outgoing Velocity" / "Lock Dimensions" / "Dimension: X - /sec" / "Influence: 0.01" / "Dimension: Y - /sec" / "Influence: 0.01 %" / "Continuous (Lock Outgoing to Incoming)" / "Setting velocity for 2 keyframes" / "Cancel" / "OK" [rest omitted]  
Shows: The Keyframe Velocity dialog for the size keyframes, with incoming and outgoing influence values.

## Morphing the diamonds into Dry Martini decorations

Anchor: 3762 · U5 · L18 · 05:50–07:25

To transform the Negroni into the Dry Martini, move to second 6 and set keyframes for Item-A. At second 7, the Dry Martini is introduced. The diamonds become distorted circles by changing size, roundness and rotation. Unlink width and height, then set the shape to 8 pixels wide and 11 pixels high. Set roundness to 7 pixels and add 180° to the previous 45°, for a total rotation of 225° (the captions read *225°C*). This turns the diamond as it morphs. The captions call the drink *Dre Martini*; the artwork labels it Dry Martini.

The shape also changes color. Open the object's controls, choose Fill, and change the fill color. At the midpoint of the morph, sample the reference color from the palette, which contains red, green, magenta and ochre blocks. Select the keyframes and change their temporal interpolation to Hold (*interpolazione temporale di tipo blocco*). The element changes color during the morph.

![3762 · U5 · L18 · 05:59.50](frames/U05L18-F0559.50.jpg)

On screen: "Size 7.0,7.0" / "Roundness 0.0" / "Rotation 0x+45.0°" [rest omitted]  
Shows: A red 7-pixel diamond at the Negroni stage, with its size, roundness and rotation controls expanded.

![3762 · U5 · L18 · 06:33.30](frames/U05L18-F0633.30.jpg)

On screen: "Size 8.0,11.0" / "Roundness 0.0" / "Rotation 0x+145.0°" [rest omitted]  
Shows: The selected red diamond during the Dry Martini shape change, with the current dimensions and rotation visible.

![3762 · U5 · L18 · 07:04.40](frames/U05L18-F0704.40.jpg)

On screen: "Fill 1" / "Composite Normal" / "Fill Rule Non-Zero Winding" / "Color" [rest omitted]  
Shows: Fill controls for the red decorative element in the After Effects composition.

![3762 · U5 · L18 · 07:12.00](frames/U05L18-F0712.00.jpg)

On screen: "Palette.ai, used 2 times" / "1080 x 1350 (1.00)" / "Millions of Colors+ (Straight)" [rest omitted]  
Shows: The imported palette artwork with red, green, magenta and ochre color blocks.

![3762 · U5 · L18 · 07:21.00](frames/U05L18-F0721.00.jpg)

On screen: "Keyframe Interpolation" / "Temporal Interpolation: Linear" / "Current Settings" / "Linear" / "Bezier" / "Continuous Bezier" / "Auto Bezier" / "Hold" / "Cancel" / "OK" [rest omitted]  
Shows: The Temporal Interpolation menu is open with Hold highlighted.

## Removing and bringing back decorations

Anchor: 3762 · U5 · L18 · 07:25–09:27

The White Lady has no decorations, so make an exit animation for the element. At second 9, add keyframes for size and roundness. At second 10, set the element to 0 × 0 pixels with roundness 0 and rotation +90°. This makes the elements disappear completely from the composition.

The same element returns in the same position for the Tequila Sunrise as a 10 × 10 circle. The transition from Margarita to Tequila Sunrise runs from second 15 to second 16. In the composition, set keyframes at second 15 for size, roundness, color and rotation. At second 16, the circle is 10 × 10 pixels, with roundness 5 and a 90° rotation. Its color is close to red, so duplicate and paste the earlier red color, then move the keyframes earlier so the circle is already red when it appears. Mimosa also uses 10 × 10 circles.

![3762 · U5 · L18 · 08:32.50](frames/U05L18-F0832.50.jpg)

On screen: "Tequila Sunrise"  
Shows: The Tequila Sunrise artboard with red decoration circles arranged across it.

![3762 · U5 · L18 · 09:18.70](frames/U05L18-F0918.70.jpg)

On screen: "Size 10.0,10.0" / "Roundness 5.0" / "Rotation 1x+45.0°" [rest omitted]  
Shows: The red circle in the After Effects composition at the point where the repeated decoration animation is being reviewed.

## Reusing transition keyframes and completing the loop

Anchor: 3762 · U5 · L18 · 09:27–12:10

For Spritz, reuse the existing animation that turns 10 × 10 circles into 7 × 7 diamonds. Scrub back through the timeline to the Boulevardier-to-Negroni transition, which occurs in the third second, and select the size, roundness and rotation values. Move to second 20 and paste the same keyframes onto the same layer.

To complete the loop, at second 22 turn the diamonds back into circles and bring the yellow squares back. Set the keyframes at second 22 and make the same animation as before for both the circles and the yellow squares. This completes the animation of the individual decoration elements.

![3762 · U5 · L18 · 10:27.00](frames/U05L18-F1027.00.jpg)

On screen: "Keyframe type: Roundness" / "0 /sec" / "0 /sec" / "Setting velocity for 10 keyframes" [rest omitted]  
Shows: The Keyframe Velocity dialog at composition second 20, with Roundness velocity values for 10 keyframes.

![3762 · U5 · L18 · 10:39.70](frames/U05L18-F1039.70.jpg)

On screen: "Size 7.0,7.0" / "Roundness 0.0" / "Rotation 0x+45.0°" [rest omitted]  
Shows: A red diamond in the decoration composition during the reused transition.

## Duplicating the decorations into a measured pattern

Anchor: 3762 · U5 · L18 · 12:10–13:01

Now duplicate the individual decoration elements and place them to match the Adobe Illustrator file. The pattern follows precise rules and proportions. To reproduce those measurements in After Effects, select an element and duplicate it. Press P to reveal Position and add 320 pixels horizontally so the duplicate lands exactly where it should. Repeat this to build a pattern with a defined spacing.

![3762 · U5 · L18 · 12:57.50](frames/U05L18-F1257.50.jpg)

On screen: "Position 1024.8,44.8" / "Position 704.8,44.8" / "Position 384.8,44.8" [rest omitted]  
Shows: A row of red circles and a yellow square, with successive decoration layers positioned at 320-pixel intervals.
