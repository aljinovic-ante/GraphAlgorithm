# (b) funkciju koja vraća n-ti prosti broj,

def isPrime(num):
    if(num<=1):
        return False
    for i in range(2,num):
        if(num%i==0):
            return False
    return True    

def nPrime(n):
    cnt=0
    i=1
    while(i):
        if(isPrime(i)):
            cnt+=1
        if(cnt==n):
            return i
        i+=1

print("Nti prosti broj je: " + str(nPrime(6)))