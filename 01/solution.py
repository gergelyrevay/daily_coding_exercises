def is_sum_simple(numbers, k):
    """Returns true if k is the sum of any two element of numbers, otherwise false."""
    if len(numbers) == 0 or len(numbers) == 1:
        return False
        
    #easy solution
    for i in range(len(numbers)):
        for j in range(i+1,len(numbers)):
            if k == numbers[i] + numbers[j]:
                return True

def is_sum_one_go(numbers, k):
    """Returns true if k is the sum of any two element of numbers, otherwise false."""
    if len(numbers) == 0 or len(numbers) == 1:
        return False

    for i in range(len(numbers)):
        if k-numbers[i] in numbers:
            return True
    
def is_sum(numbers, k):
    return is_sum_one_go(numbers, k)

assert (is_sum([1,2,3,4,5], 7)), "1 Failed"

# edge case k is smaller then all elements
assert (not is_sum([4,5,6,8], 3)), "2 Failed"

# edge case k cannot be satisfied
assert (not is_sum([4,5,6,8], 7)), "3 Failed"

# case k = 0
assert (not is_sum([4,5,6,8], 0)), "4 Failed"

# edge case numbers is empty
assert (not is_sum([], 7)), "5 Failed"

# edge case numbers is only one element
assert (not is_sum([4], 7)), "6 Failed"

# k is negative
assert (is_sum([4,5,6,8,-11], -7)), "7 Failed"

# there are negative numbers 
assert (is_sum([4,-5,6,8], 3)), "8 Failed"

assert is_sum([1,4,72,90, 827, 3], 72+90), "9 Failed"

print("All passed")
