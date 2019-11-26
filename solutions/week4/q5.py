example = [[True, False, True], [False, False, True]]

row_size = len(example)
# col_size is the length of first row, because in a 2d array we assume
# all rows have the same length
col_size = len(example[0])

for row in range(row_size):
    for col in range(col_size):
        if example[row][col]:
            content = "*"
        else:
            content = " "
        print("Row {} Col {}: {}".format(row, col, content))
