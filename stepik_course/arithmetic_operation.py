from typing import List


def solution(nums: List[int], x: int):
    signs = [True for _ in range(len(nums))]
    memo = {}
    query_to_mem = 0

    def find(s: int, n_nums: int) -> bool:
        nonlocal signs
        if (s, n_nums) in memo:
            nonlocal query_to_mem
            query_to_mem += 1
            return memo[(s, n_nums)]

        if n_nums == 1:
            return (s - nums[0]) == 0
        add_op = find(s - nums[n_nums - 1], n_nums - 1)
        sub_op = find(s + nums[n_nums - 1], n_nums - 1)
        res = add_op or sub_op
        memo[(s, n_nums)] = res
        if add_op:
            signs[n_nums - 1] = True
        if sub_op:
            signs[n_nums - 1] = False
        return res

    add_op = find(x - nums[-1], n_nums=len(nums) - 1)
    sub_op = find(x + nums[-1], n_nums=len(nums) - 1)
    if sub_op:
        signs[-1] = False
    print(query_to_mem)
    res = [str(nums[0])]
    idx = 1
    while idx < len(nums):
        res.append('+' if signs[idx] else '-')
        res.append(str(nums[idx]))
        idx += 1
    return add_op or sub_op, "".join(res)


if __name__ == '__main__':
    arr = [1, 2, 3]
    print(solution(arr, 0))
    with open('problems/arithm.in', 'r') as fp:
        _, x = fp.readline().strip().split()
        x = int(x)
        arr = [int(ch) for ch in fp.readline().strip().split()]
        print(solution(arr, x))
    with open('problems/arithm2.in', 'r') as fp:
        _, x = fp.readline().strip().split()
        x = int(x)
        arr = [int(ch) for ch in fp.readline().strip().split()]
        print(solution(arr, x))
