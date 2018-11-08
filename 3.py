import math

# 判断质数
def isprime(x):
    div_num = 2
    if x==1 or x==4:
        return False
    elif x==2 or x==3:
        return True
    else:
        pass
    while div_num <= math.sqrt(x):
        if x % div_num == 0:
            return False  
        div_num += 1
    else:
        return True

# 判断莫森数
def ismonisen(x):
    if isprime(x) and isprime(2 ** x - 1):
        # 2和它的3输出false，因为math.sqrt(3)=1,为false
        return True
    else:
        return False

# 主函数

if __name__ == "__main__":
    num_list = [1, 2, 3, 4, 5, 6, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
    result_list = []
    print("列表中的莫尼森数为：",end='')
    for num in num_list:
        temp = 2 ** num - 1
        if ismonisen(num):  #
            print(num, end=' ')
            result_list.append(str(temp) + ' ')
    print('')


with open("myf2.out", "a") as fp:     # 写入输出文件
    fp.writelines(result_list)
    fp.write("\nMy exam number is: 01124001232516\n")
