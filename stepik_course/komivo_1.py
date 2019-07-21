from typing import List


class TravelingSalesman:
    def __init__(self, edges: List[List[int]]):
        self.edges = edges
        self.size = len(self.edges)
        self.p = [0]*self.size
        self.used = [False]*self.size
        self.min_dist = float('inf')
        self.min_p = self.p

    def solve(self, idx: int, cur_dist: int = 0):
        if cur_dist > self.min_dist:
            return
        elif idx == self.size:
            cur_dist += self.edges[self.p[idx - 1]][0]
            if self.min_dist > cur_dist:
                self.min_dist = cur_dist
                self.min_p = list(self.p)
            return

        for i in range(1, self.size):
            if self.used[i]:
                continue
            self.p[idx] = i
            self.used[i] = True
            self.solve(idx + 1, cur_dist + self.edges[self.p[idx]][self.p[idx - 1]])
            self.used[i] = False


if __name__ == '__main__':
    arr = [
        [0, 1, 4, 6],
        [1, 0, 5, 2],
        [4, 5, 0, 3],
        [6, 2, 3, 0]
    ]
    sol = TravelingSalesman(arr)
    sol.solve(1, 0)
    print(sol.min_dist, sol.min_p)

    with open('problems/salesman.in', 'r') as fp:
        size = int(fp.readline())
        arr = []
        for line in fp.readlines():
           arr.append([int(ch) for ch in line.split()])
        from pprint import pprint
        pprint(arr)
        sol = TravelingSalesman(arr)
        sol.solve(1, 0)
        print(sol.min_dist, sol.min_p)
