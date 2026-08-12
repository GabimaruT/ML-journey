import requests
from bs4 import BeautifulSoup
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
}

all_data = []

for page in range(1, 500):

    url = f"https://www.ambitionbox.com/list-of-companies?campaign=desktop_nav&page={page}"
    data = requests(url,headers = headers).text

    supe = BeautifulSoup(data, "lxml")

    cards = supe.find_all('div', class_='companyCardWrapper')

    print("Page:", page, "Cards:", len(cards))

    for card in cards:
        name_tag = card.find('h2')
        info_tag = card.find('span', class_='companyCardWrapper__interLinking')
        rating_tag = card.find('span', class_='companyCardWrapper__companyRatingValue')
        counts = card.find_all('span', class_='companyCardWrapper__ActionCount')

        all_data.append({
            "Name": name_tag.text.strip() if name_tag else None,
            "Info": info_tag.text.strip() if info_tag else None,
            "Rating": rating_tag.text.strip() if rating_tag else None,
            "Reviews": counts[0].text.strip() if len(counts) > 0 else None,
            "Salaries": counts[1].text.strip() if len(counts) > 1 else None,
            "Interviews": counts[2].text.strip() if len(counts) > 2 else None,
            "   ": counts[3].text.strip() if len(counts) > 3 else None,
            "Benefits": counts[4].text.strip() if len(counts) > 4 else None,
        })

df = pd.DataFrame(all_data)

df.to_csv("ambitionbox_companies.csv", index=False)

print(df)