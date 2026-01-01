# Write a Python program that continuously prompts the user 
# to input a fruit name. If the input is "apple," the program 
# should print "You got it!" and stop. Otherwise, it should 
# display "Try again" and continue.

while True:
    fruit=input('enter fruit name: ')
    if fruit!='apple':
        print('try again:(')
    else:
        print('You got it! ;)')