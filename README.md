# Description

This script helps you to track your crypto assets value, by creating easy-to-use datasets that you can connect to data visualization tools like PowerBI or Tableau. You can use it for stock assets too!!

## How to use

You will need to fill the excel file provided in the `input/` folder. Here you will enter the information related to the transactions you make. A few remarks:

- Allowable values in the `Operation` field: `Start`, `Buy`, `Sell`, `Deposit`, `Withdrawal` & `Profits`. Any other value will throw an error.
- The `Start` operation is used to tell the script your initial balance for a given asset. If you don't specify it, the script will assume 0.
- The `Buy`, `Deposit` & `Profits` operations will always increase the balance for the `Main_Token` and decrease it for the `Sec_Token`.
- The `Sell`& `Withdrawal` operations will always increase the balance for the `Sec_Token` and decrease it for the `Main_Token`.
- If you specify a value for the `Fee_Amount` field, it will always decrease the balance for the corresponding `Fee_Token`.

Once you have your excel file ready, you will run the script specifying the following parameters:

- `start`: the start date for the analysis, it should have the format _YYYY-MM-DD_
- `end`: the end date, here you can put a specific date or just use _today_
- `input`: the path of the excel file (this allows you to move the file to wherever you find more convenient)
- `--ignoreprice` (Optional): list of assets that you don't want to track the prices for, separate several values by using a comma
- `--suffix` (Optional): you can indicate a suffix that will be added to each symbol when retrieving its price, use \ to escape special characters, separate several values by using a comma

Example:

```
python main.py 2023-01-01 today ./input/input.xlsx --ignoreprice USD --suffix \-USD
```

The script will create 3 csv files in the `output/` folder:
- `daily.csv` contains the daily balance, price and value for each of your assets in each of your wallets
- `trades.csv` is a summary of the buy/sell transactions where you can find the cumulative profits
- `summary.csv` lists the main metrics for each of your assets
