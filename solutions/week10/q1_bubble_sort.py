
def bubble_sort(numbers):
    swapped = True  # flag: whether there was a swap in the last run
    number_of_iterations = 0  # (optional)

    while swapped:
        swapped = False  # we need the initial True to enter the while loop at all

        for i in range(len(numbers)-1):
            n1 = numbers[i]
            n2 = numbers[i+1]

            if n1 > n2:
                numbers[i:i+2] = [n2, n1]
                swapped = True

        number_of_iterations += 1

    print(f"Bubble sort completed in {number_of_iterations} iterations")

    return numbers
