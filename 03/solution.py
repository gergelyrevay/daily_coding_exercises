import json

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(node):
    """ serializes a Node tree to JSON 
        node = {'val':'root', 'left':{'left.left', 'left':'null', 'right':'null'}, 'right':{'right', 'left':'null', 'right':'null'}}"""
    
    if isinstance(node.left, Node):
        left = serialize(node.left)
    elif node.left == None:
        left = "null"
    else:
        left = node.left
    
    if isinstance(node.right, Node):
        right = serialize(node.right)
    elif node.right == None:
        right = "null"
    else:
        right = node.right

    serialized_node = '{{"val":"{val}", "left":{left}, "right":{right}}}'.format(val=node.val, left=left, right=right)
    return serialized_node 

def deserialize_helper(serialized_node_obj):
    """ helper function to implement recursion"""

    if isinstance(serialized_node_obj['left'], dict):
        left = deserialize_helper(serialized_node_obj['left'])
    elif serialized_node_obj['left'] == None:
        left = None
    else:
        print("Error 1")

    if isinstance(serialized_node_obj['right'], dict):
        right = deserialize_helper(serialized_node_obj['right'])
    elif serialized_node_obj['right'] == None:
        right = None
    else:
        print("Error 1")

    node = Node(val=serialized_node_obj['val'], left=left, right=right)

    return node

def deserialize(serialized_node):
    """ deserializes a Node tree from JSON """
    serialized_node_obj = json.loads(serialized_node)

    return deserialize_helper(serialized_node_obj)




# normal cases
node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'

node = Node('root', Node('left', Node('left.left')), Node('right', right=Node('right.right')))
assert deserialize(serialize(node)).right.right.val == 'right.right'

# edge cases
node = Node('root')
assert deserialize(serialize(node)).val == 'root'

node = Node('root', Node('left', Node('left.left', Node('left.left.left'))))
assert deserialize(serialize(node)).left.left.val == 'left.left'
assert deserialize(serialize(node)).left.left.left.val == 'left.left.left'

print("All passed")