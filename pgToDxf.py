import ezdxf
import pandas as pd
import numpy as np

punkty_glowne = pd.read_csv("./resources/pg.csv", names=['x','y','z'])
# print(punkty_glowne)

df_punkty_glowne = pd.DataFrame(punkty_glowne, columns=['x', 'y'])

print(df_punkty_glowne)

doc = ezdxf.new()

msp = doc.modelspace()

for i in df_punkty_glowne.index:
    msp.add_point((df_punkty_glowne['y'][i], df_punkty_glowne['x'][i]))
    # print(df_punkty_glowne['x'][i])

doc.saveas('./result/pg.dxf')