import pandas as pd  
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from mlxtend.plotting import plot_decision_regions
import pickle

# Get the data
df = pd.read_csv("ml2.csv")

# Remove extra column - preprocing the data
df = df.iloc[:,1:4]

#perform EDA
plt.scatter(df['CGPA'],df['IQ'],c=df['Placement'])
plt.xlabel("CGPA")
plt.ylabel("IQ")
plt.title("cgpa vs iq")


# split the input and the out comums (dependent and independent colums)
X = df.iloc[:,0:2]
Y = df.iloc[:,2:]

# train test split
x_train,x_test,y_train,y_test= train_test_split(X,Y,test_size=0.1)

# feature scaling
scal = StandardScaler()
x_test=scal.fit_transform(x_test)
x_train = scal.transform(x_train)

# Train your model
model = LogisticRegression()
model.fit(x_train,y_train)

#pridict the for test sate
y_predict = model.predict(x_test)
df1= pd.DataFrame(y_predict,columns=["Placement"])
print(df1)

#cheaak accuracy score
accuracy = accuracy_score(y_test,y_predict)
print("accuracy score :",accuracy)


test1 = {"CGPA": [1, 8], "IQ": [10, 200]}
df2 = pd.DataFrame(test1)

df2_scaled = scal.transform(df2)

test_predict = model.predict(df2_scaled)
print(test_predict)

# Desicion boundery to see hoe the logasticregeration has worked on our data
plot_decision_regions(X=x_train,y=y_train.values.ravel().astype(int),clf=model,legend=2)
plt.xlabel("CGPA")
plt.ylabel("IQ")
plt.title("Decision Boundary")
plt.show()


# save the model
pickle.dump(model, open('model.pkl', 'wb'))