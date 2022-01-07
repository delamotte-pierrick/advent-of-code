import numpy as np


def parse_data(filename):
    f = open(filename, "r")
    playable_values = f.readline().rstrip().split(',')
    # Skip second line
    f.readline()

    boards = list()
    board = list()
    for row in f:
        striped_row = row.lstrip().rstrip()
        if not striped_row:
            boards.append(board)
            board = list()
            continue
        board.append(striped_row.split())
    # final add
    boards.append(board)

    return [playable_values, boards]


def day_4(filename):
    dataset = parse_data(filename)
    playable_values = dataset[0]
    boards = dataset[1]
    boards_process = np.copy(boards)

    for value in playable_values:
        for index, board in enumerate(boards_process):
            board = day_4_check_board(board, value)
            if day_4_verify_board(board):
                return sum(map(int, filter(lambda x: x != 'X', list(board.flatten())))) * int(value)

            boards_process[index] = board


def day_4_verify_board(board):
    # Verify row:
    for rowIndex, row in enumerate(board):
        if len(row) == list(row).count('X'):
            return True
    # Verify column:
    for colIndex in range(len(board[0])):
        col = list(board[:, colIndex])
        if len(col) == list(col).count('X'):
            return True

    return False


def day_4_check_board(board, value):
    positions = np.where(board == value)

    for index, row_position in enumerate(positions[0]):
        board[row_position][positions[1][index]] = 'X'

    return board


def day_4_2(filename):
    dataset = parse_data(filename)
    playable_values = dataset[0]
    boards = dataset[1]
    boards_process = np.copy(boards)

    for value in playable_values:
        if len(boards_process) == 1:
            data = list(boards_process[0].flatten())
            if value not in data:
                continue
            return (sum(map(int, filter(lambda x: x != 'X', data))) - int(value)) * int(value)

        index = 0
        while index < len(boards_process):
            board = day_4_check_board(boards_process[index], value)

            if day_4_verify_board(board):
                boards_process = np.delete(boards_process, index, 0)
                index = 0
                continue

            boards_process[index] = board
            index += 1


print(day_4('./data/input_4.txt'))
print(day_4_2('./data/input_4.txt'))
