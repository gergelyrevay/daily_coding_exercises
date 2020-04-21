def find_missing(numbers):
    pot_res = [None, None]
    min = None
    for num in numbers:
        if pot_res == [None, None]:
            pot_res[0] = num - 1
            pot_res[1] = num + 1
        elif num == pot_res[0]:
            pot_res[0] = num - 1
        elif num == pot_res[1]:
            pot_res[1] = num + 1

        if min == None or min > num:
            min = num
    
    if min - 1 != pot_res[0]:
        return pot_res[0]
    else:
        return pot_res[1]



assert (find_missing([3, 4, -1, 1]) == 2), "Error 1"
assert (find_missing([1, 2, 0]) == 3), "Error 2"
assert (find_missing([1, 2, 0, 3, 5]) == 4), "Error 3"
assert (find_missing([-1, -2, 0, 3, 2]) == 1), "Error 4"
assert (find_missing([3, -1, -2, 0, 3, 2, -1]) == 1), "Error 4"
print("All passed")