from typing import List


def solution_1(arr: List[int]) -> int:
    dp = [0]*len(arr)

    cur_max = arr[0]
    for i in range(1, len(arr)):
        dp[i] = max(arr[i], dp[i - 1] + arr[i])
        if dp[i] > cur_max:
            cur_max = dp[i]
    return cur_max


def solution(arr: List[int]) -> int:
    cum_sum = [arr[0]]
    for i in range(1, len(arr)):
        cum_sum.append(cum_sum[i - 1] + arr[i])


if __name__ == '__main__':
    arr1 = [-2, -3, 4, -1, -2, 1, 5, -3]
    print(solution_1(arr1))
