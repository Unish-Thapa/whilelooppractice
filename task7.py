# Write a Python program that simulates a login system. The program 
# should prompt the user to enter a username and password. If both are 
# correct (e.g., username is "admin" and password is "1234"), 
# print "Login successful" and exit. If either is incorrect, 
# print "Invalid credentials, try again." Allow the user up to 
# 3 attempts before locking them out with the message "Too many failed attempts."

i=0
while True:
    user_input=input('enter username : ')
    User_input=input('enter password : ')
    if user_input=='admin' and User_input=="1234":
        print('login successful')
        break
    else:
        print('invalid credential')
        i+=1
    if i==3 :
        print('too many attempts')
        break





