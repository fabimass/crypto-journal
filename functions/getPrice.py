import pandas as pd
import yfinance as yfin
from pandas_datareader import data as pdr

def getPrice(tokens, ignore, date_start, date_end):
    # Prepare dataframe for the prices
    prices_df = pd.DataFrame(columns = ["Date", "High", "Low", "Open", "Close", "Token"])

    # This overrides pandas data reader in order to fix some current issues with the library
    yfin.pdr_override()

    # Loop through each of the tokens getting the data from Yahoo Finance
    for token in tokens:
        if( token in ignore):
            pass
        else:
            print(f"Getting prices for {token}...")
            try:
                symbol = token + "-USD"
                temp_df = pdr.get_data_yahoo(symbol, start=date_start, end=date_end)
                temp_df = temp_df.reset_index(level=0)
                temp_df["Token"] = token
                del temp_df["Volume"]
                del temp_df["Adj Close"]
                prices_df = pd.concat([prices_df, temp_df])
                print("OK")
            except:
                print(f"ERROR: Something went wrong...")

    return prices_df