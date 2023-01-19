import pandas as pd

def joinDataframes(df1, df2, key1, key2):
    df1["Key"] = df1[key1].astype(str) + "-" + df1["Token"]
    df2["Key"] = df2[key2].astype(str) + "-" + df2["Token"]
    result = pd.merge(df2, df1, how='inner')
    del result["Key"]
    return result