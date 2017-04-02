#!/usr/bin/env python
# Author: TienTham - Junior Consultant - Altran
# minhtien.to@altran.com / tien.tominh@gmail.com
# 02nd April, 2017 

import matplotlib.pyplot as plt
import numpy as np

f2 = open('fakedata/data_1', 'r')
lines = f2.readlines()
f2.close()
type(lines)
len(lines)
print(type(lines[0]))
