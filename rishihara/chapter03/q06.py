import numpy as np
import matplotlib.pyplot as plt
x = x = np.linspace(-5, 5, 500)
y = x**3 - 6 * x**2 + 9 * x - 3

xx = x + 2
yy = xx**3 - 6 * xx**2 + 9 * xx - 3 + 2

plt.figure(figsize=(10, 10))
plt.plot(x, y, color="red")
plt.plot(x, yy, color="blue")

plt.show()
