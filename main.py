import sys
from functions.getParams import getParams

if __name__ == "__main__":
    # Parse script parameters
    start_date, end_date, assets_list, input_file = getParams(sys.argv)

    print('From:', start_date)
    print('To:', end_date)
    print('Assets:', assets_list)
    print('Input:', input_file)


    print("Script executed successfully!!\n Enter any key to exit")
    input()