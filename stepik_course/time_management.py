from typing import List, Tuple


def manage_time(arr: List[Tuple[int, int]]) -> int:
    max_t = max(arr, key=lambda x: x[0])[0]
    max_d = max(arr, key=lambda x: x[1])[1]
    dp = [[0 for _ in range(max_d + max_t + 1)] for _ in range(len(arr) + 1)]
    max_tasks = 1

    for i in range(len(arr)):
        for d in range(max_d + max_t + 1):
            t_i, d_i = arr[i]
            # do not do task
            dp[i + 1][d] = max(dp[i+1][d], dp[i][d])
            if d <= d_i:
                dp[i + 1][d + t_i] = max(dp[i + 1][d + t_i], dp[i][d] + 1)

    for d in range(max_d + max_t + 1):
        if max_tasks < dp[-1][d]:
            max_tasks = dp[-1][d]

    return max_tasks


def manage_time_back(arr: List[Tuple[int, int]]) -> int:
    max_t = max(arr, key=lambda x: x[0])[0]
    max_d = max(arr, key=lambda x: x[1])[1]
    dp = [[0 for _ in range(max_d + max_t + 1)] for _ in range(len(arr))]
    for d in range(arr[0][1] + 1):
        dp[0][d + arr[0][0]] = 1
    max_tasks = 1

    for i in range(1, len(arr)):
        t_i, d_i = arr[i]
        for d in range(d_i + 1):
            for j in range(i):
                val = dp[j][d] + 1
                if val > dp[i][d + t_i]:
                    dp[i][d + t_i] = val
                    if max_tasks < val:
                        max_tasks = val
    return max_tasks


def brute_force_solution(arr: List[Tuple[int, int]]) -> int:
    def build(cur_time: int, num_done: int, last_idx: int) -> int:
        cur_best = num_done
        for i in range(last_idx + 1, len(arr)):
            if cur_time <= arr[i][1]:
                assert i > last_idx
                val = build(cur_time + arr[i][0], num_done + 1, i)
                if val > cur_best:
                    cur_best = val
        return cur_best
    return build(0, 0, -1)


if __name__ == '__main__':
    arr = [
        (2, 6), (5, 6), (5, 6), (2, 9)
    ]
    print(manage_time(arr))
    print(brute_force_solution(arr))

    import random

    for j in range(100):
        n = random.randint(4, 20)
        arr = []
        for _ in range(n):
            arr.append((random.randint(1, 1000), random.randint(1, 1000)))
        br = brute_force_solution(arr)
        mt = manage_time(arr)
        assert br == mt

    arr = [
        (8, 25), (5, 12), (7, 10), (11, 28), (3, 18),
        (6, 32), (10, 45), (5, 34), (7, 28), (6, 42)
    ]

    print(manage_time(arr))
    print(brute_force_solution(arr))

    with open('problems/time.in', 'r') as fp:
        n = int(fp.readline().strip())
        arr = []
        for i in range(n):
            t, d = [int(s) for s in fp.readline().strip().split()]
            arr.append((t, d))
        print(manage_time(arr))
        print(brute_force_solution(arr))

    with open('problems/time2.in', 'r') as fp:
        n = int(fp.readline().strip())
        arr = []
        for i in range(n):
            t, d = [int(s) for s in fp.readline().strip().split()]
            arr.append((t, d))
        print(manage_time(arr))
