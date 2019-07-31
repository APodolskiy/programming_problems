from typing import List


def solve(shops: List[int], stores: List[int]) -> int:
    shops.sort()
    stores.sort()

    sum_ = 0
    for shop, store in zip(shops, stores):
        sum_ += (abs(shop - store))
    return sum_


if __name__ == '__main__':
    shops = [3, 5]
    stores = [6, 2]
    print(solve(shops, stores))

    with open('problems/shops.in', 'r') as fp:
        _ = fp.readline()
        shops = [int(s) for s in fp.readline().strip().split()]
        stores = [int(s) for s in fp.readline().strip().split()]
        print(solve(shops, stores))

    with open('problems/shops2.in', 'r') as fp:
        _ = fp.readline()
        shops = [int(s) for s in fp.readline().strip().split()]
        stores = [int(s) for s in fp.readline().strip().split()]
        print(solve(shops, stores))
