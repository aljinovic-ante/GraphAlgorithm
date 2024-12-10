import time
import aljinovic_ante_07_00
# Napisati program koji traži najkraće putove iz jednog grada do svih drugih gradova
# koristeći:
# (a) Dijkstra algoritam
# (b) Bellman-Ford algoritam
def dijkstra_algorithm(vertices, edges, starting_vertex):
    distances={}
    paths={}
    for v in vertices:
        distances[v]=float('inf')
        paths[v]=[]

    distances[starting_vertex] = 0
    paths[starting_vertex] = [starting_vertex]

    visited = set()

    while len(vertices) > len(visited):
        current_vertex = None
        current_distance = float('inf')

        for vertex in vertices:
            if vertex not in visited and distances[vertex] < current_distance:
                current_vertex = vertex
                current_distance = distances[vertex]

        if current_vertex is None: 
            break

        visited.add(current_vertex)

        for src, dest, weight in edges:
            if src == current_vertex and dest not in visited:
                new_distance = distances[current_vertex] + weight
                if new_distance < distances[dest]:
                    distances[dest] = new_distance
                    paths[dest] = paths[current_vertex] + [dest]

    return distances, paths


def bellman_ford_algorithm(vertices, edges, starting_vertex):
    distances={}
    paths={}
    for v in vertices:
        distances[v]=float('inf')
        paths[v]=[]

    distances[starting_vertex] = 0
    paths[starting_vertex] = [starting_vertex]

    for _ in range(len(vertices) - 1):
        for src, dest, weight in edges:
            if distances[src] + weight < distances[dest]:
                distances[dest] = distances[src] + weight
                paths[dest] = paths[src] + [dest]

    for src, dest, weight in edges:
        if distances[src] + weight < distances[dest]:
            raise ValueError("Negative-weight cycle detected..error")

    return distances, paths

def main(fileName):
    vertices,edges=aljinovic_ante_07_00.main(fileName)
    print(vertices,edges)

    start_time = time.time()
    dijkstra_distances,dijkstra_paths = dijkstra_algorithm(vertices, edges, 5)
    print("\nDIJKSTRA ALGORITHM\n")
    print(dijkstra_distances)
    print(dijkstra_paths)
    print("Time: ",time.time() - start_time," seconds\n\n")

    start_time = time.time()
    bellman_ford_distances,bellman_ford_paths = bellman_ford_algorithm(vertices, edges, 5)
    print("BELLMAN FORD ALGORITHM\n")
    print(bellman_ford_distances)
    print(bellman_ford_paths)
    print("Time: ",time.time() - start_time," seconds\n\n")

if __name__=="__main__":
    main('gradovi-udaljenosti.net')