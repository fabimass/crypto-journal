import pandas as pd
from vars import xlsx_columns

def getTrades(journal):
    # Prepare dataframe for trades
    trading = pd.DataFrame(columns = ["Date", "Token", "Wallet", "Operation", "Amount", "Price", "Value"])

    # Go through the journal file detecting the trading transactions
    for wallet in journal:
        print(f"Detecting trade operations in {wallet}...")
        for i in journal[wallet].index:
            if(journal[wallet][xlsx_columns["operation"]][i] in {"Buy","Sell"}):
                date = journal[wallet][xlsx_columns["date"]][i]
                token = journal[wallet][xlsx_columns["token1"]][i]
                operation = journal[wallet][xlsx_columns["operation"]][i]
                amount = journal[wallet][xlsx_columns["token1_amount"]][i]
                price = journal[wallet][xlsx_columns["price"]][i]
                value = journal[wallet][xlsx_columns["token2_amount"]][i]
                trading.loc[len(trading.index)] = [date, token, wallet, operation, amount, price, value]
        print("OK")

    return trading