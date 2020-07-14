import random

n = random.randint(1, 30)
count = 10 

print("Guess a random number from 1 to 30, you have 10 tries.")

while count > 0:
    guess = int(input("\nEnter an integer from 1 to 30: "))
    if (guess == n):
        print("You guessed the number correctly!")
        break
    elif (guess > n):
        print("Guessed number is high")
    elif (guess < n):
        print("Guessed number is low")

    count = count - 1
    if (count <= 0):
        print("You ran out of tries. Game over!")
        print("The number was", n) 
    else:
        print("Your tries remaining:", count)

