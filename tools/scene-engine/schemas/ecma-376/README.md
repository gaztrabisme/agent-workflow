# ECMA-376 schema bundle

The unmodified transitional W3C XML Schema files in `transitional/` are extracted from the official ECMA-376 Part 4, 5th edition (December 2016) archive:

- https://ecma-international.org/wp-content/uploads/ECMA-376-4_5th_edition_december_2016.zip
- Inner archive: `OfficeOpenXML-XMLSchema-Transitional.zip`

The unmodified Open Packaging Conventions schemas in `opc/` are extracted from the official ECMA-376 Part 2, 5th edition (December 2021) archive:

- https://ecma-international.org/wp-content/uploads/ECMA-376-2_5th_edition_december_2021.zip
- Inner archive: `OpenPackagingConventions-XMLSchema.zip`

The files in `dublin-core/` are local dependencies imported by the ECMA core-properties schema: the Dublin Core schemas are from [Dublin Core's QDC schema set](http://dublincore.org/schemas/xmls/qdc/2003/04/02/) and `xml.xsd` is from the [W3C XML namespace schema](https://www.w3.org/2001/xml.xsd). They are kept locally so schema validation remains offline.

These files are retained verbatim. The MCE Morph wrapper is checked for one `Choice`, one `Fallback`, the required `p159` capability and supported Morph options; its base and fallback transitions are validated against the Part 4 schemas. The `p159:morph` element is a PowerPoint extension outside the ECMA-376 XSD set. All schemas are loaded locally during PPTX validation; the validator makes no network requests.
