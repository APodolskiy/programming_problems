from typing import List


def find_bracket_num(bracket: str) -> int:
    n = len(bracket)
    dp = build_auxiliary_dp(n)
    print(dp)

    bracket_num = 0
    balance = 0
    for idx, s in enumerate(bracket):
        if s == '(':
            balance += 1
        elif s == ')':
            bracket_num += dp[n - idx - 1][balance + 1]
            balance -= 1
        else:
            raise ValueError(f"Wrong symbol {s} in bracket.")
    return bracket_num


def build_auxiliary_dp(n: int) -> List[List[int]]:
    assert n % 2 == 0
    """ 
    dp[i][j] - number of bracket sequences (with all closing brackets are related
    to some open bracket but open bracket could have no pair) i - length, j - balance
    """
    dp = [[0 for _ in range(0, n // 2 + 2)] for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(1, n // 2 + 2):
        dp[0][i] = 0

    for i in range(1, n + 1):
        for j in range(n // 2 + 2):
            open_bracket_end = dp[i - 1][j - 1] if j - 1 >= 0 else 0
            close_bracket_end = dp[i - 1][j + 1] if j + 1 <= n // 2 else 0
            dp[i][j] = open_bracket_end + close_bracket_end
    return dp


def bracket_with_num(n: int, k: int):
    dp = build_auxiliary_dp(2*n)
    assert k <= dp[2*n][0]
    bracket_seq = []
    depth = 0

    for idx in range(2*n - 1, -1, -1):
        if (depth <= n) and (dp[idx][depth + 1] >= k):
            bracket_seq.append('(')
            depth += 1
        else:
            bracket_seq.append(')')
            if depth + 1 <= n:
                k -= dp[idx][depth + 1]
            depth -= 1
    return ''.join(bracket_seq)


if __name__ == '__main__':
    print(find_bracket_num('(())'))
    print(find_bracket_num('()()'))
    print(find_bracket_num('(())()'))

    print(bracket_with_num(3, 1))
    print(bracket_with_num(3, 2))
    print(bracket_with_num(2, 2))
