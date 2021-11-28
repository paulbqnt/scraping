import pandas as pd
import time
import datetime

# two arbitrary dates to cover as much historical data as possible...
date_1 = int(time.mktime(datetime.datetime(1950,12,1,23,59).timetuple()))
date_2 = int(time.mktime(datetime.datetime(2021,12,31,23,59).timetuple()))

# adapt your path 
tickers_df = pd.read_csv("/home/zalman/Documents/code/python/test_linkedin/sp500.csv")


# convert ticker column from csv to list
tickers = tickers_df["Ticker"].to_list()
print(tickers)


stock_not_imported = [] # empty list to receive not downloaded tickers
step = 1
for ticker in tickers:
    # try allows to go to the next iteration in case of error in the loop
    try:
        query_string = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={date_1}&period2={date_2}&interval=1d&events=history&includeAdjustedClose=true"
        df = pd.read_csv(query_string)
        df.to_csv("/home/zalman/Documents/code/python/test_linkedin/data/" + ticker + ".csv")
        print("step: ", step, " on", len(tickers), " ", ticker, "is now imported as CSV")
        step += 1

        # 4 seconds between each iteration to limit the risk of being blocked by the website
        time.sleep(4)

    except:
        print("Cannot import ", ticker)
        stock_none_imported = stock_not_imported.append(ticker)
        step += 1
        pass # doing nothing on exception

print("The following stocks cannot being imported: ", stock_not_imported)
