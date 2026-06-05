from matplotlib.lines import lineStyles

print('''第一题：一周气温趋势（折线图 plot）
场景： 使用 NumPy 记录某地过去 7 天的最高气温，绘制折线图观察趋势。
要求：
使用 np.array() 创建一个包含 7 个气温数值的数组：
。
绘制折线图，线条颜色为绿色（'g'），线型为点划线（'-.'），并带有圆圈标记（'o'）
。
设置 X 轴标签为 "Day"，Y 轴标签为 "Temperature"。
添加标题 "Weekly Temperature"。''')
import numpy as np
import matplotlib.pyplot as plt
a = np.random.randint(24,32,8)
b = np.array(a)
plt.plot(b,color = 'g', linestyle = "-.",marker = "o")
plt.xlabel('Day')
plt.ylabel('Temperature')
plt.title("Weekly Temperature")
plt.show()