example = [
    [99,85,98],
    [98,57,78],
    [92,77,76],
    [94,99,90],
    [99,34,22],
    [76,59,88],
    [92,66,89],
    [97,71,24],
    [89,29,38]
]

num_rows = len(example)
num_cols = len(example[0])

transposed = []
# The example has 9 rows and 3 columns, so the transposition will have
# 3 rows and 9 columns.
# We follow the pattern of q9, but loop over the columns in the outer
# loop, and over the rows in the inner loop instead.
for i in range(num_cols):
    row = []
    for j in range(num_rows):
        # Still need to access the row of example first, column second
        row.append(example[j][i])
    transposed.append(row)

print(transposed)
