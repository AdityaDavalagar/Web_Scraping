# import xlrd 
  
# loc = ("C:/Users/ramky/Desktop/webscraping/excelsht.xlsx") 
  
# wb = xlrd.open_workbook(loc) 
# sheet = wb.sheet_by_index(0) 
  
# # For row 0 and column 0 
# sheet.cell_value(0, 0) 
  
# for i in range(sheet.ncols): 
#     print(sheet.cell_value(1, i)) 

# import xlrd 
  
# loc = ("C:/Users/ramky/Desktop/webscraping/excelsht.xlsx") 
  
# wb = xlrd.open_workbook(loc) 
# sheet = wb.sheet_by_index(0) 
  
# sheet.cell_value(0, 0) 
  
# print(sheet.row_values(1)) 

from xlrd import open_workbook
wb = open_workbook('excelsht.xlsx')
values = []
for s in wb.sheets():
    #print 'Sheet:',s.name
    
    for row in range(s.nrows):
        col_value = []
        for col in range(s.ncols):
            value  = (s.cell(row,col).value)
            try : value = str(int(value))
            except : pass
            col_value.append(value)
        values.append(col_value)
print (values)