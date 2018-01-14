#猜数字
import random
secretNumber = random.randint(1,20)
print('I am think of a number between 1 and 20.')

#六次机会猜
for guessesTaken in range(1,7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('your guess is too low.')
    elif guess > secretNumber:
        print('your guess is too high.')
    else:
        break
if guess == secretNumber:
    print('Good,job! You guess my number in ' + str(guessesTaken) + ' guesses!')
else :
    print('Nope! The number I was thinging of was ' + str(secretNumber))
    
