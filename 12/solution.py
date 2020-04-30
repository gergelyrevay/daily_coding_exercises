def num_of_ways(n):
    """ rerturs the number of ways to step up a staircase with n steps
    if you can step 1 or 2 steps at a time"""
    if n == 0 or n == 1:
        return 1
    
    n_minus_2_step = 1
    n_minus_1_step = 1
    n_step = None

    #num_of_ways(n) = num_of_ways(n-1) + num_of_ways(n-2)
    for i in range(n-1):
        n_step = n_minus_1_step + n_minus_2_step
        n_minus_2_step = n_minus_1_step
        n_minus_1_step = n_step
    
    return n_step

assert (num_of_ways(0) == 1), "Error 1"
assert (num_of_ways(1) == 1), "Error 2"
assert (num_of_ways(2) == 2), "Error 3"
assert (num_of_ways(3) == 3), "Error 4"
assert (num_of_ways(4) == 5), "Error 5"
print("All pass")
