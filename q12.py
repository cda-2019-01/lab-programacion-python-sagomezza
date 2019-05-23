##
## Imprima la suma de la columna 2 por cada letra 
## de la columna 4, ordnados alfabeticamente.
##
## a,114
## b,40
## c,91
## d,65
## e,79
## f,110
## g,35
##
import itertools
from operator import itemgetter
csv = open('data.csv', 'r').readlines()
csv = [z.replace('\t', ' ') for z in csv]
csv = [z.replace('\n', '') for z in csv]
csv = [z.split(' ') for z in csv]
words = [[word, z[1]] for z in csv for word in z[3].split(',')]
for key, group in itertools.groupby(sorted(words, key=itemgetter(0)), itemgetter(0)):  
        [print(key, sum([int(z[1]) for z in group]), sep=",")]