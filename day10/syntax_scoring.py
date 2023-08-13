from typing import List

brackets = ["()", "{}", "[]", "<>"]
error_scoring = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137
}
autocomplete_scoring = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4
}


def _reduce_line(line: str) -> str:
    while True:
        found_any = False
        for bracket in brackets:
            index = line.find(bracket)
            if index != -1:
                line = line[:index] + line[index + 2:]
                found_any = True
        if not found_any:
            return line


def _score_illegal_line(line: str) -> int:
    closing_positions = [line.find(x) for x in error_scoring.keys() if line.find(x) > -1]
    if len(closing_positions) == 0:
        return 0
    return error_scoring[line[min(closing_positions)]]


def part_1(lines: List[str]) -> int:
    return sum(_score_illegal_line(_reduce_line(line)) for line in lines)


def _score_incomplete_line(line: str) -> int:
    if _score_illegal_line(line) > 0:
        return 0
    score = 0
    for char in line[::-1]:
        score = score * 5 + autocomplete_scoring[char]
    return score


def part_2(lines: List[str]) -> int:
    scores = (_score_incomplete_line(_reduce_line(line)) for line in lines)
    scores = list(sorted(score for score in scores if score > 0))
    return scores[len(scores) // 2]
