##
## Por cada clave de la columna 5 (cadena de tres letras), obtenga
## el valor mas pequeño y el valor mas grande asociado a esa clave.
##
## aaa,0,6
## bbb,4,7
## ccc,0,1
## ddd,5,5
## eee,0,0
## fff,4,9
## ggg,3,3
## hhh,6,8
## iii,2,7
## jjj,2,5
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
def getMax (potato):
    return list(set([(row[1]) for row in a if int(row[1]) == max(int(x[1]) for x in a if x[0] == potato )]))[0]
def getMin (potato):
    return list(set([(row[1]) for row in a if int(row[1]) == min(int(x[1]) for x in a if x[0] == potato )]))[0]
[print(word, getMin(word), getMax(word), sep=",") for word in uniquewords]