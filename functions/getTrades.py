import pandas as pd
from vars import xlsx_columns, trade_operations, token_suffixes

def getTrades(journal, ignore_list, suffixes, prices):
    # Prepare dataframe for trades
    trading = pd.DataFrame(columns = ["Date", "Token", "Wallet", "Suffix", "Operation", "Amount", "Price", "Value", "Profit"])

    # Go through the journal file detecting the trading transactions
    for wallet in journal:
        print(f"Detecting trade operations in {wallet}...")
        for i in journal[wallet].index:
            if(journal[wallet][xlsx_columns["operation"]][i] in trade_operations and journal[wallet][xlsx_columns["token1"]][i] not in ignore_list):
                
                if suffixes:
                    close_prices = {}
                    for suffix in suffixes:
                        prices_row = prices[(prices['Date'] == journal[wallet][xlsx_columns["date"]][i]) & (prices['Token'] == journal[wallet][xlsx_columns["token1"]][i]) & (prices['Suffix'] == suffix)]
                        close_prices[suffix] = prices_row.iloc[0]['Close'] if not prices_row.empty else -1
                    
                    for suffix in suffixes:
                        date = journal[wallet][xlsx_columns["date"]][i]
                        token = journal[wallet][xlsx_columns["token1"]][i]
                        operation = journal[wallet][xlsx_columns["operation"]][i]
                        amount = journal[wallet][xlsx_columns["token1_amount"]][i]
                          
                        if suffix == token_suffixes[journal[wallet][xlsx_columns["token2"]][i]]:
                            price = journal[wallet][xlsx_columns["price"]][i]
                            value = journal[wallet][xlsx_columns["token2_amount"]][i]
                        else:
                            if close_prices[token_suffixes[journal[wallet][xlsx_columns["token2"]][i]]] != -1 and close_prices[suffix] != -1:
                                price = journal[wallet][xlsx_columns["price"]][i] * close_prices[suffix] / close_prices[token_suffixes[journal[wallet][xlsx_columns["token2"]][i]]]
                                value = price * amount
                            else:
                                price = None
                                value = None

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
            print(f"Calculating profits for {trading.loc[row,'Token']}{trading.loc[row,'Suffix']}...")
            if (trading.loc[row,"Value"] is None):
                trading.loc[row,"Profit"] = None
            elif (trading.loc[row,"Operation"] == "Buy"):
                trading.loc[row,"Profit"] = -trading.loc[row,"Value"]
            else:
                trading.loc[row,"Profit"] = trading.loc[row,"Value"]
        # If it goes here, it is not the first trade for the token, so previous value needs to be considered for the profit calculation
        else:
            if (trading.loc[row,"Value"] is None):
                trading.loc[row,"Profit"] = None
            elif (trading.loc[row,"Operation"] == "Buy"):
                trading.loc[row,"Profit"] = trading.loc[row-1,"Profit"] - trading.loc[row,"Value"]
            else:
                trading.loc[row,"Profit"] = trading.loc[row-1,"Profit"] + trading.loc[row,"Value"]
    print("OK")
        
    return trading