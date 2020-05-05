

def find_longest_path(fs):
    """ Iterate through the whole fs string. Maintain the current path based on tabs. Check results when file is found."""
    current_max = 0
    front_path = []
    current_element = ''
    num_tabs = 0
    is_file = False
    len_fs = len(fs)
    for i, char in enumerate(fs):

        if char == '\n' or len_fs - 1 == i:
            # at new line we need the save last dir/file to db
            # if it is a file check path length and current max
            # edge case is end of fs
            if len_fs - 1 == i:
                current_element += char
            front_path.append(current_element)
            current_element = ''
            if is_file:
                path_len = len('/'.join(front_path))
                if path_len > current_max:
                    current_max = path_len
        
        elif char == '\t':
            # counting tabs
            num_tabs += 1
        elif num_tabs != 0:
            # end of series of tabs, remove tabs number of elements from front_path
            front_path = front_path[:num_tabs]
            num_tabs = 0
            current_element = char
        elif char == '.':
            # remember, that we are dealing with a file right now
            is_file = True
            current_element += char
        else:
            # not a special char
            current_element += char

    return current_max


fs1 = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
fs2 = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
fs3 = "dir\n\tsubdir1\n\tsubdir2\n\t\t"

assert (find_longest_path(fs1) == 20), "Error 1"
assert (find_longest_path(fs2) == 32), "Error 2"
assert (find_longest_path(fs3) == 0), "Error 3"
print("All passed")