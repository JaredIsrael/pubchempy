import re
import xlsxwriter
import requests
import sys
import json

#pubchem id, IUPAC name, molecular weight, chemical formula, LC or GC spectra
properties = ["IUPACName", "MolecularWeight", "MolecularFormula"]

if(len(sys.argv)==1):
    print("Please add compounds text file")
    exit()

wb= xlsxwriter.Workbook("xlspy.xlsx")
ws = wb.add_worksheet()

try:
    f = open(sys.argv[1])
except IOError as e:
    print(e)
lines = f.read().splitlines();

ws.write(0,0, "Compound")
ws.write(0,1, "CID")
ws.write(0,2, "IUPAC Name")
ws.write(0,3, "Molecular Weight")
ws.write(0,4, "Molecular Formula")

row = 1
column = 2

for compound in lines:
    ws.write(row, 0, compound)
    #For some reason you can't directly get the ID, so we get the record and take ID from there
    recordUrl = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/"+compound+"/record/json"

    for property in properties:
        url = "https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/"+compound+"/property/"+property+"/txt"
        response = requests.get(url)
        if(response.status_code == 200):
            ws.write(row,column,response.text)
        else:
            ws.write(row,column,"ERROR")
        column+=1
    row+=1
    column = 2

wb.close()