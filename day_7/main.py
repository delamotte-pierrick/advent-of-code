import numpy as np


def parse_data(filename):
    f = open(filename, "r")

    return list(map(int, f.read().rstrip().split(',')))


def day_7(filename):
    dataset = parse_data(filename)
    median = int(np.median(np.array(dataset)).round())

    return sum(map(lambda x: median - x if median > x else x - median, dataset))


def day_7_2(filename):
    dataset = parse_data(filename)
    mean = int(np.mean(np.array(dataset)))
    movement_numbers_down = map(lambda x: mean - x if mean > x else x - mean, dataset)

    return int(sum(map(lambda x: (x ** 2 + x) / 2, movement_numbers_down)))


print(day_7("./data/input_7.txt"))
print(day_7_2("./data/input_7.txt"))
