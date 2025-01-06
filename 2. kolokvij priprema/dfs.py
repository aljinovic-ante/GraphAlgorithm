import readPajek

def dfs(vertices,edges):
    visited=set()
    stack=[]

    for start in vertices:
        if start not in visited:
            stack.append(start)
            while stack:
                v=stack.pop()
                if v not in visited:
                    visited.add(v)
                    for edge in edges:
                        if edge[0]==v and edge[1] not in visited:
                            stack.append(edge[1])
    
    return visited


def main():
    vertices,edges=readPajek.main()
    # print(vertices)
    # print(edges)
    print(dfs(vertices,edges))

if __name__=="__main__":
    main()