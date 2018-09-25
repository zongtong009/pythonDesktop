t=int(input())
n=int(input())
n_half=int(n/2)
ls=[]
for i in range(n):
    ls.append([])
    ls[i]=list(map(str,input().split()))
for listsum in ls:
    for i in ls[listsum]:
        if ls[listsum][i]=='*':
            a1,b1=listsum,i
            print(a1,b1)