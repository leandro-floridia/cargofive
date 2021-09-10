from openpyxl import load_workbook

filesheet = ""

wb = load_workbook(filesheet)
celdas = [A1, B2, E1, F1, G1, H1 ]
for cell in celdas:
    print (cell)