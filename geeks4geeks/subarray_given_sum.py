from typing import List, Tuple, Union


def solution(arr: List[int], exp_sum: int) -> Union[int, Tuple[int, int]]:
    """
    Find subarray with a given sum of elements
    :param arr: array of non-negative integers
    :param exp_sum: sum to search for
    :return: indexes of subarray boundary elements
    """
    left, right = 0, 0
    n = len(arr)
    cur_sum = arr[left]

    while right < n and left < n:
        if cur_sum == exp_sum:
            break
        elif cur_sum > exp_sum:
            cur_sum -= arr[left]
            left += 1
        else:
            right += 1
            if right == n:
                return -1
            cur_sum += arr[right]
    else:
        return -1
    return left + 1, right + 1


if __name__ == '__main__':
    print(solution([1, 2, 3, 7, 5], 12))
    assert solution([1, 2, 3, 7, 5], 12) == (2, 4)
