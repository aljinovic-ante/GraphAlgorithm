# 2. Napisati funkciju prima matricu sa cjelobrojnim elementima i vraća listu
# u kojoj su elementi sume redaka u matrici

def citaj():
    file='1.txt'
    with open(file,'r') as f:
        matrix=[list(map(int, line.split())) for line in f.readlines()]
    lista=[]
    for line in matrix:
        lista.append(sum(line))
    return lista

lista=citaj()
print(lista)