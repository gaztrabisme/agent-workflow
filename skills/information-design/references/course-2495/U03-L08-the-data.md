# Lesson 08 · The Data

Anchor: 2495 · U3 · L08 · 18:34 · https://www.domestika.org/en/courses/2495-data-visualization-and-information-design-create-a-visual-model/units/9251-setting-the-project-in-motion#course_lesson_27068

## Create a spreadsheet and import the first dataset

Anchor: 2495 · U3 · L08 · 00:00–01:11

I will use Google Sheets to work with the data. It is online and free, and it works well for datasets. I create a new file and rename it “CO2-Emissions.” Then I import the per-capita emissions dataset: open File, choose Import, and upload the file.

CSV (captions: “CSB”) means comma-separated values: the file is text, with commas separating the values. Google Sheets detects the separator automatically. I choose to import the data into the spreadsheet I already have rather than create another spreadsheet. Once imported, the values are divided into columns.

![2495 · U3 · L08 · 00:35](frames/U03L08-F0035.00.jpg)

On screen: “CO2-Emissions” [rest omitted]  
Shows: A new, empty Google Sheets spreadsheet.

![2495 · U3 · L08 · 00:45](frames/U03L08-F0045.00.jpg)

On screen: “Import file” / “co-emissions-per-capita.csv” / “Create new spreadsheet” / “Detect automatically” / “Convert text to numbers, dates, and formulas” / “Import data” [rest omitted]  
Shows: The import dialog for the per-capita emissions CSV.

![2495 · U3 · L08 · 01:08](frames/U03L08-F0108.00.jpg)

On screen: “Entity” / “Code” / “Year” / “Per capita CO2 emissions” [rest omitted]  
Shows: The imported dataset, with entity, code, year, and per-capita emissions columns.

## Keep the source data and clean a working copy

Anchor: 2495 · U3 · L08 · 01:11–02:27

The next step is to clean the dataset. I prefer to duplicate it into a new tab and rename that tab, so I can return to the original data whenever I need it. This dataset is already fairly clean, though that is not always the case. The additional resources include an article with useful advice for preparing and cleaning data for visualization.

A good dataset has no extra rows above its column headings: keep the headings and the data beneath them. Delete columns that are not needed. Here, I remove the code column and change “Entity” to “Country.” I make the headings bold and freeze the first row so it stays visible as I explore the data.

![2495 · U3 · L08 · 01:26](frames/U03L08-F0126.00.jpg)

On screen: “Duplicate” / “Rename” / “co-emissions-per-capita” [rest omitted]  
Shows: The original “co-emissions-per-capita” tab with its context menu open; “Duplicate” and “Rename” are available.

![2495 · U3 · L08 · 02:02](frames/U03L08-F0202.00.jpg)

On screen: [rest omitted]  
Shows: The Code column selected for removal from the cleaned working copy.

![2495 · U3 · L08 · 02:21](frames/U03L08-F0221.00.jpg)

On screen: “Freeze” / “No rows” / “1 row” / “2 rows” / “Up to current row (1)” [rest omitted]  
Shows: The View menu open to the freeze options, including the first row.

## Use filters to explore and choose an initial slice

Anchor: 2495 · U3 · L08 · 02:27–05:01

I use the filter tool a lot. I select the heading row and create a filter. The filter lets me sort (captions: “store”) the data, filter it, organize it, and look for stories worth telling. I can sort all rows in ascending order; the sort applies to the whole table. This is a helpful first step in selecting data.

Filters also help me see how many values a variable has. For example, I open the year filter to see the available years, clear the selections, and choose the most recent year, 2019. Now I am viewing only 2019. This is useful when I begin choosing what to show.

The visualization will be exploratory: I do not want to prove one particular point, but to give readers an overview that they can explore. A static visualization cannot show every value in a large dataset, so I first need criteria for selecting the data. I want the countries with the highest per-capita emissions in the most recent year, so I sort the countries in descending order. Then I add another criterion: include only countries with a population greater than 5 million. I will state this selection in the explanatory text and legend.

![2495 · U3 · L08 · 02:38](frames/U03L08-F0238.00.jpg)

