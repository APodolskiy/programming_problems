from typing import List


class Stack:
    def __init__(self):
        self.stack = []

    def push(self, el):
        self.stack.append(el)

    def pop(self):
        return self.stack.pop(-1)

    def is_empty(self):
        return len(self.stack) == 0

    def __len__(self):
        return len(self.stack)


OPEN_BRACKETS = ['(', '[']
CLOSE_BRACKETS = [')', ']']
PAIRS = {
    ']': '[',
    ')': '('
}


class BracketsGenerator:
    def __init__(self, n: int):
        self.n = n
        self.seq = ['(']*2*self.n
        self.cur_num = 0
        self.find_num = None
        self.num_open = 0
        self.stack = Stack()

    def find_bracket(self, find_num: int):
        self.cur_num = 0
        self.find_num = find_num
        self._find_bracket(0)

    def _find_bracket(self, idx: int):
        if idx == self.n * 2:
            if self.stack.is_empty():
                self.cur_num += 1
                if self.cur_num == self.find_num:
                    print("".join(self.seq))
            return
        if len(self.stack) > self.n:
            return

        self.open_bracket(idx, '(')
        self.close_bracket(idx, ')')
        self.open_bracket(idx, '[')
        self.close_bracket(idx, ']')

    def open_bracket(self, idx: int, bracket: str):
        self.stack.push(bracket)
        self.seq[idx] = bracket
        self._find_bracket(idx + 1)
        self.stack.pop()

    def close_bracket(self, idx: int, bracket: str):
        if self.stack.is_empty():
            return
        el = self.stack.pop()
        if PAIRS[bracket] == el:
            self.seq[idx] = bracket
            self._find_bracket(idx + 1)
        self.stack.push(el)


def check_brackets(seq: List[str]) -> bool:
    stack = Stack()
    for el in seq:
        if el in OPEN_BRACKETS:
            stack.push(el)
        else:
            if stack.is_empty():
                return False
            else:
                prev = stack.pop()
                if PAIRS[el] != prev:
                    return False
    return stack.is_empty()


if __name__ == '__main__':
    with open('problems/brackets.in', 'r') as fp:
        for line in fp.readlines():
            print(line.strip())
            print(check_brackets(list(line.strip())))

    generator = BracketsGenerator(7)
    generator.find_bracket(8233)
