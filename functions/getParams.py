import argparse
import datetime
from functions.exitScript import exitScript

def getParams():
    parser = argparse.ArgumentParser()
    parser.add_argument("start", help="Start date for the analysis, it should have the format YYYY-MM-DD", action="store")
    parser.add_argument("end", help="End date for the analysis, here you can put a specific date or just use today", action="store")
    parser.add_argument("assets", help="List of assets that you want to track. Here you will use the symbol of the asset, not the name (e.g. you will use BTC instead of Bitcoin), and you will separate different assets using a comma", action="store")
    parser.add_argument("input", help="Path of the excel file with the transactions", action="store")
    parser.add_argument("--noprice", help="List of assets that you want to track the balance but not the price, you will separate different assets using a comma", action="store")
    args = parser.parse_args()

    # Get start parameter
    try:
        datetime.datetime.strptime(args.start, '%Y-%m-%d')
        arg_from = args.start
    except:
        print("ERROR: Incorrect data format, should be YYYY-MM-DD")
        exitScript(1)

    # Get end parameter
    if (args.end == "today"):
        arg_to = datetime.date.today()
    else:
        try:
            datetime.datetime.strptime(args.end, '%Y-%m-%d')
            arg_to = args.end
        except:
            print("ERROR: Incorrect data format, should be YYYY-MM-DD")
            exitScript(1)

    # Get assets parameter
    try:
        arg_assets = args.assets.split(",")
    except:
        print("ERROR: Cannot parse the list of assets")
        exitScript(1)

    # Get input parameter
    arg_input = args.input

    # Get noprice parameter
    if (args.noprice):
        try:
            arg_noprice = args.noprice.split(",")
        except:
            print("ERROR: Cannot parse the list of assets")
            exitScript(1)
    else:
        arg_noprice = []

    return arg_from, arg_to, arg_assets, arg_input, arg_noprice
