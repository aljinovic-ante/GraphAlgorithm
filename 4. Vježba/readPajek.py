# Napisati funkciju koja čita datoteku u kojoj je zapisan graf u pajek formatu i sprema
# podatke o grafu u strukturu podataka po volji (matricu susjedstva, matricu incidencije
# ili listu susjedstva grafa).

def readPajek(file_path):
    vertices = {}
    edges = []

    with open(file_path, 'r') as file:
        mode = None

        for line in file:
            line = line.strip()
            if not line:
                continue 
            
            if line.startswith("*Vertices"):
                mode = "vertices"

            elif line.startswith("*Edges") or line.startswith("*Arcs"):
                mode = "edges"

            elif mode == "vertices":
                parts = line.split()
                vertex_id = int(parts[0])
                vertex_label = parts[1].strip('"')
                vertices[vertex_id] = vertex_label

            elif mode == "edges":
                edge = tuple(map(int, line.split()))
                edges.append(edge)

    return vertices, edges

def create_adjacency_list(vertices, edges):
    adjacency_list = {}
    
    for vertex in vertices:
        adjacency_list[vertex] = []
    
    for edge in edges:
        v1, v2 = edge
        adjacency_list[v1].append(v2)
        adjacency_list[v2].append(v1)
    
    return adjacency_list

def main():
    file_path = 'graf.net'
    vertices, edges = readPajek(file_path)
    adjacency_list = create_adjacency_list(vertices, edges)

    # print(adjacency_list)

    return adjacency_list

if __name__ == '__main__':
    main()