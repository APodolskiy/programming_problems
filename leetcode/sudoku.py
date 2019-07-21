from typing import List, Tuple


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        empty_cells = []

        for i in range(n):
            for j in range(n):
                if board[i][j] == '.':
                    empty_cells.append((i, j))
        self._solve(board, empty_cells)

    def _solve(self, board: List[List[str]], empty_cells: List[Tuple[int, int]]) -> bool:
        if not empty_cells:
            return True
        pprint(board)
        # Find appropriate values
        cell = empty_cells.pop(0)

        vals = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        box_r = cell[0] // 3
        box_c = cell[1] // 3
        for i in range(len(board)):
            cur_val = board[cell[0]][i]
            if cur_val in vals:
                vals.remove(cur_val)
            cur_val = board[i][cell[1]]
            if cur_val in vals:
                vals.remove(cur_val)

            cur_val = board[3*box_r + i//3][3*box_c + i % 3]
            if cur_val in vals:
                vals.remove(cur_val)

        for val in vals:
            board[cell[0]][cell[1]] = val
            res = self._solve(board, empty_cells)
            if res:
                return True

        empty_cells.insert(0, cell)
        board[cell[0]][cell[1]] = '.'
        return False


class PrioryQueue:
    def __init__(self, size):
        self.queue = [1]*size


class PriorSolution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        empty_cells = []

        for i in range(n):
            for j in range(n):
                if board[i][j] == '.':
                    empty_cells.append((i, j))
        self._solve(board, empty_cells)

    def _solve(self, board: List[List[str]], empty_cells: List[Tuple[int, int]]) -> bool:
        if not empty_cells:
            return True
        pprint(board)
        # Find appropriate values
        cell = empty_cells.pop(0)

        vals = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        box_r = cell[0] // 3
        box_c = cell[1] // 3
        for i in range(len(board)):
            cur_val = board[cell[0]][i]
            if cur_val in vals:
                vals.remove(cur_val)
            cur_val = board[i][cell[1]]
            if cur_val in vals:
                vals.remove(cur_val)

            cur_val = board[3*box_r + i//3][3*box_c + i % 3]
            if cur_val in vals:
                vals.remove(cur_val)

        for val in vals:
            board[cell[0]][cell[1]] = val
            res = self._solve(board, empty_cells)
            if res:
                return True

        empty_cells.insert(0, cell)
        board[cell[0]][cell[1]] = '.'
        return False


if __name__ == "__main__":
    from pprint import pprint
    sol = Solution()
    board1 = [
        ['5', '3', '.', '.', '7', '.', '.', '.', '.'],
        ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
        ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
        ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
        ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
        ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
        ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
        ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
        ['.', '.', '.', '.', '8', '.', '.', '7', '9']
    ]
    pprint(board1)
    sol.solveSudoku(board1)
    pprint(board1)
