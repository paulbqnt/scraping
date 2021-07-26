import pandas as pd 

df = pd.read_excel("df_ipos_raw.xlsx")

df.rename(columns={'isin': 'isin_code'}, inplace=True)

df['Date'] = df['Date'].str[-10:]

df["Date"] = pd.to_datetime(df["Date"], format="%d/%m/%Y")

df = df.sort_values(by="Date", ascending=False)
df = df.drop_duplicates(subset='isin_code', keep="last")

df.to_excel("df_ipos.xlsx")