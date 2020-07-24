import ezdxf
import pandas as pd
import numpy as np
from csvToExcelPalowania import palowanie_do_excela
import openpyxl
# this file compare projekt.csv and pomiar.csv then it creates lines between results and saves it to dxf file

projekt = pd.read_csv('./resources/projekt.csv')
pomiar = pd.read_csv('./resources/pomiar.csv')
print(projekt.head(5))
print(pomiar.head(5))

dfProjekt = pd.DataFrame(projekt, columns=['nr', 'x', 'y', 'h'])
dfPomiar = pd.DataFrame(pomiar, columns=['nr', 'x1', 'y1', 'h'])

print(dfProjekt.head(5))
print(dfPomiar.head(5))
doc = ezdxf.new()

msp = doc.modelspace()


# for x in range(len(dfPomiar)):
#     for y in range(len(dfProjekt)):
#         if dfProjekt.loc[x, 'nr'] == dfPomiar.loc[y, 'nr']:
#             msp.add_line((dfProjekt[x, 'x'], dfProjekt.loc[x, 'y']), (dfPomiar.loc[y, 'x1'], dfPomiar.loc[y, 'y1']))

for x in dfPomiar.index:
    for y in dfProjekt.index:
        if dfProjekt['nr'][x] == dfPomiar['nr'][y]:
            hatch = msp.add_hatch(color=1)
            edge_path = hatch.paths.add_edge_path()
            edge_path.add_ellipse((dfPomiar['x1'][y], dfPomiar['y1'][y]), major_axis=(0,0.005), ratio=1)
            msp.add_line((dfProjekt['x'][x], dfProjekt['y'][x]), (dfPomiar['x1'][y], dfPomiar['y1'][y]))
            msp.add_line((dfProjekt['x'][x], dfProjekt['y'][x]), (dfPomiar['x1'][y], dfProjekt['y'][x]), dxfattribs = {'color': 4})
            msp.add_line((dfProjekt['x'][x], dfProjekt['y'][x]), (dfProjekt['x'][x], dfPomiar['y1'][y]), dxfattribs = {'color': 2})
            msp.add_aligned_dim(p1=(dfProjekt['x'][x], dfProjekt['y'][x]), p2=(dfPomiar['x1'][y], dfPomiar['y1'][y]),
                                distance=0.05, override={
                    'dimtxsty': 'Standard',
                    'dimtad': 0,
                    'dimtxt': 0.05,
                    'dimclrt': 1,
                    'dimdle': 0.05,
                    'dimlwd': 10,  # 0.1mm line weight
                    'dimblk1': 'DOTSMALL',
                    'dimblk2': 'OPEN',
                    'dimse1': 1,  # suppress first extension line
                    'dimse2': 1,  # suppress second extension line
                }).render()

doc.saveas('./result/lines.dxf')

palowanie_do_excela(dfProjekt)