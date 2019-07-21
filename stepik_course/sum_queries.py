from typing import List


def solution(arr: List, queries: List) -> int:
    n, m = len(arr), len(arr[0])
    cum_sums = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    sum_ans = 0

    for j in range(1, m + 1):
        col_cum_sum = 0
        for i in range(1, n + 1):
            col_cum_sum += arr[i - 1][j - 1]
            cum_sums[i][j] = col_cum_sum
            if j > 0:
                cum_sums[i][j] += cum_sums[i][j - 1]

    for (i, k, j, l) in queries:
        if i != k or j != l:
            rect_sum = cum_sums[k][l] - cum_sums[k][j - 1] - cum_sums[i - 1][l] + cum_sums[i - 1][j - 1]
        else:
            # i == k, j == l
            rect_sum = arr[i - 1][j - 1]
        sum_ans += rect_sum

    return sum_ans


if __name__ == '__main__':
    arr = [
        [1, 3, 7, -1, 7, 11],
        [2, 6, 5, 1, 1, 3],
        [-3, 0, 2, 0, 3, 8],
        [5, 1, 3, 1, 4, 7],
        [6, 1, -2, 2, 1, 0]
    ]
    queries = [
        (2, 3, 2, 3),
        (1, 1, 5, 6),
        (3, 5, 3, 6)
    ]
    print(solution(arr, queries))

    with open('problems/rectangle.in', 'r') as fp:
        n, m = [int(ch) for ch in fp.readline().strip().split()]
        arr = []
        for _ in range(n):
            row = [int(ch) for ch in fp.readline().strip().split()]
            arr.append(row)
        n = int(fp.readline().strip())
        queries = []
        for _ in range(n):
            query = [int(ch) for ch in fp.readline().strip().split()]
            queries.append(query)
        print(solution(arr, queries))
