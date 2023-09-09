import numpy as np
import matplotlib.pyplot as plt

names = ['A', 'B', 'C', 'F']
values = [5, 10, 6,2]

plt.figure(1, figsize=(9, 4))

plt.subplot(131)
plt.bar(names, values)
plt.subplot(132)
plt.scatter(names, values)
plt.subplot(133)
plt.plot(names, values)
plt.suptitle('Categorical Plotting')
plt.show()

