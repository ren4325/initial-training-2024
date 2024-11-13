import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.01, 5, 500)


y1= np.log(x)
y2= np.log2(x)
y3= np.log10(x)

plt.figure(figsize=(10, 10))
plt.plot(x, y1, color="red")
plt.plot(x, y2, color="green")
plt.plot(x, y3, color="blue")

plt.show()
