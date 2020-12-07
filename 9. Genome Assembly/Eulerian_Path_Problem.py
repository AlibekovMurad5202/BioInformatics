def parse_input_data():
    adjacency_list = {}
    path_length = 0
    input_data = input().split(" -> ")
    first_vertex = int(input_data[0])
    adjacency_list[first_vertex] = sorted([int(x) for x in input_data[1].split(',')], reverse=True)
    path_length += len(adjacency_list[first_vertex])
    try:
        while True:
            input_data = input().split(" -> ")
            vertex = int(input_data[0])
            adjacency_vertices = sorted([int(x) for x in input_data[1].split(',')], reverse=True)
            adjacency_list[vertex] = adjacency_vertices
            path_length += len(adjacency_vertices)
    except EOFError:
        path_length += 1
    return adjacency_list, path_length, first_vertex


def get_additional_edge(adjacency_list) -> tuple:
    score = [0] * (max(adjacency_list.keys()) + 1)
    for vertex in adjacency_list.keys():
        score[vertex] -= len(adjacency_list[vertex])
    for vertices in adjacency_list.values():
        for vertex in vertices:
            score[vertex] += 1
    return (score.index(1), score.index(-1))


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
        vertices.insert(0, cycle.pop())
    return vertices


def output_eulerian_path(path) -> None:
    for vertex in cycle[:-1]:
        print(vertex, end='->')
    print(cycle[-1], end='')


if __name__ == "__main__":
    adjacency_list, path_length, first_vertex = parse_input_data()
    additional_edge = get_additional_edge(adjacency_list)
    if additional_edge[0] in adjacency_list.keys():
        adjacency_list[additional_edge[0]].append(additional_edge[1])
    else:
        adjacency_list[additional_edge[0]] = [additional_edge[1]]
    cycle = get_eulerian_cycle(adjacency_list, path_length + 1, additional_edge[0])
    path = get_eulerian_path(cycle, additional_edge)
    output_eulerian_path(path)
