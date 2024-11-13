# 1. Napisati funkciju koja iz datoteke čita matricu sa cjelobrojnim elementima i vraća zbroj elemenata iznad glavne dijagonale i zbroj elemenata
# iznad sporedne dijagonale. Ako matrica nije kvadratna, funkcija vraća
# nule.
# Primjer: Za matricu
# 2 4 6 8
# 5 3 4 6
# 1 3 5 6
# 0 3 5 7
# funkcija vraća (34, 21)

file="1.txt"

def citaj():
    with open(file,'r') as f:
        matrix=[list(map(int, line.split())) for line in f.readlines()]
    if(len(matrix)!=len(matrix[0])):
        return 0,0
    iznad_gl=0
    iznad_sp=0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if(j>i):
                # print(i,j)
                iznad_gl+=matrix[i][j]
            if(i+j<len(matrix)-1):
                # print(i,j)
                iznad_sp+=matrix[i][j]
    
    return iznad_gl,iznad_sp

iznad_gl,iznad_sp=citaj()
print(iznad_gl,iznad_sp)