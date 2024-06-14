import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

path = "C:\\Users\\rosha\\OneDrive\\Desktop\\code\\Workshop\\ML\\Data\\Data\\insurance_data.csv"
data=pd.read_csv(path)
print(data)
#print(data.info())

input=data.drop('bought_insurance',axis='columns')
print(input)

output=data.drop('age',axis='columns')
print(output)

plt.xlabel('age')
plt.ylabel('Insurance')
plt.title('Insurances bought by age')
plt.scatter(data.age,data.bought_insurance,color='red')
plt.show()