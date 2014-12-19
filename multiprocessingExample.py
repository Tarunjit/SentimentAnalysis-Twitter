__author__ = 'Tarun'

from multiprocessing import Process
import sys
import time

# g = 0
#
# def func1():
#     global g
#     for i in range(10):
#         print("in func1")
#         time.sleep(1)
#     print("out func1")
#
# def func2():
#     global g
#     for i in range(10):
#         print("in func2")
#         time.sleep(1)
#     print("out func2")
#
# if __name__ == "__main":
#     p1 = Process(target=func1)
#     p1.start()
#     p2 = Process(target=func2)
#     p2.start()



rocket = 0

def func1():
    global rocket
    print('start func1')
    while rocket < 10**7:
        rocket += 1
    print('end func1')

def func2():
    global rocket
    print ('start func2')
    while rocket < 10**7:
        rocket += 1
    print ('end func2')

if __name__=='__main__':
     p1 = Process(target = func1)
     p1.start()
     p2 = Process(target = func2)
     p2.start()