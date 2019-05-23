##
## Imprima una tabla en formato CSV que contenga por registro,
## la cantidad de elementos de las columnas 4 y 5
## (filas en el archivo)
##
## E,3,5
## A,3,4
## B,4,4
## ...
## C,4,3
## E,2,3
## E,3,3
##
csv = open('data.csv', 'r').readlines()
csv = [z.replace('\t', ' ') for z in csv]
csv = [z.replace('\n', '') for z in csv]
csv = [z.split(' ') for z in csv]
a = [[z[0], len(z[3].split(',')), len(z[4].split(','))] for z in csv]
[print(z[0],z[1],z[2], sep=',') for z in a]