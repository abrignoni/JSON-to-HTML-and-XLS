# Discord-JSON-chats-to-HTML

Simple python script to convert Discord JSON chats to html for easier reading.
The json2html module is required. 

``` $ pip install json2html ```

More info here:

``` https://pypi.python.org/pypi/json2html ``` 


1. Write the filename of the json chat to be converted and save script.

``` file = open('file2beconverted', 'r') ```

2. Pipe the output of the script to a file as follows.

``` python main.py >> chats.html ```

Pending work: Make script ingest all files in a directory to create one html document.
