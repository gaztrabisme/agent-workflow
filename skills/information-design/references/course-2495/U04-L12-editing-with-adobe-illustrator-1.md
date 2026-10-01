# Lesson 12 · Editing with Adobe Illustrator 1

Anchor: 2495 · U4 · L12 · 9:35 · https://www.domestika.org/en/courses/2495-data-visualization-and-information-design-create-a-visual-model/units/9252-visualizing-the-data#course_lesson_27072

## Preparing the Illustrator file

Anchor: 2495 · U4 · L12 · 00:00–01:51

In this lesson, I’m going to use Adobe Illustrator to edit our graphic and add more layers of information. This is the Illustrator template from the attachments. It already has three layers: the background, the visualization, and the layer for the legend and explanatory text. I lock the background because I do not need to change it. The visualization layer is where I will put the design we made in RAWGraphs.

I import the SVG onto the visualization layer. It is a vector file, so I can ungroup it several times using Object > Ungroup and edit its shapes, colors, and fonts. The legend is visible now. Headlines and a grid will also be added, but I will work on those aspects later. For now, I want Illustrator to help me visualize the main information: per-capita CO₂ emissions. We have 20 years for each country.

I go back to Pinterest and copy the images I found so they are available as references beside the chart. I decide that each year will be represented by a curved line, and I want to design that line.

![2495 · U4 · L12 · 00:44](frames/U04L12-F0044.00.jpg)

On screen: "legend-an..." / "visualization" / "background" [rest omitted]  
Shows: Blank Illustrator artboard and the template's three layers.

![2495 · U4 · L12 · 00:49](frames/U04L12-F0049.00.jpg)

On screen: "emissions-structure.svg" [rest omitted]  
Shows: Illustrator's import dialog with the exported SVG selected.

![2495 · U4 · L12 · 01:50](frames/U04L12-F0150.00.jpg)

On screen: "GDP-order" / "Annual CO2 emissions (2019)" / "Population-order" / "Australia" / "Austria" / "Belgium" / "Canada" / "Czechia" / "Germany" / "Iran" / "Japan" / "Kazakhstan" / "Malaysia" / "Netherlands" / "Norway" / "Poland" / "Russia" / "Saudi Arabia" / "South Africa" / "South Korea" / "Turkmenistan" / "United Arab Emirates" / "United States" [rest omitted]  
Shows: Pinterest reference images placed beside the imported bubble chart on the Illustrator pasteboard.

## Drawing and repeating the yearly curve

Anchor: 2495 · U4 · L12 · 01:51–03:17

I use the pencil tool to draw a few possible curves. If I am not satisfied with a shape, I can go to Object > Path > Simplify to simplify it. I am satisfied with this one. It will represent one year.

To make the 20 years for a country, I select the curve and press R on the keyboard, or choose the Rotate tool. I click to set the anchor point, then hold Option to duplicate the curve as I drag it. I use Object > Transform > Transform Again, or Command+D, to repeat the previous action. Repeating it gives me 20 lines quickly. Each line is one year; the group of lines represents one country.

I will resize the lines according to the actual per-capita CO₂ emissions numbers. I will not do that manually; I want to use Illustrator tools to represent the numbers accurately.

![2495 · U4 · L12 · 02:33](frames/U04L12-F0233.00.jpg)

On screen: [none]  
Shows: One curved path selected above three drawn curve options on the Illustrator pasteboard.

![2495 · U4 · L12 · 03:12](frames/U04L12-F0312.00.jpg)

On screen: [none]  
Shows: A fan-shaped group of pink curves radiating from a single anchor point.

## Using Illustrator's chart tools

Anchor: 2495 · U4 · L12 · 03:17–04:22

Illustrator can also create charts. Here is a bar chart I will not use, but I want to show how this feature works. I draw the chart, then either copy and paste the numbers or type them into its data table. I enter some example values and press the check mark to generate the graphic.

At this point the chart is not a normal vector file: I can select it, open its data, change or add numbers, and the graphic changes too. To turn it into a normal vector element, I choose Object > Ungroup. Illustrator asks me to confirm because after ungrouping I will no longer be able to change the chart data. I confirm, ungroup it a few more times, and can then work on it as a regular vector file. I am showing that this tool exists, but I will use another one.

![2495 · U4 · L12 · 03:45](frames/U04L12-F0345.00.jpg)

On screen: "10.00" / "20.00" / "30.00" / "45.00" [rest omitted]  
Shows: Example column chart and its open data table.

![2495 · U4 · L12 · 04:13](frames/U04L12-F0413.00.jpg)

On screen: "0" / "10" / "20" / "30" / "40" / "50" [rest omitted]  
Shows: Selected column chart after its data table has been closed.

## Establishing a fixed range for the radar graph

Anchor: 2495 · U4 · L12 · 04:22–05:31

