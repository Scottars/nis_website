
import  time


def test():
    i = 0
    while True:
        i = 1 + 1
        time.sleep(1)
        print('New i:',i)

if __name__=='__main__':
    test()
