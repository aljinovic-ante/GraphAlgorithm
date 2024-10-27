# 5. Napisati iterativnu i rekurzivnu funkciju koja za listu vraća element
# najveće brojčane vrijednosti. Vrijednosti u listi koji nisu brojevi ignorira.
# Primjer: Za listu lst = [7, 18, 3, 'a', True, (2,3)] funkcija vraća 18.

def rek(lst, najveci=None, i=0):
    if i==len(lst):
        return najveci
    if isinstance(lst[i],(int,float)):
        if najveci is None or najveci<lst[i]:
            najveci=lst[i]
    return rek(lst,najveci,i+1)



def iter(lst):
    najveci=None
    for e in lst:
        if isinstance(e, (int, float)):
            # print(e)
            if(najveci==None or e>najveci):
                najveci=e
    return najveci

lst = [7, 18, 31.4, 'a', True, (2,3)]
print(rek(lst))