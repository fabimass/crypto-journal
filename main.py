from functions.getParams import getParams
from functions.getPrice import getPrice
from functions.getInput import getInput
from functions.getAssets import getAssets
from functions.getBalance import getBalance
from functions.getTrades import getTrades
from functions.getOther import getOther
from functions.joinDataframes import joinDataframes
from functions.outputFile import outputFile
from functions.exitScript import exitScript
from functions.calculateValue import calculateValue
from functions.summarize import summarize
import pathlib

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
    balance_df = getBalance(input_df, assets_list, symbol_suffix, start_date, end_date)
    
    # Join both dataframes
    daily_df = joinDataframes(price_df, balance_df)

    # Having Balance and Price, calculate Value
    daily_df = calculateValue(daily_df)

    # Get trading operations
    trades_df = getTrades(input_df, ignoreprice_list, symbol_suffix, price_df)

    # Get other operations
    other_df = getOther(input_df)

    # Calculate summary
    summary_df, summary_wallet_df = summarize(daily_df, trades_df)

    # Output to csv file
    if not pathlib.Path(__file__).parent.joinpath("output").is_dir():
        pathlib.Path(__file__).parent.joinpath("output").mkdir()
    outputFile(daily_df.sort_values(["Wallet", "Token", "Date"]), "output/daily.csv")
    outputFile(trades_df, "output/trades.csv")
    outputFile(summary_df, "output/summary.csv")
    outputFile(summary_wallet_df, "output/summary_wallet.csv")
    outputFile(other_df, "output/others.csv")

    print("Script executed successfully!!")
    exitScript(0)