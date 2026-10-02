# Lesson 15 · Designing in After Effects 1

Anchor: 3762 · U5 · L15 · 20:40 · https://www.domestika.org/en/courses/3762-animated-infographics-with-illustrator-and-after-effects/units/15362-animating-the-artwork-from-static-to-dynamic#course_lesson_48415

## Moving the vector artwork into After Effects

Anchor: 3762 · U5 · L15 · 00:00–03:19

The vector visual is ready. In this lesson we move to After Effects and animate the data, morphing from one shape into another. We will use the basic version of After Effects and no external effects. The additional resources include plugins and useful links for adjusting curves and keyframe speed, which can improve your workflow. After identifying the elements and artwork in Illustrator, we will animate them in After Effects and bring the creative project to life.

Our sequence combines cocktails that always share an ingredient. We will morph from the Americano to the Spritz, creating a loop (captions: *lupo*).

Create a new composition (*composizione*) from Composition > New Composition, or use Command+N on Mac or Ctrl+N on Windows. Name the first composition Main; it will contain all the elements we animate. Set it to 1080 × 1350 pixels, with square pixels and a frame rate of 25 frames per second.

Because we will work with several compositions, keep the project panel organized with clear names. Create a `comp` folder for the compositions. Add a solid layer (*livello solid*) to Main for the background, using the color chosen in Illustrator. Press Enter to rename the layer `background`, then lock it so it cannot be moved accidentally.

Compositions make it easier to manage separate elements. The project uses three main compositions: `01 Cocktail` for the visual elements representing the cocktails; a text composition for all the necessary text; and `order` for decorations and elements that need a different blending mode (*modalità di fusione*) or special treatment from the main artwork.

![3762 · U5 · L15 · 00:49](frames/U05L15-F0049.00.jpg)

On screen: "Americano" / "Boulevardier" / "Negroni" / "Dry Martini" / "White Lady" [rest omitted]  
Shows: Illustrator board with the simplified ingredient shapes and recipe columns for five cocktails.

## Rebuilding the cocktail shapes

Anchor: 3762 · U5 · L15 · 03:19–06:25

Start in the cocktail composition. Recreate the shapes and their arrangement from Illustrator with the Rectangle tool to keep the proportions consistent. Click in the work area to make a rectangle; hold Shift to keep its sides proportional.

Pay attention to the anchor point (*punto di ancoraggio*), because it affects the movement and parameter changes applied later. Set it at the center or at a specific point on the shape. Use the Y control to move it. Hold Ctrl or Command to snap it precisely to useful points, such as the corners of a square. Here, place the anchor point in the center.

Use the Illustrator file as a reference for the proportions already chosen in the artwork. Set each element’s rotation and position to create the intended interaction, so one shape can become another over time. For the Campari bitter, use a shape 760 pixels wide by 400 pixels high, with 50-pixel rounded corners. In Contents > Rectangle > Rectangle Path, set the rectangle’s dimensions. A keyframe marks the time when the shape is 407 × 407 pixels; change the value by dragging or by entering a number. In this case, set it to 760 × 400 pixels. Adjust Roundness (*rotondità*) to 50.

![3762 · U5 · L15 · 04:49](frames/U05L15-F0449.00.jpg)

On screen: "Americano" / "Boulevardier" / "Negroni" / "30 ml Sweet Red Vermouth (15%)" / "Forma:" [Shape] / "760 px" / "400 px" / "150 px" [rest omitted]  
Shows: Illustrator reference with the Americano, Boulevardier and Negroni ingredient shapes, including the rounded rectangles being recreated.

![3762 · U5 · L15 · 06:02](frames/U05L15-F0602.00.jpg)

On screen: "Size" / "760.0,400.0" / "Roundness" / "50.0" [rest omitted]  
Shows: Rounded red rectangle in the composition with its 760-by-400 size and 50-pixel roundness values visible.

## Importing references, a palette, and gradients

Anchor: 3762 · U5 · L15 · 06:25–08:33

