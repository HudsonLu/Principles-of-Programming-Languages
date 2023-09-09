import numpy as np
import matplotlib.pyplot as plt

x = ("A","B","C","D","F") #x-axis markings
markings = np.arange(len(x))
y = [4,6,2,1,1] #grade distribution
plt.bar(markings,y, align='center',alpha=0.5) #barchart
plt.xticks(markings,x) #draw x-axis markings
plt.title("student grades")
plt.xlabel("Grades")
plt.ylabel("Grade Distribution")
plt.show()
