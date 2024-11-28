import math as m 

def is_prime(n:int)->bool:
    if n==0 or n==1:
        return False
    for i in range(2,int(m.sqrt(n))+1):
        if n%i==0:
            return False
    return True

arr=eval(input("Enter list of numbers : "))
ans={}
for i in arr:
    ans[i]=is_prime(i)

print(ans)