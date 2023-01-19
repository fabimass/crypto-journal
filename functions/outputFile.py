import pandas as pd

def outputFile(df, path):
    print(f"Creating file {path}...")
    df.to_csv(path, index=False)
    print("OK") 