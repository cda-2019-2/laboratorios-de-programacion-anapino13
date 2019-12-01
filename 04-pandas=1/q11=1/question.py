##
##  Programación con Pandas
##  ===========================================================================
##
##  Si la columna _c0 es la clave en los archivos `tbl0.tsv`
##  y `tbl2.tsv`, compute la suma de tbl2._c5b por cada
##  valor en tbl0._c1.
## 
##  Rta/
##  _c1
##  A    146
##  B    134
##  C     81
##  D    112
##  E    275
##  Name: _c5b, dtype: int64
##
##  >>> Escriba su codigo a partir de este punto <<<
##

import pandas as pd
import numpy as np
pd.set_option('display.notebook_repr_html', False)


tabla2 =  pd.read_csv(
    "tbl2.tsv",
    sep = '\t',         # separador de campos
    thousands = None,  # separador de miles para números
    decimal = '.')

tabla2= tabla2.groupby('_c0').sum()

tabla0 =  pd.read_csv(
    "tbl0.tsv",
    sep = '\t',         # separador de campos
    thousands = None,  # separador de miles para números
    decimal = '.')

tabla0["_c5b"] = tabla2["_c5b"]
tabla0 = tabla0.groupby('_c1')['_c5b'].sum()
print(tabla0)

