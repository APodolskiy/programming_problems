class BracketProducer:
    def __init__(self, n: int):
        self.n = n
        self.cur_num = 0
        self.find_num = None
        self.a = ['*']*2*self.n

    def find_bracket(self, find_num: int):
        self.find_num = find_num
        self.cur_num = 0
        self._find_bracket(0, 0)

    def _find_bracket(self, idx: int, bal: int):
        if bal > self.n or bal < 0:
            return
        if idx == 2*self.n:
            if bal == 0:
                self.cur_num += 1
                print(self.cur_num, "".join(self.a))
                # if self.cur_num == self.find_num:
                #     print("".join(self.a))
        else:
            self.a[idx] = '('
            self._find_bracket(idx + 1, bal + 1)
            self.a[idx] = ')'
            self._find_bracket(idx + 1, bal - 1)


if __name__ == '__main__':
    producer = BracketProducer(10)
    producer.find_bracket(8645)
