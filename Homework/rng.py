import random
random_integer = random.randint(1, 10)

num = int(input("Which number do you guess? : "))

if random_integer == num:
    print(random_integer)
    print("You are correct!")

else:
    print(random_integer)
    print("You guessed incorrectly.")