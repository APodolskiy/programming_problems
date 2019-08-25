def generate_subsets(n: int):
    print("Generating subsets, n={}".format(n))
    for mask in range(1 << n):
        res = []
        for j in range(n):
            if mask & (1 << j):
                res.append(j)
        print(res)


def generate_subsets_size_k(n: int, k: int):
    assert k <= n
    print("Generating subsets of size {} for the set of size {}".format(k, n))
    if k == 0:
        print([])
        return

    used = [True]*k + [False]*(n - k)
    arr = list(range(n))

    def print_subset():
        res = [arr[i] for i in range(n) if used[i]]
        print(res)

    print_subset()
    while True:
        cur_idx = 0
        ones_cnt = 0
        while (cur_idx < n) and (used[cur_idx] or (ones_cnt == 0)):
            if used[cur_idx]:
                ones_cnt += 1
            elif ones_cnt > 0:
                break
            cur_idx += 1
        if cur_idx == n:
            break

        used[cur_idx] = True
        used[:ones_cnt - 1] = [True]*(ones_cnt - 1)
        used[ones_cnt - 1:cur_idx] = [False]*(cur_idx - ones_cnt + 1)
        print_subset()


def generate_subsets_size_k_rec(n: int, k: int):
    print("Recursively generating subsets of size {} for the set of size {}".format(k, n))
    if k == 0:
        return []
    res = [-1]*k

    def generate(idx: int, cur_size: int):
        if cur_size == k:
            print(res)
            return
        for i in range(idx + 1, n - k + cur_size + 1):
            res[cur_size] = i
            generate(idx=i, cur_size=cur_size + 1)

    generate(-1, 0)


if __name__ == '__main__':
    generate_subsets(3)
    generate_subsets(4)
    generate_subsets_size_k(3, 2)
    generate_subsets_size_k(4, 3)
    generate_subsets_size_k(4, 4)
    generate_subsets_size_k(3, 0)
    generate_subsets_size_k_rec(3, 2)
    generate_subsets_size_k_rec(4, 3)
    generate_subsets_size_k_rec(4, 4)
    generate_subsets_size_k_rec(3, 0)
