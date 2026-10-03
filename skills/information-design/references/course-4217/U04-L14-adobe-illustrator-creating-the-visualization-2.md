# Lesson 14 · Adobe Illustrator: Creating the Visualization 2

Anchor: 4217 · U4 · L14 · 15:33 · https://www.domestika.org/en/courses/4217-creative-data-visualization-for-narrative-designs/units/15965-designing-the-visualization#course_lesson_50490

## Building a reusable leaf from a curve

Anchor: 4217 · U4 · L14 · 00:00–03:29

I have drawn a curve that I am satisfied with. I will use it to make a shape that recalls the leaves I looked at in the previous lesson. I like these examples because they are made of many dense lines. I want to create something similar.

In Illustrator, I go to Effect > Distort & Transform > Transform. This effect can create different shapes from a first shape; one way I use it is to create repeated forms from a single line. I want one leaf made of 100 lines. The Transform dialog shows 99 copies in addition to the original line (captions: “90 copies”). At first, the copies sit on top of one another, so they look like one line. I change the angle to separate them, then adjust the angle's anchor point until the curves start to form a leaf. I experiment with the controls until the shape is close to the reference. This is my usual process for a custom shape: know the tools, explore them, and see how they can produce the form I want.

When I am satisfied, I apply the effect. The result is not yet a normal vector object. I duplicate it, choose Object > Expand Appearance, and ungroup it. Now it is a regular vector element made of 100 separate curves, which I can edit individually.

![4217 · U4 · L14 · 00:21](frames/U04L14-F0021.00.jpg)

On screen: "Illustrator / File / Edit / Object / Type / Select / Effect / View / Window / Help / Layers / graphic / background" [rest omitted]  
Shows: A single curved line on the artboard beneath the cropped lower ends of bars from the existing visualization.

![4217 · U4 · L14 · 00:27](frames/U04L14-F0027.00.jpg)

On screen: "Business / Create / Analytics / Ads / Diagrams / 18 Pins" [rest omitted]  
Shows: The Pinterest diagram board, with botanical plates, leaf studies, and other reference images.

![4217 · U4 · L14 · 00:37](frames/U04L14-F0037.00.jpg)

On screen: "Comments / More like this" [rest omitted]  
Shows: A close view of the selected ginkgo-leaf reference and a row of related leaf images.

![4217 · U4 · L14 · 02:11](frames/U04L14-F0211.00.jpg)

On screen: "Transform Effect / Horizontal 100% / Vertical 100% / Move Horizontal 0 pt / Move Vertical 0 pt / Angle 1° / Copies 99 / Preview / Cancel / OK" [rest omitted]  
Shows: The Transform Effect dialog repeating the selected line; the new curves begin to fan out into a leaf form.

![4217 · U4 · L14 · 03:27](frames/U04L14-F0327.00.jpg)

On screen: [none]  
Shows: The completed fan-shaped leaf, composed of many separate curved lines.

## Turning per-capita values into line counts

Anchor: 4217 · U4 · L14 · 03:29–06:15

The question is how to use this shape to show per-capita data. I return to the table and simplify the displayed numbers by decreasing the decimal places. This makes values such as 29, 7.2, and 3.6 easier to read. The values are relatively small. I do not want to represent Canada with 29 lines; I want to use a higher line count to show the granularity and make the differences easier to see.

I add a column to calculate how many lines each value will need. I call it “Lines calculations - per capita.” In Google Sheets, Excel, or Numbers, I enter a formula that multiplies the per-capita value by 10. The calculation turns 29.1 into about 291 lines, 7.2 into about 72, and 3.6 into about 36. I use the suggested fill control to copy the calculation down the remaining rows, then simplify the calculated numbers as well. It is a straightforward calculation, but I prefer to keep each step in the table.

![4217 · U4 · L14 · 06:03](frames/U04L14-F0603.00.jpg)

On screen: "Renewable energy / File / Edit / View / Insert / Format / Data / Tools / Extensions / Help / Country / Renewables (% su / Renewables per c / Lines calculations - per ca / World Region according to / Population i / =C2*10 / Canada / 29.1 / 291 / Brazil / 7.2 / 72 / Ecuador / 3.6 / 36" [rest omitted]  
Shows: The source table with the new line-count column filled by the formula `=C2*10`.

