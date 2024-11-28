import aljinovic_ante_05_00

def find_biggest_companies(vertices, edges):
    ownership_graph = {}

    for u, v in edges:
        if u not in ownership_graph:
            ownership_graph[u] = []
        ownership_graph[u].append(v)

    # print(ownership_graph)

    def bfs(company):
        visited = []
        queue = [company]
        visited.append(company)
        
        while queue:
            current = queue.pop(0)
            if current in ownership_graph:
                for neighbor in ownership_graph[current]:
                    if neighbor not in visited:
                        visited.append(neighbor)
                        queue.append(neighbor)
        
        return visited

    ownership_count = {}
    for company in vertices:
        owned_companies = bfs(company)
        ownership_count[company] = len(owned_companies)-1

    ownership_count_sorted = list(ownership_count.items())
    ownership_count_sorted.sort(key=lambda x: x[1], reverse=True)
    
    return ownership_count_sorted[:10]

def main(fileName):
    vertices,edges=aljinovic_ante_05_00.main(fileName)
    # print(vertices,edges)
    biggest_companies_dict=find_biggest_companies(vertices,edges)
    print(biggest_companies_dict)
    
if __name__=='__main__':
    main('eva.net')