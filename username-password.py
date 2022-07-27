unp = {"user1":"1234","user2":"4321","user3":"123","user4":"admin123","user5":"admin321"}
user_name = str(input("Please Enter your user name:\n"))

# if user_name in unp:
#     password = str(input("Please Enter your password:\n"))
#     x= unp.get(user_name)
#     if x == password:
#         print("Welcome to our portal:\n")
#     else:
#         print("Your password is wrong\nPlease try again")

# else:
#     print("Your name is not registerd\nKindly sign up")
if user_name in unp:
     password = str(input("Please Enter your password:\n"))
     x= unp.get(user_name)
     if x == password:
         print("Welcome to our portal:\n")
        
     elif x != password:
         print("Your password is wrong\nPlease try again")
         


else:
     print("Your name is not registerd\nKindly sign up")