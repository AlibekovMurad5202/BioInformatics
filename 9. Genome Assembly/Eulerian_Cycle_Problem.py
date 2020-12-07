def parse_input_data():
    adjacency_list = {}
    cycle_length = 0
    input_data = input().split(" -> ")
    first_vertex = int(input_data[0])
    adjacency_list[first_vertex] = [int(x) for x in input_data[1].split(',')]
    cycle_length += len(adjacency_list[first_vertex])
    try:
        while True:
            input_data = input().split(" -> ")
            vertex = int(input_data[0])
            adjacency_vertices = [int(x) for x in input_data[1].split(',')]
            adjacency_list[vertex] = adjacency_vertices
            cycle_length += len(adjacency_vertices)
    except EOFError:
        cycle_length += 1
    return adjacency_list, cycle_length, first_vertex


def get_eulerian_cycle(adjacency_list, cycle_length, first_vertex) -> list:
    last_vertex = adjacency_list[first_vertex].pop(0)
    cycle = [first_vertex, last_vertex]
    while True:
        while not (cycle[0] == cycle[-1] and len(adjacency_list[cycle[0]]) == 0):
            if len(adjacency_list[last_vertex]) != 0:
                last_vertex = adjacency_list[last_vertex].pop(0)
                cycle.append(last_vertex)
            else:
                cycle.append(cycle[0])
        if len(cycle) == cycle_length:
            break
        while len(adjacency_list[cycle[-1]]) == 0:
            cycle.pop(0)
            cycle.append(cycle[0])
        last_vertex = cycle[-1]
    return cycle


def output_eulerian_cycle(cycle) -> None:
    for vertex in cycle[:-1]:
        print(vertex, end='->')
    print(cycle[-1], end='')


if __name__ == "__main__":
    adjacency_list, cycle_length, first_vertex = parse_input_data()
    cycle = get_eulerian_cycle(adjacency_list, cycle_length, first_vertex)
    output_eulerian_cycle(cycle)
