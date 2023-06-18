import numpy as np

def getLast(rows, column, limit=-1):
    atempt = 0
    if limit == -1:
        limit = len(rows)
    rows_reverse = rows.iloc[::-1]
    for index, row in rows_reverse.iterrows():          
        if atempt < limit:
            if not np.isnan(row[column]):
                value = row[column]
                break
            atempt += 1          
        else:
            value = '?'
            break
    return value