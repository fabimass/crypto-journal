import pandas as pd
from vars import xlsx_columns

def getTrades(journal):
    # Prepare dataframe for trades
    trading = pd.DataFrame(columns = ["Date", "Token", "Wallet", "Operation", "Amount", "Price", "Value", "Profit"])

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
                profit = 0
                trading.loc[len(trading.index)] = [date, token, wallet, operation, amount, price, value, profit]
        print("OK")

    # Calculate the profit for each operation
    trading.sort_values(["Token", "Date"])
    for row in trading.index:
        if(row == 0 or trading.loc[row,"Token"] != trading.loc[row-1,"Token"]):
            print(f"Calculating profits for {trading.loc[row,'Token']}...")
            if (trading.loc[row,"Operation"] == "Buy"):
                trading.loc[row,"Profit"] = trading.loc[row,"Value"]
            else:
                trading.loc[row,"Profit"] = -trading.loc[row,"Value"]
        else:
            if (trading.loc[row,"Operation"] == "Buy"):
                trading.loc[row,"Profit"] = trading.loc[row-1,"Profit"] + trading.loc[row,"Value"]
            else:
                trading.loc[row,"Profit"] = trading.loc[row-1,"Profit"] - trading.loc[row,"Value"]
    print("OK")
        
    return trading