                            #shop project ealing with files,loops and more...
import os
import random
def add():
    answer = ""
    name_file =""
    answer = input("Want to add or create a new file(add/create or q to exit):  ").lower()
    if answer == "create":
        name_file = input("Enter the name of the file: ")
        doc = open(name_file,"w")
        doc.close()
        print("Successfully created the file",doc)
        answer = input("Do you want add a product to the file? y or n: ").lower()
        if answer == "y":
            while True:
                 try:
                    answer = int(input("How many line do you want to inser the product? "))
                    for _ in range(answer):
                            file_text = input("Enter the text for line {}: ".format(_+1))
                            file = open(name_file,"a")
                            file.write(file_text +'\n')    
                   
                    print("Successfull inserted the products") 
                    file.close()
                    break               
                 except ValueError as err:  
                    print(err)
                    print("Enter only number")
        
        else:
            quit()   
    
    elif answer == "add":
        directory = r"C:\Users\NTECH\OneDrive\Desktop\GENERAL FOLDER\project.py"
        file_name = input("Enter the name of the file: ")
        files = os.listdir(directory)
        if file_name in files:
            print("File found!")
            with open(file_name,"a") as doc:
                 try:
                    answer = int(input("How many line do you want to add the product: "))
                    if answer <=0:
                        print("Invalid number, either you entered zero or decmal")
                        quit()
                    for _ in range(answer):
                        file_text = input("Enter the text for line {}:  ".format(_+1))
                        doc.write(file_text +'\n')    
                   
                    print("Successfull added the products to " + file_name)
                    print("\n")
                    choice = input("Do you want add another product(yes or no): ").lower()
                    if choice == "yes":
                        password()
                    
                    else:
                        print("Thankyou!")                  
                 except ValueError as err:  
                    print(err)
                    print("Enter only number not text nor decimals")     
        
        else:
            print("File not found")  
    
    elif answer == "q":
        quit()
    
    else:
        quit()                                   





def buy():
    print("Welcome to resto's main menu. please select your choice from the menu below..")
    directory = r"C:\Users\NTECH\OneDrive\Desktop\GENERAL FOLDER\project.py"
    file_name = "main.txt"
    good = ""
    file = os.listdir(directory)
    if file_name in file:
        print("\n")
        with open(file_name,"r") as doc:
            for lines in doc.readlines():
                print(lines)
        
            try:
             customer_num = int(input("Please you want to order how many food stuffs: "))
             for num_idx in range(customer_num):
                    good_gd = input("Enter the product {}: ".format(num_idx+1))
             with open("main.txt", "r") as doc:      
              for good in doc.readlines():       
               if good_gd in good:
                 print("Sorry we don't have this good! Please come back leter")
                 quit()
               else:
                 print("Thankyou for ordering our products!")          
                     
                 
                   
                       
                #    else:
                #        print("Success" + str(num))       
            #  print("These are the good you odered" + str(num))           
            except ValueError as err:
              print(err) 





def delete_good_from_file(file_path, good_to_delete):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("File not found!")
        return

    found = False
    with open(file_path, 'w') as file:
        for line in lines:
            if good_to_delete not in line:
                file.write(line)
            else:
                found = True

    if not found:
        print("Goods not found in the file.")
    else:
        print("Goods deleted successfully.")



def modify_good_in_file(file_path, old_good_name, new_good_name):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("File not found!")
        return

    found = False
    with open(file_path, 'w') as file:
        for line in lines:
            if old_good_name in line:
                modified_line = line.replace(old_good_name, new_good_name)
                file.write(modified_line)
                found = True
            else:
                file.write(line)

    if not found:
        print("Goods not found in the file.")
    else:
        print("Goods modified successfully.")

# Example usage:


     


def view():
        print("\t Below are our various product;")
        directory = r"C:\Users\NTECH\OneDrive\Desktop\GENERAL FOLDER\project.py"
        file_name = "main.txt"
        file = os.listdir(directory)
        if file_name in file:
               print("\t File found! ")
               with open(file_name, "r") as doc:
                  print("These are the products contain file! " + file_name)
                  print("\n")
                  lines = doc.readlines()
                  print(lines)
               print("\n")   
               chioce = input("Will you like to buy now?(yes or no):  ").lower()
               if chioce == "yes":
                   buy()
               else:
                   print("Thankyou " + name + "! for comming")  
                   quit()        
        else:
            print("\n")
            print("An Error occured ") 
            print("Please come back later! Thankyou")                            
  
  
  
                
