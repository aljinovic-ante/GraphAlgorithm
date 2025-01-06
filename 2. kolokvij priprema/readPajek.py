def readPajek():
    mode=None
    vertices={}
    edges=[]
    with open('tsp.net','r') as f:
        for line in f:
            line=line.strip()
            # print(line)

            if line.startswith('*vertices'):
                mode="v"
            elif line.startswith('*arcs') or line.startswith('*edges'):
                mode="e"
            elif mode=="v":
                parts=line.split()
                vertexID=int(parts[0])
                vertexLABEL=parts[1].strip("")
                if(len(parts)>2):
                    vertexX=int(parts[2])
                    vertexY=int(parts[3])
                    vertices[vertexID]={(vertexLABEL,vertexX,vertexY)}
                else:
                    vertices[vertexID]={vertexLABEL}
            elif mode=="e":
                edge=tuple(map(int,line.split()))
                edges.append(edge)
    return vertices,edges

def main():
    vertices,edges=readPajek()
    # print(vertices)
    # print(edges)

    return vertices,edges


if __name__=="__main__":
    main()