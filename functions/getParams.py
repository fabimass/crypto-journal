import argparse
import datetime
from functions.exitScript import exitScript

def getParams():
    parser = argparse.ArgumentParser()
    parser.add_argument("start", help="Start date for the analysis, it should have the format YYYY-MM-DD", action="store")
    parser.add_argument("end", help="End date for the analysis, here you can put a specific date or just use today", action="store")
    parser.add_argument("input", help="Path of the excel file with the transactions", action="store")
    parser.add_argument("--ignoreprice", help="List of assets that you want to track the balance but not the price, you will separate different assets using a comma", action="store")
    parser.add_argument("--suffix", help="This value will be added to each symbol when retrieving the price")
    parser.add_argument("--correctprice", help="List of assets for which you want to apply a correction factor to the price, the nomenclature is token~factor, you will separate different assets using a comma", action="store")
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

    # Get input parameter
    arg_input = args.input

    # Get ignoreprice parameter
    if (args.ignoreprice):
        try:
            arg_ignoreprice = args.ignoreprice.split(",")
        except:
            print("ERROR: Cannot parse the list of assets")
            exitScript(1)
    else:
        arg_ignoreprice = []

    # Get suffix parameter
    if (args.suffix):
        try:
            arg_suffix = args.suffix.replace('\\','').split(",")
        except:
            print("ERROR: Cannot extract the suffix")
            exitScript(1)
    else:
        arg_suffix = None

    # Get correctprice parameter
    if (args.correctprice):
        try:
            arg_corrector = {}
            temp = args.correctprice.split(",")
            for keyvalue in temp:
                arg_corrector[keyvalue.split("~")[0]] = keyvalue.split("~")[1]
        except:
            print("ERROR: Cannot parse the list of assets")
            exitScript(1)
    else:
        arg_corrector = {}

    return arg_from, arg_to, arg_input, arg_ignoreprice, arg_suffix, arg_corrector
