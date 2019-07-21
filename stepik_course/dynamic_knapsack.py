from typing import List


def solution(items: List, W: int):
    dp = [[0 for _ in range(W + 1)] for _ in range(len(items) + 1)]
    cert = [[False for _ in range(W + 1)] for _ in range(len(items) + 1)]
    max_cost = 0
    n_max, w_max = 0, 0

    for w in range(1, W + 1):
        for n in range(1, len(items) + 1):
            dp[n][w] = dp[n - 1][w]
            cert[n][w] = False
            i_w, c = items[n - 1]
            if w >= i_w:
                val = dp[n - 1][w - i_w] + c
                if val > dp[n][w]:
                    dp[n][w] = val
                    cert[n][w] = True
            if max_cost < dp[n][w]:
                max_cost = dp[n][w]
                n_max, w_max = n, w

    elems = []
    while n_max > 0 and w_max > 0:
        if cert[n_max][w_max]:
            w_max -= items[n_max - 1][0]
            elems.append(n_max)
        n_max -= 1
    elems.reverse()

    return max_cost, elems


if __name__ == '__main__':
    arr = [(2, 10), (5, 20), (10, 30)]
    print(solution(arr, 12))
    with open('problems/rucksack.in', 'r') as fp:
        n, W = [int(ch) for ch in fp.readline().strip().split()]
        arr = []
        for i in range(n):
            item = [int(ch) for ch in fp.readline().strip().split()]
            arr.append(item)
        print(solution(arr, W))
