salarys = {}
fi = open("data.txt",'r',encoding='utf-8')

for l in fi:
    # print(l)
    stud = eval(l)
    sv = stud.items()

    v = []
    k = ''
    
    for it in sv:
        if it[0] =='sid':
            k = it[1]
        else:
            v.append(it[1])
    else:
        v.append(sum(v)//len(v))
    salarys[k] = v
fi.close()


# print(scores)
so = list(salarys.items())
so.sort(key = lambda x:x[0],reverse = False)
for l in so:
    print('{}:{}'.format(l[0],l[1]))