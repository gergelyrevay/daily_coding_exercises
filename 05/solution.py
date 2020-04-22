"""
The return value of cons() is the pair() function which accepts a function
as an argument. Thus we can pass a lambda function to return the appropriate 
values and call the pair() with those.
"""

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


def car(pair):
    return pair(lambda a,b: a)

def cdr(pair):
    return pair(lambda a,b: b)

assert (car(cons(3,4)) == 3), "Error 1"
assert (cdr(cons(3,4)) == 4), "Error 2"
assert (cdr(cons(3,0)) == 0), "Error 3"
assert (car(cons(-5,4)) == -5), "Error 4"

print("all passed")