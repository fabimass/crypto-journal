import pandas as pd
from vars import xlsx_columns, trade_operations

def find_closest_key(dictionary, target_value):
    closest_key = None
    min_difference = float('inf')  # Initialize with positive infinity

    for key, value in dictionary.items():
        difference = abs(value - target_value)
        if difference < min_difference:
            min_difference = difference
            closest_key = key

    return closest_key

def getTrades(journal, suffixes, prices):
    # Prepare dataframe for trades
    trading = pd.DataFrame(columns = ["Date", "Token", "Wallet", "Suffix", "Operation", "Amount", "Price", "Value", "Profit"])

    # Go through the journal file detecting the trading transactions
    for wallet in journal:
        print(f"Detecting trade operations in {wallet}...")
        for i in journal[wallet].index:
            if(journal[wallet][xlsx_columns["operation"]][i] in trade_operations):
                if suffixes:
                    temp_value = journal[wallet][xlsx_columns["price"]][i] * journal[wallet][xlsx_columns["token1_amount"]][i]
                    values = {}
                    for suffix in suffixes:
                        prices_row = prices[prices['Date'] == journal[wallet][xlsx_columns["date"]][i] and prices['Token'] == journal[wallet][xlsx_columns["token1"]][i] and prices['Suffix'] == suffix]
                        values[suffix] = prices_row["Close"]
                    closest_key = find_closest_key(values, temp_value)
                    for suffix in suffixes:
                        date = journal[wallet][xlsx_columns["date"]][i]
                        token = journal[wallet][xlsx_columns["token1"]][i]
                        operation = journal[wallet][xlsx_columns["operation"]][i]
                        amount = journal[wallet][xlsx_columns["token1_amount"]][i]    
                        if suffix == closest_key:
                            price = journal[wallet][xlsx_columns["price"]][i]
                            value = journal[wallet][xlsx_columns["token2_amount"]][i]
                        else:
                            price = journal[wallet][xlsx_columns["price"]][i] * prices[prices['Date'] == date and prices['Token'] == token and prices['Suffix'] == suffix]["Close"] / prices[prices['Date'] == date and prices['Token'] == token and prices['Suffix'] == closest_key]["Close"]
                            value = price * amount
                        profit = 0
                        trading.loc[len(trading.index)] = [date, token, wallet, suffix, operation, amount, price, value, profit]

                else:
                    date = journal[wallet][xlsx_columns["date"]][i]
                    token = journal[wallet][xlsx_columns["token1"]][i]
                    operation = journal[wallet][xlsx_columns["operation"]][i]
                    amount = journal[wallet][xlsx_columns["token1_amount"]][i]    
                    price = journal[wallet][xlsx_columns["price"]][i]
                    value = journal[wallet][xlsx_columns["token2_amount"]][i]
                    suffix = None
                    profit = 0
                    trading.loc[len(trading.index)] = [date, token, wallet, suffix, operation, amount, price, value, profit]
        print("OK")

    trading = trading.sort_values(["Token", "Suffix", "Date"])
    trading.reset_index(inplace=True)
    del trading["index"]

    # Calculate the profit for each operation
    for row in trading.index:
        # Checks if it is the very first row or if the token changed
        if(row == 0 or trading.loc[row,"Token"] != trading.loc[row-1,"Token"] or trading.loc[row,"Suffix"] != trading.loc[row-1,"Suffix"]):
            print(f"Calculating profits for {trading.loc[row,'Token']}...")
            if (trading.loc[row,"Operation"] == "Buy"):
                trading.loc[row,"Profit"] = -trading.loc[row,"Value"]
            else:
                trading.loc[row,"Profit"] = trading.loc[row,"Value"]
        # If it goes here, it is not the first trade for the token, so previous value needs to be considered for the profit calculation
        else:
            if (trading.loc[row,"Operation"] == "Buy"):
                trading.loc[row,"Profit"] = trading.loc[row-1,"Profit"] - trading.loc[row,"Value"]
            else:
                trading.loc[row,"Profit"] = trading.loc[row-1,"Profit"] + trading.loc[row,"Value"]
    print("OK")
        
    return trading