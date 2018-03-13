# Discord JSON chats to HTML and EXCEL

**JSON2HTML**

Simple python script to convert Discord JSON chats to html for easier reading.
The json2html module is required and does all the work. 

``` pip install json2html ```

More info here:

``` https://pypi.python.org/pypi/json2html ``` 

Usage:

1. Write the filename of the json chat to be converted and save script.

``` file = open('file2beconverted', 'r') ```

2. Run the script.

**JSON2XLS**

Simple python script to convert Discord JSON chats to html for easier reading.
The pandas, xlsxwriter and xlwt modules are required.

`` pip install pandas ``

`` pip install xlsxwriter ``

`` pip install xlwt ``

Usage:

1. Write the filename of the json chat to be converted and save the script.

``` file = open('file2beconverted', 'r') ```

2. Run the script.

Pending work: 
1. Make scripts ingest all files in a directory instead of one by one.
2. Create prompts for directory location and desired output all in one script.
