def num_decode(string):

    if len(string) == 1:
        return 1
    elif len(string) == 2 and int(string) > 26:
        return 1
    elif len(string) == 2 and int(string) < 26:
        return 2
    elif int(string[:2]) <= 26:
        return num_decode(string[1:]) + num_decode(string[2:])
    else:
        return num_decode(string[1:])


# 1234:
# 1,2,3,4
# 12,3,4
# 1,23,4

# 11111:
# 1,1,1,1,1
# 11,1,1,1
# 11,11,1,
# 1,11,11
# 1,1,11,1
# 1,1,1,11
# 11,1,11
# 1,11,1,1
# print(num_decode('111'))
# print(num_decode('11111'))
assert (num_decode('111')==3), 'Error 1'
assert (num_decode('11111')==8), 'Error 2'
assert (num_decode('1234')==3), 'Error 3'
print("all passed")

