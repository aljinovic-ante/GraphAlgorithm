import readPajek

def bf(vertices, edges):
    paths={}
    distances={}

    for v in vertices:
        distances[v]=float('inf')
        paths[v]=[]

    start=list(vertices.keys())[5]
    distances[start]=0
    paths[start]=[start]

    for _ in range(len(vertices)-1):
        for src,tar,w in edges:
            if distances[src] + w < distances[tar]:
                distances[tar]=distances[src] + w
                paths[tar]=paths[src]+[tar]

    for src,tar,w in edges:
        if distances[src]+w<distances[tar]:
            raise ValueError("Negative cycle detected")
        
    return paths


def main():
    vertices, edges = readPajek.main()
    try:
        path = bf(vertices, edges)
        print(path)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
