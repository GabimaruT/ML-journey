import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Titanic-Dataset.csv')
print(df.sample(5))
print(df['Survived'].value_counts())  # Used to get total count 

#sns.countplot(x='Pclass',data=df) # count plot for categorical data
# Used to display the graph

df['Pclass'].value_counts().plot(kind='pie',autopct='%.2f')  #To see the data in Percentage


plt.hist(df['Age'])   # Use hystogram while dealing with the numerical data

sns.displot(df['Age'])
sns.boxplot(df['Fare'])
sns.boxenplot(df['Age'])