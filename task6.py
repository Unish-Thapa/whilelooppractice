# Write a Python program that generates a random number 
# between 1 and 10 and prompts the user to guess the number. 
# The program should provide hints such as "guess higher" or 
# "guess lower" based on the user's input. Once the user guesses
# the correct number, the program should display the number of 
# attempts it took to guess the correct number.


import random
total_guess=0
number=random.randint(1,10)
while True:
    guess_num=int(input('enter number  : '))
    if guess_num<number:
        print("too low")
        total_guess+=1
    elif guess_num>number:
        print('too high')
        total_guess+=1
    else:
        print(f'the num is {number}')
        print(f'total guess{total_guess}')
        total_guess+=1
        break
    
