# tempconvert.py(#代表注释)
Tempstr = input("请输入带有符号的温度值：")
if Tempstr[-1] in ['F', 'f']:  # 条件为TRUE执行冒号后语句，部位则跳过
    c = (eval(Tempstr[0:-1]) - 32)/1.8  # 从零位到-1位，但不包括-1位
    # eval表示去掉括号中引号并继续计算
    # eval能将任何字符串变成python可读语句
    print("转换后的温度是{:.2f}c".format(c))  # .format(c)表示format中的值填充到
    # 槽｛ ｝中，其中:.2f表示对槽中取两位小数,即XX.XX
elif Tempstr[-1] in ['C', 'c']:
    f = 1.8*eval(Tempstr[0:-1])+32
    print("转换后的温度是{:.2f}f".format(f))
else:
    print("输入格式错误")
