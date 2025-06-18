n = int(input("How many numbers? "))
numbers = []

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

even_sum = 0
for num in numbers:
    if num % 2 == 0:
        even_sum += num

print("Sum of even numbers is:", even_sum)
