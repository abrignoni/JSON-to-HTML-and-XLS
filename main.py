import sys, os
import pandas as pd
from json2html import *

loop = 1
count = 0

print("Convert JSON Discord chats to HTML or XLS")
print()
print("https://abrignoni.blogspot.com")
print("Twitter: @AlexisBrignoni")
print()

while loop == 1:
	print ("Write or copy-paste the path to the JSON files: ")
	path2input = input()
	if os.path.exists(path2input):
		#print ("Directory exists -> "+path2input)
		loop = 2
	else:
		print ("Directory does not exist.")

while loop == 2:
	print()
	print ("Select conversion format:")
	print ("1: HTML")
	print ("2: XLS")
	selected = input()
	if (selected == "1"):
		loop = 3
		print()
		print ("HTML selected")
		print()
		
	elif (selected == "2"):
		print()
		print ("XLS selected")
		print()
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
			try:
				file = open(path2input + "/" + filename, 'r')
				input = file.read() 
				file.close()
				data = pd.read_json(input)
				data.to_excel(path2input + "/" + "converted-XLS" + "/" + filename +'.xls', index=False)
			except:
				checkerrors = 1;
				print("Unable to convert: "+ path2input + '/' + filename)
				errors = open(path2input + "/converted-XLS/error.txt", 'a')
				errors.write("Unable to convert: "+ path2input + '/' + filename + '\n')
				errors.close()		
				pass
			
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

print()
print("Files processed: "+ str(count))

if (selected == "2"):
	print()
	print("Converted files located at: " + path2input + "/" + "converted-HTML" + "/")
	print()

if (selected == "1"):
	print()
	print("Converted files located at: " + path2input + "/" + "converted-XLS" + "/")
	print()
	
if (checkerrors == 1):
	print("See error log: "+ path2input + "/" + "converted-XLS" + "/errors.txt" + ". Process as HTML to view contents of these files." )
	print("Script will now close.")
	print() 	

os.system('pause')
