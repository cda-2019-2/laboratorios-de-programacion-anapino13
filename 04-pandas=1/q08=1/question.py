##
##  Programación con Pandas
##  ===========================================================================
##
##  Construya una tabla que contenga _c1 y una lista
##  separada por ':' de los valores de la columna _c2
##  para el archivo `tbl0.tsv`.
##
##  Rta/
##    _c0                        lista
##  0   A              1:1:2:3:6:7:8:9
##  1   B                1:3:4:5:6:8:9
##  2   C                    0:5:6:7:9
##  3   D                  1:2:3:5:5:7
##  4   E  1:1:2:3:3:4:5:5:5:6:7:8:8:9
## 
##  >>> Escriba su codigo a partir de este punto <<<
##
import pandas as pd
import numpy as np
pd.set_option('display.notebook_repr_html', False)

tabla0 =  pd.read_csv(
    "tbl0.tsv",
    sep = '\t',         # separador de campos
    thousands = None,  # separador de miles para números
    decimal = '.')

tabla0 = tabla0[['_c1','_c2']]
tabla0 = tabla0.groupby('_c1',as_index = False).agg(lambda x: x.sort_values().tolist())
tabla0['_c2'] = tabla0['_c2'].astype(str)
tabla0['_c2'] = tabla0['_c2'].str.replace(", ",":")
tabla0['_c2'] = tabla0['_c2'].str.replace("[","")
tabla0['_c2'] = tabla0['_c2'].str.replace("]","")
tabla0.rename(columns=lambda x: x.replace('_c2', 'lista'), inplace=True)
tabla0.rename(columns=lambda x: x.replace('_c1', '_c0'), inplace=True)
print(tabla0)