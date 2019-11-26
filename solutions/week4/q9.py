square = [[1,2,3],[4,5,6],[7,8,9]]
# If an array is square, then it has the same number of rows as columns
num_cols = num_rows = len(square)

copy = []
for i in range(num_rows):
    row = []
    # Go throw row, and copy into the new row array
    for j in range(num_cols):
        row.append(square[i][j])
    # append row to copy
    copy.append(row)

print(copy)


# If an array is rectangular, then the number of rows and columns may
# differ, but each row will have the same number of columns. Thus, the
# only difference will be in how we determine num_cols
rectangle = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
num_rows = len(rectangle)
# So take the length of the first row and use it for every row
num_cols = len(rectangle[0])

copy = []
for i in range(num_rows):
    row = []
    for j in range(num_cols):
        row.append(rectangle[i][j])
    copy.append(row)

print(copy)



# Finally, a ragged array is one where each row may have a different
# number of columns, so we won't be able to compute num_cols once and
# for all. Instead, we will need to compute it for *every* row.
ragged = [[1,2,3],[4,5,6,7,8],[9],[10,11],[12]]
num_rows = len(ragged)

copy = []
for i in range(num_rows):
    # So now we compute the length of the row in the loop
    num_cols = len(ragged[i])
    row = []
    for j in range(num_cols):
        row.append(ragged[i][j])
    copy.append(row)

print(copy)
