# 1. Napisati program u kojem se unose trojke brojeva. Za svaku trojku ispitati da li je pitagorejska trojka (brojevi zadovoljavaju pitagorin teorem).
# Unos ponavljati sve dok se ne unese barem jedan negativni broj ili nula
def pitagora(a,b,c):
    return c**2==a**2+b**2

a=int(input("Unesite 1. broj: "))
b=int(input("Unesite 2. broj: "))
c=int(input("Unesite 3. broj: "))
while(a>0 and b>0 and c>0):
    if(pitagora(a,b,c)):
        print("Pitagorejska trojka")
        break
    else:
        print("Nije pitagorejska trojka, ponovite unos")
        a=int(input("Unesite 1. broj: "))
        b=int(input("Unesite 2. broj: "))
        c=int(input("Unesite 3. broj: "))
