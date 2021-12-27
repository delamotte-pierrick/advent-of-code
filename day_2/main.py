def day_2(filename):
    f = open(filename, "r")
    depth = 0
    h_position = 0

    for x in f:
        y = x.split(' ')
        instruction = int(y[1])
        if y[0] == 'forward':
            h_position += instruction
        if y[0] == 'up':
            depth -= instruction
        if y[0] == 'down':
            depth += instruction

    return depth * h_position


def day_2_2(filename):
    f = open(filename, "r")
    depth = 0
    h_position = 0
    aim = 0

    for x in f:
        y = x.split(' ')
        instruction = int(y[1])
        if y[0] == 'forward':
            h_position += instruction
            depth += aim*instruction
        if y[0] == 'up':
            aim -= instruction
        if y[0] == 'down':
            aim += instruction

    return depth * h_position


print(day_2('./data/input_2.txt'))
print(day_2_2('./data/input_2.txt'))
