word = input("Enter a word: ")
reversed_word = ""

for ch in word:
    reversed_word = ch + reversed_word   # Add character at front

if word == reversed_word:
    print("Palindrome")
else:
    print("Not Palindrome")