def game():
    print("\n\t Welcome to resto's free game to win product...")
    print("Your guess shuold be between 0 and 5")
    print("You are to guess only 2 times!")
    print("If the guess matches with what we have then you win!")
    print("\n\t GET STARTED...")
    num = 2
    num_count = 0
    out_of_limit = False
    answer = int
    product_list = ["2-kg of fish",  "1-packet of maggie","20-ltr of GOil", "A bag of salt", "2- cattons of indomie","150,000"]
    guessing_answer = random.randint(0,5)
    product_win = product_list[guessing_answer]
    while answer != guessing_answer and not(out_of_limit):
           if num_count < num:
               try:
                answer = int(input("Guess the number: "))
                num_count +=1
               except ValueError as err:
                   print("\n")
                   print(err)
                   print("You entered a string!")
                   print("Enter only Numbers") 
           else:
              out_of_limit = True 
              
    if out_of_limit:
            print("\n")
            print("You are out limit")
            print("The guess was: " + str(guessing_answer),"!")
            print("You failed! Please try some other time.")
            
    
    else:
        print("\n")
        print("You win, You guess " + str(guessing_answer))
        print("You won " , product_win)
        print("Congaratulation!")                     
    
  
  
  
    
def password():
    print("\n\t Meant for administrators")
    password = "shop"
    out_of_limit = False
    password_limit = 3
    password_count = 0
    answer = ""
    
    while answer != password and not(out_of_limit):
        if password_count <password_limit:
            answer = input("Enter password: ")
            password_count +=1
        else:
           out_of_limit = True
    
    if out_of_limit:
        print("You are out of limit")
        print("Wrong Password!")
        quit()
    
    else:
        print("Password Correct!")
        add()                 
    

print("\n\t Welcome to Resto's shop...")
print("A place where you get your food stuffs")
name = input("Please enter your name: ")
print("Hi",name)
print("Select from the option below;")
print("\n")
print("1] Add products")
print("2] View products")
print("3] Buy product")
print("4] Play a guessing game to win a product")
print("5] Delete product")
print("6] Modify product be it name or price")
print("7] View total sales")
print("8] exit")

product_number =0
while True:
       if product_number<1 or product_number>8:
           print("\n")
           print("Enter a number between 1 and 8")
           try:
               product_number = int(input("Enter the which  correspond to your choice: "))
           except ValueError as err:
               print("\n")
               print(err)
               print("Do not enter text or Deacimal numbers")   
                 
       elif product_number >=1 or product_number >=8:
           break
       else:
           print("\nInvalid value")            

if product_number == 1:
    password()
elif product_number == 2:
    view()
elif product_number == 3:
    buy()    
elif product_number == 4:
    game()       
elif product_number == 5:
     directory = r"C:\Users\NTECH\OneDrive\Desktop\GENERAL FOLDER\project.py"
     file = os.listdir(directory)
     file_path = "main.txt"
     if file_path in file:
         print("\n File found")
            # Change this to your file path
         good_to_delete = input("Enter the good to delete: ").lower()
         delete_good_from_file(file_path, good_to_delete) 
     else:
         print("System error come back later! Thankyou")            
elif product_number == 6:
    directory = r"C:\Users\NTECH\OneDrive\Desktop\GENERAL FOLDER\project.py"
    file = os.listdir(directory)
    file_path = "main.txt"# Change this to your file path
    if file_path in file:
        print("\n File found")
        old_good_name = input("Enter the name of the good to modify: ")
        new_good_name = input("Enter the new name for the good: ")
        modify_good_in_file(file_path, old_good_name, new_good_name)
    
    else:
        print("System error come back later! Thankyou")    

    
elif product_number == 7:
    print() 
elif product_number == 8:
    quit() 

else:
    print("Enter a number!")       