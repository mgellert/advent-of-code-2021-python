from typing import Union, List, Tuple


class BingoBoard:

    def __init__(self, raw: str):
        self.board: List[List[Union[int, None]]] = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        for i, row in enumerate(raw.strip().split("\n")):
            for j, col in enumerate(row.strip().replace("  ", " ").split(" ")):
                self.board[i][j] = int(col.strip())

    def mark(self, num: int):
        for i in range(0, 5):
            for j in range(0, 5):
                if self.board[i][j] == num:
                    self.board[i][j] = None

    def is_winner(self) -> bool:
        for i in range(0, 5):
            if self._all_equal(self.board[i]):
                return True

        for i in range(0, 5):
            column = [self.board[j][i] for j in range(0, 5)]
            if self._all_equal(column):
                return True

        return False

    def score(self) -> int:
        score = 0
        for i in range(0, 5):
            for j in range(0, 5):
                if self.board[i][j] is not None:
                    score += self.board[i][j]
        return score

    @staticmethod
    def _all_equal(nums: List[int]) -> bool:
        return nums.count(nums[0]) == len(nums)


def parse_input(raw: str) -> Tuple[List[int], List[BingoBoard]]:
    draws, boards = raw.split("\n\n", maxsplit=1)
    return (
        [int(x) for x in draws.split(",")],  # draws
        [BingoBoard(x) for x in boards.split("\n\n")]  # boards
    )


def part_1(draws: List[int], boards: List[BingoBoard]) -> int:
    for draw in draws:
        for board in boards:
            board.mark(draw)
            if board.is_winner():
                return draw * board.score()


def part_2(draws: List[int], boards: List[BingoBoard]) -> int:
    for draw in draws:
        for board in boards:
            board.mark(draw)
        if len(boards) != 1:
            boards = [board for board in boards if not board.is_winner()]
        if len(boards) == 1 and boards[0].is_winner():
            return draw * boards[0].score()
