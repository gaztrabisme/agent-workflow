# Lesson 09 · Creating the Dataset 1

Anchor: 4217 · U3 · L09 · 9:44 · https://www.domestika.org/en/courses/4217-creative-data-visualization-for-narrative-designs/units/15964-the-data#course_lesson_50448

## Starting the spreadsheet

Anchor: 4217 · U3 · L09 · 00:00–00:57

*4217 · U03 · L09 · 00:00–00:57*

We will create the dataset in Google Sheets. I use it because it is online and free; you only need to sign in with a Google account. You can also use Microsoft Excel or Numbers—choose the tool you feel most comfortable with. I have created an empty spreadsheet, and I will rename it before importing data.

![4217 · U3 · L09 · 00:38](frames/U03L09-F0038.00.jpg)

On screen: “Google Sheets” / “Make data-driven decisions, in Google Sheets” / “Create and collaborate on online spreadsheets in real-time and from any device.” / “Try Sheets for Work” / “Go to Sheets” / “Sign up for free” [rest omitted]  
Shows: The Google Sheets homepage and its product description.

![4217 · U3 · L09 · 00:47](frames/U03L09-F0047.00.jpg)

On screen: “Untitled spreadsheet” / “File” / “Edit” / “View” / “Insert” / “Format” / “Data” / “Tools” / “Extensions” / “Help” / “Sheet1” [rest omitted]  
Shows: A new, empty spreadsheet before renaming.

## Importing the first CSV

Anchor: 4217 · U3 · L09 · 00:57–03:21

*4217 · U03 · L09 · 00:57–03:21*

I will import the CSV files (captions: “CS will fight”). In my final-project folder, I usually create two subfolders: “data” and “vids.” I put the datasets in “data” and my visualization files in “vids.” The files we downloaded are per-capita renewables, renewable share of energy, the World Regions list, and population data, which we will rename later.

I start with the renewable-share file. In Google Sheets, choose File, Import, then Upload; you can select a file or drag it in. When the import dialog asks whether to create a new spreadsheet or replace the current one, I choose to replace the current spreadsheet. It detects the separator automatically because the CSV uses commas, which I referred to as the separator of our table. I import the data. A spreadsheet can have different tabs, so I rename this one “renewable-share-energy” to keep the file clear and precise. The imported table shows all of the years the source provides, the entity—which may be a region or a country—and the renewable-share data.

![4217 · U3 · L09 · 01:13](frames/U03L09-F0113.00.jpg)

On screen: “Renewable energy” / “Import file” / “My Drive” / “Shared with me” / “Recent” / “Upload” / “Drag a file here” / “Or, if you prefer...” / “Select a file from your device” / “Select” / “Cancel” [rest omitted]  
Shows: The Google Sheets upload dialog over an empty workbook.

![4217 · U3 · L09 · 01:44](frames/U03L09-F0144.00.jpg)

On screen: “data” / “per-capita-renewables.csv” / “renewable-share-energy.csv” / “world-regions-according-to-the-world-bank.csv” [rest omitted]  
Shows: The project’s data folder in the file picker, with the downloaded CSV files listed.

![4217 · U3 · L09 · 02:19](frames/U03L09-F0219.00.jpg)

On screen: “renewable-share-energy.csv” / “Import location” / “Replace current sheet” / “Separator type” / “Detect automatically” / “Import data” / “Cancel” [rest omitted]  
Shows: The import options dialog set to replace the current sheet and detect the separator automatically.

![4217 · U3 · L09 · 03:04](frames/U03L09-F0304.00.jpg)

On screen: “Entity” / “Code” / “Year” / “Renewables (% sub energy)” [rest omitted]  
Shows: The imported renewable-share table, with entity, code, year, and renewable-share columns.

## Setting a clear selection rule

Anchor: 4217 · U3 · L09 · 03:21–04:02

*4217 · U03 · L09 · 03:21–04:02*

Before importing the other data, I want to select the countries. Some choices are inevitable and necessary, but I want an objective selection criterion that I can explain to my readers. Here, I will choose the top 40 countries for renewable share in 2020.

The column titles should be followed directly by the data, without empty rows or spaces. This is very important. I will link an excellent article about keeping a table clean and functioning properly in the Additional Resources section. I select the first row and turn on the filter tool.

