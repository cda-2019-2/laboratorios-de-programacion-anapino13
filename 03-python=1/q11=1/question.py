##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima la suma de la columna 2 para cada 
##  letra de la columna 4, ordnados alfabeticamente.
##
##  Rta/
##  a,114
##  b,40
##  c,91
##  d,65
##  e,79
##  f,110
##  g,35
##
##  >>> Escriba su codigo a partir de este punto <<<
##

data= open('data.csv', 'r').readlines()
data = [row[0:-1] for row in data]
data = [x.split('\t') for x in data]


columna = [[c[1], c[3].split(',')] for c in data]
suma = {}
for filas in columna:
  for numero in filas[1]:
    if numero not in suma.keys():
          suma[numero] = [int(filas[0])]
    else:
          suma[numero].append(int(filas[0])) 

for x in sorted(suma.keys()):
  print(x+','+str(sum(suma[x])))