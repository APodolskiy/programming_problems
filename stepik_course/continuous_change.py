from typing import List, Tuple


def solve(weight: int, arr_obj: List[Tuple[int, int]]):
    arr_obj.sort(key=lambda x: x[1]/x[0], reverse=True)

    total_cost = 0
    w_remain = weight
    for (w, c) in arr_obj:
        if w < w_remain:
            w_remain -= w
            total_cost += c
        else:
            c = c * (w_remain / w)
            total_cost += c
            break
    return total_cost


if __name__ == '__main__':
    res = solve(4, [(2, 10), (3, 12)])
    print(res)
    with open('problems/cont.in', 'r') as fp:
        _, W = fp.readline().strip().split()
        W = int(W)
        arr = []
        for line in fp.readlines():
            w, c = [int(ch) for ch in line.strip().split()]
            arr.append((w, c))
        print(solve(W, arr))
