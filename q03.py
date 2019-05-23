##
## Imprima la suma de la columna 2 por cada letra de la 
## primera columna, ordneados alfabeticamente.
##
## A,37
## B,36
## C,27
## D,23
## E,67
##
import itertools
from operator import itemgetter

csv = open('data.csv', 'r').readlines()
csv = [z.replace('\t', ' ') for z in csv]
csv = [z.replace('\n', ' ') for z in csv]
csv = [z.split(',') for z in csv]
a = [z[0].split(' ') for z in csv[0:]]
for key, group in itertools.groupby(sorted(a, key=itemgetter(0)), itemgetter(0)):
    summ= sum([int(z[1]) for z in group])
    print(f'{key},{summ}')