To match the Illustrator artwork closely, create a folder called `02asset` and collect the required assets there. Right-click in the Project panel to import the static images of the designed cocktails. Put them in the asset folder. Import the palette file from Illustrator as footage, not as a composition, and put it in the asset folder too.

Add the palette to the cocktail composition. Press S to scale the layer, and check again that it is footage rather than a composition. Use the Align panel to place it in the upper-left corner, then lock it so it cannot be moved accidentally.

Use the Americano image as the first cocktail reference to match position and color. Lock that layer, then select Shape 01. In Fill (*riempimento*), choose either a solid color or a linear gradient (*gradiente lineare*). Click the gradient to change its colors to the ones selected during design. Drag its handles to change the gradient’s extent. In Shape 01’s Rectangle and Gradient options, you can animate keyframes for the selected gradient’s start and end points, as well as its colors.

![3762 · U5 · L15 · 07:42](frames/U05L15-F0742.00.jpg)

On screen: "01_Americano.jpg" / "A splash of soda water" / "30ml" [rest omitted]  
Shows: Americano reference artwork, palette swatches and the first shape layer selected in After Effects.

![3762 · U5 · L15 · 08:08](frames/U05L15-F0808.00.jpg)

On screen: [rest omitted]  
Shows: The first shape filled with a pink-to-olive gradient over the Americano reference artwork.

## Setting up the main and secondary movement

Anchor: 3762 · U5 · L15 · 08:33–10:05

The animation needs two kinds of movement: the main movement that changes one cocktail into the next, and an auxiliary movement that makes the shapes float in the workspace. Use a null object (*oggetto nullo*) to apply movements or changes to the objects linked to it.

Create a null object from Layer > New > Null Object and place it above element 1. Center its anchor point on the anchor point of the element it controls. Link layer 1 to the null using the Parent and Link menu, or drag the spiral control to the null object or other layer you want to parent it to. The null’s position then affects the linked object’s movement. At this first stage, animate only the null object so the sequence stays linear as it passes between cocktails.

![3762 · U5 · L15 · 09:30](frames/U05L15-F0930.00.jpg)

On screen: "None" / "1. Palette.ai" / "2. Null 1" / "3. 01" [rest omitted]  
Shows: Parent and Link menu open with the null object available as a parent for the Americano shape.

## Moving from the Americano to the Boulevardier

Anchor: 3762 · U5 · L15 · 10:05–13:21

To move from the Americano to the Boulevardier, select the object and press P to open Position. Press R to open Rotation, and set a keyframe at −30 degrees. Press U to show all active keyframes on that object. The change from one cocktail to the next takes one second: move to 1 second, 0 frames on the timeline.

Replace the reference image with the Boulevardier: unlock the reference layer, select it, then hold Alt and drag the new image over it. Adjust the null object’s parameters to put the ingredient in the right place in the composition. Return to the start and press Space to preview the movement. Repeat for the cocktail’s other ingredients.

The soda needs a stroke (*traccia*) because it is an inner path. Create another rectangle with the same dimensions. Remove its fill and add a stroke in the chosen color. To keep the stroke inside the path, add Offset Paths (*tracciati di offset*). The teacher says to set it to 10, but the on-screen Amount is −10.0; use the displayed −10.0 value to pull the stroke inside the path rather than extending it 10 pixels on either side. Add the soda to the null object as well so it follows the main transition.

The first cocktail elements are now in place. Turn off the reference image to check that the shapes keep the same positions and rotations as the reference. Move to one second and apply the same movement to all the shapes. Turn the Boulevardier reference back on and place it higher in the composition. Press T to set its opacity so you can see both the shapes underneath and the reference image. At this stage, only the null object’s position and rotation affect the shapes.

The Boulevardier no longer contains soda. Rotate the null object and move the ingredient beyond the visible area so it disappears. Set the rotation and position of layer 2 correctly. Scrub along the timeline to preview the movement from the Americano to the Boulevardier.

![3762 · U5 · L15 · 11:44](frames/U05L15-F1144.00.jpg)

