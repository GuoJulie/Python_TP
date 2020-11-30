import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

x = np.random.randint(1,100,size=9)
y = np.random.randint(10,100,size=9)
y2 = np.random.randint(10,100,size=9)


plt.plot(x,y,color='red',label='rouge')
plt.plot(x,y2,color='blue',label='blue')

plt.title(u'Courbe')
plt.xlabel(u'test_x')
plt.ylabel(u'test_y')

#遍历每一个点，使用text将y值显示
for i,j in list(zip(x,y)):
    plt.text(i,j+1,j,fontsize=12)


plt.legend()
# plt.figure()
plt.show()