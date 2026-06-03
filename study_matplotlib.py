'''使用 np.linspace(0, 2*np.pi, 100)
生成 100 个等间距的点作为 X 轴，计算其正弦值（np.sin(x)）
作为 Y 轴。请绘制一条红色、虚线（linestyle='--'）的折线图，
并添加标题 "Sine Wave"。'''

import numpy
from matplotlib import pyplot

x = numpy.linspace(0, 2*numpy.pi , 100)
y = numpy.tan(x)
pyplot.plot(x,y, linestyle = "--", color = "r", label = '趋势线')
pyplot.title("Hi")

pyplot.show()