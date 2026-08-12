import pandas as pd
from ydata_profiling import ProfileReport
import seaborn as sns 

iris = sns.load_dataset('iris')
tips =sns.load_dataset('tips')

tipsprof = ProfileReport(tips)
irisprof = ProfileReport(iris)
df = pd.read_csv('Titanic-Dataset.csv')
prof = ProfileReport(df)
prof.to_file('Titanic_EDA.html')
tipsprof.to_file('tips_EDA.html')
irisprof.to_file('iris_EDA.html')   

web = pd.read_csv("AmbationBox_all_Compenies_data.csv")
web_site = ProfileReport(web)
web_site.to_file('ambation_box.html')