"""四、 综合挑战题（无参考答案，请尝试自测）
场景：班级成绩分析可视化
 请使用 NumPy 生成 5 位学生的数学成绩
 范围 60-100 的随机整数），并使用 Matplotlib 绘制一张天蓝色的直条图。要求：
设置图表标题为 "Math Scores"。
直条宽度设置为 0.5。
解决中文乱码问题（如果标题包含中文）。
使用 plt.xticks() 将 X 轴刻度标记为
['Student A', 'Student B', 'Student C', 'Student D', 'Student E']。"""



import numpy as np
import matplotlib.pyplot as plt
a = np.random.randint(60,101,5)
b = ['Student A', 'Student B', 'Student C', 'Student D', 'Student E']
plt.title("Math Scores")
plt.bar(b,a,color = 'skyblue',width= 0.5)
plt.xticks(b)
plt.show()

