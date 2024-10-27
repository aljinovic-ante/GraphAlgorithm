# 1. Napisati funkciju koja za dvije liste vraća listu koja se sastoji od 
# elemenata koji se nalaze u obje liste bez iteriranja po listama.
def both_lists(lst1,lst2):
    set1=set(lst1)
    set2=set(lst2)
    return list(set1 & set2)

lst1=[1,2,3,4,5]
lst2=[2,4,6,8,10]
lst3=both_lists(lst1,lst2)
print(lst3)