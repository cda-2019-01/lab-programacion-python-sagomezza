##
## Imprima una tabla en formato CSV que contenga por cada clave 
## de la columna 5, la correspondiente cantidad de registros 
## asociados (filas en el archivo)
##
## aaa,13
## bbb,16
## ccc,23
## ddd,23
## eee,15
## fff,20
## ggg,13
## hhh,16
## iii,18
## jjj,18
##
##
csv = open('data.csv', 'r').readlines()
csv = [z.replace('\t', ' ') for z in csv]
csv = [z.replace('\n', '') for z in csv]
csv = [z.split(' ') for z in csv]
a = ','.join([z[4] for z in csv]).split(',')
a = [z.split(':') for z in a]
b = []
[b.append(z[0]) for z in a]
uniquewords = sorted(list(set(b)))
b=[(w, b.count(w)) for w in uniquewords]
[ print(z[0],z[1], sep=",") for z in b]