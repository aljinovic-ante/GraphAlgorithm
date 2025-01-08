import readPajek

def gbfs(vertices, edges):
    path = []
    visited = set()
    current = 1
    end = 10

    def dist(x1, y1, x2, y2):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    while current != end:
        visited.add(current)
        path.append(current)
        neighbors = []
        for edge in edges:
            if edge[0] == current and edge[1] not in visited:
                neighbors.append((edge[1], edge[2]))

        if not neighbors:
            raise ValueError("no path found")

        t_data = list(vertices[end])[0]
        t_x, t_y = t_data[1], t_data[2]

        distances = []
        for n, w in neighbors:
            n_data = list(vertices[n])[0]
            n_x, n_y = n_data[1], n_data[2]
            distance = dist(n_x, n_y, t_x, t_y)
            distances.append((n, distance))

        closest = min(distances, key=lambda x: x[1])[0]
        current = closest

    path.append(end)
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