On screen: "02_Boulevardier.jpg" [rest omitted]  
Shows: Boulevardier reference artwork with the colored ingredient shapes and their motion controls visible in the timeline.

![3762 · U5 · L15 · 13:05](frames/U05L15-F1305.00.jpg)

On screen: "Offset Paths 1" / "Amount" / "−10.0" [rest omitted]  
Shows: The cocktail artwork with the outlined square selected and Offset Paths set to −10.0.

## Adding an ingredient and morphing into the Negroni

Anchor: 3762 · U5 · L15 · 13:21–17:13

For a new ingredient, follow the same steps: create a rectangle, remove its fill, and apply a flat fill in the reference color. Like the soda, it will enter the visible area. Go back in time and change its rotation and position. In the animated preview it moves into the composition and settles in its intended place.

For the secondary movement, use two seconds. Go to three seconds in the composition and give the null object matching position and rotation keyframes. From the one-second mark through the three-second mark, the null objects will stay still. Now move to the second cocktail and examine how the shapes change as it becomes the third. The Boulevardier-to-Negroni change is an ingredient change. Keep the null object’s position and rotation settings, and also change the individual element’s size and color.

![3762 · U5 · L15 · 14:16](frames/U05L15-F1416.00.jpg)

On screen: "Opacity" / "50%" / "Null 3" / "Shape Layer 1" / "Null 4" / "02" / "Null 1" / "01" / "BG" [rest omitted]  
Shows: Overlapping cocktail shapes at the one-second point, with the reference artwork at reduced opacity.

![3762 · U5 · L15 · 16:25](frames/U05L15-F1625.00.jpg)

On screen: [none]  
Shows: The composition with the red, pink and green Negroni elements visible as separate shapes.

## Holding the color change

Anchor: 3762 · U5 · L15 · 17:13–20:29

As the elements move from the second cocktail to the third, the null object’s position and rotation keep changing.

![3762 · U5 · L15 · 17:45](frames/U05L15-F1745.00.jpg)

On screen: "Dry Martini" / "White Lady" / "Margarita" / "Forma:" [Shape] / "760 px" / "400 px" / "0 px" [rest omitted]  
Shows: Illustrator document with the cocktail artboards and color panel visible while a 760-by-400 shape is selected.

For the third element, work directly in layer 4. Add keyframes under Contents > Rectangle > Rectangle Path > Size and under the color fill. Turn the palette layer back on and sample the required reference color for the color keyframe. Change the size from 760 × 600 pixels to the size set in Illustrator, which is 400 pixels in this case. Turn the reference layer back on and add the third cocktail, the Negroni. Animate only the null object’s keyframes for its movement, adjusting them until the forms reach the Negroni’s final positions. Turn the reference off to check that the change into the next cocktail is continuous.

For the color change, avoid blending the two colors together, which would create new colors. Select the element’s color keyframe and press 1 to show it on the timeline. Move to the midpoint of the motion and bring the color-change keyframe forward. Select the two keyframes, right-click, and open Keyframe Interpolation. Set Temporal Interpolation (*interpolazione temporale*) to Hold. The color will then change instantly when it reaches the keyframe instead of changing linearly. This prevents new colors from appearing.

![3762 · U5 · L15 · 19:29](frames/U05L15-F1929.00.jpg)

On screen: "03_Negroni.jpg" [rest omitted]  
Shows: Negroni reference image behind the red, pink and violet animated shapes, with the relevant keyframes displayed.

![3762 · U5 · L15 · 20:21](frames/U05L15-F2021.00.jpg)

On screen: "Keyframe Interpolation" / "Temporal Interpolation" / "Hold" [rest omitted]  
Shows: Keyframe Interpolation dialog with Temporal Interpolation set to Hold, over the Negroni composition.

### Key points (derived)

- Keep the project organized into named compositions and asset folders before adding the animation.
- Use a null object for the main transitions, then animate individual shape properties for changes in size, color and shape.
- A Hold temporal interpolation switches color instantly and prevents intermediate colors from appearing.
