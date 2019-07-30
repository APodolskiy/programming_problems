from typing import List

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


def find_min_news(graph: Graph):
    def visit_children(vert_idx: int, visited: List[bool]):
        visited[vert_idx] = True
        e_idx = graph.vertices[vert_idx]
        while e_idx != -1:
            next_vert = graph.edges[e_idx].to
            visited[next_vert] = True
            e_idx = graph.edges[e_idx].next_id

    min_num = graph.n
    for mask in range(1, 1 << graph.n):
        visited = [False for _ in range(graph.n + 1)]
        visited[0] = True  # no vertex with this number

        for i in range(graph.n):
            if mask & (1 << i):
                visit_children(i + 1, visited)
        if all(visited):
            num = number_of_ones(mask)
            if num < min_num:
                min_num = num
    return min_num


def number_of_ones(num: int):
    ones_num = 0
    while num > 0:
        ones_num += num % 2
        num //= 2
    return ones_num


if __name__ == '__main__':
    num_vert, num_edges = 4, 3
    arr = [[1, 2], [2, 3], [3, 4]]
    graph = Graph(num_vert)
    for (from_vert, to_vert) in arr:
        graph.add_edge(from_vert, to_vert)
        graph.add_edge(to_vert, from_vert)
    print(find_min_news(graph))

    with open('problems/new.in', 'r') as fp:
        n, m = [int(s) for s in fp.readline().strip().split()]
        graph = Graph(n)
        for _ in range(m):
            v1, v2 = [int(s) for s in fp.readline().strip().split()]
            graph.add_edge(v1, v2)
            graph.add_edge(v2, v1)
        print(find_min_news(graph))

    with open('problems/new2.in', 'r') as fp:
        n, m = [int(s) for s in fp.readline().strip().split()]
        graph = Graph(n)
        for _ in range(m):
            v1, v2 = [int(s) for s in fp.readline().strip().split()]
            graph.add_edge(v1, v2)
            graph.add_edge(v2, v1)
        print(find_min_news(graph))
