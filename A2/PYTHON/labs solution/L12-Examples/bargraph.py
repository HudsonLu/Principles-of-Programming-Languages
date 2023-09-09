import numpy as np
import matplotlib.pyplot as plt

grades = ("A","B","C","F")
markings = np.arange(len(grades))
distribution = [5,2,2,1]
plt.bar(markings,distribution, align='center',alpha=0.3)
plt.xticks(markings,grades) #x axis markings
plt.title("student grades")
plt.xlabel("Grades")
plt.ylabel("distribution")
    
plt.show()
