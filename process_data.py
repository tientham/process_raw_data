#!/usr/bin/env python
# Author: TienTham
# tien.tominh@gmail.com
# 02nd April, 2017 

import matplotlib.pyplot as plt
import numpy as np
import re, glob, os

########################
# User-define Functions#
########################
def avg(list):
	sum = 0
	for element in list:
		sum += element
	print "Average: " + str(sum/len(list))
def max(list):
	tmp =0
	for element in list:
		if(element > tmp):
			tmp = element
	print "Max: " + str(tmp)

#######################
# Processing raw data #
#######################

# Appeding all data
file_list = glob.glob('./fakedata/data_*') 
#file_list=sorted(os.listdir('./fakedata/data_*')
# Check before appending file
try:
	os.remove('data.dat')
except OSError:
	pass

with open("data.dat", "a") as fout:
	for file_path in file_list :
		data_list= open(file_path, 'r').readlines()
		fout.writelines(data_list)

# Chaning data format if needed
with open('data.dat', 'r+') as f:
	newf= re.sub(r'(\s*[0-9]+),([0-9]+\s+)', r'\1.\2', f.read())
	f.seek(0)
	f.write(newf)

###############
# Draw graph  #
###############

# Storing data
f2 = open('data.dat', 'r')
lines = f2.readlines()
f2.close()

# Initialize some variable to be lists:
x_axis= []
y_axis= []

# Scan the row of the file stroed in lines and put the values into some variables
for line in lines:
	p = line.split()
	x_axis.append(float(p[0]))
	y_axis.append(float(p[1]))

xv = np.array(x_axis)
yv = np.array(y_axis)

avg(yv)
max(yv)
# Plot the data
data_plot=plt.plot(xv,yv, linestyle='', marker='o')
plt.setp(data_plot, 'color', 'r', 'linewidth', 2.0)
plt.xlabel('Time Stamp')
plt.ylabel('Loads [%]')
plt.title('Calculation Raw Data - [minhtien.to@gmail.com]')
plt.axis([0, 100, 0, 100])
plt.grid(True)
plt.show()
