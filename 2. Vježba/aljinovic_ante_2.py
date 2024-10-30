# 2. Napisati program u kojem korisnik unosi granice dvaju zatvorenih intervala [a, b] i [c, d] 
# i ispisuje njihov presjek. Primjer: Za intervale [1, 5]
# i [-3, 2], presjek je interval [1, 2], a za intervale [-3.5, 2] i [4, 6.5]
# presjek je prazan skup.
from math import ceil
import math


while True:
    try:
        a=float(input("Unesi prvu granicu prvog intervala: "))
        b=float(input("Unesi drugu granicu prvog intervala: "))
        c=float(input("Unesi prvu granicu drugog intervala: "))
        d=float(input("Unesi drugu granicu drugog intervala: "))
        if(b<a):
            a,b=b,a
        if(d<c):
            c,d=d,c
        start=max(a,c)
        end=min(b,d)
        lst=[]
        for i in range(int(ceil(start)),int(math.floor(end+1))):
            lst.append(i)
        print(lst)
    except ValueError as e:
        print("Pogreska: ",e)