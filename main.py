import sys
from functions.getParams import getParams
from functions.getPrice import getPrice
from functions.getInput import getInput
from functions.getBalance import getBalance
from functions.getTrades import getTrades
from functions.joinDataframes import joinDataframes
from functions.outputFile import outputFile
from functions.exitScript import exitScript

if __name__ == "__main__":
    # Parse script parameters
    start_date, end_date, assets_list, input_file = getParams(sys.argv)

    # Create prices table
    price_df = getPrice(assets_list, start_date, end_date)

    # Read input file
    input_df = getInput(input_file)
    
    # Calculate balance
    balance_df = getBalance(input_df, assets_list, start_date, end_date)

    # Join both dataframes
    joined_df = joinDataframes(price_df, balance_df, "Date", "Date")
    
    # Output to csv file
    outputFile(joined_df.sort_values(["Wallet", "Token", "Date"]), "output/results.csv")

    # Get trading operations
    trades_df = getTrades(input_df)

    print("Script executed successfully!!")
    exitScript(0)