On screen: [rest omitted]  
Shows: The filtered table with country, year, and per-capita emissions columns.

![2495 · U3 · L08 · 03:07](frames/U03L08-F0307.00.jpg)

On screen: [rest omitted]  
Shows: The table after the filter has sorted the data in ascending order.

![2495 · U3 · L08 · 03:39](frames/U03L08-F0339.00.jpg)

On screen: “Sort A → Z” / “Sort Z → A” / “Filter by values” / “2016” / “2017” / “2018” / “2019” [rest omitted]  
Shows: The year filter with 2019 selected.

![2495 · U3 · L08 · 04:37](frames/U03L08-F0437.00.jpg)

On screen: “Qatar” / “38.61042” / “New Caledonia” / “29.864318” [rest omitted]  
Shows: The 2019 per-capita emissions rows ordered from the highest values down.

## Combine the emissions ranking with population data

Anchor: 2495 · U3 · L08 · 05:01–08:58

For the population figures, the World Bank is another excellent source I use pretty often (the captions say “WordBack”). Its datasets can be browsed by country or by indicator; I browse by indicator and look for population. The indicator is called “Population, total.” The World Bank lets me explore these data as a chart and map, but I need the actual numbers. They are already listed by most recent year, so I copy the relevant values into my Google Sheet instead of downloading the dataset.

I split my screen so I can see both datasets. I have two tasks: check which countries in my emissions ranking have a population greater than 5 million, and add population figures for the countries I choose so I can use population as contextual information later. I add a Population column and extend the filter to include it by deselecting and reselecting the filters. Then I repeat the selection of the most recent year and check that the countries are still ordered by per-capita emissions.

To check each country against the population threshold, I use Command-F on the World Bank page. Its population values are in thousands. Qatar, for example, has 2,832.07 thousand people, below the 5-million threshold, so I leave it out. I continue checking the ranked countries. The United Arab Emirates has 9,770.53 thousand people, so it qualifies. I copy the population value into the sheet, making sure it is on the correct row. I continue this process until I have population values for the 20 countries in my selection.

![2495 · U3 · L08 · 05:37](frames/U03L08-F0537.00.jpg)

On screen: “All Countries and Economies” / “Country” / “Most Recent Year” / “Most Recent Value (Thousands)” [rest omitted]  
Shows: The World Bank’s country table with the latest population figures in thousands.

![2495 · U3 · L08 · 07:00](frames/U03L08-F0700.00.jpg)

On screen: “Population” / “qatar” / “Qatar” / “2019” / “2,832.07” [rest omitted]  
Shows: The search result for Qatar’s 2019 population beside the emissions sheet.

![2495 · U3 · L08 · 07:37](frames/U03L08-F0737.00.jpg)

On screen: “United Arab Emirates” / “9,770.53” [rest omitted]  
Shows: The World Bank result for the United Arab Emirates beside the country list.

## Select 20 countries and a 20-year span

Anchor: 2495 · U3 · L08 · 08:58–12:22

I select the 20 countries with the highest per-capita emissions among those with a population over 5 million. Twenty countries is a good number to visualize, though you can choose 10 if that is a better number for you to begin with. I am building this dataset manually, something I also do pretty often, because the information I want is not always available in one source; combining datasets by hand can be a useful way to get started.

The emissions dataset also includes continents. I do not want to show them, so I remove them from my selection. After counting, I have 20 countries to work with. I color the selected country rows, then use the country filter: clear the list and check only the countries in my selection. With those 20 countries selected, I show all their available years and sort by year and country to review the complete data.

There are too many years to fit in a static visualization, so I choose the last 20 years, starting in 2000. I copy this filtered table into a new tab and set the zoom to 100%. It becomes the starting point for my dataset: 20 countries, 20 years of per-capita CO₂ emissions for each, and population data for the most recent year. I bold the headings and freeze the first row.

![2495 · U3 · L08 · 10:53](frames/U03L08-F1053.00.jpg)

On screen: “Australia” / “Austria” [rest omitted]  
Shows: The country filter open while the selected country names are being checked.

