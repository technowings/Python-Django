import time
import threading

def thread1(i):
    time.sleep(3)
    #print('No. printed by Thread 1: %d' %i)

def thread2(i):
    time.sleep(3)
    #print('No. printed by Thread 2: %d' %i)

if __name__ == '__main__':
    t1 = threading.Thread(target=thread1, args=(10,))
    t2 = threading.Thread(target=thread2, args=(12,))
    t1.start()
    t2.start()
    x=threading.active_count()
    print("No. of active threads: "+str(x))
    t1.join()
    t2.join()