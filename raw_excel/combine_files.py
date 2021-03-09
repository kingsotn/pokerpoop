import pandas as pd

excel_files = ['/Users/kingston/Desktop/POKER/poker2.xlsm', '/Users/kingston/Desktop/POKER/poker.xlsm']

merge = pd.DataFrame()

for file in excel_files:
    df = pd.read_excel(file, skiprows = 2)
    merge = merge.append(df, ignore_index = True)br


