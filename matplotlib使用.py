import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def uitl_1():
    data = pd.DataFrame(np.random.randn(1000,4),index=np.arange(1000),columns=list('ABCD'))
    # data = data.cumsum()
    # 有多种的情况下多个叠加就好了,这种是B,C,D
    ax  = data.plot.scatter(x='A',y='B',color = 'Blue',label = 'Class_1')
    ax_2 = data.plot.scatter(x='A',y='C',color = 'Green',label = 'Class_2',ax = ax)
    data.plot.scatter(x='A',y='D',color = 'red',label = 'Class_3',ax = ax_2)
    # data.plot()
def uitl_2():
    x = np.linspace(-1,1,50)
    y = 2*x + 1
    plt.plot(x,y)
def uitl_3():
    #figure的作用是把两个曲线分开成两个图

    x = np.random.random(9)
    y= x**2
    y2=x*2+1
    plt.figure(num=3)#num是figure窗口的命名顺序，如果不定义的话默认从1开始，如果前面有定义了后面都没有定义则从定义了之后的开始数起
    plt.plot(x,y)
    plt.figure()
    plt.plot(x,y2)
def uitl_4():
    x = np.linspace(0,10,50)
    y= x**2
    y2=x*2+1
    plt.plot(x,y)
    plt.plot(x,y2)
    # plt.ylim((0,1))#限制Y的显示范围
    # plt.xlim((0,2))#限制X的显示范围
    new_ticks = np.linspace(0,2,5)
    plt.yticks([0.2,0.4,0.6,0.8,1],
               ['v low','low','ok','better','best'])#改变y轴显示的标记

    #移动横线
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.spines['bottom'].set_position(('data',5))
    ax.spines['left'].set_position(('data',5))
if __name__ == "__main__":
    #uitl_1()
    #uitl_2()
    uitl_4()

    plt.show()


    plt.show()