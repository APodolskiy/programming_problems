class SequenceProducer:
    def __init__(self, n: int, m: int):
        self.n, self.m = n, m
        self.a = [0]*self.n
        self.find_num = None
        self.cur_num = 0

    def find_sequence(self, find_num: int):
        self.cur_num = 0
        self.find_num = find_num
        self._find_sequence(0)

    def _find_sequence(self, idx: int):
        if idx != self.n:
            for i in range(1, self.m + 1):
                self.a[idx] = i
                self._find_sequence(idx + 1)
        else:
            self.cur_num += 1
            if self.cur_num == self.find_num:
                print(self.a)


if __name__ == '__main__':
    producer = SequenceProducer(6, 5)
    producer.find_sequence(6659)
