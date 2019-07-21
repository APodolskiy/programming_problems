from typing import List
import random


def solution(arr: List[int]) -> int:
    assert arr
    cum_sum = [0]

    for i in range(len(arr)):
        cum_sum.append(cum_sum[-1] + arr[i])
    cum_sum.sort()

    min_diff = None
    for i in range(1, len(cum_sum)):
        drop = cum_sum[i] - cum_sum[i - 1]
        if min_diff is None or drop < min_diff:
            min_diff = drop
    return min_diff


# Naive solution just for tests
def naive_solution(arr: List[int]) -> int:
    assert arr
    min_sum = abs(arr[0])
    for i in range(len(arr)):
        cur_sum = 0
        for j in range(i, len(arr)):
            cur_sum += arr[j]
            min_sum = min(min_sum, abs(cur_sum))
    return min_sum


if __name__ == '__main__':
    tests = {
        (0, -2, -3, 4): 0,
        (10, -18, 3, -4): 1,
        (2, 1, 3, 4, 5): 1,
        (100,): 100,
        (-2, -3, -4, -5, -100): 2,
        (-3,): 3,
        (7, -4, 3): 1
    }
    for test, ans in tests.items():
        res = solution(test)
        print(res)
        assert res == ans

    # Random tests with naive solution
    print("Test on random arrays")
    for _ in range(10):
        n = random.randint(1, 10)
        arr = []
        for _ in range(n):
            arr.append(random.randint(-10, 10))
        assert naive_solution(arr) == solution(arr)
