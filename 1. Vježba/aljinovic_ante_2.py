# 2. Napisati funkciju koja će za prirodan broj n < 20 ispisati brojevni trokut
# prema sljedećem primjeru (za n = 9):
# 1
# 2 3 2
# 3 4 5 4 3
# 4 5 6 7 6 5 4
# 5 6 7 8 9 8 7 6 5
# 6 7 8 9 0 1 0 9 8 7 6
# 7 8 9 0 1 2 3 2 1 0 9 8 7
# 8 9 0 1 2 3 4 5 4 3 2 1 0 9 8
# 9 0 1 2 3 4 5 6 7 6 5 4 3 2 1 0 9

def ispis(n):
    for i in range(1,n+1):
        for j in range(i, 2*i):
            print(j%10,end="")
        for j in range(2*i-2,i-1,-1):
            print(j%10,end="")
        print("")

n=-1
while(n>=20 or n<0):
    n=int(input("Unesite broj: "))
ispis(n)
