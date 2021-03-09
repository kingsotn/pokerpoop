import openpyxl

excel_files = ['/Users/kingston/Desktop/POKER/poker2.xlsm', '/Users/kingston/Desktop/POKER/poker.xlsm']

values = []

for file in excel_files:
    workbook = openpyxl.load_workbook(file)
    worksheet = ''