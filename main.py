import sys
from functions.getParams import getParams
from functions.getPrice import getPrice
from functions.getInput import getInput
from functions.exitScript import exitScript

if __name__ == "__main__":
    # Parse script parameters
    start_date, end_date, assets_list, input_file = getParams(sys.argv)

    # Create prices table
    price_df = getPrice(assets_list, start_date, end_date)

    # Read input file
    input_df = getInput(input_file)
    print(input_df)

    print("Script executed successfully!!")
    exitScript(0)