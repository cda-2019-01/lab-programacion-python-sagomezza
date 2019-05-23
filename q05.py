##
## Imprima el valor maximo y minimo por cada letra de la columa 1.
##
## A,9,1
## B,9,1
## C,9,0
## D,7,1
## E,9,1
##
csv = open('data.csv', 'r').readlines()
csv = [z.replace('\t', ' ') for z in csv]
csv = [z.replace('\n', ' ') for z in csv]
csv = [z.split(',') for z in csv]
a = [z[0].split(' ') for z in csv[0:]]
b = []
[b.append(z[0]) for z in a]
uniquewords = sorted(list(set(b)))
def getMax (potato):
    return list(set([(row[1]) for row in a if int(row[1]) == max(int(x[1]) for x in a if x[0] == potato )]))[0]
def getMin (potato):
    return list(set([(row[1]) for row in a if int(row[1]) == min(int(x[1]) for x in a if x[0] == potato )]))[0]
[print(word, getMax(word), getMin(word), sep=",") for word in uniquewords]