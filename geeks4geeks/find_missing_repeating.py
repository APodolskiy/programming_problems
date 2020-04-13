from typing import List, Tuple


def sol(n: int, l: List) -> Tuple[int, int]:
    true_sum, true_sq_sum = 0, 0
    list_sum, list_sq_sum = 0, 0

    for i, l_i in zip(range(1, n + 1), l):
        true_sum += i
        true_sq_sum += i**2
        list_sum += l_i
        list_sq_sum += l_i**2

    diff = true_sum - list_sum
    diff_sq = true_sq_sum - list_sq_sum
    val_1 = (diff_sq - diff**2) / (2 * diff)
    val_2 = (diff_sq + diff**2) / (2 * diff)
    return val_1, val_2


if __name__ == '__main__':
    assert sol(2, [2, 2]) == (2, 1)
    assert sol(3, [1, 3, 3]) == (3, 2)
    print(sol(11, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]))
    assert sol(11, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10]) == (10, 11)
