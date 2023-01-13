import sys
import getopt
import datetime

def getParams(argv):
    arg_from = ""
    arg_to = ""
    arg_assets = []
    arg_input = ""
    arg_help = f"{format(argv[0])} --from 2023-01-01 --to today --assets BTC,ETH --input ./input/input.xlsx"

    try:
        opts, args = getopt.getopt(argv[1:], "hf:t:a:i:", ["help", "from=", "to=", "assets=", "input="])      

    except:
        print(f"ERROR: Wrong parameters passed.\n Example of usage:\n{arg_help}")
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            # print the help message
            print(arg_help)  
            sys.exit(2)
        elif opt in ("-f", "--from"):
            # obtain the start date
            arg_from = arg
        elif opt in ("-t", "--to"):
            # obtain the end date
            if (arg == "today"):
                arg_to = datetime.date.today()
            else:
                arg_to = arg 
        elif opt in ("-a", "--assets"):
            # obtain and parse the assets list
            arg_assets = arg.split(",")
        elif opt in ("-i", "--input"):
            # obtain the input file path
            arg_input = arg

    # check for missing parameters
    if (arg_from == ""):
        print("ERROR: required --from parameter is missing")
        sys.exit(2)
    if (arg_to == ""):
        print("ERROR: required --to parameter is missing")
        sys.exit(2)
    if (len(arg_assets) == 0):
        print("ERROR: required --assets parameter is missing")
        sys.exit(2)
    if (arg_input == ""):
        print("ERROR: required --input parameter is missing")
        sys.exit(2)

    return arg_from, arg_to, arg_assets, arg_input
