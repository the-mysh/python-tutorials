array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9]

# We loop from 0 till half way through the list
# If we loop all the way, we will undo our work (try it and see)
for i in range(len(array) // 2):
    # Save array[i] for later, or we will lose it when we assign to array[i]
    temp = array[i]
    # take the ith value from back and put it in the ith place from the front
    array[i] = array[len(array) - i - 1]
    # then put the value that was in the ith place from front, and put
    # it to the ith place from the back
    array[len(array) - i - 1] = temp
