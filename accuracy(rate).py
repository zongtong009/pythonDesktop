import random
'''random.seed(10)   #不用种子会使用系统时间
for i in range(20):  
    print(random.random())'''






right=[1,2,3,4,5,6,7,8,9,10]
'''random.shuffle(right)
print(right)'''
tempsum=0
sum0=0
sum1=0
sum2=0
sum3=0
sum4=0
sum5=0
for i in range(100):
    temp=0    
    if right[0]==1:
        temp=temp+1
    if right[1]==2:
        temp=temp+1
    if right[2]==3:
        temp=temp+1
    if right[3]==4:
        temp=temp+1
    if right[4]==5:
        temp=temp+1
    if right[5]==6:
        temp=temp+1
    if right[6]==7:
        temp=temp+1
    if right[7]==8:
        temp=temp+1 
    if right[8]==9:
        temp=temp+1
    if right[9]==10:
        temp=temp+1
    if temp==0:
        sum0=sum0+1
    if temp==1:
        sum1=sum1+1
    if temp==2:
        sum2=sum2+1
    if temp==3:
        sum3=sum3+1
    if temp==4:
        sum4=sum4+1
    if temp==5:
        sum5=sum5+1
    tempsum=tempsum+temp        
    random.shuffle(right)
    print(right,temp/10,tempsum/10)
print(sum0/100,sum1/100,sum2/100,sum3/100,sum4/100,sum5/100)