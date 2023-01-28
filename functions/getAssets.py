from vars import xlsx_columns
from functions.exitScript import exitScript

def getAssets(journal):
    print("Extracting list of assets...")
    assets_list = []
    try:
        for wallet in journal:
            for i in {xlsx_columns["token1"], xlsx_columns["token2"], xlsx_columns["tokenfee"]}:
                assets_list += journal[wallet][i].unique().tolist()
    except Exception as e:
        print(e)
        print(f"ERROR: Couldn't extract list of tokens")
        exitScript(2)
    print("OK")
    
    # I need only the unique values, use the filter to remove nan
    assets_list_unique = set(filter(lambda x: x == x , assets_list))

    return assets_list_unique