import threading
def cal_fun():
    print("thread")
t1=threading.Thread(target=cal_fun(),args=cal_fun())
t1.start()