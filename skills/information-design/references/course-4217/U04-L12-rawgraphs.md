# Lesson 12 · RAWGraphs

Anchor: 4217 · U4 · L12 · 12:44 · https://www.domestika.org/en/courses/4217-creative-data-visualization-for-narrative-designs/units/15965-designing-the-visualization#course_lesson_50450

## Finding a chart and loading the table

Anchor: 4217 · U4 · L12 · 00:00–03:29

In this lesson, I use RAWGraphs, a free online tool, to design the first piece of the project. I often use it to build the skeleton, or macro structure, of a visualization. Its home page has a gallery of projects made with the tool. The Learn section has tutorials and explanations for using RAWGraphs and creating specific graphics, so I recommend exploring it.

To begin, upload the data or, preferably, copy and paste it directly. I select the first column of the main table, hold Shift, select the last column, copy the selection, and paste it into RAWGraphs. It recognizes the data as a table and displays each column title. Clear column names matter because they identify the dimensions you will map later. You can also set the thousand and decimal separators, edit the data, or reset it. At this point, the table is fine as it is.

Next, scroll down and choose a chart. RAWGraphs offers many options. Selecting a chart gives you a short description of how to use it and a link to a tutorial. Knowing what different graphics are best used for can help you decide, alongside the other resources discussed earlier in the course. Explore the choices and see which one fits your project. Start from what interests you; your first experiment does not need to use the same graphic as mine.

![4217 · U4 · L12 · 00:30](frames/U04L12-F0030.00.jpg)

On screen: "RAWGraphs / About / News / Support us / Learning / Resources / Use it now! / A free and open source tool for data visualization / Main Features / Open source / A wide range of charts / Your data is safe / Export and go anywhere" [rest omitted]  
Shows: RAWGraphs home page, a sample visualization, and four feature headings.

![4217 · U4 · L12 · 00:56](frames/U04L12-F0056.00.jpg)

On screen: "Topics / Getting started / Data / Mapping / Customize / Export / Charts and templates / How to update data and how to work with projects / How to map the dimensions of your data with the chart variables / What can you customize in RAWGraphs?" [rest omitted]  
Shows: The tutorial page, its topic menu, and tutorial cards for updating data, mapping dimensions, and customizing a chart.

![4217 · U4 · L12 · 01:14](frames/U04L12-F0114.00.jpg)

On screen: "RAWGraphs 2.0 beta / About / Learning / GitHub / Report issue / 1. Load your data / Paste your data / Upload your data / Try our data samples / SPARQL query / From URL / Open your project / Copy and paste your data from other applications or websites. You can use tabular (TSV, CSV, DSV) or JSON data." [rest omitted]  
Shows: The empty data input area with options to paste or upload a table, use sample data, query SPARQL, load from a URL, or open a project.

![4217 · U4 · L12 · 01:21](frames/U04L12-F0121.00.jpg)

On screen: "File / Edit / View / Insert / Format / Data / Tools / Extensions / Help / Country / Renewables (% su / Renewables per ca / World Regio / Population i" [rest omitted]  
Shows: The renewable-energy source table in Google Sheets, with its five column headers and country data.

![4217 · U4 · L12 · 01:59](frames/U04L12-F0159.00.jpg)

On screen: "1. Load your data / 2. Choose a chart / Alluvial Diagram / Correlations, proportions / Arc Diagram / Networks / Bar chart / Correlations / Multi-set bar chart / Stacked bar chart / Beeswarm plot / Box plot / Bubble chart / Bumpchart" [rest omitted]  
Shows: The chart-selection gallery beneath the loaded renewable-energy table.

## Choosing a chart and mapping the data

Anchor: 4217 · U4 · L12 · 03:29–05:30

For this project, I choose a linear dendrogram because it shows hierarchy: the regions first, then the countries within each region. The chart-selection page also lets you inspect other graphics. For example, a bubble chart has two axes; its available variables include an x-axis and a y-axis. The variable choices depend on the chart you select.

