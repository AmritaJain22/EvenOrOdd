word = input("Enter a word: ")
count = 0
for ch in word:
    if ch in "aeiouAEIOU":
        count += 1
print("Vowels:", count)
