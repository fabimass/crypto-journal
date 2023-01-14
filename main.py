import sys
from functions.getParams import getParams
from functions.buildPricesTable import buildPricesTable
from functions.exitScript import exitScript

if __name__ == "__main__":
    # Parse script parameters
    start_date, end_date, assets_list, input_file = getParams(sys.argv)

    # Create prices table
    prices = buildPricesTable(assets_list, start_date, end_date)
    print(prices)


    print("Script executed successfully!!")
    exitScript(0)