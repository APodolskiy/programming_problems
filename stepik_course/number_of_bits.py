from typing import List


def number_of_bits(arr: List):
    def find_number_of_bits(num: int):
        bits_num = 0
        while num > 0:
            if num & 1:
                bits_num += 1
            num = num >> 1
        return bits_num
    return [find_number_of_bits(num) for num in arr]


if __name__ == '__main__':
    arr = [5, 13, 0]
    print(number_of_bits(arr))

    with open("problems/ones.in", 'r') as fp:
        _ = fp.readline()
        arr = [int(s) for s in fp.readline().strip().split()]
        print(number_of_bits(arr))
