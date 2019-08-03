from typing import List


def fair_cut(arr: List[int]) -> int:
    if len(arr) <= 30:
        return fair_cut_brute(arr)
    return fair_cut_dynamic(arr)


def fair_cut_dynamic(arr: List[int]) -> int:
    n = len(arr)
    assert n > 0
    inf = sum(arr) + 1

    dp = [[0 for _ in range(inf // 2)] for _ in range(n + 1)]

    dp[0][0] = 0
    best_w = 0
    for i in range(1, n + 1):
        for w in range(inf // 2):
            if arr[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w - arr[i - 1]] + arr[i - 1], dp[i][w])
            dp[i][w] = max(dp[i - 1][w], dp[i][w])
            if dp[i][w] > best_w:
                best_w = dp[i][w]
    return sum(arr) - 2*best_w


def fair_cut_brute(arr: List[int]) -> int:
    n = len(arr)
    assert n <= 30
    best_cut = sum(arr) + 1
    for mask in range(2**n - 1):
        cur_sum = 0
        for i in range(n):
            if mask & (1 << i):
                cur_sum += arr[i]
            else:
                cur_sum -= arr[i]
        if abs(cur_sum) < best_cut:
            best_cut = abs(cur_sum)
    return best_cut


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    print(fair_cut(arr))

    with open('problems/gold.in', 'r') as fp:
        _ = fp.readline()
        arr = [int(s) for s in fp.readline().strip().split()]
        print(fair_cut(arr))

    with open('problems/gold2.in', 'r') as fp:
        _ = fp.readline()
        arr = [int(s) for s in fp.readline().strip().split()]
        print(fair_cut(arr))

    with open('problems/gold3.in', 'r') as fp:
        _ = fp.readline()
        arr = [int(s) for s in fp.readline().strip().split()]
        print(fair_cut(arr))
