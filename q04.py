##
## Imprima la cantidad de registros por cada mes.
##
## 01,3
## 02,4
## 03,2
## 04,4
## 05,3
## 06,3
## 07,5
## 08,6
## 09,3
## 10,2
## 11,2
## 12,3
##

csv = open('data.csv', 'r').readlines()
csv = [z.replace('\t', ' ') for z in csv]
csv = [z.replace('\n', ' ') for z in csv]
csv = [z.split(',') for z in csv]
a = [z[0].split(' ') for z in csv[0:]]
b = []
[b.append(z[2].split('-')[1]) for z in a]
uniquemonths = sorted(list(set(b)))
b=[(w, b.count(w)) for w in uniquemonths]
[ print(z[0],z[1], sep=",") for z in b]
