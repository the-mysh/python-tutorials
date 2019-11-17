for i in range(1000, 2000):
    print(i, end=" ") # prints a space after the number
    if i % 5 == 4:    # 1004, 1009, 1014, etc.
        print("")     # prints a newline only
