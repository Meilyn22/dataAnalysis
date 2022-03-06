import pandas as pd

import pandas as pd
from bs4 import BeautifulSoup as bs
import requests


r = requests.get("https://en.wikipedia.org/wiki/Toy_Story_3")

soup = bs(r.content)

contents = soup.prettify()
print(contents)

info_box = soup.find(class_ = "infobox vevent")
info_rows = info_box.find_all("tr")
for row in info_rows:
    print(row.prettify())
    
def get_content_value(row_data):
    if row_data.find('li'):
        return [li.get_text().replace('\xa0', " ") for li in row_data.find_all('li')]
    else:
        return row_data.get_text().replace('\xa0', " ")
    
movie_info = {}

for index, row in enumerate (info_rows):
    if index == 0:
        movie_info['title'] = row.find('th').get_text()
    elif index == 1:
        continue
    else:
        content_key = row.find('th').get_text()
        content_value = get_content_value(row.find('td'))
        movie_info[content_key] = content_value

movie_info