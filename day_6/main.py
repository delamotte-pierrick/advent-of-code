import cProfile


def parse_data(filename):
    f = open(filename, "r")

    return f.read().rstrip().split(',')


def day_6(filename, duration_simulation):
    dataset = list(map(int, parse_data(filename)))

    for i in range(duration_simulation):
        # print(dataset)
        # Here create fish
        new_fish = [8] * dataset.count(0)

        # Here make them lived
        dataset = list(map(lambda fish_time: fish_time - 1, dataset))

        # Restart reproduction circle and add the new fish
        dataset = list(map(lambda fish_time: 6 if fish_time == -1 else fish_time, dataset))
        dataset = dataset + new_fish
    return len(dataset)


# Here use subtraction in place of an array to optimise the previous algorithm
def day_6_try_2(filename, duration_simulation):
    dataset = parse_data(filename)
    fishes = list(map(lambda x: '9' + ''.join(x), chunks(dataset, 1000)))

    for i in range(duration_simulation):
        new_fishes = sum(map(lambda x: str(x).count('0'), fishes))
        fishes = list(map(lambda x: x.replace('0', '7'), fishes))

        # Here create fish
        fishes = list(map(lambda x: str(int(x) - int('1' * (len(x) - 1))), fishes))
        if new_fishes > 0:
            for group in chunks('8' * new_fishes, 10000):
                fishes.append('9' + group)

    return sum(map(lambda x: len(x), fishes)) - len(fishes)


def chunks(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


# Here group all fishes by there reproduction time and make the array rotating to make them live
def day_6_2(filename, duration_simulation):
    dataset = parse_data(filename)
    fishes = []
    for i in range(9):
        fishes.append(dataset.count(str(i)))

    for i in range(duration_simulation):
        fishes_zero = fishes.pop(0)
        fishes[6] = fishes[6] + fishes_zero
        # Here add newborn fish
        fishes.append(fishes_zero)

    return sum(fishes)


cProfile.run('print(day_6("./data/input_6.txt", 80))')
cProfile.run('print(day_6_try_2("./data/input_6.txt", 80))')  # Doesn't work for 256 days, but better than the first one
cProfile.run('print(day_6_2("./data/input_6.txt", 256))')
