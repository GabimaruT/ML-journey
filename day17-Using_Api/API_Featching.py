import pandas as pd
import requests

response = requests.get("https://api.themoviedb.org/3/movie/popular?api_key=a018c7e4695508397e9c629495cbdf75")
# to get ap key login on TMDB website go to seating and in api section you will get your api key
#put the apikey in your api and now you can see your data


data = response.json()

df = pd.DataFrame(data["results"])
df = df[["id", "title", "overview"]]

print(df)
df.to_csv('movies.csv') 