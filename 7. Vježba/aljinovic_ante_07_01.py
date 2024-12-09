import time
import aljinovic_ante_07_00
# Napisati program koji traži najkraće putove iz jednog grada do svih drugih gradova
# koristeći:
# (a) Dijkstra algoritam
# (b) Bellman-Ford algoritam
def dijkstra_algorithm(vertices,edges):
    pass

def bellman_ford_algorithm(vertices,edges):
    pass

def main(fileName):
    vertices,edges=aljinovic_ante_07_00.main(fileName)
    print(vertices,edges)

    start_time = time.time()
    dijkstra_result = dijkstra_algorithm(vertices, edges)
    print("\nDIJKSTRA ALGORITHM\n")
    print(dijkstra_result)
    print("Time: ",time.time() - start_time," seconds\n\n")

    start_time = time.time()
    bellman_ford_result = bellman_ford_algorithm(vertices, edges)
    print("BELLMAN FORD ALGORITHM\n")
    print(bellman_ford_result)
    print("Time: ",time.time() - start_time," seconds\n\n")

if __name__=="__main__":
    main('gradovi-udaljenosti.net')