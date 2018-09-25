L, R = 5,10
#map(int, input().split())

# Write here the logic to print all integers between L and R
cha=int(R)-int(L)


for sum in range(cha+1):
    sum_integer=int(L)
    sum_integer+=sum
    print(sum_integer,end=' ')