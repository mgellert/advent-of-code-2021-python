from typing import Union, List


class BingoBoard:

    def __init__(self, raw: str):
        self.board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
        for i, row in enumerate(raw.strip().split("\n")):
            for j, col in enumerate(row.strip().replace("  ", " ").split(" ")):
                self.board[i][j] = int(col.strip())

    def mark(self, num: int) -> Union[None, int]:
        for i in range(0, 5):
            for j in range(0, 5):
                if self.board[i][j] == num:
                    self.board[i][j] = -1

        if self._is_winner():
            return self._sum_rest() * num

    def _is_winner(self) -> bool:
        for i in range(0, 5):
            if self._all_same(self.board[i]) or self._all_same([self.board[j][i] for j in range(0, 5)]):
                return True

    def _sum_rest(self) -> int:
        sum = 0
        for i in range(0, 5):
            for j in range(0, 5):
                if self.board[i][j] != -1:
                    sum += self.board[i][j]
        return sum

    @staticmethod
    def _all_same(nums: List[int]) -> bool:
        return len(set(nums)) == 1


def read_draws() -> List[int]:
    with open("../inputs/day04", "r") as file:
        full = file.read()
        draws = full.split("\n\n")[0]
        return [int(x) for x in draws.split(",")]


def read_boards() -> List[BingoBoard]:
    with open("../inputs/day04", "r") as file:
        full = file.read()
        boards = full.split("\n\n")[1:]
        return [BingoBoard(x) for x in boards]


def calculate_first_winner() -> int:
    draws = read_draws()
    boards = read_boards()

    for draw in draws:
        for board in boards:
            res = board.mark(draw)
            if res is not None:
                return res


def calculate_last_winner() -> int:
    draws = read_draws()
    boards = read_boards()

    for draw in draws:
        to_remove: List[BingoBoard] = []
        for board in boards:
            res = board.mark(draw)
            if res is not None and len(boards) - len(to_remove) > 1:
                to_remove.append(board)
            elif res is not None:
                return res
        for board in to_remove:
            boards.remove(board)
