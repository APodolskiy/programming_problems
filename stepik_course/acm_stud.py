from typing import List


def solve(time: int, probs: List[int]):
    probs.sort()
    cur_time = 0
    penalty = 0
    num_tasks = 0
    for prob in probs:
        if prob > time - cur_time:
            break
        penalty += prob + cur_time
        cur_time += prob
        num_tasks += 1
    return penalty, num_tasks


if __name__ == '__main__':
    arr = [30, 40, 20, 20]
    print(solve(60, arr))
    arr = [30, 40, 20]
    print(solve(60, arr))
    with open("problem/contest.in", 'r') as fp:
        n, t = fp.readline().strip().split()
        t = int(t)
        arr = [int(ch) for ch in fp.readline().strip().split()]
        print(solve(t, arr))
