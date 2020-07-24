import openpyxl
import pandas as pd

#dataFrame1, dataFrame2

def palowanie_do_excela(projekt):
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Pale"
    ws.sheet_properties.tabColor = "00ff00"
    ws['B1'] = 'TABELA zbiorcza'
    ws['A2'] = 'pomiar powykonawczy oczepow'
    ws['A3'] = 'Projektowana S7 – na odcinku Koszwały Kazimierzowo'
    ws['A4'] = 'Projekt'
    ws['G4'] = 'Inwentaryzacja'
    ws.merge_cells('A4:F4')
    ws.merge_cells('G4:M4')

    for element in projekt.index:
        ws['C' + str(6+element)] = projekt['nr'][element]

    
    wb.save("./result/palowanie.xlsx")
