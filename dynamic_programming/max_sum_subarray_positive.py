from typing import List


def solution(arr: List[int]) -> List[str]:
    dp = [-1] * len(arr)
    cur_max = -1
    end_idx = -1
    if arr[0] > 0:
        dp[0] = arr[0]
        end_idx = 0
    seg_length = 0
    l_seg_length = 0
    for i in range(1, len(arr)):
        if arr[i] >= 0:
            seg_length += 1
            dp[i] = max(
                arr[i],
                dp[i - 1] + arr[i]
            )
            if cur_max < dp[i]:
                cur_max = dp[i]
                end_idx = i
            elif cur_max == dp[i] and arr[i] == 0 and end_idx == i - 1:
                end_idx = i
                l_seg_length = seg_length
            elif dp[i] == cur_max and l_seg_length < seg_length:
                end_idx = i
                l_seg_length = seg_length
        else:
            seg_length = 0
    ans = []
    while end_idx > -1 and dp[end_idx] >= 0:
        ans.append(str(arr[end_idx]))
        end_idx -= 1
    ans.reverse()
    return ans


if __name__ == '__main__':
    arr3 = [-2, -4, -5, 0, -1]
    res = solution(arr3)
    print(" ".join(res))
    arr1 = [9, -7, -9, -1, 8, 6, 5, 0, -8, -2, -4, -10, -8]
    res = solution(arr1)
    print(" ".join(res))
    arr2 = [2, 3, 0, -1, -2, 3, 2, 0, -1]
    res = solution(arr2)
    print(" ".join(res))
