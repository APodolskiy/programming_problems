def generate_permutations(n: int):
    print(f"Generating permutations of size {n}")
    used = [False]*n
    res = [-1]*n

    def generate(idx: int):
        if idx == n:
            print(res)
            return
        for i in range(n):
            if not used[i]:
                used[i] = True
                res[idx] = i
                generate(idx + 1)
                used[i] = False

    generate(0)


if __name__ == '__main__':
    generate_permutations(2)
    generate_permutations(3)
    generate_permutations(4)
