"""Ask the user for a string and print out whether this string
is a palindrome or not. (A palindrome is a string that reads the
same forwards and backwards.)"""

text = input("enter some word or phrase ")
isP = True

for i in range(int(len(text)/2)+1):
    if text[i-1] != text[-i]:
        isP = False
    else:
        pass

if isP:
    print("it is a palindrome")
else:
    print("it is not a palindrome")
