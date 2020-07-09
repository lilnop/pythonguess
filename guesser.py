import random

n = random.randint(1, 30)
count = 10 

print("Guess a random number from 1 to 30, you have 10 tries.")
guess = int(input("Enter an integer from 1 to 30: "))
while count != 1:
    if guess < n:
        print("Guessed number is low")
        count  = count - 1
        print("Your tries remaining:")
        print(count)
        guess = int(input("Try again: "))

    elif guess > n:
        print("Guessed number is high")
        count  = count - 1
        print("Your tries remaining:")
        print(count)
        guess = int(input("Try again: "))

    elif count == 0:
        print("You ran out of tries. Game over!")
        break

    else:
        print("You guessed the number correctly!")
        break
    print("Game over")
    
