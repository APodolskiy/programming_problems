from typing import List


def cut(arr: List[int]) -> int:
    arr.sort(reverse=True)
    first_sum = sum(arr[:len(arr) // 2])
    second_sum = sum(arr[len(arr) // 2:])
    return first_sum - second_sum


if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    print(cut(arr))

    with open("problems/gold4.in", 'r') as fp:
        _ = fp.readline()
        arr = [int(s) for s in fp.readline().strip().split()]
        print(cut(arr))
