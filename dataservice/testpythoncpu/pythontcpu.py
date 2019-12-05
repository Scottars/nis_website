
import threading



def testcpu():
    j=1
    for i in range(1000000000000000000000):
        j=j+1
if __name__=='__main__':
    t1=threading.Thread(target=testcpu)
    t1.start()
    # t2=threading.Thread(target=testcpu)
    # t2.start()
