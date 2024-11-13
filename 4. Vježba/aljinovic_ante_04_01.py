# 1. Napisati funkcije koje će raditi konverzije zapisa grafa u matricu susjedstva,
# matricu incidencije i listu susjedstva grafa (iz svake strukture radi se konverzija u
# ostale dvije).

from aljinovic_ante_04_00 import main
def getGraph():    
    return main()

def to_adjacency_matrix(vertices, adjacency_list):
    n = len(vertices)
    adjacency_matrix = []
    for i in range(n):
        row = [0] * n
        adjacency_matrix.append(row) 
    
    for vertex, neighbors in adjacency_list.items():
        for neighbor in neighbors:
            i = vertices.index(vertex)
            j = vertices.index(neighbor)
            
            adjacency_matrix[i][j] = 1
            adjacency_matrix[j][i] = 1  
    
    return adjacency_matrix

def to_incidence_matrix(vertices, adjacency_list):
    edges = []
    
    for vertex, neighbors in adjacency_list.items():
        for neighbor in neighbors:
            if (neighbor, vertex) not in edges:
                edges.append((vertex, neighbor))
    
    n = len(vertices)
    m = len(edges) 
    
    incidence_matrix = []
    for i in range(n):
        row = [0] * m
        incidence_matrix.append(row)
    
    for edge_idx, (v1, v2) in enumerate(edges):
        v1_idx = vertices.index(v1)
        v2_idx = vertices.index(v2)
        
        incidence_matrix[v1_idx][edge_idx] = 1
        incidence_matrix[v2_idx][edge_idx] = 1
    
    return incidence_matrix

adjacency_list = getGraph()
print(adjacency_list)
vertices=list(adjacency_list.keys())
print(vertices)

adjacency_matrix = to_adjacency_matrix(vertices, adjacency_list)
print("\nAdjacency Matrix:")
for row in adjacency_matrix:
    print(row)

incidence_matrix = to_incidence_matrix(vertices, adjacency_list)
print("\nIncidence Matrix:")
for row in incidence_matrix:
    print(row)