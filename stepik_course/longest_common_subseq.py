from typing import List


def solution(arr1: List[int], arr2: List[int]):
    dp = [[0 for _ in range(len(arr2) + 1)] for _ in range(len(arr1) + 1)]

    for i in range(1, len(arr1) + 1):
        for j in range(1, len(arr2) + 1):
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            if arr1[i - 1] == arr2[j - 1]:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)

    # build certificate
    cert = []
    i, j = len(arr1), len(arr2)
    while i > 0 and j > 0:
        if arr1[i - 1] == arr2[j - 1]:
            cert.append(arr1[i - 1])
            i, j = i - 1, j - 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i, j = i - 1, j
        else:
            i, j = i, j - 1
    cert.reverse()
    return dp[-1][-1], cert


if __name__ == '__main__':
    arr1 = [3, 2, 4, 2, 1, 7, 6]
    arr2 = [4, 2, 5, 3, 1, 6, 5, 2, 3]
    print(solution(arr1, arr2))

    with open('problems/seq.in', 'r') as fp:
        _ = int(fp.readline().strip())
        arr1 = [int(ch) for ch in fp.readline().strip().split()]
        _ = int(fp.readline().strip())
        arr2 = [int(ch) for ch in fp.readline().strip().split()]
        print(solution(arr1, arr2))

    with open('problems/seq2.in', 'r') as fp:
        _ = int(fp.readline().strip())
        arr1 = [int(ch) for ch in fp.readline().strip().split()]
        _ = int(fp.readline().strip())
        arr2 = [int(ch) for ch in fp.readline().strip().split()]
        print(solution(arr1, arr2))
