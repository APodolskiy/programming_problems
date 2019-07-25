from typing import List


def find_min_path_length(adj_mat: List[List[int]]):
    n = len(adj_mat)
    inf = sum([sum(l) for l in adj_mat])
    dp = [[inf for _ in range(1 << n)] for _ in range(n)]
    dp[0][0] = 0

    for mask in range(1 << n):
        for i in range(n):
            if dp[i][mask] == inf:
                continue
            for j in range(n):
                if not (mask & (1 << j)):
                    dp[j][mask ^ (1 << j)] = min(dp[i][mask] + adj_mat[i][j], dp[j][mask ^ (1 << j)])
    return dp[0][(1 << n) - 1]


if __name__ == '__main__':
    adj_mat = [
        [0, 1, 4, 6],
        [1, 0, 5, 2],
        [4, 5, 0, 3],
        [6, 2, 3, 0]
    ]
    print(find_min_path_length(adj_mat))
