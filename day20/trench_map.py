DARK_PX = '.'
LIGHT_PX = '#'


def parse(lines):
    algorithm = [*lines[0]]
    image = [line for line in lines[2:] if len(line) > 0]
    return algorithm, image


def add_border(image, outside_px):
    width = len(image[0])

    image.insert(0, outside_px * width)
    image.append(outside_px * width)

    for idx, line in enumerate(image):
        image[idx] = outside_px + line + outside_px
    return image


def _enhance_pixel(image, i, j, algorithm, outside_px):
    width = len(image[0])
    height = len(image)

    window = [[outside_px] * 3 for i in range(3)]
    for k in range(-1, 2):
        for l in range(-1, 2):
            dx = i + k
            dy = j + l

            if (0 <= dx < width) and (0 <= dy < height):
                window[k + 1][l + 1] = image[dx][dy]

    binary = ''.join(''.join(line) for line in window).replace(DARK_PX, '0').replace(LIGHT_PX, '1')
    idx = int(binary, 2)
    return algorithm[idx]


def enhance(algorithm, image, outside_px):
    new_image = []
    for i, line in enumerate(image):
        new_line = ''
        for j, px in enumerate(line):
            new_line += _enhance_pixel(image, i, j, algorithm, outside_px)
        new_image.append(new_line)
    return new_image


def count_light(image):
    count = 0
    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j] == LIGHT_PX:
                count += 1
    return count


def apply_enhancement(algorithm, image, steps):
    for step in range(steps):
        outside = DARK_PX if step % 2 == 0 else LIGHT_PX
        add_border(image, outside)
        image = enhance(algorithm, image, outside)
    return count_light(image)
