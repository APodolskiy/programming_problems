def solution(n: int, k: int) -> int:
    memo = {}
    def comp_coeff(n: int, k: int) -> int:
        if (n, k) in memo:
            return memo[(n, k)]
        if k == n or k == 0:
            return 1
        res = comp_coeff(n - 1, k) + comp_coeff(n - 1, k - 1)
        memo[(n, k)] = res
        return res
    return comp_coeff(n, k)


if __name__ == '__main__':
    n, k = 3, 2
    print(solution(n, k))
    n, k = 50, 20
    print(solution(n, k))
