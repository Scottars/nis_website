import numpy as np
import matplotlib.pyplot as plt

#生成数组的x坐标轴
x=np.arange(0,2*np.pi,0.01)

#根据numpy的sin函数，生成对应的y的坐标。
y=np.sin(x)

plt.plot(x,y)
plt.show()
