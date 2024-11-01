# 4. U datoteci se u svakom retku nalaze dva cijela broja. Napisati funkciju
# koja čita datoteku i sprema podatke u dictionary tako da je prvi broj u
# retku ključ, a drugi broj element liste vrijednosti tog ključa.

with open('2.txt','r') as f:
    matrix=[list(map(int,line.split())) for line in f.readlines()]
    
# print(matrix)
dict={}
for list in matrix:
    print(list)
    dict[list[0]]=list[1]

print(dict)