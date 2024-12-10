import time
import aljinovic_ante_07_00
# Napisati program koji traži najkraći put između dva grada koristeći:
# (a) Greedy BFS
# (b) A* algoritam
def greedy_BFS_algorithm(vertices, edges, starting_vertex, end_vertex):
    visited = set()
    path = []
    current_vertex = starting_vertex

    while current_vertex != end_vertex:
        visited.add(current_vertex)
        path.append(current_vertex)

        neighbors = [(dest, weight) for src, dest, weight in edges if src == current_vertex and dest not in visited]

        if not neighbors:
            return "Path not found"

        current_vertex, _ = min(neighbors, key=lambda x: x[1])

    path.append(end_vertex)
    return path

def a_star_algorithm(vertices, edges, starting_vertex, end_vertex):
    distances = {vertex: float('inf') for vertex in vertices}
    distances[starting_vertex] = 0

    paths = {vertex: [] for vertex in vertices}
    paths[starting_vertex] = [starting_vertex]

    open_list = [(starting_vertex, 0)]

    visited = set()

    while open_list:
        current_vertex, current_cost = min(open_list, key=lambda x: x[1])
        open_list.remove((current_vertex, current_cost))

        if current_vertex == end_vertex:
            return paths[end_vertex]

        visited.add(current_vertex)

        for src, dest, weight in edges:
            if src == current_vertex and dest not in visited:
                g_cost = distances[current_vertex] + weight
                h_cost = 0 
                f_cost = g_cost + h_cost

                if g_cost < distances[dest]:
                    distances[dest] = g_cost
                    paths[dest] = paths[current_vertex] + [dest]
                    open_list.append((dest, f_cost))

    return "Path not found"

def main(fileName):
    vertices,edges=aljinovic_ante_07_00.main(fileName)
    print(vertices,edges)

    start_time = time.time()
    greedy_BFS_result = greedy_BFS_algorithm(vertices, edges,1,10)
    print("\nGREEDY BFS ALGORITHM\n")
    print(greedy_BFS_result)
    print("Time: ",time.time() - start_time," seconds\n\n")

    start_time = time.time()
    a_star_result = a_star_algorithm(vertices, edges,1,10)
    print("A* ALGORITHM\n")
    print(a_star_result)
    print("Time: ",time.time() - start_time," seconds\n\n")

if __name__=="__main__":
    main('gradovi-udaljenosti.net')