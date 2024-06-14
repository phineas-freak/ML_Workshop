import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

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

X_train, X_test, y_train, y_test = train_test_split(input,output,test_size=0.2)

model=LogisticRegression()
model.fit(X_train,y_train)

y_pred=model.predict(X_test)
print(y_pred)
print(y_test)
print(model.score(X_test,y_test))