# Map variables to the xlsx columns
xlsx_columns = {
    "date": "Date",
    "price": "Price",
    "token1": "Main_Token",
    "token2": "Sec_Token",
    "tokenfee": "Fee_Token",
    "operation": "Operation",
    "token1_amount": "Main_Amount",
    "token2_amount": "Sec_Amount",
    "tokenfee_amount": "Fee_Amount"
}

# Possible operations
zero_operations = {"Start"} # Used to indicate the initial balance
add_operations = {"Buy", "Deposit", "Staking", "Airdrop", "Profits", "Dividends", "Debt"} # These operations increment token1 balance 
subs_operations = {"Sell", "Withdrawal"} # These operations decrement token1 balance    