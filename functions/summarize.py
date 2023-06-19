import pandas as pd
import numpy as np
from functions.getFirst import getFirst
from functions.getLast import getLast

def summarize(daily_df, trades_df):
    # Prepare summary dataframe
    summary_df = pd.DataFrame(columns = ["Token", "Initial_Value", "Current_Value", "Traded_Value", "Profit"])
    summary_wallet_df = pd.DataFrame(columns = ["Wallet", "Token", "Current_Value", "Current_Balance"])

    # List unique tokens
    tokens = daily_df['Token'].unique().tolist()

    # List unique wallets
    wallets = daily_df['Wallet'].unique().tolist()

    # Go through each token summarizing the values
    for token in tokens:
        print(f"Summarizing for {token}...")
        
        initial_value = 0
        traded_value = 0
        current_value = 0

        for wallet in wallets:
            # Filter corresponding records in the daily dataframe
            filtered_records = daily_df[ (daily_df['Wallet'] == wallet) & (daily_df['Token'] == token) ]
            if not filtered_records.empty:   
                # Grab initial value
                temp = getFirst(filtered_records, 'Value', 5)
                if isinstance(initial_value, (int, float)):
                    if isinstance(temp, (int, float)):
                        initial_value += temp
                    else:    
                        initial_value = temp                  
                # Grab current value
                temp = getLast(filtered_records, 'Value', 5)
                if isinstance(current_value, (int, float)):
                    if isinstance(temp, (int, float)):
                        current_value += temp
                    else:    
                        current_value = temp   
                # Add record in the wallet summary
                summary_wallet_df.loc[len(summary_wallet_df.index)] = [wallet, token, getLast(filtered_records, 'Value', 5), getLast(filtered_records, 'Balance', 5)]

        # Filter corresponding records in the trades dataframe
        filtered_records = trades_df[ (trades_df['Token'] == token) ]
        if not filtered_records.empty:
            # Grab traded value
            traded_value = getLast(filtered_records, 'Profit')
        
        summary_df.loc[len(summary_df.index)] = [token, initial_value, current_value, traded_value, 0]

    # Calculate overall profit
    for index, row in summary_df.iterrows():
        if row["Initial_Value"] == '?' or row["Current_Value"] == '?' or row["Traded_Value"] == '?':
            summary_df.loc[index,"Profit"] = '?'
        else:
            summary_df.loc[index,"Profit"] = row["Current_Value"] - row["Initial_Value"] + row["Traded_Value"]           
    
    return summary_df, summary_wallet_df