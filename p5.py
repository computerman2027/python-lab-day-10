def reverse_sentence_and_count_vowels(sentence):
    words = sentence.split()
    vowels = set("aeiouAEIOU")
    noofvowels = sum(1 for ch in sentence if ch in vowels) #using list comprehension
    revsen = " ".join(reversed(words))
    return revsen, noofvowels

st=input("Enter a Sentence : ")
print(reverse_sentence_and_count_vowels(st))