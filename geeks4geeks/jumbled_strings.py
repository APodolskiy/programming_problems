TEMPLATE = 'GEEKS'


def sol(s: str) -> int:
    tmp_size = len(TEMPLATE)
    str_size = len(s)
    dp = [[0 for _ in range(tmp_size + 1)] for _ in range(str_size + 1)]

    for i in range(1, str_size + 1):
        for j in range(1, tmp_size + 1):
            if TEMPLATE[j - 1] == s[i - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                if j == 1:
                    dp[i][j] += 1
            else:
                dp[i][j] = dp[i - 1][j]
    return dp[-1][-1]


if __name__ == '__main__':
    assert sol('GEEKS') == 1
    assert sol('AGEEKKSB') == 2
