import numpy as np
import matplotlib.pyplot as plt



def triangle_wave(start,size):
    x = np.arange(start, start+1, 1.0/size)
    # y = np.where(x<start+0.5, x-start, 0)
    y = np.where(x>=start+0.5, start+1-x,x-start )
    return x, y


def triangle_wave2(size):
    x = np.arange(0, 1, 1.0/size)
    y = np.where(x<0.5, x, 0)
    y = np.where(x>=0.5, 1-x, y)
    return x, y

def square_wave(start,size):
    x = np.arange(start, start+1, 1.0/size)
    y = np.where(x<start+0.5, 1.0, 0)
    return x, y


if __name__=='__main__':
    xout=[]
    yout=[]
    for i in range(10):
    # i=10
        x,y=square_wave(i,100)

        xout=np.append(xout,x)
        yout=np.append(yout,y)

    # x,y=triangle_wave2(3)

    plt.plot(xout,yout)
    plt.show()