The mapping area has a Dimensions column, where the table's column names appear as green rectangles, and a Chart Variables area specific to the chosen graphic. In this dendrogram, the variables include hierarchy, size, and color. Drag a data column to the chart variable where you want it represented; RAWGraphs updates the graphic in real time. I map World Region as the first hierarchy and Country as the second, so countries appear within their regions.

Population could be mapped to size to create circles, but I will visualize population another way. This is still a useful possibility to see. The chart is mainly giving me the grouping structure I need.

![4217 · U4 · L12 · 03:45](frames/U04L12-F0345.00.jpg)

On screen: "Linear dendrogram / Hierarchies, proportions / It displays hierarchically structured data with a tree structure, where the root node is on the left and leaves are on the right. The size of nodes can be used to encode a further quantitative dimension within size and a categorical or numerical dimension with color." [rest omitted]  
Shows: Linear dendrogram selected in the chart gallery, with its preview and description.

![4217 · U4 · L12 · 03:52](frames/U04L12-F0352.00.jpg)

On screen: "3. Mapping / DIMENSIONS / Country / Renewables (% sub energy) 2020 / Renewables per capita (kWh) 2020 / World Region according to the World Ba... / Popolation in 2020 / CHART VARIABLES / Hierarchy / Size / Color / Label / 4. Customize / Required chart variables: you need to map Hierarchy" [rest omitted]  
Shows: The Dimensions column beside the Hierarchy, Size, Color, and Label chart-variable fields.

![4217 · U4 · L12 · 04:31](frames/U04L12-F0431.00.jpg)

On screen: "Bubble chart / The basic layout is a scatter plot, which allows to see correlations among two continuous dimensions. A further quantitative dimension is used as a quantitative or categorical dimension with color. / Code / Tutorial" [rest omitted]  
Shows: Bubble chart selected in the chart gallery, with its preview and description.

![4217 · U4 · L12 · 05:23](frames/U04L12-F0523.00.jpg)

On screen: "4. Customize / ARTBOARD / Width (px) 805 / Height (px) 600 / Background #FFFFFF / Margin (top) 10 / Margin (right) 150 / Margin (bottom) 10 / Margin (left) 10 / Show legend No / Legend width 200 / CHART / COLOR / LABELS" [rest omitted]  
Shows: The preview has region and country mapped to Hierarchy. The population field remains in the Dimensions column, Size is empty, and the leaf nodes are equal-size circles.

## Adjusting the chart and considering regional order

Anchor: 4217 · U4 · L12 · 05:30–08:40

You can customize the chart. In my case, a legend is not particularly helpful, but it becomes useful when you visualize another variable. For example, mapping World Region to color assigns a color to each region, and the legend explains the assignment. Chart settings also let you change values such as the maximum circle diameter and sort the nodes. Country should be the label so the reader can tell which item each branch represents.

After removing population from the size mapping and reducing the maximum diameter, the chart resembles the earlier rough sketch. I want the world regions to display horizontally, so I will rotate the graphic 90 degrees in Illustrator. I also want their order to reflect their geographic positions after rotation. From left to right, I plan for North America to appear first, then Latin America and the Caribbean, Europe and Central Asia, South Asia, and East Asia and the Pacific last. The reference screen shows regional maps from the World Bank and the World Health Organization.

![4217 · U4 · L12 · 06:22](frames/U04L12-F0622.00.jpg)

On screen: "Show legend / Yes / World Region according to the World Bank / East Asia and Pacific / Europe and Central Asia / Latin America and Caribbean / North America / South Asia" [rest omitted]  
Shows: The dendrogram preview with region colors and the corresponding legend.

![4217 · U4 · L12 · 06:31](frames/U04L12-F0631.00.jpg)

