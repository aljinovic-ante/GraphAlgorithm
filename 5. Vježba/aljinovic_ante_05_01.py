import aljinovic_ante_05_00

# Dana je udaljenost između gradova u pajek formatu. Napišite program koji će naći
# minimalno razapinjuće stablo
# (a) koristeći Primov algoritam
# (b) koristeći Kruskalov algoritam

def prim_algorithm(vertices,edges):
    graph={}
    for i in vertices.keys():
        graph[i]=[]
    # print(graph)
    added_edges=set()

    for u,v,w in edges:
        if(v,u,w) not in added_edges:
            graph[u].append((v,w))
            graph[v].append((u,w))
            added_edges.add((u,v,w))

    visited=set()
    mst_edges=[]
    total_w=0

    visited.add(0)

    neighbourin_edges=[]

    for n,w in graph[0]:
        neighbourin_edges.append((0,n,w))

    while len(visited)<len(vertices):
        min_edge=None
        for edge in neighbourin_edges:
            if edge[1] not in visited:
                if min_edge is None or edge[2]<min_edge[2]:
                    min_edge=edge
        
        if min_edge:
            u,v,w=min_edge
            visited.add(v)
            mst_edges.append((u,v,w))
            total_w+=w

            for n,w in graph[v]:
                if n not in visited:
                    neighbourin_edges.append((v,n,w))

    return total_w,mst_edges
    

    print("neighb",neighbourin_edges)
    
    print("graph: ", graph)
    print("ovde:", min_edge)

    
def kruskal_algorithm(vertices,edges):
    return None

def main():
    vertices,edges=aljinovic_ante_05_00.main()
    print("hehe")
    total_weight,mst_prim=prim_algorithm(vertices,edges)
    print(total_weight,mst_prim)
    mst_kruskal=kruskal_algorithm(vertices,edges)
    print(mst_kruskal)


if __name__=="__main__":
    main()