## Filtering for 2020 and ranking the countries

Anchor: 4217 · U3 · L09 · 04:02–06:06

*4217 · U03 · L09 · 04:02–06:06*

Filters let you filter the data. First, I want only 2020. The icon beside a column title opens its filter. The Year column lists all available years. I can clear the selections; to demonstrate, I select 1990 and apply the filter, so only 1990 remains. That is not the year we need, so I change the selection to 2020.

I want the top 40 countries by renewable share in 2020. The filter also sorts data: A to Z is ascending, and Z to A is descending. I choose descending order so it is easy to see the countries with the highest values.

![4217 · U3 · L09 · 04:55](frames/U03L09-F0455.00.jpg)

On screen: “Sort A → Z” / “Sort Z → A” / “Filter by color” / “Filter by condition” / “Filter by values” / “Select all” / “Clear” / “Cancel” / “OK” [rest omitted]  
Shows: The Year column’s filter menu above the full renewable-share table.

![4217 · U3 · L09 · 05:14](frames/U03L09-F0514.00.jpg)

On screen: “1988” / “1989” / “1990” / “1991” / “1992” / “Cancel” / “OK” [rest omitted]  
Shows: The year filter with 1990 highlighted for the demonstration.

![4217 · U3 · L09 · 05:28](frames/U03L09-F0528.00.jpg)

On screen: “2017” / “2018” / “2019” / “2020” / “Cancel” / “OK” [rest omitted]  
Shows: The year filter with 2020 selected.

![4217 · U3 · L09 · 05:38](frames/U03L09-F0538.00.jpg)

On screen: “2020” [rest omitted]  
Shows: Renewable-share values filtered to 2020, including country and regional entities.

## Keeping the original and making a country-only tab

Anchor: 4217 · U3 · L09 · 06:06–09:18

*4217 · U03 · L09 · 06:06–09:18*

Before deleting data I do not need, I prefer to keep the original file and put each step in a different tab or file. I create a new sheet in the same Google spreadsheet and rename it “Top40-renewable-share-energy.” I return to the first tab, copy the filtered data, and paste it into the new one. The filter for 2020 stays selected, so the new tab contains only the year I want.

I use the filter tool again and change “Entity” to “Country.” The next lessons will show how important it is to give every column a very clear title. The data are already in the right order because I copied them from the previous tab, but I sort again to make sure. Now I can delete the rows that are not countries, such as the regional or continental entries. I select the row numbers and choose Delete row. Delete all the unwanted rows so that each country remains matched to its correct value.

![4217 · U3 · L09 · 07:38](frames/U03L09-F0738.00.jpg)

On screen: “Top40-renewable-share-energy” [rest omitted]  
Shows: The copied 2020 data in a second tab, in descending renewable-share order.

![4217 · U3 · L09 · 08:12](frames/U03L09-F0812.00.jpg)

On screen: “Country” / “Code” / “Year” / “Renewables (% sub energy)” / “Sort A → Z” / “Sort Z → A” / “Sort by color” / “Filter by color” / “Filter by condition” / “Filter by values” / “Select all” / “Clear” / “0.006” / “0.007” / “0.064” / “0.087” / “Cancel” / “OK” [rest omitted]  
Shows: The Renewables column’s filter menu open above the table, listing renewable-share values.

![4217 · U3 · L09 · 08:24](frames/U03L09-F0824.00.jpg)

On screen: “Eastern Africa” / “Middle Africa” / “Europe” / “European Union (27)” / “OECD” / “World” [rest omitted]  
Shows: The Eastern Africa row selected in the descending table, with regional aggregates still among the entries.

## Confirming the 40 selected countries

Anchor: 4217 · U3 · L09 · 09:18–09:44

*4217 · U03 · L09 · 09:18–09:44*

These are the countries I have selected. I chose 40. If I select the country cells, the count at the bottom confirms that I selected 40 of them. It is a useful feature in Google Sheets.

![4217 · U3 · L09 · 09:41](frames/U03L09-F0941.00.jpg)

On screen: “A2:A41” / “Count: 40” [rest omitted]  
Shows: The 40 country cells selected in the completed country-only table.
