# Lesson 08 · Knowing Your Data

Anchor: 3601 · U3 · L08 · 15:14 · https://www.domestika.org/en/courses/3601-information-design-storytelling-with-data-in-illustrator/units/14537-working-with-data#course_lesson_45518

## Ask questions about the data

Anchor: 3601 · U3 · L08 · 00:00–00:47

It is time to investigate the statistics and look for stories hidden in the numbers. Design starts in how we format the table and uncover insights. My approach is to ask questions: who, what, where, when, and how much. Statistics often describe behavior or trends among individuals, so begin with: who is this about, and who are we describing?

## Choose the people and measure

Anchor: 3601 · U3 · L08 · 00:47–02:24

This dataset gives the percentage of a country’s population with access to drinking water. Add a percent sign to the categories during cleaning to prevent confusion later. You could convert percentages to absolute numbers, but keeping the ratio supports comparison between countries of different sizes: we are asking, out of 100 people, how many have access to clean water? Another option is to measure the percentage without access. When using percentages, the total should be 100%. Here the categories do not total 100%: summing them gives 111 for one year and 112 for the next. I know this quickly by selecting the cells and reading the preview box at the bottom right. The reason is that “at least basic” includes “safely managed.” To create a basic metric that excludes safely managed, insert a column and subtract the safely managed value from at least basic.

![3601 · U3 · L08 · 01:44](frames/U03L08-F0144.00.jpg)

On screen: “/ Valentina D'Efilippo” / “Who” / “% of national population” / “ASK: who is your data about? Do you have absolute numbers or percentages?” / “Data shows the share of people across the world that have access to safe drinking water. An alternative approach would be to show the number of people across the world that do not have access to safe drinking water.” [rest omitted]  
Shows: The “Who” slide and an example table of country percentages for safely managed and other water-service categories.

![3601 · U3 · L08 · 02:13](frames/U03L08-F0213.00.jpg)

On screen: “Domestika_JMP_Water_2021” / “At least basic %” / “Safely managed %” / “Limited (more than 30 mins) %” / “Unimproved %” / “Surface water %” / “Sum: 111” [rest omitted]  
Shows: The water-category cells selected for Afghanistan, with the status bar showing a sum of 111.

## Make a basic metric and define what the data means

Anchor: 3601 · U3 · L08 · 02:24–04:35

I know this because I have been reading the methodology on the website. In a spreadsheet, enter an equals sign to start a formula. For example, 2 + 4 returns a result when you press Enter. You can copy a result across blank cells, but in this case use cell references instead of fixed numbers: click one cell, type a minus sign, then click the other. A cell is identified by its column letter and row number. Press Enter to confirm, then drag the fill handle or double-click its small square to copy the formula down. The resulting column is basic access excluding safely managed; copy the formatting from the BASIC column.

![3601 · U3 · L08 · 03:33](frames/U03L08-F0333.00.jpg)

