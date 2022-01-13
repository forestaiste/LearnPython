import threading
from time import sleep
from datetime import datetime

loops = [4, 2]
date_time_format = '%y-%M-%d %H:%M:%S'


class MyThread(threading.Thread):
    def __init__(self, func, args, name=''):
        threading.Thread.__init__(self)
        # self.res = None
        self.name = name
        self.func = func
        self.args = args

    # def get_result(self):
    #     return self.res

    def run(self):
        print(f'starting {self.name} at: {date_time_str(datetime.now())}')
        # self.res = self.func(*self.args)
        self.func(*self.args)
        print(f'{self.name} finished at: {date_time_str(datetime.now())}')


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
        t = MyThread(loop, (i, loops[i]), loop.__name__)
        threads.append(t)

    for i in n_loops:
        threads[i].start()

    for i in n_loops:
        threads[i].join()

    print(f'---all threads end at: {date_time_str(datetime.now())}')


if __name__ == '__main__':
    main()
