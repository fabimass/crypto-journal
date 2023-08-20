import pandas as pd
import yfinance as yfin
from pandas_datareader import data as pdr
from vars import correctors

def getPrice(tokens, ignore, date_start, date_end, suffixes):
    # Prepare dataframe for the prices
    prices_df = pd.DataFrame(columns = ["Date", "High", "Low", "Open", "Close", "Token", "Suffix"])

    # This overrides pandas data reader in order to fix some current issues with the library
    yfin.pdr_override()

    # Prepair the list of symbols
    symbols = []
    for token in tokens:
        if token in ignore:
            print(f"{token} prices will be ignored...")
            pass
        else:
            if suffixes:
                for suffix in suffixes:
                    symbols.append({"symbol": f"{token}{suffix}", "token": token, "suffix": suffix})
            else:
                symbols.append({"symbol": token, "token": token, "suffix": None})

    # Loop through each of the symbols getting the data from Yahoo Finance
    for symbol in symbols:  
        print(f"Getting prices for {symbol['symbol']}...")
        try:
            temp_df = pdr.get_data_yahoo(symbol['symbol'], start=date_start, end=date_end)
            temp_df = temp_df.reset_index(level=0)
            temp_df["Token"] = symbol['token']
            temp_df["Suffix"] = symbol['suffix']
            del temp_df["Volume"]
            del temp_df["Adj Close"]
            print(temp_df)
            if symbol["symbol"] in list(correctors.keys()):
                print(f"Price will be multiplied by {correctors[symbol['symbol']]}...")
                temp_df['High'] = temp_df['High'].apply(lambda x: x * float(correctors[symbol["symbol"]]) if pd.notnull(x) else x)
                temp_df['Low'] = temp_df['Low'].apply(lambda x: x * float(correctors[symbol["symbol"]]) if pd.notnull(x) else x)
                temp_df['Open'] = temp_df['Open'].apply(lambda x: x * float(correctors[symbol["symbol"]]) if pd.notnull(x) else x)
                temp_df['Close'] = temp_df['Close'].apply(lambda x: x * float(correctors[symbol["symbol"]]) if pd.notnull(x) else x)
            prices_df = pd.concat([prices_df, temp_df])
            print("OK")
        except Exception as e:
            print(f"ERROR: Something went wrong...")

    return prices_df