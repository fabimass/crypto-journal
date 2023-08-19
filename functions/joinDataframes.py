import pandas as pd

def joinDataframes(df1, df2):
    df1["Key"] = df1["Date"].astype(str) + "-" + df1["Token"]
    df2["Key"] = df2["Date"].astype(str) + "-" + df2["Token"]
    result = pd.merge(df2, df1, how='left')
    del result["Key"]
    return result