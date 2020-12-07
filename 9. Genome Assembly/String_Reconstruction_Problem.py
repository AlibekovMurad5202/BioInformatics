def parse_input_data():
    input()
    path_length = 0
    patterns = []
    try:
        while True:
            patterns.append(input())
    except EOFError:
        path_length += 1
    de_bruijn_graph = { x: [] for x in sorted(pattern[:-1] for pattern in patterns) }
    for pattern in patterns:
        de_bruijn_graph[pattern[:-1]].append(pattern[1:])
        path_length += len(de_bruijn_graph[pattern[:-1]])
    return de_bruijn_graph, path_length


def get_additional_edge(adjacency_list) -> tuple:
    keys = list(adjacency_list.keys())
    score = [0] * len(keys)
    for idx, vertex in enumerate(keys):
        score[idx] -= len(adjacency_list[vertex])
    for elems in adjacency_list.values():
        for elem in elems:
            if elem not in keys:
                keys += [elem]
                score += [0]
    for vertices in adjacency_list.values():
        for vertex in vertices:
            score[keys.index(vertex)] += 1
    return (keys[score.index(1)], keys[score.index(-1)])


def get_eulerian_cycle(adjacency_list, cycle_length, first_vertex) -> list:
    last_vertex = adjacency_list[first_vertex].pop()
    cycle = [first_vertex, last_vertex]
    while True:
        while not (cycle[0] == cycle[-1] and len(adjacency_list[cycle[0]]) == 0):
            if len(adjacency_list[last_vertex]) != 0:
                last_vertex = adjacency_list[last_vertex].pop()
                cycle.append(last_vertex)
            else:
                cycle.append(cycle[0])
        if len(cycle) == cycle_length:
            break
        cycle.pop()
        while len(adjacency_list[cycle[-1]]) == 0:
            cycle.insert(0, cycle.pop())
        last_vertex = cycle[-1]
    return cycle


def get_eulerian_path(vertices, additional_edge) -> list:
    vertices.pop()
    while not vertices[0] == additional_edge[1]:
        vertices.insert(0, vertices.pop())
    return vertices


def reconstruct_string(de_bruijn_graph, path_length) -> str:
    additional_edge = get_additional_edge(de_bruijn_graph)
    if additional_edge[0] in de_bruijn_graph.keys():
        de_bruijn_graph[additional_edge[0]].append(additional_edge[1])
    else:
        de_bruijn_graph[additional_edge[0]] = [additional_edge[1]]
    eulerian_cycle = get_eulerian_cycle(de_bruijn_graph, path_length + 1, additional_edge[0])
    eulerian_path = get_eulerian_path(eulerian_cycle, additional_edge)
    result = eulerian_path[0]
    for vertex in eulerian_path[1:]:
        result += vertex[-1]
    return result


if __name__ == "__main__":
    de_bruijn_graph, path_length = parse_input_data()
    reconstructed_string = reconstruct_string(de_bruijn_graph, path_length)
    print(reconstructed_string)
