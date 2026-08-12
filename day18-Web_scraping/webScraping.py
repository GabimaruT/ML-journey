import pandas as pd
import requests
from bs4 import BeautifulSoup

data = requests.get('https://books.toscrape.com/catalogue/page-1.html').text


supe = BeautifulSoup(data,'lxml')


print(supe.find_all('h1')[0].text)
print(supe.find_all('h3')[0].find('a')['title'])

print(len(supe.find_all('a')))
for i in range(1,20):
    print(supe.find_all('a')[i].text.strip())

print("\n")
print(len(supe.find_all('a')))
for i in range(1,20):
    print(supe.find_all('h3')[i].find('a')['title'])
    



print(supe.find_all('div', class_='alert alert-warning')[0].text)

books = supe.find_all('li', class_='col-xs-6 col-sm-4 col-md-3 col-lg-3')

fields = []

for i in books:
    fields.append(i.find('a').text)

print(fields)