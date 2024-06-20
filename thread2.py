import threading
import time

def square(n):
    for i in n:
        time.sleep(1.5)
        print(i*i)

def cube(n):
    for i in n:
        time.sleep(1.5)
        print(i*i*i)

a=[1,2,3,4,5]
t1=threading.Thread(target=square,args=(a,))
t2=threading.Thread(target=cube,args=(a,))
t1.start()
t2.start()
t1.join()
t2.join()