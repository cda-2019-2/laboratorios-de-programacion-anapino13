##
##  Programación con Pandas
##  ===========================================================================
##
##  Construya una tabla que contenga _c0 y una lista
##  separada por ',' de los valores de la columna _c5a
##  y _c5b (unidos por ':') de la tabla tbl2.tsv
## 
##  Rta/
##      _c0                                lista
##  0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
##  1     1              aaa:3,ccc:2,ddd:0,hhh:9
##  ...
##  38   38                    eee:0,fff:9,iii:2
##  39   39                    ggg:3,hhh:8,jjj:5
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

tabla2 = tabla2[['_c0','_c5a','_c5b']]
tabla2['_c5b'] = tabla2['_c5b'].astype(str)
tabla2["lista"] = tabla2["_c5a"] +":" + tabla2["_c5b"]
tabla2 = tabla2.groupby('_c0',as_index = False).agg(lambda x: x.sort_values().tolist())
tabla2 = tabla2[['_c0','lista']]
tabla2
tabla2['lista'] = tabla2['lista'].astype(str)
tabla2['lista'] = tabla2['lista'].str.replace(", ",",")
tabla2['lista'] = tabla2['lista'].str.replace("'","")
tabla2['lista'] = tabla2['lista'].str.replace("[","")
tabla2['lista'] = tabla2['lista'].str.replace("]","")

print(tabla2)