from collections import Counter
from typing import Optional


def exists_sol(s: str) -> bool:
    """
    Analyze whether repeated sub-sequence exists or not
    :param s: string of characters to be analyzed
    :return: true if repeated sub-sequence exists else false
    """
    cnt = Counter(s)
    ls = []
    for el in s:
        if cnt[el] < 2:
            continue
        ls.append(el)
    res = False
    size = len(ls)
    for i in range(size // 2):
        if ls[i] != ls[size - i - 1]:
            res = True
            break
    if size % 2 and ((ls[size // 2 + 1] == ls[0]) or (ls[size // 2 + 1] == ls[-1])):
        res = True
    return res


def find_longest_repeated_subseq(s: str) -> str:
    """
    Finds repeated subsequence in a given sequence.
    If there are no such subsequence then it returns empty string.
    :param s: string to be analyzed
    :return: repeated subsequence or empty string if there is none such substring.
    """
    # Finding longest common sub-sequence
    seq1 = list(s)
    seq2 = list(s)
    size = len(seq1)
    if size <= 1:
        return None

    # Dynamic programming
    dp = [[0 for _ in range(size + 1)] for _ in range(size + 1)]
    max_val = 0
    i_idx, j_idx = 0, 0
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            if i == j:
                continue
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            if seq1[i - 1] == seq2[j - 1]:
                dp[i][j] = max(dp[i - 1][j - 1] + 1, dp[i][j])
    i_idx, j_idx = size - 1, size
    max_val = dp[i_idx][j_idx]
    res_seq = []
    while max_val > 0:
        if seq1[i_idx - 1] == seq2[j_idx - 1]:
            res_seq.append(seq1[i_idx - 1])
            max_val -= 1
            i_idx, j_idx = i_idx - 1, j_idx - 1
        else:
            if dp[i_idx - 1][j_idx] > dp[i_idx][j_idx - 1]:
                i_idx = i_idx - 1
            else:
                j_idx = j_idx - 1
    res_seq.reverse()
    return "".join(res_seq)


if __name__ == "__main__":
    assert exists_sol('ABCABD')
    assert exists_sol('ABBB')
    assert not exists_sol('AAB')
    assert exists_sol('AABBC')
    assert exists_sol('ABCDACB')
    assert not exists_sol('ABCD')
    assert exists_sol('AAA')

    assert len(find_longest_repeated_subseq('ABCABD')) == 2
    assert len(find_longest_repeated_subseq('AAA')) == 2
    print(find_longest_repeated_subseq('ABCABD'))
    print(find_longest_repeated_subseq('AAA'))
    print(find_longest_repeated_subseq('ABCDACB'))
