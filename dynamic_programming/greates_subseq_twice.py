from pprint import pprint


def solution(s: str) -> int:
    chars = list(s)
    l = len(chars)
    dp = [[0]*l for _ in range(l)]

    cur_max = 0
    for j in range(l):
        for i in range(j + 1, l):
            if j == 0:
                dp[i][j] = max(1 if chars[i] == chars[j] else 0, dp[i - 1][j] if i > 0 else 0)
            else:
                if chars[i] == chars[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(
                        dp[i][j - 1],
                        dp[i - 1][j]
                    )
            if dp[i][j] > cur_max:
                cur_max = dp[i][j]
    assert cur_max == max(max(d) for d in dp)
    return cur_max


if __name__ == "__main__":
    tests = {
        'abaaca': 3,
        'ccacassuiaca': 5,
        'ABCABD': 2,
        'ABBB': 2,
        'AAB': 1,
        'AABBC': 2,
        'ABCDACB': 2,
        'ABCD': 0,
        'iiaucsdwzpushmomgdyphxg'
        'mdbibucycmyxoscnutjmcvcq'
        'dgoupocbremuaqsdcsctneih'
        'zrvboyrsghmvvpyovkjvadadw'
        'cylggshzninnbhvjusglrvibgd'
        'ejgjfihqrpkyoajdpkllvhfes'
        'wzaahfeqlnyuwqnlblbdwesjpde'
        'wjiohjqjqynjlchhyxulagmdcrw'
        'lgbsfmcvwomfgmtpxxyfywzjyhycmpy'
        'xxbrcowakkmpqakixkgciectdjrhvgh'
        'vgiokykkkuycnymvwydagicanorwladiil'
        'xsmhfwedytenocltcsdfusvnognrrvfoqrxv'
        'pdyowedmgoijilqeelsstfmkdtatkaobforctu'
        'qbjyktmayqnqkhxytarwvdyjfdawhvrywcyhxkjvc'
        'xnpglnbnfxjkxspbuoiphimjhvgteewbrnhcaj'
        'qhibugtjjqzrfgctploygteewvrgaupsbztx'
        'hohqegkmpmfezuefpiklgbrgviazktw'
        'rjfiooucdihjhdqosayegcxozgoa'
        'qjzjtgtjunlzvuleydvqdtwkxuazcpzuaa'
        'fthzedorfmmqqktlcyhbigvjfzahvaha'
        'wozcsouxaipsukgwipztvu': 202
    }

    for s, v in tests.items():
        assert v == solution(s)
        print(solution(s))
