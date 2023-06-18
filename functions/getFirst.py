import numpy as np

def getFirst(rows, column, limit=-1):
    atempt = 0
    if limit == -1:
        limit = len(rows)
    for index, row in rows.iterrows():          
        if atempt < limit:
            if not np.isnan(row[column]):
                value = row[column]
                break
            atempt += 1          
        else:
            value = '?'
            break
    return value