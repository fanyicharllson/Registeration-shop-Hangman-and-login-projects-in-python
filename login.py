#LOGIN, REGISTER AND FORGOT PASSWORD PROJECT USING FILES IN PYTHON
def login():
    print("\n\tWelcome to Login page...")
    user_name = input("Enter your user name: ")
    user_pass = input("Enter user password: ")
    with open("file.txt", "r") as doc:
        for lines in doc:
            if user_name and user_pass in lines:
                print("Login successful")
            
            else:
                print("Failed to login! Incorrect user name or password")    

def register():
    
    print("\n\t Welcome to Reistration page...")
    with open("file.txt", "a") as file:
        user_name = input("Enter your user name: ")
        user_pass = input("Enter your password: ")
        file.write(user_name + " = " + user_pass + '\n')
    
    print("You have registered successfully!")    
    

def forgot_password():
    print("\n\t Forgot password...")
    user_name = input("Enter the user name: ")
    with open("file.txt","r") as doc:
        for lines in doc:
            if user_name in lines:
                print("Password found")
                print("password is:", lines)
            
            else:
                print("Incorrect username")    
                 
                       

print("\n\tLogin,Register and Forgot password page...")
print("1) Register")
print("2) Login")
print("3) forgot password")
print("4) exit")
choice = input("Enter your choice here: ").lower()
if choice.isdigit():
    choice = int(choice)
    if choice == 1:
        register()
    
    elif choice == 2:
        login()
    
    elif choice ==3:
        forgot_password()
    
    elif choice == 4:
        quit()    
    else:
        print("Invalid option")            
if choice == "login":
    login()

elif choice == "register":
    register()

elif choice == "forgot password":
    forgot_password()

elif choice == "exit":
    quit()   
else:
    print("Invalid option")    
    
        
        
