n = int(input("How many numbers? "))
numbers = []
for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
unique = list(set(numbers))
unique.sort()

if len(unique) >= 2:
    print("Second largest is:", unique[-2])
else:
    print("Not enough unique numbers.")
