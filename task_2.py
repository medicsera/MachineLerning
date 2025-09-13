import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
import numpy as np


fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(1, 1, 1)

ax.set_title("Элементы изображения")
ax.set_xlabel("Подпись оси Х")
ax.set_ylabel("Подпись оси Y")

x1 = np.random.rand(20) * 3 + 0.5 
y1 = np.random.rand(20) * 2 + 1

ax.scatter(x1, y1, color="white", linewidths=2, edgecolors="black")

x2 = np.array([0.3, 1, 2, 3, 3.7])
y2 = np.array([1, 0.5, 0.7, 0.8, 1])

ax.plot(x2, y2, linewidth=3, color="red", label="line-1")

x3 = np.array([0.3, 1, 2, 3, 3.7])
y3 = np.array([3.3, 3.5, 3.8, 3.7, 3.3])

ax.plot(x3, y3, color="blue", linewidth=3, label="line-2")

ax.set_xlim(0, 4)
ax.set_ylim(0, 4)

ax.xaxis.set_major_locator(MultipleLocator(1))
ax.xaxis.set_minor_locator(MultipleLocator(0.5))

ax.xaxis.set_major_formatter(FormatStrFormatter("%d"))
ax.xaxis.set_minor_formatter(FormatStrFormatter("%.1f"))

ax.minorticks_on()

ax.grid(which="major", linestyle="--", linewidth=0.5, color="black")
ax.legend()

plt.show()
