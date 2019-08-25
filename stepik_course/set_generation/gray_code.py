from typing import List


def generate_gray_codes_rec(n: int) -> List[List[int]]:
    if n == 1:
        return [[0], [1]]
    codes_prev = generate_gray_codes_rec(n - 1)
    codes_new = [[0] + code for code in codes_prev]
    codes_new.extend([[1] + code for code in reversed(codes_prev)])
    return codes_new


def generate_gray_codes_iter(n: int):
    codes = [[0 for _ in range(n)]]

    for i in range(n):
        for j in range(2 ** i):
            codes.append(list(codes[2 ** i - j - 1]))
            codes[-1][i] = 1
    print(codes)


def generate_k_dim_gray_codes(n: int, k: int):
    arr = [0 for _ in range(n)]
    print(arr)
    direct = [1 for _ in range(n)]

    while True:
        ind = n - 1
        while ind >= 0:
            if (arr[ind] == 0 and direct[ind] == 0) or (arr[ind] == k - 1 and direct[ind] == 1):
                # Change direction
                direct[ind] = (direct[ind] + 1) % 2
            else:
                break
            ind -= 1
        if ind < 0:
            break
        arr[ind] += 2*direct[ind] - 1
        print(arr)


if __name__ == '__main__':
    from pprint import pprint
    pprint(generate_gray_codes_rec(2))
    pprint(generate_gray_codes_rec(3))
    pprint(generate_gray_codes_rec(4))

    generate_gray_codes_iter(2)
    generate_gray_codes_iter(3)
    generate_gray_codes_iter(4)

    generate_k_dim_gray_codes(3, 3)
