# Lesson 07 · Data Preparation

Anchor: 3601 · U3 · L07 · 7:19 · https://www.domestika.org/en/courses/3601-information-design-storytelling-with-data-in-illustrator/units/14537-working-with-data#course_lesson_45517

## Choose a tool and open the downloaded dataset

Anchor: 3601 · U3 · L07 · 00:00–01:16

Now that the dataset is ready, open it and begin exploring. I demonstrate in Google Sheets, but you can use any tool you are comfortable with. If you are new to tables and spreadsheets, use the Google Sheets resource at the bottom of the unit. In Google Sheets, open a saved file through File > Open, or use the browser shortcut sheet.new (captions: “shit. New in the browser in Google Chrome”) to create a new spreadsheet and then import the dataset. The downloaded JMP dataset is already open here; it is a large file and takes a little time to load.

![3601 · U3 · L07 · 00:48](frames/U03L07-F0048.00.jpg)

On screen: “Domestika_JMP_Water_2021” / “DRINKING WATER” / “COUNTRY, AREA OR TERRITORY” / “NATIONAL” / “RURAL” / “At least basic” [rest omitted]  
Shows: The original workbook’s water table, with national, rural and urban data and several subject tabs.

![3601 · U3 · L07 · 01:08](frames/U03L07-F0108.00.jpg)

On screen: “Untitled spreadsheet” / “File” / “Open” / “Import” [rest omitted]  
Shows: A new blank Google spreadsheet with the File menu open.

## Inspect the workbook and remove unrelated material

Anchor: 3601 · U3 · L07 · 01:16–02:24

First understand what the dataset contains and which data is unnecessary for the investigation. Because I retrieved the whole research dataset from its original source, it also includes sanitation, hygiene, and menstrual health. Delete material that is not needed; this also makes the file lighter. Rename the working file to show its source—JMP water—and remove the title page. The first rows contain the information needed to read the data: the headers. A filter is already applied, and this is a tool we use often for filtering and ranking. You can apply it to a selection or remove it from the selection by clicking the tool. I turn it off because I do not want rows hidden; previously, the selection showed only 2020 and concealed some years. The dataset also contains rural, urban, and world values and several types of improved water supply, so take time to inspect its structure.

![3601 · U3 · L07 · 01:45](frames/U03L07-F0145.00.jpg)

On screen: “MENSTRUAL HEALTH” / “Delete” / “Duplicate” / “Copy to” / “Rename” / “Change color” / “Hide sheet” [rest omitted]  
Shows: The menstrual-health sheet and its sheet menu.

![3601 · U3 · L07 · 02:06](frames/U03L07-F0206.00.jpg)

On screen: “DRINKING WATER” / “COUNTRY, AREA OR TERRITORY” / “Year” / “2020” / “NATIONAL” / “RURAL” / “URBAN” [rest omitted]  
Shows: The water table with the Year filter applied, displaying only 2020 rows.

![3601 · U3 · L07 · 02:12](frames/U03L07-F0212.00.jpg)

On screen: “DRINKING WATER” / “COUNTRY, AREA OR TERRITORY” / “NATIONAL” / “RURAL” / “URBAN” / “At least basic” / “Limited (more than 30 mins)” / “Unimproved” / “Surface water” [rest omitted]  
Shows: The water table with its existing filter control.

## Reveal the linked sheet and work with a copy

Anchor: 3601 · U3 · L07 · 02:24–03:34

When I click the cells, I see that they are not plain numbers: they return results from formulas linked to a hidden data sheet called wat (captions: “D.W.A.T.”). You can reveal hidden sheets through View > Show. I show the rest of the workbook to check what is there, then remove the sanitation, regional, hygiene, and menstrual-health sheets because they are not needed for this investigation.

![3601 · U3 · L07 · 02:56](frames/U03L07-F0256.00.jpg)

On screen: “Domestika_JMP_Water_2021” / “DRINKING WATER” / “=IF(ISNUMBER(wat!D15), wat!D15, "-")” [rest omitted]  
Shows: A water-table cell and the formula that retrieves a value from the wat sheet.

## Duplicate, verify and format the water table

Anchor: 3601 · U3 · L07 · 03:34–05:38

The water data is the table to keep, so make a copy by duplicating it. Copy the first three rows and insert three rows above the table to bring the formatting to the top. Before deleting the old rows, verify that the headings and values match: check the year and population, and work through the table. As another check, take the first data row, Afghanistan, put it above the copied data and compare the values. They match, apart from rounding. For example, selecting a cell shows 1 in the preview, while the underlying value is 0.79. To show fewer decimals, select the cell and decrease the decimal places. Once the formatting is right, delete the two temporary rows. This is the JMP water raw data to keep; do not alter it, and delete the other two sheets. Then duplicate the table again, rename it, and keep only the national matrix for now. I may add rural and urban data later, but first I want to reduce how much information I need to process.

![3601 · U3 · L07 · 03:34](frames/U03L07-F0334.00.jpg)

On screen: “Domestika_JMP_Water_2021” / “name” / “iso3” / “year” / “pop_n” / “prop_u” [rest omitted]  
Shows: The linked water data in rows, with country, year and measurement columns.

![3601 · U3 · L07 · 04:31](frames/U03L07-F0431.00.jpg)

On screen: “=IF(ISBLANK(wat!A3), "", wat!A3)” / “RURAL” / “URBAN” / “Free from contamination” / “Annual rate of change in safely managed” / “Piped” / “Non-piped” / “Safely managed” / “Accessible on premises” / “Available when needed” [rest omitted]  
Shows: The copied water table, with rural and urban columns and their water-service fields.

## Use the methodology to choose and organize the fields

Anchor: 3601 · U3 · L07 · 05:38–07:19

While cleaning, make sure you know what the data means. Read the methodology and download the report published with the dataset. Here, knowing the water-ladder methodology establishes a hierarchy among categories. I will use safely managed water as the main category and keep the other categories as context. I will also keep a region field so I can organize or cluster countries. The first row should be the dataset heading, so remove anything above it. Freeze that row through View > Freeze > First row so it remains visible while scrolling. If the current arrangement does not suit you, change it. Design starts with the table, and at this point I am happy with its appearance. Cleaning and preparing data may not be exciting, but it is fundamental. In the next lesson, we will investigate the spreadsheet more deeply and look for stories.

![3601 · U3 · L07 · 05:41](frames/U03L07-F0541.00.jpg)

On screen: “/ Valentina D'Efilippo” / “Drinking water ladder” / “SAFELY MANAGED” / “BASIC” / “LIMITED” / “UNIMPROVED” / “SURFACE WATER” / “Definitions across the drinking water ladder” [rest omitted]  
Shows: A five-level drinking-water ladder with descriptions and a comparison of category definitions.

![3601 · U3 · L07 · 06:25](frames/U03L07-F0625.00.jpg)

On screen: “DRINKING WATER” / “COUNTRY, AREA OR TERRITORY” / “NATIONAL” / “Safely managed” / “At least basic” / “SDG region” / “WHO region” / “UNICEF Programming region” / “UNICEF Reporting region” [rest omitted]  
Shows: The cleaned table with water categories and regional fields.
