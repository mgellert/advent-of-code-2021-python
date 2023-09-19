class Wrapper:
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return str(self.value)

    def add(self, other):
        self.value += other.value

    def split(self):
        new_value = self.value // 2
        return Wrapper(new_value), Wrapper(new_value + (self.value % 2))


def parse(raw):
    return eval(raw)


def wrap(number):
    for idx, n in enumerate(number):
        if type(n) == int:
            number[idx] = Wrapper(n)
        else:
            wrap(n)
    return number


def unwrap(number):
    if number is None:
        return
    for idx, n in enumerate(number):
        if type(n) == Wrapper:
            number[idx] = n.value
        else:
            unwrap(n)
    return number


def add(left, right):
    return [left, right]


def _flatten(number, flattened):
    for idx, n in enumerate(number):
        if type(n) == list:
            _flatten(number[idx], flattened)
        else:
            flattened.append(n)
    return flattened


def _find_left(flattened, left):
    idx = flattened.index(left)
    if idx > 0:
        return flattened[idx - 1]


def _find_right(flattened, right):
    idx = flattened.index(right)
    if (idx + 1) < len(flattened):
        return flattened[idx + 1]


def explode(number):
    return _explode(number, number, 0)


def _explode(number, original, depth):
    for idx, n in enumerate(number):
        if type(n) == list and depth == 3:
            flattened = _flatten(original, [])
            left, right = number[idx]

            left_neighbour = _find_left(flattened, left)
            right_neighbour = _find_right(flattened, right)

            number[idx] = Wrapper(0)

            if left_neighbour is not None:
                left_neighbour.add(left)

            if right_neighbour is not None:
                right_neighbour.add(right)

            return original
        elif type(n) == list:
            result = _explode(n, original, depth + 1)
            if result is not None:
                return result


def split(number):
    return _split(number, number)


def _split(number, original):
    for idx, n in enumerate(number):
        if type(n) == Wrapper and n.value > 9:
            number[idx] = [*n.split()]
            return original
        elif type(n) == list:
            result = _split(n, original)
            if result is not None:
                return result


def magnitude(number):
    if type(number) == list and len(number) == 2 and all(type(n) is Wrapper for n in number):
        return number[0].value * 3 + number[1].value * 2
    elif type(number[0]) == list and type(number[1]) == Wrapper:
        return magnitude(number[0]) * 3 + number[1].value * 2
    elif type(number[0]) == Wrapper and type(number[1]) == list:
        return number[0].value * 3 + magnitude(number[1])
    else:
        return magnitude(number[0]) * 3 + magnitude(number[1]) * 2


def reduce(number):
    while True:
        has_split = False
        has_exploded = explode(number) is not None
        if not has_exploded:
            has_split = split(number) is not None
        if not has_exploded and not has_split:
            break
    return number


def calc_sum(lines):
    numbers = [wrap(parse(line)) for line in lines]
    number = numbers[0]
    for i in range(1, len(numbers)):
        number = add(number, numbers[i])
        number = reduce(number)
    return magnitude(number)


def calc_max_sum(lines):
    magnitudes = []
    for x in lines:
        for y in lines:
            if x != y:
                n = wrap(parse(x))
                m = wrap(parse(y))
                magnitudes.append(magnitude(reduce(add(n, m))))

                o = wrap(parse(x))
                p = wrap(parse(y))
                magnitudes.append(magnitude(reduce(add(p, o))))

    return max(magnitudes)
