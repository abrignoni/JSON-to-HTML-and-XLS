# Discord JSON chats to HTML and EXCEL

For an explanation on how to find Discord app chats in Windows see here:

(https://abrignoni.blogspot.com/2018/03/finding-discord-app-chats-in-windows.html)

**JSON2HTML**

Simple python script to convert Discord json chats to html or xls for easier reading.

Required modules:

``` pip install json2html ```

`` pip install pandas ``

`` pip install xlsxwriter ``

`` pip install xlwt ``

Usage:

1. Run the main.py script
2. Write the path to the directory that contains the Discord chat json files.
3. Select conversion format. Select #1 for html or #2 for xls.
4. After conversion see the count of processed files. Converted files will be located in a new folder within the Discord chat json files directory.
