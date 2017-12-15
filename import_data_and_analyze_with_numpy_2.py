# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt

data_file = np.loadtxt('data_file.txt', delimiter=',')

time = data_file[: , 0]
time = time - time[0]

sensors = data_file[:, 1:5]
print(sensors[0:6])

# 所有資料列，第一欄～第四欄，每欄的平均值
#avg = np.mean(sensors,0)
 
# 每列資料的平均值
avg = np.mean(sensors, axis=1)

my_data = np.vstack((time, sensors.T, avg))
my_data = my_data.T
np.savetxt('export.csv', my_data, delimiter=',')

plt.plot(time/60, sensors[: ,1], 'ro')
plt.plot(time/60, avg, 'b.')
plt.legend(['Sesor 2', 'Average'], loc='best')
plt.xlabel('Time (min)')
plt.ylabel('Values')
plt.savefig('my_plot.png')
plt.show()
