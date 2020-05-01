def num_uniq_chars(s):
    seen = ''
    res = 0
    for char in s:
        if char not in seen:
            res += 1
            seen += char
    
    return res

def longest_substring(k, s):
    if k <= 0:
        return 0
    
    tmp_string = {'num_uniq_chars':0, 'string':''}
    curr_best_substring = {'num_uniq_chars':0, 'string':''}

    for char in s:
        if tmp_string['num_uniq_chars'] < k:
            # haven't reached k yet
            if tmp_string['string'].find(char) == -1:
                tmp_string['num_uniq_chars'] += 1   
            tmp_string['string'] += char

        elif tmp_string['num_uniq_chars'] == k and \
            tmp_string['string'].find(char) != -1:
            # already reached k, but the char is already in the string
            tmp_string['string'] += char
   

        elif tmp_string['num_uniq_chars'] == k and \
            tmp_string['string'].find(char) == -1:
            # already reached k, and char is not used yet
            temp = tmp_string['string'] + char
            while num_uniq_chars(temp) > k:
                temp = temp[1:]

            tmp_string['string'] = temp

        if len(tmp_string['string']) > len(curr_best_substring['string']):
            curr_best_substring = tmp_string.copy()
        
    return len(curr_best_substring['string'])

            
assert (longest_substring(2, 'abcba') == 3), "Error 1"
assert (longest_substring(2, 'aaabcd') == 4), "Error 2"
assert (longest_substring(4, 'aaabcdd') == 7), "Error 3"
assert (longest_substring(3, 'aaabddcddd') == 7), "Error 4"
assert (longest_substring(1, 'aaabddcddd') == 3), "Error 5"
assert (longest_substring(3, 'aaaabdcdddeeeeee') == 11), "Error 5"
print('All passed')