![2495 · U3 · L08 · 12:20](frames/U03L08-F1220.00.jpg)

On screen: [rest omitted]  
Shows: The new working table, with the first row ready to be frozen.

## Add GDP and record the measurement details

Anchor: 2495 · U3 · L08 · 12:22–15:43

I also want to add the annual CO₂ emissions dataset and another kind of country context: GDP. It is often useful to show countries alongside contextual information. I add columns for these additional values and use the World Bank again to find GDP. It provides a chart, but I need the country figures, so I look up each country and copy its number into the spreadsheet.

I only need GDP for the most recent year, 2019, just as I only need population for the most recent year. The World Bank GDP table already shows the data for 2019, so I do not need to search for a separate year. The per-capita emissions are the values I want to track over time; for the other contextual information, the latest value is enough. Some complete datasets are available online, which saves us from building them manually, but additional contextual layers often have to be assembled by hand. There are 20 countries, a manageable number to look up and paste. This work takes patience, which will also be necessary when we use Illustrator.

For Turkmenistan, the World Bank provides a GDP figure only for 2018. That is not a problem, but I note the exception so I can explain it in the legend. I also add the year to the column heading and note the only exception, “Volta to Khmelnytskyi.” I label the population and GDP columns with their year and units: population is in thousands, and GDP is in US dollars. These annotations will be used in the legend.

![2495 · U3 · L08 · 13:09](frames/U03L08-F1309.00.jpg)

On screen: “GDP (current US$)” [rest omitted]  
Shows: The working dataset beside the World Bank GDP chart and country data.

![2495 · U3 · L08 · 14:00](frames/U03L08-F1400.00.jpg)

On screen: “Australia” / “2019” / “1,396,567.01” [rest omitted]  
Shows: Australia’s 2019 GDP value being copied from the World Bank into the working table.

![2495 · U3 · L08 · 14:49](frames/U03L08-F1449.00.jpg)

On screen: “Turkmenistan” / “2018” / “40,761.14” [rest omitted]  
Shows: The World Bank page and sheet row illustrating that Turkmenistan’s GDP value is from 2018.

![2495 · U3 · L08 · 15:24](frames/U03L08-F1524.00.jpg)

On screen: “Population (2019, T)” [rest omitted]  
Shows: The population column heading annotated with its year and unit.

## Import annual emissions and complete the dataset

Anchor: 2495 · U3 · L08 · 15:43–18:34

The last data to add is total annual emissions for each country. I open a new spreadsheet so I can split the screen and copy values into my working table. I import the annual emissions dataset I downloaded earlier. As before, Google Sheets recognizes the comma-separated values automatically.

I filter the imported data to show 2019 and only the countries I selected. I do not need to clean this dataset as I did the main one because I only need it as a source for copying values, though the general cleanup rules still apply. I add an Annual CO₂ Emissions column, label it with the year, make the heading bold, and copy the selected countries’ values into the main sheet.

The dataset is now complete, and I use the filters to review it. I have selected 20 countries and 20 years of per-capita emissions for each country. If 20 is too many, 10 countries or 10 years can be a good smaller starting point. For 2019, the dataset also includes population, GDP, and annual CO₂ emissions. Population and GDP will help position and contextualize each country, while annual emissions and the 20 years of per-capita emissions are the other information I will represent. In the next lesson, we will begin sketching and shifting from the table toward a visual form.

![2495 · U3 · L08 · 16:26](frames/U03L08-F1626.00.jpg)

On screen: “annual-co2-emissions-per-country.csv” / “Insert new sheet(s)” [rest omitted]  
Shows: The import dialog for the downloaded annual-emissions CSV.

![2495 · U3 · L08 · 17:02](frames/U03L08-F1702.00.jpg)

On screen: “Annual CO2” / “2019” [rest omitted]  
Shows: The imported annual-emissions dataset beside the main dataset.

![2495 · U3 · L08 · 18:20](frames/U03L08-F1820.00.jpg)

On screen: “Annual CO2 emissions (2019)” [rest omitted]  
Shows: The completed spreadsheet with the 2019 contextual values alongside each country’s per-capita series.
