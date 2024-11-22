def calculate_average(scores):
    ans={}
    for student in scores:
        ans[student[0]]=round(sum(student[1])/len(student[1]),2)
    return ans

st=eval(input("Enter data : "))
print("Ans = ",calculate_average(st))