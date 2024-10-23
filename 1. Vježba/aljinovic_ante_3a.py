# (a) funkciju koja vraća koliko je prostih brojeva između dva decimalna broja

import math
def isPrime(num):
    if(num<=1):
        return False
    for i in range(2,num):
        if(num%i==0):
            return False
    return True    

def numOfPrime(a,b):
    cnt=0
    for i in range(int(a),math.ceil(b)):
        if(isPrime(i)):
            print(i)
            cnt+=1
    return cnt

print("Broj prostih je: "  + str(numOfPrime(2.3,30.6)))
