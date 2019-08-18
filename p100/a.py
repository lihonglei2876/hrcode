#!/usr/bin/env python
# -*- coding: utf-8 -*-


import time
import random
from multiprocessing import Process
from multiprocessing import JoinableQueue


def consumer(name, q):
    while True:
        res = q.get()
        time.sleep(random.randint(1, 3))
        print('%s 准备开吃%s' % (name, res))
        q.task_done()


def producer(name, q):
    for i in range(5):
        time.sleep(random.randint(1, 2))
        res = '大虾%s' % i
        q.put(res)
        print('%s 生产了%s' % (name, res))
    q.join()


if __name__ == '__main__':
    q = JoinableQueue()

    p1 = Process(target=producer, args=('monicx1', q))
    p2 = Process(target=producer, args=('monicx2', q))

    c1 = Process(target=consumer, args=('lili1', q))
    c2 = Process(target=consumer, args=('lili2', q))
    c3 = Process(target=consumer, args=('lili3', q))
    c1.daemon = True
    c2.daemon = True
    c3.daemon = True

    p1.start()
    p2.start()

    c1.start()
    c2.start()
    c3.start()

    p1.join()
    p2.join()