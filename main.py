from json2html import *

file = open('50', 'r') 
input = file.read() 
file.close()

afuera = json2html.convert(json = input, clubbing = False)
print (afuera)

