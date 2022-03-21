"""
@description:

@author:Jack2Gao
@time:2022/3/20:10:29
"""

from module_ import  multi
from datetime import datetime
from multiprocessing import  cpu_count, Pool as ProcessPool
from multiprocessing.pool import ThreadPool
from multiprocessing import freeze_support
import  random

def main():
    #多进程
    freeze_support() # windows 平台要加上，并且一定要放在__name__ == "__main__":下才能避免错误
    #pool = ProcessPool() # 有效控制并发进程或者线程数，默认为内核书（推荐）
    cpus = cpu_count()
    print(cpus)

    #多线程
    pool = ThreadPool(100) # 如果不写数量就按照CPU的核数

    print(datetime.now().strftime("%X"))
    results = []
    for i in range(0,10):
        x = random.randint(1,10)
        y = random.randint(1,10)
        z = random.randint(1,10)
        result = pool.apply_async(multi, args=(x,y,z))
        results.append(result)

    pool.close()
    pool.join() # 调用join之前，先调用close函数，否则会出错。执行完

    for i in results:
        print(i.get())


if __name__ == '__main__':
    main()
