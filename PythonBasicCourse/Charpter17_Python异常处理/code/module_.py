"""
@description:

@author:Jack2Gao
@time:2022/3/20:10:32
"""
import  os
import threading
import time


def multi(x,y,z):
    #打印进程和线程ID
    print("pid tid ==>", os.getpid(),threading.currentThread().ident )
    i = 1
    sum = 0
    while i < 10:
        sum = x * y * z
        x +=1
        y +=1
        z +=1
        i +=1
        time.sleep(1)
        print(i)
    #返回计算结果，进程号，线程号
    return  sum, os.getpid(), threading.currentThread().ident


def main():
    print(multi(1,3,5))


if __name__ == '__main__':
    main()
