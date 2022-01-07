import numpy as np


def parse_data(filename):
    f = open(filename, "r")
    return list(
        map(lambda row: list(map(lambda coordinate: list(map(int, coordinate.split(','))), row.rstrip().split(' -> '))),
            f))


def day_5(filename):
    cleared_dataset = list(filter(lambda row: row[0][0] == row[1][0] or row[0][1] == row[1][1], parse_data(filename)))

    matrix = {}
    for data in cleared_dataset:
        x1 = data[0][0]
        x2 = data[1][0]
        y1 = data[0][1]
        y2 = data[1][1]

        if x1 > x2 or y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2 + 1) or [x1]:
            for y in range(y1, y2 + 1) or [y1]:
                key = "{},{}".format(x, y)
                matrix[key] = (matrix[key] if key in matrix else 0) + 1

    return len(list(filter(lambda value: value >= 2, matrix.values())))


def day_5_2(filename):
    parsed_data = parse_data(filename)

    # auto define max_x and max_y
    max_y = max(map(lambda data: max([data[0][0], data[1][0]]), parsed_data)) + 1
    max_x = max(map(lambda data: max([data[0][1], data[1][1]]), parsed_data)) + 1

    matrix = list(map(lambda y: [0] * max_y, [None] * max_x))
    for data in parsed_data:
        y1, x1 = data[0][0], data[0][1]
        y2, x2 = data[1][0], data[1][1]

        range_x = range(x1, x2 + 1, 1)
        if x1 > x2:
            range_x = range(x1, x2 - 1, -1)
        range_y = range(y1, y2 + 1, 1)
        if y1 > y2:
            range_y = range(y1, y2 - 1, -1)

        if y1 == y2:
            range_y = [y1] * len(range_x)
        if x1 == x2:
            range_x = [x1] * len(range_y)

        for idx, x in enumerate(range_x):
            matrix[x][range_y[idx]] += 1

    return len(list(filter(lambda value: value >= 2, np.array(matrix).flatten())))


print(day_5("./data/input_5.txt"))
print(day_5_2("./data/input_5.txt"))
