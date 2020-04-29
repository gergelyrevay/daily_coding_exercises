from datetime import datetime
from time import sleep, time
import threading

class Scheduler:
    def __init__(self):
        self.functions = []
        t = threading.Thread(target=self.poll)
        t.start()

    def poll(self):
        while True:
            now = time() * 1000
            for fn, due in self.functions:
                if now > due:
                    fn()
            self.functions = [(fn, due) for (fn, due) in self.functions if due > now]
            sleep(0.01)

    def schedule(self, f, n):
        print('{} [+] Scheduling job'.format(datetime.now()))
        self.functions.append((f, time() * 1000 + n))


def job():
    print('{} [+] Job running'.format(datetime.now()))

s = Scheduler()
s.schedule(job, 10)
s.schedule(job, 100)
s.schedule(job, 1000)
