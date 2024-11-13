import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-2, 2, 500)

y1 = 2 ** x
y2 = 2 ** (-x)

plt.figure(figsize=(10, 10))
plt.plot(x, y1, color="red")
plt.plot(x, y2, color="blue")

plt.show()
