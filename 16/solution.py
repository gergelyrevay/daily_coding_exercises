log = []
N = 5

def record(order_id):
    if len(log) >= 5:
        log.pop(0)
        log.append(order_id)
    else:
        log.append(order_id)

def get_last(i):
    return log[-1*i]


record(1)
record(2)
record(3)
record(4)
record(5)
record(6)
record(7)
assert (log[0] == 3), 'Error 1'
assert (log[N-1] == 7), 'Error 2'
assert (get_last(3) == 5), 'Error 3'
print('All passed')