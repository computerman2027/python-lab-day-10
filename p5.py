def reverse_sentence_and_count_vowels(sentence):
    sentence=sentence+" "
    ans=""
    w=""
    noofvowel=0
    for ch in sentence:
        if ch in "aeiouAEIOU":
            noofvowel+=1
        if ch==' ':
            ans=w+" "+ans
            w=""
        else:
            w=w+ch
    return ans.strip(),noofvowel

st=input("Enter a Sentence : ")
print(reverse_sentence_and_count_vowels(st))