import pandas as pd

url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

df = pd.read_html(url)
df = df[0] # select the first table
df.to_csv("sp500.csv", index=False)
