import requests
from bs4 import BeautifulSoup
from random import randint
from time import sleep
import pandas as pd


url = "https://live.euronext.com/en/ipo-showcase?field_iponi_ipo_date_value%5Bmin%5D=&field_iponi_ipo_date_value%5Bmax%5D=&page="
page_nb = 105 # should find the variable in html code...

names, dates, isins, locations, markets = ([] for i in range(5))

for i in range(page_nb):
    url_temp= url + str(i)
    response_temp = requests.get(url_temp)
    soup_temp = BeautifulSoup(response_temp.content, "html.parser")
    #rows_temp = soup_temp.find(class_ = "table views-table views-view-table cols-5").find_all("tr")
    rows_temp = soup_temp.find("tbody").find_all("tr")
    for row_temp in rows_temp:
            date = row_temp.find(class_ = "views-field views-field-field-iponi-ipo-date").text.strip()
            name = row_temp.find(class_ = "views-field views-field-field-iponi-display-title").text.strip()
            isin = row_temp.find(class_ = "views-field views-field-field-iponi-isin-code").text.strip()
            location = row_temp.find(class_ = "views-field views-field-term-node-tid").text.strip()
            market = row_temp.find(class_ = "views-field views-field-term-node-tid-1").text.strip()
            names.append(name)
            dates.append(date)
            isins.append(isin)
            locations.append(location)
            markets.append(market)
    sleep(randint(1,3))


#print(markets)

df = pd.DataFrame(list(zip(names, dates, isins, locations, markets)),
               columns =['Company Name', 'Date', "ISIN", "Location", "Market"])


print(df)
