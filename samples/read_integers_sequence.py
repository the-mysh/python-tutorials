"""Ask the user for a sequence of positive integers"""

# first, define a list to store the numbers in
user_numbers = []

# Think of how the user should terminate the input. This is up to you. You can use e.g. an empty string, a space,
# a letter (e.g. 'q' for quit), or a longer string, such as 'exit' or 'done')
# We'll use an empty string, which means that an 'enter' alone terminates the input
terminator = ''

# define the first number here; remember, it is a string, i.e. text containing the number, not an integer
a_number_str = input("Enter an integer (or press 'enter' to terminate): ")

# build a while loop to process as many numbers as the user enters
# break the loop when the input is the terminator
while a_number_str != terminator:
    # alright, the input was not 'q'
    # let's convert it to an integer
    a_number_int = int(a_number_str)

    # you are only interested in positive numbers
    if a_number_int > 0:
        # if the number is positive, add it to the list
        user_numbers.append(a_number_int)
    else:
        # otherwise, notify the user that you're not accepting negatives - and do not add the number to the list
        print("Positive numbers only!")

    # in any case, ask for another number
    # otherwise, the loop will still be dealing with the old 'a_number_str' - most likely, it will run with it forever
    a_number_str = input("Enter another integer (or press 'enter' to terminate): ")

    # that's all for the loop; after the new input, you are moved back to the top of the loop

# display all the numbers in the list
print(f"The entered numbers: {user_numbers}")
