import time
import aljinovic_ante_07_00
# Napisati program koji traži najkraći put između dva grada koristeći:
# (a) Greedy BFS
# (b) A* algoritam
def euclidean_distance(x1, y1, x2, y2):
    return ((int(x2) - int(x1)) ** 2 + (int(y2) - int(y1)) ** 2) ** 0.5

def greedy_BFS_algorithm(vertices, edges, starting_vertex, end_vertex):
    visited = set()
    path = []
    current_vertex = starting_vertex
    
    while current_vertex != end_vertex:
        visited.add(current_vertex)
        path.append(current_vertex)

        current_data = list(vertices[current_vertex])[0]
        current_x = current_data[1]
        current_y = current_data[2]

        target_data = list(vertices[end_vertex])[0]
        target_x = target_data[1]
        target_y = target_data[2]
        
        neighbors = []
        for src, dest, weight in edges:
            if src == current_vertex and dest not in visited:
                neighbors.append((dest, weight))

        if not neighbors:
            return "Path not found"

        closest_vertex = None
        min_distance = float('inf')

        for neighbor, _ in neighbors:
            neighbor_data = list(vertices[neighbor])[0]
            neighbor_x = neighbor_data[1]
            neighbor_y = neighbor_data[2]

            distance = euclidean_distance(neighbor_x, neighbor_y, target_x, target_y)

            if distance < min_distance:
                min_distance = distance
                closest_vertex = neighbor

        current_vertex = closest_vertex

    path.append(end_vertex)
    return path

def a_star_algorithm(vertices, edges, starting_vertex, end_vertex):
    distances = {}
    for vertex in vertices:
        distances[vertex] = float('inf')
    distances[starting_vertex] = 0

    paths = {}
    for vertex in vertices:
        paths[vertex] = []
    paths[starting_vertex] = [starting_vertex]

    open_list = [(starting_vertex, 0)]
    visited = set()

    target_data = list(vertices[end_vertex])[0]
    target_x = target_data[1]
    target_y = target_data[2]

    while open_list:
        current_vertex, current_cost = min(open_list, key=lambda x: x[1])
        open_list.remove((current_vertex, current_cost))

        if current_vertex == end_vertex:
            return paths[end_vertex]

        visited.add(current_vertex)

        current_data = list(vertices[current_vertex])[0]
        current_x = current_data[1]
        current_y = current_data[2]

        for src, dest, weight in edges:
            if src == current_vertex and dest not in visited:
                g_cost = distances[current_vertex] + weight

                dest_data = list(vertices[dest])[0]
                dest_x = dest_data[1]
                dest_y = dest_data[2]
                h_cost = euclidean_distance(dest_x, dest_y, target_x, target_y)

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
