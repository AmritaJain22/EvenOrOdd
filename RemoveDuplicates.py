n = int(input("How many numbers? "))
numbers = []

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    if num not in numbers:
        numbers.append(num)

print("List after removing duplicates:", numbers)
