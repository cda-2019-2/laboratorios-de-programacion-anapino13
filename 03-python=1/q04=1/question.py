##
##  Programación en Python
##  ===========================================================================
##
##  La columna 3 del archivo `data.csv` contiene una fecha en formato 
##  `YYYY-MM-DD`. Imprima la cantidad de registros por cada mes separados
##  por comas, tal como se muestra a continuación.
##
##  Rta/
##  01,3
##  02,4
##  03,2
##  04,4
##  05,3
##  06,3
##  07,5
##  08,6
##  09,3
##  10,2
##  11,2
##  12,3
##
##  >>> Escriba su codigo a partir de este punto <<<
##
data= open('data.csv', 'r').readlines()
data = [row[0:-1] for row in data]
data = [x.split('\t') for x in data]

fecha= [[row[2]] for row in data]
meses=[[row[0][5:]] for row in fecha]
meses=[[row[0][:2]] for row in meses]

listamesesunicos = []
listamesesunicos2 = []

for i in meses: 

  encontrado = 0
  for r in listamesesunicos:
    if r == i[0]:
      encontrado = 1
  if encontrado == 0:
    listamesesunicos.append(i[0])
    listamesesunicos2.append(i[0] + ",0")

for i in sorted(listamesesunicos2):
  
  num = 0
  for r in meses:
    if i[0:2] == r[0]:
      num = num + 1
  print( i[0:2]+","+str(num))