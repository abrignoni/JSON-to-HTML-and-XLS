import pandas as pd

file = open('50', 'r') 
input = file.read() 
file.close()

data = pd.read_json(input)
data.to_excel('output.xls', index=False)
