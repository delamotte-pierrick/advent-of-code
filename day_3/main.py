import numpy as np


def day_3(filename):
    f = np.array(list(map(list, open(filename, "r"))))
    epsilon = ''
    gamma = ''

    for i in range(len(f[0]) - 1):
        bits = list(f[:, i])
        if bits.count('0') > bits.count('1'):
            gamma += '0'
            epsilon += '1'
        else:
            gamma += '1'
            epsilon += '0'

    return int(gamma, 2) * int(epsilon, 2)


def day_3_2(filename):
    f = np.array(list(map(list, open(filename, "r"))))
    oxygen = day3_2_find_data(np.copy(f), False)
    co2 = day3_2_find_data(np.copy(f), True)

    return int(oxygen, 2) * int(co2, 2)


def day3_2_find_data(dataset, opposite):
    sub_array_len = len(dataset[0]) - 1
    i = 0
    while (len(dataset) > 1) and (i < sub_array_len):
        bits = list(dataset[:, i])
        bits0 = bits.count('0')
        bits1 = bits.count('1')

        greater = '0'
        smaller = '1'
        if opposite:
            greater = '1'
            smaller = '0'

        filtered_dataset = dataset
        if bits0 > bits1:
            filtered_dataset = filter(lambda c: c[i] == greater, dataset)
        elif bits0 <= bits1:
            filtered_dataset = filter(lambda c: c[i] == smaller, dataset)

        dataset = np.array(list(filtered_dataset))

        i += 1

    return ''.join(list(dataset[0]))


print(day_3('./data/input_3.txt'))
print(day_3_2('./data/input_3.txt'))
