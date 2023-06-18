import numpy as np

def calculateValue(daily_df):
    result = daily_df
    result["Value"] = 0
    result["Value"] = np.where(result['Balance'] == 0, 0, result['Balance'] * result['Close'])
    return result