##
##  Programación en Bash
##  ===========================================================================
##
##  Usando los archivos `data1.csv`, `data2.csv`, `data3.csv`, escriba en el
##  archivo `script.sh`  un programa en Bash que imprima en pantalla
##  la siguiente salida por linea:
## 
##  * El nombre del archivo.
##  * El número de la línea procesada.
##  * La letra de la primera columna del archivo.
##  * La cadena de tres letras y el valor asociado de la columna 2 del archivo original. 
##
##  Note que se genera una línea de salida por cada cadena de tres letras.
##   
##  Rta/
##
##  data1.csv,1,E,jjj:3
##  data1.csv,1,E,bbb:0
##  ...
##  data3.csv,3,B,hhh:1
##  data3.csv,3,B,ddd:2
##
##  >>> Escriba su codigo a partir de este punto <<<
##
awk '{print FILENAME","$0}' data1.csv | sed "s/\t/,/g" |sed '/^$/d' | awk '{printf "%s,%s\n", NR,$1}' > 1.txt
awk '{print FILENAME","$0}' data2.csv| sed "s/\t/,/g" | sed '/^$/d'| sed "s/ /,/g"| sed "s/ //g"| sed '1d'|awk '{printf "%s,%s\n", NR,$1}' >> 1.txt
awk '{print FILENAME","$0}' data3.csv | sed "s/\t/,/g" | awk '{printf "%s,%s\n", NR,$1}' >> 1.txt
awk 'BEGIN{FS=OFS=","} {t=$1; $1=$2; $2=t; print} ' 1.txt > 2.txt
for f in 2.txt
do
awk -F "," '{for(i=4;i<=NF;i++) print $1,$2,$3,$i}' OFS="," $f
done > 3.txt

sed '14d' 3.txt | sed '14d' > resultado.csv
rm *.txt
cat resultado.csv