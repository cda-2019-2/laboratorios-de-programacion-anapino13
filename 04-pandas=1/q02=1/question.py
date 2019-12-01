##
##  Programación con Pandas
##  ===========================================================================
##
##  Imprima el promedio de la _c2 por cada letra de la _c1 
##  del archivo `tbl0.tsv`.
## 
##  Rta/
##  _c1
##  A    4.625000
##  B    5.142857
##  C    5.400000
##  D    3.833333
##  E    4.785714
##  Name: _c2, dtype: float64
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

tabla0 =tabla0.groupby('_c1')['_c2'].mean()
print(tabla0)