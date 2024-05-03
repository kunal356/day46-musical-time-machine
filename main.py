import requests
from bs4 import BeautifulSoup

date = input("Which year do you want to travel to? Type date in this format YYYY-MM-DD")
response = requests.get(f'https://www.billboard.com/charts/hot-100/{date}')
soup = BeautifulSoup(response.text, "html.parser")
# print(soup)
top_100 = [i.text.strip() for i in soup.select("li.o-chart-results-list__item h3.c-title")]
print(top_100)
