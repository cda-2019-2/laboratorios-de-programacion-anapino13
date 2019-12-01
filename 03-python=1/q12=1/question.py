##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima por cada fila, la columna 1 y la suma 
##  de los valores de la columna 5.
##
##  Rta/
##  E,22
##  A,14
##  B,14
##  ....
##  C,8
##  E,11
##  E,16
##
##  >>> Escriba su codigo a partir de este punto <<<
##
import re
data= open('data.csv', 'r').readlines()
data = [row[0:-1] for row in data]
data = [x.split('\t') for x in data]

columna = [[c[0], c[4]] for c in data]
for filas in columna:
        num = re.findall('\d+', filas[1])
        num = [int(i) for i in num]
        print(filas[0]+','+str(sum(num)))



