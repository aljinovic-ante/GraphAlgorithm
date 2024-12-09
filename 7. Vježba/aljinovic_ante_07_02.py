import time
import aljinovic_ante_07_00
import networkx as nx
# Napisati program koji traži najkraći put između dva grada koristeći:
# (a) Greedy BFS
# (b) A* algoritam
def greedy_BFS_algorithm(vertices,edges):
    return nx.

def a_star_algorithm(vertices,edges):
    pass

def main(fileName):
    vertices,edges=aljinovic_ante_07_00.main(fileName)
    print(vertices,edges)

    start_time = time.time()
    greedy_BFS_result = greedy_BFS_algorithm(vertices, edges)
    print("\nGREEDY BFS ALGORITHM\n")
    print(greedy_BFS_result)
    print("Time: ",time.time() - start_time," seconds\n\n")

    start_time = time.time()
    a_star_result = a_star_algorithm(vertices, edges)
    print("A* ALGORITHM\n")
    print(a_star_result)
    print("Time: ",time.time() - start_time," seconds\n\n")

if __name__=="__main__":
    main('gradovi-udaljenosti.net')