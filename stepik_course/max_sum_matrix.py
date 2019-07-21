from typing import List


def solution(arr: List) -> int:
    n, m = len(arr), len(arr[0])
    cum_sums = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    max_sum = -float('inf')

    for j in range(1, m + 1):
        col_cum_sum = 0
        for i in range(1, n + 1):
            col_cum_sum += arr[i - 1][j - 1]
            cum_sums[i][j] = col_cum_sum
            if j > 0:
                cum_sums[i][j] += cum_sums[i][j - 1]

    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    if i != k or j != l:
                        rect_sum = cum_sums[k + 1][l + 1] - cum_sums[k + 1][j] - cum_sums[i][l + 1] + cum_sums[i][j]
                    else:
                        # i == k, j == l
                        rect_sum = arr[i][j]
                    max_sum = max(max_sum, rect_sum)

    return max_sum


if __name__ == '__main__':
    arr = [
        [-1, -1, -1],
        [-1, -1, -1],
        [1, 1, 1]
    ]
    print(solution(arr))  # 3
    arr = [
        [-1, -1, -1],
        [1, 1, 1],
        [-1, -1, -1]
    ]
    print(solution(arr))  # 3
    arr = [
        [5, 0, 9],
        [1, 2, 7]
    ]
    print(solution(arr))  # 24
    arr = [
        [-7, 8, -1, 0, -2],
        [2, -9, 2, 4, -6],
        [-7, 0, 6, 8, 1],
        [4, -8, -1, 0, -6]
    ]
    print(solution(arr))  # 20
    arr = [
        [1, 2, 3]
    ]
    print(solution(arr))  # 6
    arr = [
        [1],
        [2],
        [3]
    ]
    print(solution(arr))  # 6
    arr = [[-1]]
    print(solution(arr))  # -1
    arr = [
        [100, -2, -3],
        [-20, -30, -20],
        [-1, -1, -1]
    ]
    print(solution(arr))  # 100
    arr = [
        [-1, -1, -1],
        [-1, -1, -1],
        [-1, -1, 100]
    ]
    print(solution(arr))  # 100
    arr = [
        [1, -1, -1],
        [1, -1, -1],
        [1, -1, -1]
    ]
    print(solution(arr))  # 3

    arr = [
        [1, 1, 1],
        [-1, -1, -1],
        [-1, -1, -1]
    ]
    print(solution(arr))  # 3
