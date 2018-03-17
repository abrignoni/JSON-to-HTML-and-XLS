import sys, os
import pandas as pd
from json2html import *

loop = 1
count = 0

while loop == 1:
	print ("Write path to files: ")
	path2input = input()
	if os.path.exists(path2input):
		#print ("Directory exists -> "+path2input)
		loop = 2
	else:
		print ("Directory does not exist.")

while loop == 2:
	print ("Select conversion format:")
	print ("1: HTML")
	print ("2: XLS")
	selected = input()
	if (selected == "1"):
		loop = 3
		print ("HTML selected")
		
	elif (selected == "2"):
		print ("XLS selected")
		loop = 3
	else:
		print ("Invalid selection.")
		

if (selected == "2"):
	# open folder to write to
	os.makedirs(path2input + "/" + "converted-XLS" + "/")
	#open folder to read from
	for filename in os.listdir(path2input):
		count = count+1
		if os.path.isdir(path2input + "/" + filename):
			count=count-1 #make sure a directory check does not count as a processed file.
		else:
			file = open(path2input + "/" + filename, 'r')
			input = file.read() 
			file.close()
			data = pd.read_json(input)
			data.to_excel(path2input + "/" + "converted-XLS" + "/" + filename +'.xls', index=False)
			
if (selected == "1"):
	os.makedirs(path2input + "/" + "converted-HTML" + "/")
	for filename in os.listdir(path2input):
		count = count+1
		if os.path.isdir(path2input + "/" + filename):
			count=count-1 
		else:
			file = open(path2input + "/" + filename, 'r', encoding="utf-8") 
			input = file.read() 
			file.close()

			afuera = json2html.convert(json = input, clubbing = False)

			file = open(path2input + "/" + "converted-HTML" + "/" + filename +'.html', 'w', encoding="utf-8")
			file.write(afuera)
			file.close()
print("Files processed: "+ str(count))

if (selected == "2"):
	print("Files located at: " + path2input + "/" + "converted-XLS" + "/")

if (selected == "1"):
	print("Files located at: " + path2input + "/" + "converted-XLS" + "/")
		
