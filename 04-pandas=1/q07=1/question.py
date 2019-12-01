##
##  Programación con Pandas
##  ===========================================================================
##
##  Agregue el año como una columna al archivo `tbl0.tsv`.
## 
##  Rta/
##      _c0 _c1  _c2         _c3   ano
##  0     0   E    1  1999-02-28  1999
##  1     1   A    2  1999-10-28  1999
##  ...
##  38   38   E    1  1999-09-28  1999
##  39   39   E    5  1998-01-26  1998
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

tabla0["ano"] = tabla0["_c3"].str.split("-", n = 1, expand = True)[0]
print(tabla0)