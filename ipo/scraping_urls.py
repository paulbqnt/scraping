import requests
from bs4 import BeautifulSoup
from random import randint
from time import sleep
import pandas as pd

url = "https://live.euronext.com/en/ipo-showcase?field_iponi_ipo_date_value%5Bmin%5D=&field_iponi_ipo_date_value%5Bmax%5D=&page="
links = []

page_nb = 110 # should find a robust method to find the number of pages...

for i in range(page_nb):
    url_temp= url + str(i)
    page = requests.get(url_temp)
    soup = BeautifulSoup(page.content, "html.parser")
    for link in soup.tbody.find_all('a'):
        links.append(link.get("href"))
    
    # A few seconds of pauses between each iteration to avoid
    # being detected and blocked by the website
    sleep(randint(1,3)) 
    print("step number",i, "on  110")

    
df = pd.DataFrame(list(zip(links)),columns =['Urls'])
df.to_csv("/home/zalman/Documents/code/python/test_linkedin/urls.csv")