On screen: "4. Customize / ARTBOARD / Width (px) 800 / Height (px) 1000 / Background #FFFFFF / Margin (top) 10 / Margin (right) 150 / Margin (bottom) 10 / Margin (left) 10 / Show legend Yes / Legend width 200 / CHART / COLOR / LABELS / 1410929362.0" [rest omitted]  
Shows: The chart preview with the legend enabled and the ARTBOARD settings visible; the CHART, COLOR, and LABELS sections are collapsed.

![4217 · U4 · L12 · 07:11](frames/U04L12-F0711.00.jpg)

On screen: "4. Customize / ARTBOARD / Width (px) 800 / Height (px) 1000 / Background #FFFFFF / Margin (top) 10 / Margin (right) 150 / Margin (bottom) 10 / Margin (left) 10 / Show legend No / Legend width 200 / CHART / Max diameter 60 / Layout algorithm Tree / Sort nodes by Size (descending) / Size only leaf nodes Yes / COLOR / Label / Country / CSV (unique)" [rest omitted]  
Shows: The dendrogram with population removed from size and the maximum diameter set to 60, resembling the earlier sketch.

![4217 · U4 · L12 · 07:54](frames/U04L12-F0754.00.jpg)

On screen: "The World Bank / World Bank's published list of countries belonging to world regions, split into a total of seven regions. / World regions according to the World Bank / East Asia and Pacific / Europe and Central Asia / Latin America and Caribbean / Middle East and North Africa / North America / South Asia / Sub-Saharan Africa / World Health Organization / WHO's definition of the world's countries by continent / WHO Regions / WHO Member States are grouped into six regions." [rest omitted]  
Shows: Two regional reference maps, one labelled with the World Bank's regions and one with WHO regions.

## Reordering regions in the source data

Anchor: 4217 · U4 · L12 · 08:40–11:14

To control the order, I sort the nodes by name. Alphabetical order is not the order I want, so I use a simple trick: add a number before each region name in the source table. I number the regions in the order that will produce the desired left-to-right sequence after rotation: East Asia and the Pacific is 1, South Asia is 2, Europe and Central Asia is 3, Latin America and the Caribbean is 4, and North America is 5. I apply each prefix to every country in that region.

When I return to RAWGraphs and use Change data to paste the revised table, I keep the work already done. Reset would clear the chart choices as well as the data. The updated ordering puts East Asia and the Pacific first in the unrotated chart; after rotation, North America will be first, followed by Latin America and the Caribbean, Europe and Central Asia, South Asia, and East Asia and the Pacific. I will remove the numbers in Illustrator because they are only there to control the sorting.

![4217 · U4 · L12 · 10:01](frames/U04L12-F1001.00.jpg)

On screen: "3. Europe and Central Asia" [rest omitted]  
Shows: A source-table cell with the numeric prefix added to the Europe and Central Asia region label.

![4217 · U4 · L12 · 11:14](frames/U04L12-F1114.00.jpg)

On screen: "1. East Asia and Pacific / 2. South Asia / 3. Europe and Central Asia / 4. Latin America and Caribbean / 5. North America" [rest omitted]  
Shows: The updated dendrogram ordered by the numbered region labels, with countries listed under each region.

## Exporting the graphic

Anchor: 4217 · U4 · L12 · 11:14–12:44

This is all I need from RAWGraphs for this part of the project. The tool offers many other variables and options, but I use the parts that answer my specific need. I do not want to feel constrained by tools: of course, you have to know them, explore them, and learn what they can do. Then decide what you want to make and look for tools or small tricks that will help you make it.

When the graphic is ready, export it as a JPEG, PNG, or SVG. I need an SVG because I can bring it into Illustrator and edit it there. I download the file and will import the graphic into Illustrator in the next lesson.

![4217 · U4 · L12 · 12:28](frames/U04L12-F1228.00.jpg)

On screen: "5. Export / viz / .svg / Download" [rest omitted]  
Shows: The dendrogram above the export controls, with SVG selected as the file format.
