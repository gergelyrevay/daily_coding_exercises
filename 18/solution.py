def max_in_subarrays(array, k):
    # sub_array should be max k long
    sub_array = []

    for v in array:
        if len(sub_array) < k:
            sub_array.append(v)
        elif len(sub_array) == k:
            sub_array.pop(0)
            sub_array.append(v)
    
        if len(sub_array) == k:
            print(max(sub_array))

    pass

max_in_subarrays( [10, 5, 2, 7, 8, 7], 3)