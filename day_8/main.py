import numpy as np


def parse_data(filename):
    f = open(filename, "r")

    dataset = []
    for row in f:
        dataset.append(list(map(lambda x: x.split(' '), row.rstrip().split(' | '))))

    return dataset


def day_8(filename):
    dataset = np.array(list(map(lambda x: x[1], parse_data(filename)))).flatten()
    expected_values = [2, 4, 3, 7]
    return len(list(filter(lambda x: len(x) in expected_values, dataset)))


def day_8_2(filename):
    total_result = 0

    for data in parse_data(filename):
        schema_data = list(map(lambda x: list(x), data[0]))
        result_data = list(map(lambda x: ''.join(sorted(list(x))), data[1]))
        # Here identify 1, 7, 4, 8
        one = next(x for x in schema_data if len(x) == 2)
        seven = next(x for x in schema_data if len(x) == 3)
        four = next(x for x in schema_data if len(x) == 4)
        eight = next(x for x in schema_data if len(x) == 7)
        # Here identify 3 with 7
        three, two, five, nine, zero, six = '', '', '', '', '', ''
        for x in schema_data:
            if (len(x) == 5) and (len([i for i in x if i in seven]) == 3):
                three = x
                break

        for x in schema_data:
            if len(x) == 5:
                if len([i for i in x if i in four]) == 2:
                    two = x
                if len([i for i in x if i in four]) == 3 and x != three:
                    five = x
            if len(x) == 6:
                if len([i for i in x if i in three]) == 5:
                    nine = x
                if len([i for i in x if i in seven]) == 2:
                    six = x
                if len([i for i in x if i in three]) == 4 and (len([i for i in x if i in seven]) == 3):
                    zero = x

        # Here make schema
        schema = list(map(lambda x: ''.join(sorted(x)), [zero, one, two, three, four, five, six, seven, eight, nine]))

        result = ''
        for x in result_data:
            result += str(schema.index(x))
        total_result += int(result)
        # Here find numbers
    # SUM EVERYTHING'S
    return total_result


# print(day_8("./data/input_8.txt"))
print(day_8_2("./data/input_8.txt"))
