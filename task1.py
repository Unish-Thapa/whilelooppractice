# 1. Create a Python program that prompts the user to enter their age. 
# If the age is less than 18, print "You are a minor." If the age is 
# between 18 and 60, print "You are an adult." For ages over 60, print 
# "You are a senior citizen." The program should continue until the user 
# inputs "stop."


# flag:True
# while flag:
#     user_input=int(input('enter your age: (or type stop to exit)'))
# if user_input.lower()=='stop':
#     print('program terminanted')
#     break
# if not user_input.isdigit():
#     print('enter a valid age')




while True:
    age=int(input('enter age:'))
    if age<18:
        print('you are minor')
    elif 18<=age<60:
        print('you are adult')
    else:
        print('you are a senior citizen')

    user_input=input('do you want to stop?').lower()
    if user_input == ('stop '):
        break