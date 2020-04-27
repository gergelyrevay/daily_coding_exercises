
def count_unival_tree(tree):
    # check if leaf, then return (ctr, val, is_broken)
    if tree['left'] == None and tree['right'] == None:
        return 1, tree['val'], False

    # case when only right continues
    elif tree['left'] == None and tree['right'] != None:
        ctr, val, is_broken = count_unival_tree(tree['right'])
        if is_broken:
            return ctr, tree['val'], is_broken
        elif val == tree['val']:
            return ctr+1, tree['val'], is_broken
        else:
            return ctr, tree['val'], True
    
    # case when only left continues
    elif tree['left'] != None and tree['right'] == None:
        ctr, val, is_broken = count_unival_tree(tree['left'])
        if is_broken:
            return ctr, tree['val'], is_broken
        elif val == tree['val']:
            return ctr+1, tree['val'], is_broken
        else:
            return ctr, tree['val'], True

    #case when both left and right continue       
    else:
        ctr_l, val_l, is_broken_l = count_unival_tree(tree['left'])
        ctr_r, val_r, is_broken_r = count_unival_tree(tree['right'])
        
        ctr = ctr_l + ctr_r

        if is_broken_r or is_broken_l:
            return ctr, tree['val'], True
        elif val_l == tree['val'] and val_r == tree['val']:
            return ctr+1, tree['val'], False
        else:
            return ctr, tree['val'], True
        
testtree = {'val':0, 'left':{'val': 1, 'left': None, 'right': None}, 'right':{'val': 0, 'left': {'val': 1, 'left': {'val': 1, 'left': None, 'right': None}, 'right': {'val': 1, 'left': None, 'right': None}}, 'right': {'val': 0, 'left': None, 'right': None}} }

ctr, val, is_broken = count_unival_tree(testtree) 
assert (ctr == 5), 'Error 1'

testtree = {'val':0, 'left':{'val': 1, 'left': None, 'right': None}, 'right':{'val': 0, 'left': {'val': 1, 'left': {'val': 1, 'left': None, 'right': None}, 'right': {'val': 1, 'left': None, 'right': {'val': 1, 'left': {'val': 1, 'left': None, 'right': None}, 'right': None}}}, 'right': {'val': 0, 'left': None, 'right': None}} }

ctr, val, is_broken = count_unival_tree(testtree) 
assert (ctr == 5), 'Error 2'
print('All passed')