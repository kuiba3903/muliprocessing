import multiprocessing as mp
import time
import threading as td
import matplotlib.pyplot as plt


def j(a,b):
    print(a+b)


def job(a):
    return a*a

def add(q,k):
    res = 0
    for i in range(k):
        res += i+i**2+i**3
    q.put(res)

def multi_core():
    # 定义一个pool,并定义CPU的核数量为3
    pool = mp.Pool(processes=3)
    res = pool.map(job, range(10))
    print(res)
    res = pool.apply_async(job, (2,))
    print(res.get())
    multi_res = [pool.apply_async(job, (i,)) for i in range(10)]
    print([res.get() for res in multi_res])

def multicore(k):
    q = mp.Queue()
    p1 = mp.Process(target=add,args=(q, k))
    p2 = mp.Process(target=add, args=(q, k))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print("multicore:",res1+res2)


def normal(k):
    res = 0
    for _ in range(2):
        for i in range(k):
            res += i+i**2+i**3
    print("normal:",res)


def multithread(k):
    q = mp.Queue()
    t1 = td.Thread(target=add, args=(q,k))
    t2 = td.Thread(target=add, args=(q,k))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    res1 = q.get()
    res2 = q.get()
    print("multiThread:", res1+res2)


if __name__=="__main__":
    k = 10000
    p1 = mp.Process(target=j, args=(1, 2))
    p1.start()
    p1.join()
    q = mp.Queue()
    p2 = mp.Process(target=add, args=(q, k))
    p3 = mp.Process(target=add, args=(q, k))
    p2.start()
    p3.start()
    p2.join()
    p3.join()
    res1 = q.get()
    res2 = q.get()
    print(res1+res2)
    # time_normal = []
    # time_multicore = []
    # time_multithread = []
    # y= [10, 100, 1000, 10000, 100000, 1000000, 1000000, 100000000]
    # for number in y:
    #     print("数量级为{}的时间比较".format(number))
    #     st = time.time()
    #     normal(number)
    #     st1 = time.time()
    #     print("normal:",st1-st)
    #     time_normal.append(st1-st)
    #     multithread(number)
    #     st2 = time.time()
    #     print("multiThread time:",st2-st1)
    #     time_multithread.append(st2-st1)
    #     multicore(number)
    #     st3 = time.time()
    #     print("multicore time:", st3-st2)
    #     time_multicore.append(st3-st2)
    #     print("***********************************")
    # plt.plot(y, time_normal,  label="normal")
    # plt.plot(y, time_multithread, label="multithread")
    # plt.plot(y, time_multicore,  label="multicore")
    # plt.legend()
    # plt.show()

    multi_core()