## Preparing the leaf units and visual guide

Anchor: 4217 · U4 · L14 · 06:15–09:33

Now I bring the data into Illustrator. I make the leaf smaller because each instance will take less space in the visualization, and reduce the line thickness. To avoid counting paths by hand, I use Window > Document Info. This panel displays information about the document. In its menu, I choose Objects; when I select a shape, it reports how many paths it contains. My leaf has 100 paths, which makes the panel a quick way to count the lines I am using.

I will build larger forms by combining leaves. If I need 200 lines, for example, I can use multiple leaves instead of counting every path manually. I duplicate a leaf with Option, reflect the copy vertically, and overlap the two. Then I add a visual cue: every tenth line should be thicker. The thicker lines help readers estimate the scale of the value. I use Document Info to count as I add these markers—10, 20, 30, and so on—and repeat the treatment for each leaf.

![4217 · U4 · L14 · 08:16](frames/U04L14-F0816.00.jpg)

On screen: "Document Info / Paths: 100 (100 open, 0 closed, 200 points)" [rest omitted]  
Shows: The lower leaf unit selected and the Document Info panel reporting 100 paths; the upper leaf is not selected.

![4217 · U4 · L14 · 09:30](frames/U04L14-F0930.00.jpg)

On screen: "Document Info / Paths: NONE" [rest omitted]  
Shows: A finished dense leaf form with heavier lines at intervals and the Document Info panel open.

## Creating a maximum shape for the largest value

Anchor: 4217 · U4 · L14 · 09:33–12:12

With the leaf ready, I create the maximum shape: the form for the country with the largest value. I sort the calculated line-count column in descending order. Iceland is first, with a value around 1,400, so the maximum shape needs about 1,400 lines. I duplicate the leaf units with Option, reflect and overlap them, and alternate their positions to build the larger form. I count the paths as I go; one intermediate version contains 800 lines, and I continue until I reach the maximum.

I keep the maximum shape as a reusable master and leave it somewhere on the artboard. I will need it to make the other countries' shapes by deleting whatever lines are not needed. I make copies with Option-drag or with Command-C and Command-V, and group the master shape.

![4217 · U4 · L14 · 09:57](frames/U04L14-F0957.00.jpg)

On screen: "Sort A → Z / Sort Z → A / Sort by color / Filter by color / Filter by condition / Filter by values" [rest omitted]  
Shows: The calculated line-count column's sort menu open before ordering the values from largest to smallest.

![4217 · U4 · L14 · 11:27](frames/U04L14-F1127.00.jpg)

On screen: "Document Info / Paths: 1400" [rest omitted]  
Shows: The completed maximum leaf form, built from repeated leaf units, with 1,400 paths counted in Document Info.

## Placing and trimming the shapes for each country

Anchor: 4217 · U4 · L14 · 12:12–15:33

I return the table to its original order and begin with Canada, whose calculated target is 291 lines. I place the grouped shapes in the country's position. Some overlap is acceptable if the data remains readable; I can refine it later. I select the extra lines and delete them until the shape matches the target. The Document Info panel lets me check the count, and the first country is done.

This process takes time, as much of my static-visualization work does, but I sometimes enjoy the repetitive part and listen to music or podcasts while I work. For the next country, I use about 72 lines (captions: “72, 2”), then move to the following value, 36. I check that each country is the right one. Keeping the data and Illustrator visible side by side makes it quicker to compare the row and the shape. The guide lines also help me estimate how many curves to remove. I repeat the process for all the countries.

![4217 · U4 · L14 · 13:26](frames/U04L14-F1326.00.jpg)

On screen: "Paths: 291" [rest omitted]  
Shows: The first country's selected leaf shape beside the vertical guide marks, with 291 paths in the Document Info panel.

![4217 · U4 · L14 · 14:44](frames/U04L14-F1444.00.jpg)

On screen: "Paths: 72" [rest omitted]  
Shows: The next, smaller leaf shape selected beside the completed first-country form; the panel counts 72 paths.

![4217 · U4 · L14 · 15:24](frames/U04L14-F1524.00.jpg)

On screen: "Paths: 36" [rest omitted]  
Shows: A 36-path leaf shape selected beside the larger country forms, with the reference guides still visible.
