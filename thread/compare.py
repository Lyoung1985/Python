#!/usr/bin/python3
# -*- coding:UTF-8 -*-

from myThread import MyThread
from time import ctime, sleep


def fib(x):
    # 斐波拉契
    sleep(0.005)
    if x < 2:
        return 1
    return fib(x-2)+fib(x-1)


def fac(x):
    # 阶乘
    sleep(0.1)
    if x < 2:
        return 1
    return x*fac(x-1)


def sum(x):
    # 累加
    sleep(0.1)
    if x < 2:
        return 1
    return x + sum(x-1)

funcs = [fib, fac, sum]
n = 12


def main():
    nfuncs = range(len(funcs))
    print('***SINGLE THREAD***')
    for i in nfuncs:
        # 单线程顺序执行
        print('starting', funcs[i].__name__, 'at:', ctime())
        print(funcs[i](n))
        print(funcs[i].__name__, 'finished at:', ctime(), '\n')

    print('\n ***MULTIPLE THREADS***')
    threads = []
    for i in nfuncs:
        # 多线程执行
        t = MyThread(funcs[i], (n,),funcs[i].__name__)
        threads.append(t)

    for i in nfuncs:
        threads[i].start()

    for i in nfuncs:
        threads[i].join()
        print(threads[i].get_result())

    print('all DONE')

if __name__ == '__main__':
    main()