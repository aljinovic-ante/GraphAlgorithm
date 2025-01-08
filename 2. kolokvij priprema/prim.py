import readPajek

def prim(vertices, edges):
    start_v=list(vertices.keys())[0]
    visited=[start_v]
    mst=[]

    while len(mst)<len(vertices)-1:
        min_e=None
        min_w=float('inf')

        for edge in edges:
            u,v,w=edge
            if (u in visited and v not in visited) or (v in visited and u not in visited):
                if w<min_w:
                    min_e=edge
                    min_w=w

        if min_e is None:
            raise ValueError("graf odvojen")
        
        mst.append(min_e)
        u,v,w=min_e
        visited.append(u)
        visited.append(v)
        edges.remove(min_e)

    return mst

def main():
    vertices, edges = readPajek.main()
    try:
        path = prim(vertices, edges)
        print("prim:")
        print(" -> ".join(map(str, path)))
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
