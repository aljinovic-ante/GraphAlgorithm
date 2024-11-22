def readPajek():
    vertices={}
    edges=[]
    with open('airports.net','r') as file:
        mode=None

        for line in file:
            line=line.strip()
            if not line:
                continue

            if line.startswith("*vertices"):
                mode="v"

            elif line.startswith("*edges") or line.startswith("*arcs"):
                mode="e"

            elif mode=="v":
                parts=line.split()
                vertexID=int(parts[0])
                vertexLABEL=parts[1].strip('"')
                vertices[vertexID]=vertexLABEL
            
            elif mode=="e":
                edge = tuple(map(int, line.split()))
                edges.append(edge)

    return vertices,edges
                


def main():
    vertices,edges=readPajek()
    print(vertices)
    print(edges)
    return vertices,edges

if __name__=="__main__":
    main()