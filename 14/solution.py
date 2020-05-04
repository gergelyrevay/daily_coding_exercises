import random
import sys

n_inner = 1
n_total = 1

while True:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)

    if (x*x + y*y) <=1:
        n_inner += 1
    n_total += 1

    pi = 4*(n_inner / n_total)
    sys.stdout.write('\rPi is: {:.3f} '.format(pi))
    sys.stdout.flush()
