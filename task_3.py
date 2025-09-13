import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(-3, 4, 1000)
y = x**2 - x - 6

fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(x, y, label="y(x) = x^2 - x - 6", color="green", linewidth=2)

ax.axhline(0, color='gray', linestyle='--', linewidth=1)

ax.axvline(-2, color='red', linestyle='-', linewidth=1.5, label="Корень: x = -2")
ax.axvline(3, color='blue', linestyle='-', linewidth=1.5, label="Корень: x = 3")

ax.set_title("y(x) = x^2 - x - 6")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.legend()
ax.grid(True)

plt.show()
