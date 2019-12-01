##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima el valor maximo y minimo de la columna
##  2 por cada letra de la columa 1.
##
##  Rta/
##  A,9,1
##  B,9,1
##  C,9,0
##  D,7,1
##  E,9,1
##
##  >>> Escriba su codigo a partir de este punto <<<
##
data= open('data.csv', 'r').readlines()
data = [row[0:-1] for row in data]
data = [x.split('\t') for x in data]


columna = [c[0:2] for c in data]
num = {}
for fila in columna:
        if fila[0] not in num.keys():
          num[fila[0]] = [int(fila[1])]
        else:
            num[fila[0]].append(int(fila[1])) 

for fila in sorted(num.keys()):
    print(fila +','+ str(max(num[fila]))+','+str(min(num[fila]))) 

