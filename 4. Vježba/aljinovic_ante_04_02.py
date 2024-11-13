# 2. Napisati funkcije koje računaju:
# — broj vrhova u grafu
# — broj bridova u grafu
# — stupanj svakog vrha
# — vrhove s maksimalnim brojem incidentnih bridova

from aljinovic_ante_04_00 import main

def getGraph():    
    return main()

def number_of_vertices(adjacency_list):
    return len(adjacency_list)

def number_of_edges(adjacency_list):
    edges = set()
    for vertex, neighbors in adjacency_list.items():
        for neighbor in neighbors:
            edges.add(tuple(sorted((vertex, neighbor))))
    
    # print(edges)
    return len(edges)


def degree_of_vertices(adjacency_list):
    degree_dict = {}
    for vertex, neighbors in adjacency_list.items():
        degree_dict[vertex] = len(neighbors)
    return degree_dict

def vertices_with_max_degree(degree_dict):
    max_degree = -1
    max_degree_vertices = []  

    for vertex, degree in degree_dict.items():
        if degree > max_degree:
            max_degree = degree
    
    for vertex, degree in degree_dict.items():
        if degree == max_degree:
            max_degree_vertices.append(vertex)

    return max_degree_vertices


adjacency_list = getGraph()
print("Adjacency List:", adjacency_list)
vertices = list(adjacency_list.keys())
print("Vertices:", vertices)

num_vertices = number_of_vertices(adjacency_list)
print("Number of vertices:", num_vertices)

num_edges = number_of_edges(adjacency_list)
print("Number of edges:", num_edges)

degree_dict = degree_of_vertices(adjacency_list)
print("Degree of each vertex:", degree_dict)

max_degree_vertices = vertices_with_max_degree(degree_dict)
print("Vertices with the maximum degree:", max_degree_vertices)
