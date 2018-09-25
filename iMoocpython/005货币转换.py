
a = input()

if a[0:3] in ['RMB']:  #[0]代表第一位字符
    u = (eval(a[3:]) )/6.78   #[1:]代表从第二位到最后一位字符
    print("USD{:.2f}".format(u))  
elif a[0:3] in ['USD']:
    r = 6.78*eval(a[3:])
    print("RMB{:.2f}".format(r))
else:
    print("输入格式错误") 








