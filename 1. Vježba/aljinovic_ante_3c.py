# (c) funkciju koja ispisuje i vraća sve susjedne proste brojeve do n. Za
# dva prosta broja kažemo da su susjedni ako im je razlika jednaka 2.

def isPrime(num):
    if(num<=1):
        return False
    for i in range(2,num):
        if(num%i==0):
            return False
    return True    

def neighbourPrime(n):
    lst=[]
    for i in range(1,n,2):
        if(isPrime(i) and isPrime(i+2)):
            lst.append((i,i+2))
    return lst

print("Susjedi: "+str(neighbourPrime(100)))

