def lnan(arr):
    if len(arr) <= 2:
        return max(0, max(arr))

    max_excluding_last= max(0, arr[0])
    max_including_last = max(max_excluding_last, arr[1])

    for num in arr[2:]:
        prev_max_including_last = max_including_last

        max_including_last = max(max_including_last, max_excluding_last + num)
        max_excluding_last = prev_max_including_last

    return max(max_including_last, max_excluding_last)

assert (lnan([2, 4, 6, 2, 5])==13), 'Error 1'
assert (lnan([5, 1, 1, 5])==10), 'Error 2'
assert (lnan([1, 1, 1, 1])==2), 'Error 3'
assert (lnan([-5, 1, 3, 1])==3), 'Error 4'
assert (lnan([5, 1, 3, 1, -7])==8), 'Error 5'
assert (lnan([5, 1, 3, 1, 0])==8), 'Error 6'
print("All passed")