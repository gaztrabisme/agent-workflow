# Lesson 11 · Designing the Skeleton with RAWGraphs

Anchor: 2495 · U4 · L11 · 6:11 · https://www.domestika.org/en/courses/2495-data-visualization-and-information-design-create-a-visual-model/units/9252-visualizing-the-data#course_lesson_27071

## Loading the data and choosing a chart

Anchor: 2495 · U4 · L11 · 00:00–01:31

In this lesson, I’m going to show you how to use RAWGraphs, a free online tool for designing data visualizations. I use it fairly often for the main structure of my projects. You will find the link in the additional resources section. You can copy and paste data into its box, or explore the tool with its sample datasets. For my project, I want RAWGraphs to build the overall structure; I will create a custom visualization in Illustrator for the more expressive elements.

I select the 2019 data, because that is the year I will use in RAWGraphs, and copy the dataset. I select all with Command+A, copy with Command+C, and paste it into the tool. The data is already organized. Scrolling down, I can choose the visual model. There are many options, and I can explore them with sample data to try different representations. For this project I choose a bubble chart.

![2495 · U4 · L11 · 00:32](frames/U04L11-F0032.00.jpg)

On screen: "RAWGraphs" / "The missing link between spreadsheets and data visualization." [rest omitted]  
Shows: RAWGraphs home page with its tagline and start button.

![2495 · U4 · L11 · 00:55](frames/U04L11-F0055.00.jpg)

On screen: "Country" / "Year" / "Per capita C..." [rest omitted]  
Shows: Spreadsheet with all years from 2000 through 2019 displayed and cell A2 (“Australia”) selected.

![2495 · U4 · L11 · 01:20](frames/U04L11-F0120.00.jpg)

On screen: "2. Choose a chart" / "Bubble chart" [rest omitted]  
Shows: RAWGraphs chart chooser with the Bubble chart option among other chart types.

## Mapping variables and handling the data gap

Anchor: 2495 · U4 · L11 · 01:31–02:46

This is the section where I create the graphic. RAWGraphs shows the titles of all the columns, which is why every column needs a clear, correct title before I use it. I drag columns into the chart variables. Population goes on the X axis, GDP on the vertical axis, and country becomes the label so I can identify which country each circle represents.

The graph is hard to read because the United States is far from the other countries in the data. One option would be to break the axis and clearly explain the gap, but I do not like that solution. Population and GDP are contextual data here, not the main information I want to convey; I only need them to plot countries in the space. To get a cleaner layout, I will order the countries by population and GDP. I will show only their order on the axes, not the actual values.

![2495 · U4 · L11 · 02:22](frames/U04L11-F0222.00.jpg)

On screen: "RAWGraphs 2.0 beta" / "4. Customize" / "GDP (2019, current US$)" / "Population (2019, Thousands)" / "Country" [rest omitted]  
Shows: Bubble chart using actual 2019 GDP and population values, with the United States separated from the cluster of other countries.

## Adding ordinal columns for the axes

Anchor: 2495 · U4 · L11 · 02:46–04:21

I go back to the spreadsheet, make a new tab by duplicating the existing one, and call it “For-RAWGraphs.” I add two columns: population order and GDP order. First I remove the filters, then recreate them and select 2019 again. I sort the countries by population; with them in order, I write numbers from 1 to 20. I do the same for GDP, sorting in ascending order and entering numbers from 1 to 20.

I select and copy the whole table, return to RAWGraphs, reset the data, and paste in the new table. I choose the bubble chart again and drag population order to the horizontal axis and GDP order to the vertical axis. Now the countries are much better organized and the visualization is cleaner and more readable. I make country the label. The numbers from 1 to 20 place the countries in the right order along the axes. I will delete these numbers in Illustrator, because I do not need them in the finished graphic. Instead, I will add the actual population and GDP figures there: they are not being visualized on these axes, but I still want to show the correct numerical information.

![2495 · U4 · L11 · 03:54](frames/U04L11-F0354.00.jpg)

On screen: "Country" / "Year" / "Population-o" / "GDP-order" [rest omitted]  
Shows: Filtered spreadsheet with population and GDP rank columns filled from 1 through 20.

![2495 · U4 · L11 · 04:16](frames/U04L11-F0416.00.jpg)

On screen: "GDP-order" / "Population-order" [rest omitted]  
Shows: Bubble chart arranged on ordinal axes from 0 to 20, without country labels yet.

## Sizing and exporting the bubble chart

Anchor: 2495 · U4 · L11 · 04:21–06:11

There is one last thing I want to do in RAWGraphs: add the annual CO₂ emissions data to the circles. The circles resize. I can change the settings to make them visible enough, including increasing their maximum radius. I also change the artwork size and switch on Show legend. The legend is not included in the view here, but I will be able to see it after exporting the file and working on it in Illustrator.

Finally, I export the graphic as an SVG. I could also export it as a PNG or JPEG, but SVG is useful because I will be able to edit it in Illustrator. I download the file. Now that the main structure is ready, I will open and edit it in Illustrator in the next lesson.

![2495 · U4 · L11 · 05:20](frames/U04L11-F0520.00.jpg)

On screen: "GDP-order" / "Population-order" [rest omitted]  
Shows: Ordered bubble chart with country names as labels and circles sized by annual emissions.

![2495 · U4 · L11 · 05:44](frames/U04L11-F0544.00.jpg)

On screen: "Show legend" / "Yes" / "Max radius (px)" / "70" / "emissions-structure" / ".svg" / "Download" [rest omitted]  
Shows: Configured chart and export controls with the legend enabled and maximum circle radius set to 70 pixels.

![2495 · U4 · L11 · 05:58](frames/U04L11-F0558.00.jpg)

On screen: "emissions-struct...svg" [rest omitted]  
Shows: Downloaded SVG filename in the browser download bar beneath the configured RAWGraphs chart.
