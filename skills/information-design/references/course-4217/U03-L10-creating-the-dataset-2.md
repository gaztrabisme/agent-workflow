# Lesson 10 · Creating the Dataset 2

Anchor: 4217 · U3 · L10 · 18:56 · https://www.domestika.org/en/courses/4217-creative-data-visualization-for-narrative-designs/units/15964-the-data#course_lesson_50489

## Finalizing the country list and starting the combined table

Anchor: 4217 · U3 · L10 · 00:00–00:58

*4217 · U03 · L10 · 00:00–00:58*

Now I can delete the countries we do not need, leaving the top 40. After deleting the selected rows, I duplicate the tab and call the copy “final.” This will be the table where I add the information I want to display: renewable share, per-capita renewable consumption, world region, and population.

![4217 · U3 · L10 · 00:21](frames/U03L10-F0021.00.jpg)

On screen: “Renewable energy” / “Delete selected rows” / “Clear rows 42 - 84” [rest omitted]  
Shows: Selected rows in the top-40 sheet with the delete-rows menu open.

![4217 · U3 · L10 · 00:31](frames/U03L10-F0031.00.jpg)

On screen: “Country” / “Code” / “Year” / “Renewables” / “Top40-renewable-share-energy” [rest omitted]  
Shows: The sorted top-40 country table in its own tab.

## Preparing the per-capita table

Anchor: 4217 · U3 · L10 · 00:58–02:22

*4217 · U03 · L10 · 00:58–02:22*

I start adding the per-capita data by importing it. I choose a new sheet in the existing spreadsheet rather than creating another spreadsheet. Because the file is comma-separated, I let the separator type be detected automatically. The imported table contains all the years, but I only want 2020. I create a filter, clear the other years, select 2020, and copy those data to a new tab. This gives me a per-capita table for 2020 that I can merge into the final table.

![4217 · U3 · L10 · 01:24](frames/U03L10-F0124.00.jpg)

On screen: “Import file” / “per-capita-renewables.csv” / “Import location” / “Insert new sheet(s)” / “Separator type” / “Detect automatically” [rest omitted]  
Shows: The per-capita import dialog with “Insert new sheet(s)” open and “Detect automatically” set for the separator.

![4217 · U3 · L10 · 01:53](frames/U03L10-F0153.00.jpg)

On screen: “Entity” / “Code” / “Year” / “Renewables per capita (kWh)” [rest omitted]  
Shows: The imported per-capita table with its year values.

![4217 · U3 · L10 · 02:20](frames/U03L10-F0220.00.jpg)

On screen: “Entity” / “Code” / “Year” / “Renewables” / “2020” [rest omitted]  
Shows: The per-capita data filtered to 2020.

## Choosing a method and finding the merge extension

Anchor: 4217 · U3 · L10 · 02:22–05:09

*4217 · U03 · L10 · 02:22–05:09*

There are different ways to combine the two tables. One way is to do it manually: split the screen in half, keep the table that needs information on one side and the per-capita data on the other, then copy and paste values by matching the country names. It is not ideal, but with only 40 countries it is manageable, and I have done it before. Still, learning additional tools and tricks can be helpful, which is why I am showing Merge Sheets.

Another option is an extension from the Google Sheets Extensions menu. Extensions add tools; some are free, some cost money, and some offer trials. They can do more complex tasks than the standard Google Sheets features. I already have the extension I want, called Merge Sheets. It offers a free trial and an annual fee; the Additional Resources section has the details. I show how to find an extension by opening Extensions, Add-ons, and Get add-ons, then searching for “Merge.” There are several possible extensions. I already installed the Merge Sheets tool I will use; to demonstrate installation, I also open another listing and choose Install. Once an extension is installed, it appears in the Extensions menu.

![4217 · U3 · L10 · 03:53](frames/U03L10-F0353.00.jpg)

On screen: “Extensions” / “Add-ons” / “Get add-ons” / “Manage add-ons” / “Merge Sheets” [rest omitted]  
Shows: The Extensions menu and its add-ons submenu.

![4217 · U3 · L10 · 04:23](frames/U03L10-F0423.00.jpg)

On screen: “Google Workspace Marketplace” / “merge” / “Merge Sheets” / “EPHOD SAS” / “Merge Sheets” / “Ablebits” [rest omitted]  
Shows: Marketplace results for “merge,” including two add-ons titled Merge Sheets.

![4217 · U3 · L10 · 04:47](frames/U03L10-F0447.00.jpg)

On screen: “Merge Sheets” / “EPHOD SAS” / “Install” / “Works with: Sheets” [rest omitted]  
Shows: The Merge Sheets extension detail panel and its Install button.

