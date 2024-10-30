# 1. Napisati funkciju koja za dvije liste vraća listu koja se sastoji od
# elemenata koji se nalaze u obje liste bez iteriranja po listama.
def unique(lst1,lst2):
    return (set(lst1) & set(lst2))

lst1=[1,2,3,4,5]
lst2=[2,4,6,8,10]
print(unique(lst1,lst2))