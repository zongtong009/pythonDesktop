n=eval(input())
s=''

while n>0:
    if n%2==0:  # 偶数判断
        s=s+'3'
        n=(n-2)/2        
    else:       #奇数判断
        s=s+'2'
        n=(n-1)/2
        
print(s[::-1])  # 倒序输出
        
        
        
    
  
    
    
    
    