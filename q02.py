##
## Imprima la cantidad de registros por letra para la 
## primera columna, ordenados alfabeticamente.
##
## A,8
## B,7
## C,5
## D,6
## E,14
##
csv = open('data.csv', 'r').readlines()
csv = [z.replace('\t', ' ') for z in csv]
csv = [z.replace('\n', ' ') for z in csv]
csv = [z.split(',') for z in csv]
a = [z[0] for z in csv[0:]]
a = [z.split(' ') for z in a]
b = []
[b.append(z[0]) for z in a]
uniquewords = sorted(list(set(b)))
b=[(w, b.count(w)) for w in uniquewords]  
[ print(z[0],z[1], sep=",") for z in b]