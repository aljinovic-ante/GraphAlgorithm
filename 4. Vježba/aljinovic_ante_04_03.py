# 3. Napisati funkciju u kojoj se ispituje je li graf Eulerov.

from aljinovic_ante_04_00 import main

def getGraph():    
    return main()

def isEuler(adjacency_list):
    for vertex, neighbors in adjacency_list.items():
        if len(neighbors) % 2 != 0:
            return False
    return True

adjacency_list = getGraph()
print(isEuler(adjacency_list))