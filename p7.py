import string_operations as sop

print("Menu\n1. Reverse a string\n2. Frequency of a character\n3. Convert to uppercase\n4. Palindrome string\n5. Exit")
while True:
    choice=int(input("Enter your choice : "))
    if choice==1:
        st=input("Enter a string : ")
        print("Reversed String =",sop.rev_a_string(st))
    elif choice==2:
        st=input("Enter a string : ")
        ch=input("Enter a character : ")
        print("Frequency of",ch,"is",sop.frequency_of_a_character(st,ch))
    elif choice ==3:
        st=input("Enter a string : ")
        print("UPPERCASE STRING =",sop.uppercase(st))
    elif choice==4:
        st=input("Enter a string : ")
        print("PALINDROME STRING =",sop.palindrome(st))
    elif choice == 5:
        break

