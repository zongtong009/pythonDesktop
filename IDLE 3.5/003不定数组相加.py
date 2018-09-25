N = input()

# Get the input
numArray = map(int, input().split())

sum_integer = 0
# Write the logic to add these numbers here


num = 0
n = int(N)  # N的属性是str,这里转换成整数
for sum in numArray:
    sum_integer += sum
    num += 1
    if num == n:
        break


# Print the sum
print(num)
print(sum_integer)
