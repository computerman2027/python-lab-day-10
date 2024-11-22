def fibonacci_sequence(n):
    ans=[]
    a=-1
    b=1
    for i in range(n):
        c=a+b
        ans.append(c)
        a=b
        b=c
    return tuple(ans)

try:
    n=int(input("Enter number of terms of fibonacci : "))
    print(fibonacci_sequence(n))
except:
    print("Some error occured")