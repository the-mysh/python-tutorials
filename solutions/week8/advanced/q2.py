import sys

# The number of permutation of n letters is n! which grows
# exponentially, e.g., 10! is already ~3.6 million, so don't expect a
# fast answer for large n.

# First, we are going to use a function which returns the permutation
# of the numbers 1...n.
def permutations_helper(n):
    if n == 1:
        # if n == 1, we have one permutation of [1], namely [1], so we
        # must return the list containing [1]
        return [[1]]
    else:
        # Otherwise, we will take the permutations on n-1 and fill in
        # the number n at *every* possible position in *every*
        # permutation returned by the recursive call
        perms = permutations_helper(n-1)
        results = []
        # For every permutation
        for perm in perms:
            # At each of the n possible positions, we insert n
            for i in range(n):
                # Make a copy so we can use pythons insert method
                x = perm.copy()
                x.insert(i, n) # insert n at position i
                # Add to results
                results.append(x)
        return results

# To complete the specification, we are expected to return strings of
# letters, so we need a function to turn a permutation into a string
letters = "abcdefghijklmnopqrstuvwxyz"

def stringify(permutation):
    s = ""
    for i in permutation:
        # Permutations start at 1, but string indexes start at 0
        s += letters[i-1]
    return s

# Finally, we loop through everything returned by permutations, and
# stringify all the results
def permutations(n):
    perms = permutations_helper(n)
    result = []
    for perm in perms:
        result.append(stringify(perm))
    return result


# Finally, we get our integer argument from the user
print(permutations(int(sys.argv[1])))
