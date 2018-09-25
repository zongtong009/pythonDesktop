from functools import reduce
print(reduce(lambda x, y: x + y, [a*2 for a in range(101) if a%2]))