from math import sqrt


def prime(num):
    k = int(sqrt(num))
    for i in range(2, k + 1):
        if num % i == 0:
            return False
    return True


def monisen(no):
    j = 0
    i = 2
    while (j != no):
        if prime(i):
            M = 2 ** i - 1
            if prime(M):
                j += 1
        i += 1
    else:
        return M



print(monisen(input()))
