import pandas as pd
path = "C:\\Users\\rosha\\OneDrive\\Desktop\\code\\Workshop\\ML\\Data\\Data\\homeprices.csv"
data=pd.read_csv(path)
print(data)
#print(data.info())

input=data.drop('price',axis='columns')
print(input)

output=data.drop('area',axis='columns')
print(output)

