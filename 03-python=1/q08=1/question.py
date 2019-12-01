##
##  Programación en Python
##  ===========================================================================
##
##  Genere una lista de tuplas, donde cada tupla contiene en la primera 
##  posicion, el valor de la segunda columna; la segunda parte de la 
##  tupla es una lista con las letras (ordenadas y sin repetir letra) 
##  de la primera  columna que aparecen asociadas a dicho valor de la 
##  segunda columna. Esto es:
##
##  Rta/
##  ('0', ['C'])
##  ('1', ['A', 'B', 'D', 'E'])
##  ('2', ['A', 'D', 'E'])
##  ('3', ['A', 'B', 'D', 'E'])
##  ('4', ['B', 'E'])
##  ('5', ['B', 'C', 'D', 'E'])
##  ('6', ['A', 'B', 'C', 'E'])
##  ('7', ['A', 'C', 'D', 'E'])
##  ('8', ['A', 'B', 'E'])
##  ('9', ['A', 'B', 'C', 'E'])
##
##  >>> Escriba su codigo a partir de este punto <<<
##
data= open('data.csv', 'r').readlines()
data = [row[0:-1] for row in data]
data = [x.split('\t') for x in data]


listanum = []

for i in data:

  encontrado = 0
  for r in listanum :
    if r == i[1]:
      encontrado = 1
  if encontrado == 0:
    listanum.append(i[1])
    
for i in sorted(listanum):
  listalet = []
  for r in data:
    if i == r[1]:
      listalet.append(r[0])
  print((i,sorted(set(listalet))))
    
  