print('''题目场景： 你有一个名为 scores.txt 的文件，内容如下（每行一个分数）：
85
92
78
90
88
要求：
使用 with open 读取该文件，并将这些分数存入一个 Python 列表。
将该列表转换为 NumPy 数组，并计算这些分数的平均分。
（可选挑战）使用 Matplotlib 绘制一张折线图来展示这些分数的波动。
你可以尝试写一下读取文件并计算平均分的部分，写好后贴给我！''')
import numpy as np
import matplotlib.pyplot as plt
a = []
with open ('score.txt','r') as f :
    for i in f:
        a.append(int(i))
b = np.array(a)
c = np.mean(b)
plt.plot(a,linestyle = "--")
print(b)
print(c)
plt.show()