## Merging the per-capita values

Anchor: 4217 · U3 · L10 · 05:09–09:24

*4217 · U03 · L10 · 05:09–09:24*

The Merge Sheets tool guides the merge through several steps. First, I choose the main sheet, which the narration calls “Top 40 final,” and check that the range is correct. The screen shows the tab as “Top40-renewable-share-energy.” It already selects the right range, and I want the whole table included. Then I choose the lookup sheet: the table from which I want to retrieve the information. Here, that is “per-capita-2020,” in the same spreadsheet.

Next, I tell the tool which columns to match. If the main table has Italy, I want its per-capita data for Italy, so the matching columns must line up. I ask the tool to look for the country name in the main table’s Country column and match it with the name in the lookup table’s Entity column. Then I select the per-capita renewable data as the column to add, unselecting the other columns. I want the new column at the end of the main table.

The tool offers other options. For example, it can add non-matching rows or a status column. I click the information icon to see what adding a status column means, but I am not interested in that option and do not want to overcomplicate the table. The tool reports 40 of 40 matching rows and one inserted column. I close the dialog. The main table now contains the per-capita column. I also want filters on all of the columns, so I remove and recreate the filter after the merge.

![4217 · U3 · L10 · 05:18](frames/U03L10-F0518.00.jpg)

On screen: “Step 1 of 5: Select the main sheet” / “A1:D41” / “Auto select” / “Next” / “Cancel” [rest omitted]  
Shows: The first merge step with the top-40 sheet selected as the main table.

![4217 · U3 · L10 · 07:18](frames/U03L10-F0718.00.jpg)

On screen: “Merge Sheets” / “Step 3 of 5: Select matching columns (key columns to compare)” / “Main table columns” / “1st row content” / “Lookup columns” / “Country” / “Iceland” / “Entity” [rest omitted]  
Shows: The matching-columns step, pairing the main table’s Country column with the lookup table’s Entity column.

![4217 · U3 · L10 · 07:48](frames/U03L10-F0748.00.jpg)

On screen: “Step 4 of 5: Select columns to add or update in the main sheet” / “Lookup columns” / “Action” / “Main columns” / “Renewables per capita (kWh)” [rest omitted]  
Shows: The selectable lookup columns in the fourth merge step.

![4217 · U3 · L10 · 08:18](frames/U03L10-F0818.00.jpg)

On screen: “Step 5 of 5: Choose additional options” / “Add rows and columns” / “Add non-matching rows to the end of the main table” / “Add a status column” / “Place results to” / “Update your main table” / “Create a new spreadsheet” [rest omitted]  
Shows: The final merge options, including the choices to add rows or a status column.

![4217 · U3 · L10 · 08:56](frames/U03L10-F0856.00.jpg)

On screen: “Renewables per capita (kWh)” [rest omitted]  
Shows: The main table after the per-capita column has been inserted.

## Adding the World Bank region

Anchor: 4217 · U3 · L10 · 09:24–12:48

*4217 · U03 · L10 · 09:24–12:48*

The table now has renewable share and per-capita renewable consumption. I want to add the population and world-region context, starting with the regions. I import the original region file into a new sheet. It is a simple table: country, a code that I do not need, and the World Bank region. I change the “Entity” heading to “Country,” then open Merge Sheets (captions: “Malshwin”) and merge the region column into the main table using the same process.

I select the main table, then the lookup sheet named for the World Bank regions. Clear tab names are important because they make each step easier to follow. I keep the full table range. In the matching-columns step, I pair Country with Country. For the column to add, I choose World Region, not Code, and append it to the end. As before, I do not add non-matching rows or a status column. The tool finds 40 of 40 matching rows and inserts one column. I recreate the filter. Now each country has not only the values, but also its group and world-region information, which will be a helpful column.

![4217 · U3 · L10 · 09:56](frames/U03L10-F0956.00.jpg)

On screen: “world-regions-according-to-the-world-bank.csv” / “Open” [rest omitted]  
Shows: The World Bank region CSV selected in the file picker.

![4217 · U3 · L10 · 10:42](frames/U03L10-F1042.00.jpg)

On screen: “Country” / “Code” / “Year” / “World Region according to the World Bank” [rest omitted]  
Shows: The imported World Bank table with country, code, year, and region columns.

![4217 · U3 · L10 · 11:11](frames/U03L10-F1111.00.jpg)

On screen: “Step 2 of 5: Select the lookup sheet” / “renewable-share-energy” / “A1:D4836” / “world-regions-according-to-the-world-bank” [rest omitted]  
Shows: The merge dialog is at step 2 with “renewable-share-energy” still in the lookup-sheet dropdown; the World Bank regions tab is visible below.

