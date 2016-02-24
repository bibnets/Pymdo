#!/usr/bin/python
# openpyxl operate excel rows

from openpyxl import Workbook
from openpyxl import load_workbook

wb = load_workbook(filename = 'test.xlsx')
ws1 = wb.worksheets[0]


for row in ws1.rows:
    for col in row:
        ns_name = col.value
        print ns_name

