import pandas as pd
from functions.exitScript import exitScript

def getInput(input_file):
    print("Opening input file...")
    try:
        input_df = pd.read_excel(input_file, sheet_name=None, header=1)
    except:
        print(f"ERROR: Couldn't open file at: {input_file}")
        exitScript(2)
    print("OK")
    return input_df