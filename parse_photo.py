# import matplotlib.pyplot as plt
# import numpy as np
# plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
# plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
# y=[1,2,3,4,5]
# plt.figure(1)
# width=1
# for i in range(len(y)):
#     plt.figure(1)
#     plt.bar(i*width,y[i],width)
# plt.xlabel("分数")
# plt.ylabel("人数")
# plt.show()




import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif']=['SimHei']

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2, 1.03*height, '%s'%float(height))


plt.xlabel('性别')
plt.ylabel('人数')


plt.title('性别比例分析')
plt.xticks([0, 1], ['男', '女'])
rect = plt.bar(left=(0, 1), height=(1, 0.2), width=0.35, align="center", yerr=0.0001)


plt.legend((rect, ), ('图例', ))
autolabel(rect)
plt.show()