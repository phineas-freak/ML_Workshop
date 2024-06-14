import pandas as pd
#import matplotlib.pyplot as plt
from sklearn import linear_model

path = "C:\\Users\\rosha\\OneDrive\\Desktop\\code\\Workshop\\ML\\Data\\Data\\Exammarks.csv"
data=pd.read_csv(path)
print(data)

median_age=data.age.median()
data.age=data.age.fillna(median_age)


median_hours=data.hours.median()
data.hours=data.hours.fillna(median_hours)

median_internet=data.internet.median()
data.internet=data.internet.fillna(median_internet)
print(data)

input=data.drop('marks',axis='columns')
print(input)

output=data.drop(['hours','age','internet'],axis='columns')
print(output)


reg=linear_model.LinearRegression()
reg.fit(input,output)

print(reg.predict([[6.8,16,1]]))