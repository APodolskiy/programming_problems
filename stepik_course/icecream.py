from typing import List


def solve(icecreams: List[str]):
    sorts = set()
    num_companies = 1
    for idx, icecream in enumerate(icecreams):
        if icecream in sorts:
            sorts = {icecream}
            num_companies += 1
            print("Idx", idx)
        else:
            sorts.add(icecream)
    return num_companies


if __name__ == '__main__':
    arr = [
        'vanilla20',
        'pistachio',
        'strawberry',
        'blackberry',
        'vanilla20',
        'pistachio',
        'pistachio',
        'vanilla20'
    ]
    print(solve(arr))
    with open('problems/ice.in', 'r') as fp:
        _ = fp.readline().strip()
        arr = [line.strip() for line in fp.readlines()]
        print(solve(arr))
    with open('problems/ice2.in', 'r') as fp:
        _ = fp.readline().strip()
        arr = [line.strip() for line in fp.readlines()]
        print(solve(arr))
