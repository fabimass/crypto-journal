import pandas as pd
from functions.getFirst import getFirst

def summarize(daily_df, trades_df):
    # Prepare summary dataframe
    summary_df = pd.DataFrame(columns = ["Token", "Initial_Value", "Current_Value", "Traded_Value", "Profit"])

    # List unique tokens
    tokens = daily_df['Token'].unique().tolist()

    # List unique wallets
    wallets = daily_df['Wallet'].unique().tolist()

    # Go through each token summarizing the values
    for token in tokens:
        print(f"Summarizing for {token}...")
        
        initial_value = 0

        for wallet in wallets:

            # Filter corresponding records
            filtered_records = daily_df[ (daily_df['Wallet'] == wallet) & (daily_df['Token'] == token) ]
            if not filtered_records.empty:
                
                # Grab initial value
                temp = getFirst(filtered_records, 'Value', 5)
                if isinstance(temp, (int, float)):
                    initial_value += temp
                else:    
                    initial_value = temp
                    break
        
        summary_df.loc[len(summary_df.index)] = [token, initial_value, 0, 0, 0]            
    
    return summary_df