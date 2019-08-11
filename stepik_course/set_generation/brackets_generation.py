def generate_brackets(n: int):
    assert n > 0, "Number of ops should be positive"
    print(f"Generating all valid bracket sequences of size: {n}")
    arr = ['(' for _ in range(2*n)]

    def _generate(idx: int, balance: int):
        if idx == 2*n:
            if balance == 0:
                print(''.join(arr))
            return
        if balance < n:
            arr[idx] = '('
            _generate(idx=idx + 1, balance=balance + 1)
        if balance > 0:
            arr[idx] = ')'
            _generate(idx=idx + 1, balance=balance - 1)
    _generate(idx=0, balance=0)


def generate_brackets_iteratively(n: int):
    assert n > 0, "Number of ops should be positive"
    print(f"Generating all valid bracket sequences of size: {n}")
    arr = ['(']*n + [')']*n
    idx = 2*n - 1
    while idx != 0:
        print(''.join(arr))
        balance = 0
        idx = 2*n - 1
        while idx > 0:
            if arr[idx] == '(':
                balance -= 1
                if balance > 0:
                    break
            else:
                balance += 1
            idx -= 1
        balance -= 1
        arr = arr[:idx] + [')'] + ['(']*(n - (idx + 1 + balance)//2) + [')']*(n - (idx + 1 - balance)//2)


if __name__ == '__main__':
    generate_brackets(3)
    generate_brackets(4)
    generate_brackets_iteratively(3)
    generate_brackets_iteratively(4)
