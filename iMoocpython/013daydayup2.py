#daydayup2
"""
Created on Thu Mar 22 19:31:14 2018

@author: Administrator
"""
def dayUpS(df):
    dayup=1.0000
    for i in range(365):
        if i%7 in [0,6]:
            dayup=dayup*(1-0.01)
        else:
            dayup=dayup*(1+df)
    return dayup
dayfac=0.01
while dayUpS(dayfac)<37.78:
    dayfac +=0.001
print("向上：{:.2f}".format(dayfac))

