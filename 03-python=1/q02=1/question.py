data= open('data.csv', 'r').readlines()
data = [row[0:-1] for row in data]
data = [x.split('\t') for x in data]##
##  Programación en Python
##  ===========================================================================
##
##  Imprima la cantidad de registros por letra para la primera columna del 
##  archivo `data.csv`, ordenados alfabeticamente por la letra.
##
##  Rta/
##  A,8
##  B,7
##  C,5
##  D,6
##  E,14
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

for i in sorted(listaletrasunicas2):
  
  cant = 0
  for r in data:
    if i[0] == r[0]:
      cant = cant + 1
  print( i[0]+","+str(cant))