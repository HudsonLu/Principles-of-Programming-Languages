import matplotlib.pyplot as plt
import numpy as np

#line graph
Year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
Data_breaches = [662, 421, 471, 614, 783, 780, 1091, 1632, 1257, 1473]
plt.plot(Year, Data_breaches, marker = "o")
plt.title("Number of Data Breaches from 2010-2019")
plt.xlabel("Year")
plt.ylabel("Number of breaches")
plt.show()
