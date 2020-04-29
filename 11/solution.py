
class AutoComplete():

    class Node():
        def __init__(self, val):
            """Each node has a value, which is a character, all strings that are below this node and branches to next characters"""
            self.val = val
            self.strings = []
            self.branches = {}
    
    
    def __init__(self, strings):
        """ Constructing a tree from the input strings """
        self.strings = self.Node('')
        for string in strings:
            curr_node = self.strings
            for char in string:
                curr_node.strings.append(string)
                if char not in curr_node.branches:
                    curr_node.branches[char] = self.Node(char)
                
                curr_node = curr_node.branches[char]
            curr_node.strings.append(string)
    
    def lookup(self, qry):
        """ searches the strings tree to find the subtree that contains all strings for the provided substring"""
        curr_node = self.strings
        for char in qry:
            if char not in curr_node.branches:
                return []
            else:
                curr_node = curr_node.branches[char]
        return curr_node.strings
        


ac = AutoComplete(['dog', 'deer', 'deal', 'test', 'tett', 'red'])
assert (ac.lookup('de') == ['deer', 'deal']), 'Error 1'
assert (ac.lookup('dee') == ['deer']), 'Error 2'
assert (ac.lookup('te') == ['test', 'tett']), 'Error 3'
assert (ac.lookup('r') == ['red']), 'Error 4'
print('All passed')