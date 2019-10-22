"""User arguments (standard input) vs command line arguments and how to get them"""

# command line arguments are those you input after the file name when executing it from the terminal window
# - like the useargument.py file, for example:
# python useargument.py Bob
# -> 'Bob' is a command line argument
# you can put multiple arguments there, separated by spaces
# to access them, use sys package

import sys
import stdio

# command line arguments are stored as a list in sys.argv
all_cmd_arguments = sys.argv
print(f"All command line arguments: {all_cmd_arguments}")  # Note: the first argument (position 0) is the file name

# you can access the arguments by indexing the list
# the two ways below are exactly equivalent
cmd_argument1 = all_cmd_arguments[1]
cmd_argument2 = sys.argv[2]
# careful: this is going to give you an index error if you don't actually put the arguments after the file name
# can you think of how to check how many arguments are there?

print(f"Command line argument 1: {cmd_argument1}; command line argument 2: {cmd_argument2}")


# =================================================================================================
print("\nLet's consider the standard input now")
# standard input arguments are those you explicitly ask the user for in your code
# two ways to do that:

# 1) Python built-in 'input' function
user_argument1 = input("\nEnter an integer: ")  # you can add a custom message
print(f"User argument 1: {user_argument1} (type: {type(user_argument1)}")  # be careful, in Python 3 it is a string!
user_argument1_num = int(user_argument1)  # convert the argument to an integer; works similarly for floats etc
print(f"After conversion: {user_argument1_num} (type: {type(user_argument1_num)})")

# 2) stdio.readInt function (or equivalent)
print(f"\nEnter another integer")
user_argument2 = stdio.readInt()  # it's not that simple to put a message inside
print(f"User argument 2: {user_argument2} (type: {type(user_argument2)}")  # already an integer
