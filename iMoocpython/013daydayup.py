#daydayup1.py
'''
Created on Thu Mar 22 20:06:01 2018

@author: Administrator
'''
dayup=1.0
for i in range(365):
    if i%7 in [0,6]:
        dayup=dayup*0.99
    else:
        dayup=dayup*1.01
print("向上：{:.2f}".format(dayup))
