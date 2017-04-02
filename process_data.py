#!/usr/bin/env python
# Author: TienTham
# tien.tominh@gmail.com
# 02nd April, 2017 

import matplotlib.pyplot as plt
import numpy as np
import re

# Chaning data format if needed
with open('fakedata/data_2', 'r+') as f:
	newf= re.sub(r'(\s+[0-9]+),([0-9]+\s+)', r'\1.\2', f.read())
	f.seek(0)
	f.write(newf)

# Storing data
f2 = open('fakedata/data_2', 'r')
lines = f2.readlines()
f2.close()
#type(lines)
#len(lines)
#print(type(lines[0]))

# Initialize some variable to be lists:
x1= []
y1= []

# Scan the row of the file stroed in lines and put the values into some variables
for line in lines:
	p = line.split()
	x1.append(float(p[0]))
	y1.append(float(p[1]))

xv = np.array(x1)
yv = np.array(y1)

# Plot the data
data_plot=plt.plot(xv,yv)
plt.setp(data_plot, 'color', 'r', 'linewidth', 2.0)
plt.xlabel('Time Stamp')
plt.ylabel('Loads [%]')
plt.title('Calculation Raw Data - [minhtien.to@gmail.com]')
plt.axis([0, 10000, 0, 100])
plt.grid(True)
plt.show()
