a=[3,4,1,2,3,1,2,3,4,1,1,2,2,3,]
dicA=dict()
for key in a:
    dicA[key]=dicA.get(key,0)+1
dicA = sorted(dicA.items(),key=lambda x:x[1],reverse = True)

'''
s=[]
s.append(dicA[0][0])
s.append(dicA[1][0])
print(s)
'''
s='['+str(dicA[0][0])+','+str(dicA[1][0])+']'
print(s)