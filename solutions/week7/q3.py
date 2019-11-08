# The condition on this question that you shouldn't use 'if' sounds
# like it is a big restriction, but it really isn't. What you should
# do is try and combine your conditions into one 'if' of the form
#
#   if condition:
#       return True
#   else:
#       return False
#
# because this can be replaced with the equivalent expression
#
#   return condition

def majority(a, b, c):
    return (a and b) or (a and c) or (b and c)

# Alternatively, we can treat booleans as integers as in the example
# in q2.py
def majority_2(a, b, c):
    return a + b + c >= 2
