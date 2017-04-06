# auto_survey
A script to be lazy and auto populate a receipt

To use call run_survey.populate_survey(page_info)

## page_info structure
* website(string) - Landing page for survey
* continue(string) - ID of the button to transition to the next part of the survey
* pages(Array) -  Dictionaries containing form data info where each dictionary represents a single page
    * page(Dict) -  Contains form properties
        * currency_range_text(Array<Dict>)
        * date_text(Array<Dict>)
        * int_range_text(Array<Dict>)
        * string_text(Array<Dict>)
        * radio(Array<str>)

## Page Arguments 
* currency_range_text(dict) 
    * id(string) - ElementID, min(float), max(float)

* currency_range_text arguments
    * id(string) - ElementID, days_ago(int)

* int_range_text(dict)
    * id(string) - ElementID, min(float), max(float)

* string_text(dict)
    * id(string) - ElementID, key(string) - Value for textbox

* radio(array)
    * ElementIDs list

* continue(string)

## Notes
Only adding form options as needed 
There is a static date format - Will add strftime support at some point
