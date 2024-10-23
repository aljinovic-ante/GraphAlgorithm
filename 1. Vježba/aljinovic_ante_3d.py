# (d) funkciju koja za uneseni paran broj ispisuje sve različite načine na
# koje se on može prikazati kao zbroj dva prosta broja. Pretpostavka
# je da se svaki parni broj može napisati u obliku zbroja dva prosta
# broja (Goldbachova slutnja).

def isPrime(num):
    if(num<=1):
        return False
    for i in range(2,num):
        if(num%i==0):
            return False
    return True    

def neighbourPrime(n):
    if(n%2!=0):
        return []
    lst=[]
    for i in range(2,n//2 + 1):
        j = n - i
        if isPrime(i) and isPrime(j):
            lst.append((i, j))
    return lst

print("Kombinacije: "+str(neighbourPrime(10)))