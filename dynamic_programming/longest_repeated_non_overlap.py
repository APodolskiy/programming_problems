# Longest Repeated non-overlapping substring


def solution(string: str) -> int:
    chars = list(string)
    length = len(chars)
    dp = [[0]*length for _ in range(length)]
    cur_max = 0
    sol_i, sol_j = 0, 0

    for j in range(1, length):
        if chars[0] == chars[j]:
            dp[0][j] = 1
            cur_max = 1
            sol_i, sol_j = 0, j

    for i in range(1, length):
        for j in range(i+1, length):
            if chars[i] == chars[j] and (j - i) > dp[i - 1][j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if cur_max < dp[i][j]:
                    cur_max = dp[i][j]
                    sol_i, sol_j = i, j
            else:
                dp[i][j] = 0
    sol = []
    if sol_i or sol_j:
        while sol_i >= 0 and chars[sol_i] == chars[sol_j]:
            sol.append(chars[sol_i])
            sol_i -= 1
            sol_j -= 1
    sol.reverse()
    print("".join(sol))
    return cur_max


if __name__ == '__main__':
    tests = [
        'geeksforgeeks',
        'aab',
        'aaaaaaaaaaa',
        'banana'
    ]
    for test in tests:
        print(solution(test))
