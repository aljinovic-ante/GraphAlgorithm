import readPajek

def hierholzer(vertices, edges):
    def is_eulerian():
        for v in vertices:
            degree = 0
            for e in edges:
                if v in e:
                    degree += 1
            if degree % 2 != 0:
                return False
        return True

    if not is_eulerian():
        raise ValueError("nije eulerov neparni stupanj error")

    circuit=[]
    stack=[]
    stack.append(list(vertices.keys())[0])
    
    while stack:
        curr_v=stack[-1]
        for e in edges:
            if curr_v in e:
                if curr_v==e[0]:
                    next_v=e[1]
                    edges.remove(e)
                    stack.append(next_v)
                    break
        else:
            circuit.append(stack.pop())

    return circuit[::-1]


def main():
    vertices, edges = readPajek.main()
    try:
        path = hierholzer(vertices, edges)
        print("Eulerian Circuit:")
        print(" -> ".join(map(str, path)))
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