On screen: “Domestika_JMP_Water_2021” / “At least basic %” / “Basic (excluding” [rest omitted]  
Shows: A new column for the basic-water percentage that excludes safely managed service.

The next question is what the data is about: which dimensions are primary, which are secondary, and whether you need more contextual information from elsewhere. Here, safely managed is the best answer to my original question. The source’s methodology and analysis explain that experts use different definitions of clean water. Safely managed describes access at home, on premises, when needed, and free from contamination.

![3601 · U3 · L08 · 04:11](frames/U03L08-F0411.00.jpg)

On screen: “What” / “Drinking water ladder” / “ASK: what is the key metric and what are the secondary dimensions? And is there any other dimensions you wish to add to your dataset that can provide context or better answer your investigative question?” / “In this scenario, Safely Managed is the category that best answers my initial question: who has access to clean drinking water?” [rest omitted]  
Shows: The “What” slide, drinking-water ladder and safely managed category.

## Compare years and build a pivot table

Anchor: 3601 · U3 · L08 · 04:35–07:26

The next question is when. A time dimension might be weeks or months; here the data is organized by year, from 2000 to 2020, covering two decades. With a timeline, you can study change over time. Decide whether to use every year or compare selected points such as 2000 and 2020.

A pivot table is a tool I use often to aggregate and disaggregate categories, calculate sums, averages, totals and other values, and rebuild a table in a different structure. To put years side by side, select the whole dataset using its corner, then choose Insert > Pivot table. It creates a new sheet, a blank canvas where you map headers into rows and columns. Put countries in Rows and years in Columns. Keep all years or add a filter to select only 2000 and 2020. Remove the grand total because it is not relevant here, and add safely managed under Values. This is a useful exercise because it immediately helps me identify gaps and whether data is available. When zeros appear, I add another filter and deselect blanks to find the gaps. Croatia has data for 2000 but no value for 2020; other countries have present-year data but no past value. For each gap, find the closest available data point and note it.

![3601 · U3 · L08 · 04:41](frames/U03L08-F0441.00.jpg)

On screen: “When” / “2000–2020” / “Entity” / “2000” / “2020” / “Afghanistan” / “Create a Pivot Table and note any missing data” [rest omitted]  
Shows: The “When” slide with a two-year comparison and a pivot-table example.

![3601 · U3 · L08 · 06:07](frames/U03L08-F0607.00.jpg)

On screen: “Pivot table editor” / “Rows” / “Columns” / “Values” / “Filters” [rest omitted]  
Shows: A new blank pivot table and its field editor.

![3601 · U3 · L08 · 06:31](frames/U03L08-F0631.00.jpg)

On screen: “COUNTRY, AREA OR TERRITORY” / “Year” / “2000” / “2020” / “Safely managed, %” / “Pivot table editor” / “Rows” / “Columns” / “Values” / “Filters” [rest omitted]  
Shows: The pivot table with countries in rows and 2000 and 2020 in columns; its Values section is still empty.

![3601 · U3 · L08 · 07:17](frames/U03L08-F0717.00.jpg)

On screen: “Croatia” / “82” [rest omitted]  
Shows: A pivot table row with a value for 2000 and a blank value for 2020.

## Investigate missing values and choose geographic groups

Anchor: 3601 · U3 · L08 · 07:26–10:06

I have copied the pivot table into another spreadsheet behind the scenes to make this faster. Filter the 2000 column for blanks, research each gap, enter the closest available values, and add a column recording the year for each value. When you remove the filter, you can see which entries were filled; for example, one value belongs to 2001, not 2000.

I chose to include countries with missing 2000 data, using the closest available year so countries such as the United States are not omitted. I left out countries with 2000 data but no latest-year data because missing data is part of the story. The analysis covers 138 countries, while almost 100 countries have no data; Our World in Data visualizes this coverage on a map. Consider both the data you have and the data that is missing. A geographic tag may be a postcode, city, or country, and countries can be grouped into regions. The regional dataset offers different segmentations, but I am not satisfied with them because of gaps and difficulty organizing the countries. The infographic is part of a larger publication where geographic tagging and language should stay consistent, so I simplify the tagging to five geographic continents: Africa, the Americas, Asia, Europe, and Oceania. Add a column for this new grouping.

![3601 · U3 · L08 · 08:01](frames/U03L08-F0801.00.jpg)

On screen: “Continents” / “Income levels” / “COUNTRY, AREA OR TERRITORY” / “Safely managed, (%) 2000” / “Safely managed, (%) 2020” / “Notes: missing data for SM 2020, Earliest available year” [rest omitted]  
Shows: The cleaned table and the list of countries whose earliest available values fill gaps.

![3601 · U3 · L08 · 09:23](frames/U03L08-F0923.00.jpg)

On screen: “Where” / “138 countries” / “ASK: Does your data include information about geographies (postcode, city, country, etc) and how do these compare?” / “It is important to note the dataset’s limitations: almost 100 countries have no data” [rest omitted]  
Shows: A world map of safely managed drinking-water coverage and a note about missing country data.

![3601 · U3 · L08 · 09:53](frames/U03L08-F0953.00.jpg)

On screen: “Various methods to tag the countries by regions are offered in the primary source” / “I decided to simplify the regions to the main geographical continents: Africa, Americas, Asia, Europe, Oceania” [rest omitted]  
Shows: Alternative regional groupings, a cleaned country table and the five-continent grouping.

## Compare coverage, income and change over time

Anchor: 3601 · U3 · L08 · 10:06–14:14

The last question is how much, how long, or how far. Investigate the smallest and largest values, whether they change, notable characteristics, and outliers. Visualizing the data is the best way to find these insights. You can make simple bar or line charts in Google Sheets, or inspect the source dashboard’s existing visualizations. Globally, access has progressed to 74%, meaning three-quarters of the population has drinking water. Another way to tell the story is the remaining gap: one in four people still lacks safe drinking water.

Progress differs by region and income group. Countries perform very differently: compare low-income and high-income countries, or Sub-Saharan Africa and North America. Keep region in the dataset, and also include income group because wealth matters. The dataset has region but not income group, so combine a list of countries and income groups from the dashboard with the existing data. Doing this manually would take a long time and introduce human error. Automate it with a formula, even for a short list, to reduce mistakes. Look up a term in another list and return its associated result in an empty cell. You can use VLOOKUP or INDEX and MATCH; the principle is similar, but one is a nested formula and the other is a function. Learn more about both and choose what fits the analysis. I use these tools every day when analyzing data.

![3601 · U3 · L08 · 10:23](frames/U03L08-F1023.00.jpg)

On screen: “How much access and progress” / “Household data - World - Service Levels” / “2020, Drinking Water / Safely managed: 74.27” / “1 in 4 people do not have access to safe drinking water” [rest omitted]  
Shows: A dashboard bar chart rising from 2000 to 2020, with the 2020 value highlighted.

![3601 · U3 · L08 · 11:23](frames/U03L08-F1123.00.jpg)

On screen: “Regions” / “Income” / “North America” / “Sub-Saharan Africa” / “High income” / “Low income” [rest omitted]  
Shows: Side-by-side charts for service levels across regions and income groups.

![3601 · U3 · L08 · 11:53](frames/U03L08-F1153.00.jpg)

On screen: “How to insert the income string?” / “Income Group” / “Income level” [rest omitted]  
Shows: A country income-group list connected to an empty income-level column in the water dataset.

![3601 · U3 · L08 · 12:23](frames/U03L08-F1223.00.jpg)

On screen: “INDEX & MATCH” / “=INDEX('Income Index'!$B$2:$B$296, MATCH(A2, 'Income Index'!$A$2:$A$296,0))” / “Alternatively, use Index & Match formula to return the income level from a different sheet” [rest omitted]  
Shows: The INDEX and MATCH formula with notes identifying its lookup and return ranges.

We also have two points in time, 2000 and 2020, and should understand the ratio of change. Add columns and formulas to calculate absolute or relative change. Absolute change is the latest point minus the original point: 2020 minus 2000. It gives the difference between those two points. Togo went from 10% to 20%, an increase of 10 percentage points. Iceland went from 90% to 100%, also a 10-point increase. The relative story changes when you put that difference in the context of each country’s starting point. Togo doubled, a 100% increase. Calculate relative change by dividing the absolute difference by the starting point and multiplying by 100. Relative change expresses the absolute difference in relation to the initial value.

![3601 · U3 · L08 · 13:02](frames/U03L08-F1302.00.jpg)

On screen: “Calculate Absolute and Relative Change” / “COUNTRY” / “2000” / “2020” / “Absolute” / “Relative” / “10” / “20” / “10” / “100%” [rest omitted]  
Shows: A one-row example of the two change calculations.

![3601 · U3 · L08 · 13:42](frames/U03L08-F1342.00.jpg)

On screen: “Absolute change measures the exact numerical change between two periods” / “= 2020 - 2000” / “10 points increase” / “Iceland” / “Togo” [rest omitted]  
Shows: The same 10-point absolute increase for Iceland and Togo, with different starting values.

![3601 · U3 · L08 · 14:12](frames/U03L08-F1412.00.jpg)

On screen: “Relative change measures the change relative to the starting point.” / “(2020 - 2000) / 2000 × 100” / “10% increase” / “100% increase” [rest omitted]  
Shows: A comparison where the 10-point changes become different relative increases.

## Keep the analysis organized

Anchor: 3601 · U3 · L08 · 14:14–15:14

We have covered a lot, so keep track of the work. Add a table of contents at the beginning of the dataset with annotations and notes, name every tab appropriately, and keep the work and analysis organized and clean. These materials are available to download. This lesson became technical, but it helps break the ice with data. If this is your first time working with a spreadsheet, start with a smaller dataset. If you are using the same clean-water topic, you could focus on the global statistics or regional geographic distribution, or use personal data. In the next lesson, we will start turning the data into visuals.

![3601 · U3 · L08 · 14:23](frames/U03L08-F1423.00.jpg)

On screen: “Keep it clean!” / “Keep a record of your analysis and organise your data by adding a table of content” [rest omitted]  
Shows: A table-of-contents sheet with source links, notes, and dataset tabs.
