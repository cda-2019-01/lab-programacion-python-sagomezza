##
## Imprima la suma de la segunda columna.
##
csv = open('data.csv', 'r').readlines()
csv = [z.replace('\t', ' ') for z in csv]
csv = [z.replace('\n', ' ') for z in csv]
csv = [z.split(',') for z in csv]
a = [z[0].split(' ') for z in csv[0:]]
b = []
[b.append(int(z[1])) for z in a]
print(str(sum(b)))