import pandas as pd
import requests
import time

url = "https://api.themoviedb.org/3/movie/top_rated"

headers = {
    "User-Agent": "Mozilla/5.0"
}

df_list = []

for i in range(1, 429):
    try:
        params = {
            "api_key": "a018c7e4695508397e9c629495cbdf75",
            "language": "en-US",
            "page": i
        }

        response = requests.get(url, params=params, headers=headers, timeout=20)

        print("Page:", i, "Status:", response.status_code)

        data = response.json()

        df = pd.DataFrame(data["results"])[
            ["id", "title", "overview", "release_date", "popularity", "vote_average", "vote_count"]
        ]

        df_list.append(df)

        time.sleep(0.5)

    except Exception as e:
        print("Error on page:", i)
        print(e)
        continue

df1 = pd.concat(df_list, ignore_index=True)
df1.to_csv("movies.csv")
print(df1)