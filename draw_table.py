import matplotlib.pyplot as plt
import os
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
#区间的形式都是[l,r),左闭右开区间
def get_score():
    score_num=[]
    for i in range(6):
        score_num.append(0)
    list=os.listdir()
    for name in list:
        if len(name)==24:
            score=float(name[:3])
            if score>=3 and score<4:
                score_num[0]+=1
            elif score>=4 and score<5:
                score_num[1]+=1
            elif score>=5 and score<6:
                score_num[2]+=1
            elif score>=6 and score<7:
                score_num[3]+=1
            elif score>=7 and score<8:
                score_num[4]+=1
            elif score>=8 and score<=9:
                score_num[5]+=1
    return score_num

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+ 0.3, height+ 0.05, '%d' % height, ha='center', va='bottom')

def draw_column():
    score=get_score()
    plt.title('nyist证件照颜值分数分析   总数：2118')
    plt.xlabel('颜值区间')
    plt.ylabel('人数')
    plt.xticks([0,1,2,3,4,5], ['3~4分', '4~5分','5~6分','6~7分','7~8分','8~9分'])
    rect=plt.bar(left=(0,1,2,3,4,5), height=score, width=0.7, align="center")
    plt.legend((rect,), ('数量',))
    autolabel(rect)
    plt.show()

def draw_circle():
    score = get_score()
    labels='3~4分', '4~5分','5~6分','6~7分','7~8分','8~9分'
    sizes=score
    explode=(0,0,0,0.05,0,0)
    plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=False,startangle=90)
    plt.axis('equal')
    plt.show()



def main():
    os.chdir('D:\\我的程序\\Python\\nyist_photo\\南阳理工所有照片')
    #draw_column()
    draw_circle()

if __name__ == '__main__':
    main()

