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
    

class UnionFind:
    def __init__(self, num_vertices):
        self.parent = list(range(num_vertices))

    def find(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find(self.parent[v])
        return self.parent[v]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_v] = root_u

def kruskal_algorithm(vertices, edges):
    uf = UnionFind(len(vertices))
    
    sorted_edges = sorted(edges, key=lambda edge: edge[2])
    
    mst_edges = []
    total_weight = 0
    
    for u, v, w in sorted_edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst_edges.append((u, v, w))
            total_weight += w
    
    return total_weight, mst_edges

def main(fileName):
    vertices,edges=aljinovic_ante_05_00.main(fileName)
    print("hehe")
    total_weight,mst_prim=prim_algorithm(vertices,edges)
    print('----------------PRIM ALGORITHM------------------------')
    print(total_weight,mst_prim)
    total_weight,mst_prim=kruskal_algorithm(vertices,edges)
    print('----------------KRUSKAL ALGORITHM---------------------')
    print(total_weight,mst_prim)


if __name__=="__main__":
    main('airports.net')