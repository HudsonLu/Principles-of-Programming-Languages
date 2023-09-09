import matplotlib.pyplot as plt
import numpy as np

objects=('2010','2011','2012','2013','2014','2015','2016','2017','2018')
y_pos=np.arange(len(objects)) #y-axis values
values=[16.2,22.9,17.3,91.98,85.61,169.07,36.6,197.61,471.23]
plt.barh(y_pos,values,align='center',alpha=0.5) #plotting y-axis and x-axis values
plt.yticks(y_pos,objects)
plt.xlabel('Records exposed in millions') #x-axis name
plt.title('Annual number of exposed records in the United States from 2010 to 2018') #title
plt.show()
