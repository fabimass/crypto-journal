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
- `assets`: the list of assets that you want to track. Here you will use the symbol of the asset, not the name (e.g. you will use _BTC_ instead of _Bitcoin_), and you will separate different assets using a comma
- `input`: the path of the excel file (this allows you to move the file to wherever you find more convenient)

Example:

```
python main.py --from 2023-01-01 --to today --assets BTC,ETH --input ./input/input.xlsx
```
