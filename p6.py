def char_frequency(text):
    ans={}
    for ch in text:
        if ch == " ":
            continue
        if ans.get(ch) is not None:
            ans[ch]+=1
        else:
            ans[ch]=1
    return ans

st=input("Enter a string : ")
print(char_frequency(st))