The three dots in the toolbar open tools that are not in Illustrator's standard view. I drag the Radar Graph tool into the toolbar so I can use it. To demonstrate, I type some random numbers, and Illustrator displays them as a radar graph. I will use this chart structure as the basis for calculating the correct lengths of my curves from the actual data.

I double-click the Radar Graph tool and open Value Axis. There I can set a minimum and a maximum. The example currently has a minimum of 0 and a maximum of 80. This matters because I will paste different values into the graph, but I want the minimum and maximum to stay the same. That keeps the grid and its reference points consistent. First I need to find the minimum and maximum values in the data I am going to use.

![2495 · U4 · L12 · 04:42](frames/U04L12-F0442.00.jpg)

On screen: "23.00" / "54.00" / "32.00" / "65.00" / "77.00" / "44.00" [rest omitted]  
Shows: Example radar graph with its data table open.

![2495 · U4 · L12 · 05:11](frames/U04L12-F0511.00.jpg)

On screen: "Min: 0" / "Max: 80" / "Divisions: 8" [rest omitted]  
Shows: Radar Graph Type dialog with its value-axis range settings.

## Preparing the data and shaping it as a semicircle

Anchor: 2495 · U4 · L12 · 05:31–07:47

I duplicate the dataset sheet and call the copy “For-Illustrator.” I like to keep separate versions of the dataset at different stages so I can return to an earlier one if needed. I select all the years and sort the per-capita CO₂ emissions. The minimum is 7 and the maximum is 35. I leave the graph minimum at 0 and use a simplified maximum of 40. That works well, and I can delete the example graph.

I sort my data by year and then by country. Now I have every country, with its data ordered by year from 2000 to 2019, which is the order I want. I select and copy the values, return to Illustrator, draw my graph, and press Command+V. The values are now visualized, and the minimum and maximum are the ones I want.

The values are arranged on a circle, but I want them on a semicircle because that makes comparison among years easier. I add empty values—in this case, 15 zeros—and confirm. The data are no longer arranged in a full circle; they form the semi-radial shape I want to use as a reference for resizing all the lines correctly. I adjust the shape, then use it as the basis for resizing each line. I will do that process later.

![2495 · U4 · L12 · 06:04](frames/U04L12-F0604.00.jpg)

On screen: "35.669453" / "Country" / "Year" / "Per capita C..." [rest omitted]  
Shows: Spreadsheet sorted through the per-capita emissions values, with a cell containing 35.669453 selected.

![2495 · U4 · L12 · 06:11](frames/U04L12-F0611.00.jpg)

On screen: "Min: 0" / "Max: 40" / "Divisions: 8" [rest omitted]  
Shows: Radar Graph Type dialog after the maximum is changed to 40.

![2495 · U4 · L12 · 06:50](frames/U04L12-F0650.00.jpg)

On screen: "18.4401" / "18.44" / "18.63" / "18.67" / "18.84" / "19.28" / "19.15" [rest omitted]  
Shows: Radar graph data table after the per-capita emissions values have been pasted.

![2495 · U4 · L12 · 07:45](frames/U04L12-F0745.00.jpg)

On screen: "30" / "20" / "10" [rest omitted]  
Shows: Pink yearly curves overlaid on a black radial reference graph.

## Repeating the process for each country

Anchor: 2495 · U4 · L12 · 07:47–09:35

First I want to visualize the data for all the countries, and I usually work on these outside the artboard. I can create a new layer for them and call it “in-progress.” I prefer to keep the different stages so I can go back to an earlier one if a change is needed and make it without redoing everything.

We have already done Australia, but let’s do it again. The size does not need to be exact yet, because I can edit it later. I copy the graph and paste it outside the artboard, add the zero values, and copy the country name as a reference. Holding Option, I drag to duplicate it, then press Command+D to repeat that action 20 times.

For the next country, I copy the data, select the graph, open its data, and press Command+V. This changes the data while keeping the same grid and the empty values needed to make the shape. I will enter the country number and name, then repeat the process for all the countries.

![2495 · U4 · L12 · 08:31](frames/U04L12-F0831.00.jpg)

On screen: "in-progress" [rest omitted]  
Shows: Illustrator pasteboard with a new in-progress layer, a data table, and the artboard chart.

![2495 · U4 · L12 · 09:03](frames/U04L12-F0903.00.jpg)

On screen: [rest omitted]  
Shows: Four repeated circular country graphs arranged in a row, each labeled Australia.

![2495 · U4 · L12 · 09:21](frames/U04L12-F0921.00.jpg)

On screen: "8.19964" / "8.20" / "8.66" / "8.84" / "9.49" / "9.45" / "9.59" [rest omitted]  
Shows: Updated chart selected with its data table open, beside the repeated Australia charts.
