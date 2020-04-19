import math

def array_multiply_simple(array):

    # case one 0 in array
    if array.count(0) == 1:
        orig_array = array.copy()
        array.remove(0)
        return [0 if i !=0 else math.prod(array) for i in orig_array]

    # case short input or more 0 in array
    if len(array) <= 2 or array.count(0) > 1:
        return [0 for i in range(len(array))]

    total = math.prod(array)

    return [int(total/i) for i in array] 

def array_multiply_nodiv(array):
    # case one 0 in array
    if array.count(0) == 1:
        orig_array = array.copy()
        array.remove(0)
        return [0 if i !=0 else math.prod(array) for i in orig_array]

    # case short input or more 0 in array
    if len(array) <= 2 or array.count(0) > 1:
        return [0 for i in range(len(array))]
    
    ret_array = []

    for i in range(len(array)):
        tmp_array = array.copy()
        del tmp_array[i]
        ret_array.append(math.prod(tmp_array))

    return ret_array

def array_multiply(array):
    return array_multiply_nodiv(array) 

assert ([120, 60, 40, 30, 24] == array_multiply([1, 2, 3, 4, 5])), "1 Failed {}".format(array_multiply([1, 2, 3, 4, 5]))
assert ([2, 3, 6] == array_multiply([3, 2, 1])), "2 Failed"
assert ([0] == array_multiply([3])), "3 Failed"
assert ([0, 0] == array_multiply([1,2])), "4 Failed"
assert ([0, 3, 0] == array_multiply([3, 0, 1])), "5 Failed {}".format(array_multiply([3, 0, 1]))
assert ([0, 0, 0, 0] == array_multiply([3, 0, 1, 0])), "6 Failed {}".format(array_multiply([3, 0, 1, 0]))


print("[+] All passed")