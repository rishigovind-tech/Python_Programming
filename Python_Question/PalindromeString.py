s1 = input("Enter the word: ")

s2 = s1.replace(' ', '')
rev = s2[::-1]

if s2.casefold() == rev.casefold():
    print("Palindrome:", s1)
else:
    print("Not a palindrome")