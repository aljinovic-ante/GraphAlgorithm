import readPajek

def nearest_neighbor(vertices, edges):
    n=len(vertices)
    visited=set()
    curr_v=list(vertices.keys())[0]
    tour=[]
    tour.append(curr_v)
    visited.add(curr_v)
    while len(visited)<n:
        nearest_v=None
        nearest_w=float('inf')
        for e in edges:
            u,v,w=e
            if u==curr_v and v not in visited and w<nearest_w:
                nearest_w=w
                nearest_v=v
            elif v==curr_v and u not in visited and w<nearest_w:
                nearest_w=w
                nearest_v=u

        if nearest_v is not None:
            visited.add(nearest_v)
            curr_v=nearest_v
            tour.append(nearest_v)

    tour.append(tour[0])

    return [vertices[v] for v in tour]



def main():
    vertices, edges = readPajek.main()
    print(vertices,edges)
    try:
        tour = nearest_neighbor(vertices, edges)
        print("Nearest Neighbor Tour:")
        print(" -> ".join([list(city)[0] for city in tour]))
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
