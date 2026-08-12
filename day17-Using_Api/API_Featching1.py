import pandas as pd
import requests 

responce = requests.get('https://api.themoviedb.org/3/movie/popular?api_key=a018c7e4695508397e9c629495cbdf75')
df = pd.DataFrame(responce.json()['results'])
df = df[['id', 'title', 'overview']]

df1 = pd.DataFrame()

for i in range(0,500):
    responce = requests.get('https://api.themoviedb.org/3/movie/popular?api_key=a018c7e4695508397e9c629495cbdf75&page={i}')
    temp_df = pd.DataFrame(responce.json()['results'])
    temp_df = temp_df[['id', 'title', 'overview']]
    df1=df1.concat([temp_df],ignore_index=True)


print(df1.shape)
print(df1)