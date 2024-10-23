# 1. Napisati program u kojem se unose trojke brojeva. Za svaku trojku ispitati da li je pitagorejska trojka (brojevi zadovoljavaju pitagorin teorem).
# Unos ponavljati sve dok se ne unese barem jedan negativni broj ili nula
# def pitagora(a,b,c):
#     return c**2==a**2+b**2

# # a=int(input("Unesite 1. broj: "))
# # b=int(input("Unesite 2. broj: "))
# # c=int(input("Unesite 3. broj: "))
# k=tuple(map(int,input("Unesite 3 broja:").split()))
# print(k)
# a,b,c=sorted(k)
# while(a>0 and b>0 and c>0):
#     if(pitagora(a,b,c)):
#         print("Pitagorejska trojka")
#         break
#     else:
#         print("Nije pitagorejska trojka, ponovite unos")
#         k=tuple(map(int,input("Unesite 3 broja:").split()))
#         print(k)
#         a,b,c=sorted(k)

def pitagora(a, b, c):
    return c**2 == a**2 + b**2

while True:
    try:
        k = tuple(map(int, input("Unesite 3 broja: ").split()))
        if len(k)!=3:
            raise ValueError("Nisu unesena 3 broja")
        print(k)
        a,b,c=sorted(k)
        if a <= 0 or b <= 0 or c <= 0:
            print("Brojevi nisu pozitivni i veci od nule")
            continue
        if(pitagora(a,b,c)):
            print("Pitagorejska trojka")
            break
        else:
            print("Nije pitagorejska trojka, ponovite unos")
    except ValueError as e:
        print("Pogrešan unos, pokušajte ponovo:", e)

        