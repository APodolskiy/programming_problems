from typing import List


def find_min_path_length(adj_mat: List[List[int]]):
    n = len(adj_mat)
    inf = sum([sum(l) for l in adj_mat])
    dp = [[inf for _ in range(1 << n)] for _ in range(n)]
    dp[0][0] = 0
    cert = [[0 for _ in range(1 << n)] for _ in range(n)]

    for mask in range(2**n - 1):
        for i in range(n):
            if dp[i][mask] == inf:
                continue
            for j in range(n):
                if not (mask & (1 << j)):
                    trip_length = dp[i][mask] + adj_mat[i][j]
                    if dp[j][mask ^ 1 << j] > trip_length:
                        dp[j][mask ^ (1 << j)] = trip_length
                        cert[j][mask ^ (1 << j)] = i
    cur_mask = 2**n - 1
    vert = 0
    path = [vert]
    while cur_mask:
        mask = cur_mask
        cur_mask ^= (1 << vert)
        vert = cert[vert][mask]
        path.append(vert)

    return dp[0][2**n - 1], path


if __name__ == '__main__':
    adj_mat = [
        [0, 1, 4, 6],
        [1, 0, 5, 2],
        [4, 5, 0, 3],
        [6, 2, 3, 0]
    ]
    print(find_min_path_length(adj_mat))

    with open('problems/salesman2.in') as fp:
        n = int(fp.readline().strip())
        adj_mat = []
        for _ in range(n):
            row = [int(s) for s in fp.readline().strip().split()]
            adj_mat.append(row)
        print(find_min_path_length(adj_mat))
