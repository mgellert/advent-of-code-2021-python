from typing import List


def read_file() -> List[str]:
    with open("../inputs/day10", "r") as file:
        return [line.strip() for line in file.readlines()]


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
    found_at_least_one = True
    while found_at_least_one:
        found_at_least_one = False
        for bracket in brackets:
            index = line.find(bracket)
            if index != -1:
                line = line[:index] + line[index + 2:]
                found_at_least_one = True
    return line


def _score_illegal_line(line: str) -> int:
    closing_positions = [line.find(x) for x in error_scoring.keys() if line.find(x) > -1]
    if len(closing_positions) == 0:
        return 0
    return error_scoring[line[min(closing_positions)]]


def calculate_syntax_error_score(lines: List[str]) -> int:
    return sum([_score_illegal_line(_reduce_line(l)) for l in lines])


def _score_incomplete_line(line: str) -> int:
    if _score_illegal_line(line) > 0:
        return 0
    score = 0
    for c in line[::-1]:
        score = score * 5 + autocomplete_scoring[c]
    return score


def calculate_autocomplete_score(lines: List[str]) -> int:
    scores = []
    for line in lines:
        score = _score_incomplete_line(_reduce_line(line))
        if score > 0:
            scores.append(score)
    scores = list(sorted(scores))
    return scores[len(scores) // 2]
