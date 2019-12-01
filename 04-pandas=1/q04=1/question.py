##
##  Programación con Pandas
##  ===========================================================================
##
##  Imprima una lista con los valores unicos de la columna _c4 de 
##  del archivo `tbl1.csv` en mayusculas.
## 
##  Rta/
##  ['A', 'B', 'C', 'D', 'E', 'F', 'G']
##
##  >>> Escriba su codigo a partir de este punto <<<
##

import pandas as pd
import numpy as np
pd.set_option('display.notebook_repr_html', False)

tabla1 =  pd.read_csv(
    "tbl1.tsv",
    sep = '\t',         # separador de campos
    thousands = None,  # separador de miles para números
    decimal = '.')

tabla1 = pd.unique(tabla1['_c4'].str.upper())
tabla1.sort()
print(tabla1.tolist())