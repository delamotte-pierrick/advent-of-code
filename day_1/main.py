def day_1(filename):
    f = open(filename, "r")

    previous = None
    result = 0

    for x in f:
        if (previous is not None) and (int(x) > previous):
            result += 1
        previous = int(x)

    return result


def day_1_2(filename):
    previous = None
    result = 0

    with open(filename, "r") as f:
        dataset = f.read().split('\n')

        for index, x in enumerate(dataset):
            subset = list(map(int, filter(None, dataset[index:index + 3])))
            elem_sum = sum(subset)
            if (previous is not None) and (int(elem_sum) > previous):
                result += 1
            previous = int(elem_sum)

    return result


print(day_1("./data/input_1.txt"))
print(day_1_2("./data/input_1.txt"))
