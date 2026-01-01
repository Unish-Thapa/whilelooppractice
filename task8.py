# Write a Python program that simulates a basic arithmetic quiz. 
# Generate two random numbers between 1 and 30 and ask the user to 
# provide the result of their multiplication. If the answer is correct, 
# print "Correct!" and generate a new question. If the answer is wrong, 
# print "Incorrect, try again." Allow the user to stop the quiz when the 
# user enters "exit"

import random
while True:
    num1=random.randint(1,30)
    num2=random.randint(1,30)
    user_input=input(f'what is {num1}*{num2}?(type "exit" to quit):')
    if user_input.lower()=='exit':
        print("Quiz ends,Gooodbye!")
        break
    if not user_input.isdigit():
        print('enter a valid number : ')
        continue
    answer=int(user_input)
    if answer==num1*num2:
        print('correct')
    else:
         print('incorrect,try again')

    

        
    

   

