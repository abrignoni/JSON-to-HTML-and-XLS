from json2html import *

file = open('50', 'r', encoding='utf-8') 
input = file.read() 
file.close()

afuera = json2html.convert(json = input, clubbing = False)

file = open('output.html', 'w', encoding='utf-8')
file.write(afuera)
file.close()
