import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

path = "C:\\Users\\rosha\\OneDrive\\Desktop\\code\\Workshop\\ML\\Data\\Data\\homeprices.csv"
data=pd.read_csv(path)
print(data)
#print(data.info())

input=data.drop('price',axis='columns')
print(input)

output=data.drop('area',axis='columns')
print(output)

plt.xlabel('area')
plt.ylabel('price')
plt.title('Home Prices')
plt.scatter(data.area,data.price,color='red')
plt.show()

reg=linear_model.LinearRegression()
reg.fit(input,output)

print(reg.predict([[5000]]))
print(reg.score(input,output)) #for accuracy
