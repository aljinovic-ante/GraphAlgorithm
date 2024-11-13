# 5. Dan je dictionary kojem su ključevi brojevi, a vrijednosti liste brojeva.
# Napisati funkciju koja okreće dictionary, na način da brojevi iz value listi
# postaju keys, a keys postaju članovi value listi.
# Primjer: Za d = {1:[2,3,5], 2:[1, 4], 3:[1,2]} novi dictionary je {1:[2,3],
# 2:[1,3], 3:[1], 4:[2], 5:[1]}

d = {1:[2,3,5], 2:[1, 4], 3:[1,2]}
new_d={}
for key,value in d.items():
    print(key,value)
    for n in value:
        if n in new_d:
            new_d[n].append(key)
        else:
            new_d[n]=[key]

new_d=dict(sorted(new_d.items()))
print(new_d)