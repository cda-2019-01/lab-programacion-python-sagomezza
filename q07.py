##
## Genere una lista de tuplas, donde cada tupla contiene en la primera 
## posicion, el valor de la segunda columna; la segunda parte de la 
## tupla es una lista con las letras de la primera columna que aparecen
## asociadas a dicho valor de la segunda columna. Esto es:
##
##    ('0', ['C'])
##    ('1', ['E', 'B', 'D', 'A', 'A', 'E'])
##    ('2', ['A', 'E', 'D'])
##    ('3', ['A', 'B', 'D', 'E', 'E'])
##    ('4', ['E', 'B'])
##    ('5', ['B', 'C', 'D', 'D', 'E', 'E', 'E'])
##    ('6', ['C', 'E', 'A', 'B'])
##    ('7', ['A', 'C', 'E', 'D'])
##    ('8', ['E', 'E', 'A', 'B'])
##    ('9', ['A', 'B', 'E', 'C'])
##
##
csv = open('data.csv', 'r').readlines()
csv = [z.replace('\t', ' ') for z in csv]
csv = [z.replace('\n', ' ') for z in csv]
csv = [z.split(',') for z in csv]
a = [z[0].split(' ') for z in csv[0:]]
b = []
[b.append(z[1]) for z in a]
uniquenums = sorted(list(set(b)))
def getLetters(potato):
    return [(row[0]) for row in a  if row[1] == potato ]
[print((num, getLetters(num))) for num in uniquenums]