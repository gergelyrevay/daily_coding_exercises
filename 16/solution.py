class Log:
    def __init__(self):
        self.log = []
        self.N = 5
        self.current = 0

    def record(self, order_id):
        if len(self.log) == self.N:
            self.log[self.current] = order_id
        else:
            self.log.append(order_id)
        self.current = (self.current + 1) % self.N

    def get_last(self, i):
        return self.log[self.current-i]

l = Log()
l.record(1)
l.record(2)
l.record(3)
l.record(4)
l.record(5)
l.record(6)
l.record(7)
assert (l.get_last(3) == 5), 'Error 3'
print('All passed')