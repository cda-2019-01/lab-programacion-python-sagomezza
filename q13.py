##
## Imprima por cada fila, la columna 1 y la suma de los valores
## de la columna 5
##
## E,22
## A,14
## B,14
## ....
## C,8
## E,11
## E,16
##
import itertools
from operator import itemgetter
csv = open('data.csv', 'r').readlines()
csv = [z.replace('\t', ' ') for z in csv]
csv = [z.replace('\n', '') for z in csv]
csv = [z.split(' ') for z in csv]
a = [[z[0], sum([int(y.split(':')[1]) for y in z[4].split(',')])] for z in csv]
[print(z[0], z[1], sep=',') for z in a]