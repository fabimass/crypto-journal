from functions.getParams import getParams
from functions.getPrice import getPrice
from functions.getInput import getInput
from functions.getAssets import getAssets
from functions.getBalance import getBalance
from functions.getTrades import getTrades
from functions.joinDataframes import joinDataframes
from functions.outputFile import outputFile
from functions.exitScript import exitScript

if __name__ == "__main__":
    # Parse script parameters
    start_date, end_date, input_file, ignoreprice_list, symbol_suffix = getParams()
    
    # Read input file
    input_df = getInput(input_file)

    # Extract the list of assets
    assets_list = getAssets(input_df)

    # Create prices table
    price_df = getPrice(assets_list, ignoreprice_list, start_date, end_date, symbol_suffix)
    
    # Calculate balance
    balance_df = getBalance(input_df, assets_list, start_date, end_date)

    # Join both dataframes
    joined_df = joinDataframes(price_df, balance_df, "Date", "Date")
    
    # Output to csv file
    outputFile(joined_df.sort_values(["Wallet", "Token", "Date"]), "output/results.csv")

    # Get trading operations
    trades_df = getTrades(input_df)

    # Output to csv file
    outputFile(trades_df, "output/trades.csv")

    print("Script executed successfully!!")
    exitScript(0)