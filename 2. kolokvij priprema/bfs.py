import readPajek

def bfs(vertices,edges):
    visited=set()
    queue=[]

    for start in vertices:
        if start not in visited:
            queue.append(start)
            while queue:
                v=queue.pop(0)
                if v not in visited:
                    visited.add(v)
                    for edge in edges:
                        if edge[0]==v and edge[1] not in visited:
                            queue.append(edge[1])
    
    return visited


def main():
    vertices,edges=readPajek.main()
    # print(vertices)
    # print(edges)
    print(bfs(vertices,edges))

if __name__=="__main__":
    main()