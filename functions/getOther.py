import pandas as pd
from vars import xlsx_columns, other_operations

def getOther(journal):
    # Prepare dataframe for others
    trading = pd.DataFrame(columns = ["Date", "Token", "Wallet", "Operation", "Amount"])

    # Go through the journal file detecting the other transactions
    for wallet in journal:
        print(f"Detecting other operations in {wallet}...")
        for i in journal[wallet].index:
            if(journal[wallet][xlsx_columns["operation"]][i] in other_operations):
                date = journal[wallet][xlsx_columns["date"]][i]
                token = journal[wallet][xlsx_columns["token1"]][i]
                operation = journal[wallet][xlsx_columns["operation"]][i]
                amount = journal[wallet][xlsx_columns["token1_amount"]][i]
                trading.loc[len(trading.index)] = [date, token, wallet, operation, amount]
        print("OK")

    trading = trading.sort_values(["Token", "Date"])
    trading.reset_index(inplace=True)
    del trading["index"]
        
    return trading