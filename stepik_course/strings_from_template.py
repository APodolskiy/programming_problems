from typing import List, Optional


class StringSearcher:
    def __init__(self, template: str):
        self.template = template
        self.cur_num = 0
        self.find_num = None
        self.vocab = ['a', 'b', 'c', 'd', 'e']

    def find_string(self, str_num: int):
        self.cur_num = 0
        self.find_num = str_num
        self._find_string(0)

    def _find_string(self, idx: int, cur_str: Optional[str] = None):
        if cur_str is None:
            cur_str = ''

        if idx == len(self.template):
            self.cur_num += 1
            if self.cur_num == self.find_num:
                print("".join(cur_str))
            #print("".join(cur_str))
            return

        ch = self.template[idx]
        if ch == '?':
            for c in self.vocab:
                self._find_string(idx + 1, cur_str + c)
        else:
            self._findK_string(idx + 1, cur_str + ch)


if __name__ == '__main__':
    searcher = StringSearcher(template='ab?c')
    searcher.find_string(2)

    searcher = StringSearcher(template='a??cab?d?ba')
    searcher.find_string(500)

    searcher = StringSearcher(template='?be?bdcb?dcb?debcd??bdad?ee')
    searcher.find_string(5151)
