import random
num = random.randint(1, 100)
guess = 0
while guess != num:
    guess = int(input("Guess number: "))
    if guess < num:
        print("Too low")
    elif guess > num:
        print("Too high")
print("Correct!")
