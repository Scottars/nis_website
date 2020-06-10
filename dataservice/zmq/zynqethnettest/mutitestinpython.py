import threading
import time


def wait2s():
    time.sleep(2)
    print('we have sleep 2s')


if __name__=="__main__":
    t=threading.Thread(target=wait2s)
    t.start()
    t.join()
    print('main thread over')
    print(t.is_alive())
    t.isAlive()
