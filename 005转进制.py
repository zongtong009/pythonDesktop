# print("二进制{0:b}、十进制{0}、八进制{0:o}、十六进制{0:x}".format(0x4DC0+50))

xe0 = 0x4DC0+50   # 0x4DF2
bs2 = bin(xe0)
xe3 = hex(xe0)
of3 = oct(xe0)
hs1 = xe0

print("二进制{}、十进制{}、八进制{}、十六进制{}".format(bs2,hs1,of3,xe3))

print(hex(11),oct(11),bin(11),int(0xb))