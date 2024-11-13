import numpy as np
import matplotlib.pyplot as plt

for i in range(0, 361, 1):
  sin = np.sin(i*2*np.pi/360)
  cos = np.cos(i*2*np.pi/360)
  tan = np.tan(i*2*np.pi/360)

  print(i, "{:.5f}".format(sin), "{:.5f}".format(cos), "{:.5f}".format(tan))

a = [1, 2, 3]
b = [2, 3, 4]

c = [a,
     b]
print(c)

c = [[1, 2, 3],
     [2, 3, 4]]

print(c)