![4217 · U3 · L10 · 11:41](frames/U03L10-F1141.00.jpg)

On screen: “World Region according to the World Bank” [rest omitted]  
Shows: The region merge set to match Country in the main and lookup tables.

![4217 · U3 · L10 · 12:18](frames/U03L10-F1218.00.jpg)

On screen: “Merge sheets results” / “40 of 40 matching rows were found.” / “1 column was inserted.” / “0 rows were updated.” / “0 rows were inserted.” [rest omitted]  
Shows: The completed region merge and its result count.

## Cleaning the population data

Anchor: 4217 · U3 · L10 · 12:48–15:31

*4217 · U03 · L10 · 12:48–15:31*

Finally, I add population. The population file I select has a very long name. World Bank (captions: “War Bank”) downloads may arrive in a ZIP file rather than as a CSV directly; unzip it to find the CSV inside. I import it as a new sheet. This table is slightly different from the Our World in Data tables and needs some cleanup. A clean table should not have empty rows or rows that are not data. It is useful to know when the source was last updated, but I do not need that information in this working sheet, so I remove the introductory rows (captions: “The Litty Rose”) and keep the data heading and values.

![4217 · U3 · L10 · 13:33](frames/U03L10-F1333.00.jpg)

On screen: “data” / “API_SP.POP.TOTL__DS2_en_csv_v2_4218816.csv” / “CSV Document · 183 KB” / “Open” [rest omitted]  
Shows: The long World Bank population CSV filename selected in the data folder.

The population data are displayed differently: each year has its own column. I rename the tab “population” and make a copy for the 2020 data. The year needs to match the year in the main dataset. I select the first column, hold Shift, select the last column, and delete the columns I do not need, including 2021, which is empty. The cleaned lookup table should contain just the country and its 2020 population.

![4217 · U3 · L10 · 13:54](frames/U03L10-F1354.00.jpg)

On screen: “Data Source” / “World Development Indicators” / “Country Name” / “Country Code” / “Indicator Name” / “Indicator Code” / “1960” / “1961” / “1962” / “1963” / “1964” [rest omitted]  
Shows: The imported population table in its wide format, with country metadata and one column per year.

![4217 · U3 · L10 · 15:17](frames/U03L10-F1517.00.jpg)

On screen: “Delete columns B - BL” [rest omitted]  
Shows: The population sheet’s year columns selected with the delete-columns menu open.

## Merging population and completing the dataset

Anchor: 4217 · U3 · L10 · 15:31–18:56

*4217 · U03 · L10 · 15:31–18:56*

Again, I could copy and paste the population data by hand. There are only 40 countries, and I have done this before. Still, knowing additional tools and tricks can be helpful, so I am showing Merge Sheets.

I merge the population data into the main table. As before, the matching column is Country, the lookup sheet is “population in 2020,” the lookup value is the 2020 column, and I add it at the end. I do not add a status column or other unmatched rows. This time, 39 of 40 rows match, so one country is missing. I rename the new column “population,” then remove and recreate the filter so I can identify the missing country as Venezuela.

![4217 · U3 · L10 · 15:35](frames/U03L10-F1535.00.jpg)

On screen: “Country” / “2020” [rest omitted]  
Shows: The cleaned population lookup table with one country column and one year column.

I open Edit > Find and replace, which lets me look for words within the table, and search for Venezuela manually. The names did not match because the World Bank table adds “, RB” after Venezuela. That is why Merge Sheets could not find it. I copy the value and paste it into the main table manually. Now I have the complete dataset.

The code column is not needed, and I remove it. Since all the data are from 2020, I also remove the separate year column and write “2020” next to each data value. The dataset is ready, and in the next lesson we will start sketching.

![4217 · U3 · L10 · 16:59](frames/U03L10-F1659.00.jpg)

On screen: “Merge sheets results” / “39 of 40 matching rows were found.” / “1 column was inserted.” / “0 rows were updated.” / “0 rows were inserted.” [rest omitted]  
Shows: The population merge result with one country unmatched.

![4217 · U3 · L10 · 17:59](frames/U03L10-F1759.00.jpg)

On screen: “Venezuela, RB” / “Find and replace” / “Find” / “venezuela” / “Replace with” / “Search” / “All sheets” / “Done” [rest omitted]  
Shows: The population table search for “venezuela,” with the World Bank country name selected.

![4217 · U3 · L10 · 18:45](frames/U03L10-F1845.00.jpg)

On screen: “Renewables (% su” / “Renewables per ca” / “World Regio” / “Population i” [rest omitted]  
Shows: The final table with country, renewable-share, per-capita, region, and population columns.
