from bs4 import BeautifulSoup
import requests
import pandas as pd

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"}
all_data = []
for i in range(1,500) :
    url = f"https://www.ambitionbox.com/list-of-companies?campaign=desktop_nav&page={i}"
    data = requests.get(url,headers = headers).text
    supe = BeautifulSoup(data,"lxml")

    cards = supe.find_all('div',class_='companyCardWrapper')

    print("Page",i,"cards",len(cards))

    for card in cards :
        name_tag = card.find('h2')
        rating_tag = card.find('span',class_='companyCardWrapper__companyRatingValue')
        info_tag = card.find('span',class_='companyCardWrapper__interLinking')
        counts = card.find_all('span',class_='companyCardWrapper__ActionCount')

        all_data.append({
            "name":name_tag.text.strip() if name_tag else None,
            "Rating":rating_tag.text.strip() if rating_tag else None,
            "Information":info_tag.text.strip() if info_tag else None,
            "Reviews" : counts[0].text.strip() if len(counts)>0 else None,
            "Salaries" : counts[1].text.strip() if len(counts)>1 else None,
            "Interviews" : counts[2].text.strip() if len(counts)>2 else None,
            "Jobs" : counts[3].text.strip() if len(counts)>3 else None,
            "Benefits" : counts[4].text.strip() if len(counts)>4 else None,

        })

    df = pd.DataFrame(all_data)
    df.to_csv("AmbationBox_all_Compenies_data.csv",index=False)
    