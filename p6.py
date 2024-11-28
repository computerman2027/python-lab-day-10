def char_frequency(text):
    text=text.lower()
    ans = {}
    for ch in text:
        if ch != " ":
            ans[ch] = ans.get(ch, 0) + 1 #dictionary comprehension
    return ans

st=input("Enter a string : ")
print(char_frequency(st))