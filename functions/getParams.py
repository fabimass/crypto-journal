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
            arg_to = arg
        elif opt in ("-a", "--assets"):
            # obtain and parse the assets list
            arg_assets = arg
        elif opt in ("-i", "--input"):
            # obtain the input file path
            arg_input = arg

    print('From:', arg_from)
    print('To:', arg_to)
    print('Assets:', arg_assets)
    print('Input:', arg_input)
