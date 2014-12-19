__author__ = 'Tarun'

import _thread
import time

def print_time(tname,delay):
    count = 0

    while count<5:
        time.sleep(delay)
        print(tname)
        count +=1

def new_print(i):
    count = 0
    while count<5:
        print(i)
        count+=1

try:
    _thread.start_new(print_time, ("Thread1",1))
    _thread.start_new(new_print, ("Thread2"))
except:
    print("Error")

while 1:
    pass
