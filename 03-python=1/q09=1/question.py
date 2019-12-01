##
##  Programación en Python
##  ===========================================================================
##
##  Para el archivo `data.csv, imprima una tabla en formato CSV que contenga 
##  la cantidad de registros en que aparece cada clave de la columna 5.
##
##  Rta/
##  aaa,13
##  bbb,16
##  ccc,23
##  ddd,23
##  eee,15
##  fff,20
##  ggg,13
##  hhh,16
##  iii,18
##  jjj,18
##
##  >>> Escriba su codigo a partir de este punto <<<
##

data= open('data.csv', 'r').readlines()
data = [row[0:-1] for row in data]
data = [x.split('\t') for x in data]

columnas = [row[4].split(',') for row in data]
filas = [f[:3] for x in columnas for f in x]

for letras in sorted(set(filas)): #todo lo anterior quedó guardado en f, por eso recorro f (le aplico set pa no
                             #repetir y sorted pa ordenar, posteriormente guardo en b)
  print(letras+','+str(filas.count(letras)))



