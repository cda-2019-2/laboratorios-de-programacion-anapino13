##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv`, imprima la suma de la columna 2 por cada letra 
##  de la primera columna, ordneados alfabeticamente.
##
##  Rta/
##  A,37
##  B,36
##  C,27
##  D,23
##  E,67
##
##  >>> Escriba su codigo a partir de este punto <<<
##

data= open('data.csv', 'r').readlines()
data = [row[0:-1] for row in data]
data = [x.split('\t') for x in data]

listaletrasunicas = []
listaletrasunicas2 = []
listaletrasunicas3 = []

for i in data: 

  encontrado = 0
  for r in listaletrasunicas:
    if r == i[0]:
      encontrado = 1
  if encontrado == 0:
    listaletrasunicas.append(i[0])
    listaletrasunicas2.append(i[0] + ",0")
    listaletrasunicas3.append(i[0] + ",0" + ",0")
    
for i in sorted(listaletrasunicas):
  
  cant = 0
  for r in data:
    if i[0] == r[0]:
      cant = cant + int(r[1])
  print( i[0]+","+str(cant))