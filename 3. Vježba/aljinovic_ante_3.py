# 3. Napisati funkciju prima matricu sa cjelobrojnim elementima i provjerava
# ima li matrica točno dvije jedinice u svakom stupce, a ostale elemente
# stupca nula. Ako postoji stupac koji ne zadovoljava taj uvjet, funkcija
# vraća False, inače True.

def provjera(matrix):
    for j in range(len(matrix[0])):
        zbroj_1=0
        for i in range(len(matrix)):
            if(matrix[i][j]!=1 and matrix[i][j]!=0):
                return False
            else:
                zbroj_1+=matrix[i][j]
        if(zbroj_1!=2):
            return False
    return True




matrix=[[0,1,1], [0,1,0], [1,0,1], [1,0,0]]
print(provjera(matrix))