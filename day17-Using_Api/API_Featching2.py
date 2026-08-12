import pandas as pd
import requests 



df1 = pd.DataFrame()

for i in range(1, 501):
    responce = requests.get(f'https://api.themoviedb.org/3/movie/popular?api_key=key=a018c7e4695508397e9c629495cbdf75&page&page={i}')
    temp_df = pd.DataFrame(responce.json()['results'])
    temp_df = temp_df[['id', 'title', 'overview']]
    df1 = pd.concat([df1, temp_df], ignore_index=True)

print(df1.shape)
print(df1)