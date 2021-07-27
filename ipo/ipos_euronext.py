import requests
from bs4 import BeautifulSoup
from random import randint
from time import sleep
import pandas as pd
from urllib.request import urlopen

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36"} 

company_names, agents, symbols, isin_codes, LEI_codes, exchange_markets, trading_locations, ICBs, websites, ipo_dates, ipo_prices, ipo_types, compartiments, operations_des, instruments_names, products_families,capitals_raised = ([] for i in range(17))

urls_df = pd.read_csv("urls.csv", sep = ",")
urls_df.columns = ["url"]

urls_df["url"] = "https://live.euronext.com/" + urls_df["url"].astype(str) 

urls = urls_df["url"].tolist()

nb = 0

for i in urls:
    try:
        page = requests.get(i,headers=headers)
        soup = BeautifulSoup(page.content, "html.parser")
        article = soup.article.find("div").find("div")
        
        try:
            company_name = soup.h1.text
        except AttributeError:
            company_name = "NaN"
            
        try:
            agent = article.find(class_ = "clearfix text-formatted field field--name-field-iponi-listing-sponsor field--type-text-long field--label-above field__items").find("p").text
        except AttributeError:
            agent = "NaN"
        
        try:
            symbol = article.find(class_ = "field field--name-field-iponi-ticker-symbol field--type-string field--label-above field__items").find(class_ = "field__item").text.strip()
        except AttributeError:
            symbol = "NaN"
            
        try:
            isin_code = article.find(class_ = "field field--name-field-iponi-isin-code field--type-string field--label-above field__items").find(class_ = "field__item").text.strip()
        except AttributeError:
            isin_code = "NaN"
            
        try:
            LEI_code = article.find(class_ = "field field--name-field-iponi-lei-code field--type-string field--label-above field__items").find(class_ = "field__item").text.strip()
        except AttributeError:
            LEI_code = "NaN"
            
        try:
            exchange_market = article.find(class_ = "field field--name-field-exchange__market field--type-entity-reference field--label-above field__items").find(class_ = "field__item").text.strip()
        except AttributeError:
            exchange_market = "NaN"
        
        try:
            trading_location = article.find(class_ = "field field--name-field-trading-location field--type-entity-reference field--label-above field__items").find(class_ = "field__item").text.strip()
        except AttributeError:
            trading_location = "NaN"
            
            
        try:
            ICB = article.find(class_ = "field field--name-field-icb field--type-entity-reference field--label-above field__items").find(class_ = "field__item").text.strip()
        except AttributeError:
            ICB = "NaN"
        
        try:
            website = article.find(class_ = "field field--name-field-iponi-website-address field--type-string field--label-above field__items").find(class_ = "field__item").text.strip()
        except AttributeError:
            website = "NaN"
            
        try:
            ipo_date = soup.article.find(class_ = "bg-light-green js-form-item form-item js-form-wrapper form-group col-auto").find(class_ = "datetime").text
        except AttributeError:
            ipo_date = "NaN"
        
        try:
            ipo_price = soup.article.find(class_ = "field field--name-field-iponi-ipo-price field--type-string field--label-above field__items").find(class_ = "field__item").text.strip()
        except AttributeError:
            ipo_price = "NaN"
            
        try:
            ipo_type = soup.article.find(class_ = "field field--name-field-issue-type field--type-entity-reference field--label-above field__items").find(class_ = "field__item").text.strip()
        except AttributeError:
            ipo_type = "NaN"
        
        try:
            compartiment = article.find(class_ = "field field--name-field-capitalization-compartment field--type-entity-reference field--label-above field__items").find(class_ = "field__item").text
        except AttributeError:
            compartiment = "NaN"
            
        try:
            operation_des = soup.article.find(class_ = "clearfix text-formatted field field--name-field-iponi-operation-desc field--type-text-long field--label-above field__items").p.text.strip()
        except AttributeError:
            operation_des = "NaN"
        
        try:
            instrument_name = article.find(class_ = "field field--name-field-iponi-instrument-name field--type-string field--label-above field__items").find(class_ = "field__item").text.strip()
        except AttributeError:
            instrument_name = "NaN"
        
        try:
            products_family = article.find(class_ = "field field--name-field-products-family field--type-entity-reference field--label-above field__items").find(class_ = "field__item").text.strip()
        except AttributeError:
            products_family = "NaN"
            
        try:
            capital_raised = soup.article.find(class_ = "field field--name-field-iponi-capital-raised field--type-string field--label-above field__items").find(class_ = "field__item").text.strip()   
        except AttributeError:
            capital_raised = "NaN"
    
        company_names.append(company_name)
        agents.append(agent)
        symbols.append(symbol)
        isin_codes.append(isin_code)
        LEI_codes.append(LEI_code)
        exchange_markets.append(exchange_market)
        trading_locations.append(trading_location)
        ICBs.append(ICB)
        websites.append(website)
        ipo_dates.append(ipo_date)
        ipo_prices.append(ipo_price)
        ipo_types.append(ipo_type)
        compartiments.append(compartiment)
        operations_des.append(operation_des)
        instruments_names.append(instrument_name)
        products_families.append(products_family)
        capitals_raised.append(capital_raised)
        #sleep(randint(1,2))
        nb = nb + 1
        #print(round(((nb/len(urls))*100),2), "%")
        df = pd.DataFrame(list(zip(company_names, symbols ,ipo_dates, isin_codes, ICBs, ipo_prices, LEI_codes, exchange_markets, agents, trading_locations, websites, ipo_types, compartiments, operations_des, instruments_names, products_families, capitals_raised)),
                   columns =['Company Name', 'Symbol', "Date", "isin", "ICB", "price","LEI","Exchange","Agent","location","website","ipo type","compartiment", "operation description","instrument"," product family","capital raised"])
        #df.to_excel("df_ipos_raw.xlsx", engine='xlsxwriter')
    except:
        pass # doing nothing on exception
    

df.to_excel("df_ipos_raw.xlsx", engine='xlsxwriter')

