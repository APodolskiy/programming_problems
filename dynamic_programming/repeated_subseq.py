from collections import Counter


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


if __name__ == "__main__":
    assert exists_sol('ABCABD')
    assert exists_sol('ABBB')
    assert not exists_sol('AAB')
    assert exists_sol('AABBC')
    assert exists_sol('ABCDACB')
    assert not exists_sol('ABCD')
    assert exists_sol('AAA')
