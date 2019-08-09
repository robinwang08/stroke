import os
import xlrd

mainpath = 'F:/Research/newer/'
#mainpath = 'C:/research/deepmedic/data/'

# Give the location of the file
loc = ('F:/Research/list.xlsx')

folders = list()
for root, dirs, files in os.walk(mainpath):
    if dirs not in folders:
        folders.append(dirs)

workbook = xlrd.open_workbook(loc)
sheet = workbook.sheet_by_index(0)

col_a = sheet.col_values(0, 1)
col_b = sheet.col_values(1, 1)

my_dict = {a : b for a, b in zip(col_a, col_b)}

for x in my_dict:
    accession = str(int(x))
    folderNumber = str(int(my_dict.get(x)))
    if not os.path.isdir(mainpath+accession):
        print(accession)
    if os.path.isdir(mainpath+accession):
        old = mainpath + accession
        new = mainpath + folderNumber
        os.rename(old, new)
