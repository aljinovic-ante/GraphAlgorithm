import readPajek

def fleury(vertices, edges):
    def is_eulerian():
        for v in vertices:
            degree = sum(1 for edge in edges if v in edge)
            if degree % 2 != 0:
                return False
        return True

    def is_bridge(edge):
        temp_edges = edges.copy()
        temp_edges.remove(edge)

        def bfs(node):
            visited = set()
            queue = [node]
            while queue:
                v = queue.pop(0)
                if v not in visited:
                    visited.add(v)
                    for e in temp_edges:
                        if v in e:
                            next_v = e[1] if e[0] == v else e[0]
                            if next_v not in visited:
                                queue.append(next_v)
            return visited

        visited_after_removal = bfs(edge[0])
        return len(visited_after_removal) < len(vertices)

    if not is_eulerian():
        raise ValueError("The graph is not Eulerian")

    circuit = []
    copy_edges = edges.copy()
    curr_vertex = list(vertices.keys())[-1]

    while copy_edges:
        for edge in copy_edges:
            if curr_vertex in edge:
                next_vertex = edge[1] if curr_vertex == edge[0] else edge[0]
                if len(copy_edges) == 1 or not is_bridge(edge):
                    circuit.append(edge)
                    curr_vertex = next_vertex
                    copy_edges.remove(edge)
                    break

    return circuit


def main():
    vertices, edges = readPajek.main()
    try:
        path = fleury(vertices, edges)
        print("Eulerian Circuit:")
        for edge in path:
            print(edge)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()