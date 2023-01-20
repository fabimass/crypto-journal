import pandas as pd
import datetime
from vars import xlsx_columns

def getBalance(journal, tokens, start_date, end_date):
    # Possible operations
    zero_operations = {"Start"} # Used to indicate the initial balance
    add_operations = {"Buy", "Deposit", "Staking", "Profits", "Dividends"} # These operations increment token1 balance 
    subs_operations = {"Sell", "Withdrawal"} # These operations decrement token1 balance
    
    # Prepare dataframe for balances
    balance = pd.DataFrame(columns = ["Date", "Token", "Wallet", "Balance"])

    # Go day by day calculating the balance for each token in each wallet
    delta = datetime.timedelta(days=1)
    for wallet in journal:
        for token in tokens:
            print(f"Calculating balance for {token} in {wallet}...")
            date_i = datetime.datetime.strptime(start_date, '%Y-%m-%d')
            while date_i <= datetime.datetime(end_date.year,end_date.month,end_date.day):
                # Look for a match for date and token
                records = journal[wallet][(journal[wallet][xlsx_columns["date"]] == date_i) & ( (journal[wallet][xlsx_columns["token1"]] == token) | (journal[wallet][xlsx_columns["token2"]] == token) | (journal[wallet][xlsx_columns["tokenfee"]] == token) )]  
                if not records.empty:
                    # Found a movement for the token in that date, calculate the new balance
                    for i in records.index:
                        new_balance = -1;  
                        if (records[xlsx_columns["token1"]][i] == token):
                            if (records[xlsx_columns["operation"]][i] in zero_operations):
                                new_balance = records[xlsx_columns["token1_amount"]][i]
                            elif (records[xlsx_columns["operation"]][i] in add_operations):
                                new_balance = balance.loc[len(balance.index)-1].Balance + records[xlsx_columns["token1_amount"]][i]
                            elif (records[xlsx_columns["operation"]][i] in subs_operations):
                                new_balance = balance.loc[len(balance.index)-1].Balance - records[xlsx_columns["token1_amount"]][i]
                        if (records[xlsx_columns["token2"]][i] == token):
                            if (records[xlsx_columns["operation"]][i] in add_operations):
                                if (new_balance == -1):
                                    new_balance = balance.loc[len(balance.index)-1].Balance - records[xlsx_columns["token2_amount"]][i]
                                else:
                                    new_balance -= records[xlsx_columns["token2_amount"]][i]
                            elif (records[xlsx_columns["operation"]][i] in subs_operations):
                                if (new_balance == -1):
                                    new_balance = balance.loc[len(balance.index)-1].Balance + records[xlsx_columns["token2_amount"]][i]
                                else:
                                    new_balance += records[xlsx_columns["token2_amount"]][i]
                        if (records[xlsx_columns["tokenfee"]][i] == token):
                            if (new_balance == -1):
                                new_balance = balance.loc[len(balance.index)-1].Balance - records[xlsx_columns["tokenfee_amount"]][i]
                            else:
                                new_balance -= records[xlsx_columns["tokenfee_amount"]][i]       
                else:
                    if date_i.month == 1 and date_i.day == 1:
                        # Assign 0 as initial balance if there is no 'Start' entry for the token
                        new_balance = 0
                    else:
                        # If no movement is found, copy the last registered balance
                        new_balance = balance.loc[len(balance.index)-1].Balance     
                
                # Insert a new record with the updated balance
                balance.loc[len(balance.index)] = [date_i, token, wallet, new_balance]
                
                date_i += delta
            print("OK")
        
    return balance
