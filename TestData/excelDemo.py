import openpyxl

book = openpyxl.load_workbook("C:\\Mohana\\PythonDemo.xlsx")
sheet = book.active
Dict = {}
cell = sheet.cell(row=1, column=2)
print(cell.value)

