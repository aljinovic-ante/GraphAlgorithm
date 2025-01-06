import readPajek

def sorted_edges(vertices, edges):
    sorted_edges = sorted(edges, key=lambda x: x[2])
    v_d={}
    parent={}
    tour=[]

    for v in vertices:
        v_d[v]=0
        parent[v]=v

    def find(v):
        if parent[v]!=v:
            parent[v]=find(parent[v])
        return parent[v]
    
    def union(u,v):
        root_u=find(u)
        root_v=find(v)
        if root_u!=root_v:
            parent[root_v]=root_u

    while sorted_edges: 
        u,v,_ = sorted_edges.pop(0)
        if v_d[u]<2 and v_d[v]<2 and find(u)!=find(v):
            tour.append((u,v))
            v_d[u]+=1
            v_d[v]+=1
            union(u,v)

        if len(tour)==len(vertices):
            break
    
    for u,v,_ in edges:
        if (u,v) not in tour and (v,u) not in tour:
            if v_d[u]<2 and v_d[v]<2:
                tour.append((u,v))
                break

    return tour

    


def main():
    vertices, edges = readPajek.main()
    try:
        path = sorted_edges(vertices, edges)
        print("sorted_edges:")
        print(" -> ".join(map(str, path)))
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
