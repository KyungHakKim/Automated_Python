import openpyxl as op

wb = op.load_workbook("test.xlsx")
ws = wb["update"]

# for row_rng in ws.rows:
#     print(row_rng)

# for col_rng in ws.columns:
#     print(col_rng)    
    
for row_rng in ws.rows:
    for cell in row_rng:
        print(cell.value)    
        
print("-----------------------------------")        
for col_rng in ws.columns:
    for cell in col_rng:
        if cell.value != None:
            print(cell.value)            