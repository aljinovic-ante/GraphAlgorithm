import readPajek

def kruskal(vertices, edges):
    edges=sorted(edges,key=lambda x:x[2])
    mst=[]
    parent={}
    for v in vertices:
        parent[v]=v

    def find(v):
        if parent[v]!=v:
            parent[v]=find(parent[v])
        return parent[v]
    
    def union(u,v):
        root_u=find(u)
        root_v=find(v)
        if root_u != root_v:
            parent[root_v]=root_u
    
    while len(mst)<len(vertices)-1:
        u,v,w=edges.pop(0)
        if find(u)!=find(v):
            mst.append((u,v))
            union(u,v)

    return mst


def main():
    vertices, edges = readPajek.main()
    try:
        path = kruskal(vertices, edges)
        print("kruskal:")
        print(" -> ".join(map(str, path)))
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
