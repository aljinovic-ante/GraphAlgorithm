import readPajek

def gbfs(vertices, edges):
    path=[]
    visited=[]
    current_vertex=1
    end_vertex=10

    while current_vertex!=end_vertex:
        neighbors=[]
        visited.append(current_vertex)
        path.append(current_vertex)
        for edge in edges:
            if edge[0]==current_vertex and end_vertex not in visited:
                neighbors.append((edge[1],edge[2]))

        t_x=list(vertices[end_vertex])[0][1]
        t_y=list(vertices[end_vertex])[0][2]

        if not neighbors:
            raise ValueError("ERROR")
        
        closest_v=None
        closes_w=float('inf')

        def euclidean_distance(x1, y1, x2, y2):
            return ((int(x2) - int(x1)) ** 2 + (int(y2) - int(y1)) ** 2) ** 0.5

        for n,w in neighbors:
            n_data=list(vertices[n])[0]
            n_x=n_data[1]
            n_y=n_data[2]

            distance = euclidean_distance(n_x,n_y,t_x,t_y)

            if distance<closes_w:
                closes_w=distance
                closest_v=n
            
        current_vertex=closest_v

    path.append(end_vertex)
    return path



def main():
    vertices, edges = readPajek.main()
    try:
        path = gbfs(vertices, edges)
        print(path)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
