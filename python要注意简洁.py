from functools import reduce

list_a = [a * 2 for a in range(3) if a % 2]
print(list_a)
print(reduce(lambda x, y: x + y, list_a))
input()
