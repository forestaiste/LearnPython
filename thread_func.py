import threading
from time import sleep
from datetime import datetime


loops = [4, 2]
date_time_format = '%y-%M-%d %H:%M:%S'


class ThreadFunc(object):
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)


def date_time_str(date_time):
    return datetime.strftime(date_time, date_time_format)


def loop(n_loop, n_sec):
    print(f'Thread({n_loop}) start: {date_time_str(datetime.now())}, after sleep {n_sec} seconds')
    sleep(n_sec)
    print(f'Thread({n_loop}) sleep end, end at: {date_time_str(datetime.now())}')


def main():
    print(f'--- all threads start at: {date_time_str(datetime.now())}')
    threads = []
    n_loops = range(len(loops))

    for i in n_loops:
        t = threading.Thread(target=ThreadFunc(loop, (i, loops[i]), loop.__name__))
        threads.append(t)

    for i in n_loops:
        threads[i].start()

    for i in n_loops:
        threads[i].join()

    print(f'---all threads end at: {date_time_str(datetime.now())}')


if __name__ == '__main__':
    main()
