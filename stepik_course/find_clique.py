from dataclasses import dataclass


@dataclass
class Edge:
    to: int
    next_id: int


class Graph:
    def __init__(self, num_vert: int):
        self.n = num_vert
        self.vertices = [-1 for idx in range(self.n + 1)]
        self.edges = []

    def add_edge(self, from_vert: int, to_vert: int):
        prev_edge_idx = self.vertices[from_vert]
        new_edge = Edge(to_vert, prev_edge_idx)
        self.edges.append(new_edge)
        self.vertices[from_vert] = len(self.edges) - 1


def find_max_clique(graph: Graph):
    num_vert = graph.n
    memory = [-1 for _ in range(1 << num_vert)]
    memory[0] = 1
    for i in range(num_vert):
        memory[(1 << i)] = 1

    max_clique = 1
    max_clique_set = 1
    for mask in range(1, 1 << num_vert):
        if memory[mask] == -1:
            continue
        vert_set = []
        idx = 0
        while idx < num_vert:
            if mask & (1 << idx):
                vert_set.append(idx)
            idx += 1
        e_idx = graph.vertices[vert_set[-1] + 1]
        vert_set = set(vert_set)
        while e_idx != -1:
            next_vert = graph.edges[e_idx].to
            if not (mask & (1 << (next_vert - 1))):
                next_vert_set = []
                next_e_idx = graph.vertices[next_vert]
                while next_e_idx != -1:
                    v = graph.edges[next_e_idx].to
                    next_vert_set.append(v)
                    next_e_idx = graph.edges[next_e_idx].next_id
                next_vert_set = set(next_vert_set)
                print(vert_set, next_vert_set)
                if not vert_set.difference(next_vert_set):
                    memory[mask ^ (1 << (next_vert - 1))] = 1
                    num_ones = number_of_ones(mask ^ (1 << (next_vert - 1)))
                    if num_ones > max_clique:
                        max_clique = num_ones
                        max_clique_set = (mask ^ (1 << (next_vert - 1)))
            e_idx = graph.edges[e_idx].next_id
    print(memory)
    return max_clique, max_clique_set


def number_of_ones(num: int):
    ones_num = 0
    while num > 0:
        ones_num += num % 2
        num //= 2
    return ones_num


if __name__ == '__main__':
    num_vert, num_edges = 4, 4
    arr = [[1, 2], [2, 3], [3, 1], [2, 4]]
    graph = Graph(num_vert)
    for (from_vert, to_vert) in arr:
        graph.add_edge(from_vert, to_vert)
        graph.add_edge(to_vert, from_vert)
    print(find_max_clique(graph))
