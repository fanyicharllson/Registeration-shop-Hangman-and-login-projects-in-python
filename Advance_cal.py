from math import *
def arithmetic():
    print("1) Addition(+)")
    print("2) Multiplication(*)")
    print("3) Subtraction(-)")
    print("4) Division(/)")
    try: 
        while True:
            choice = input("Do you want to perform operation?(yes or no): ").lower()
            if choice == "yes":  
              op = input("Enter your operator: ")  
              num1 = float(input("Enter first number: "))
              num2 = float(input("Enter second number: "))
              if op == "+":
               result =  num1 + num2
               print( "The result is: ", str(result))
              elif op == "*":
               result = num1 * num2 
               print( "The result is: ", str(result))
                 
              elif op == "-":
               result = num1 - num2
               print( "The result is: ", str(result))
              elif op == "/":
               result = num1 / num2
               print( "The result is: ", str(result))
              else:
               print("Invalid operator") 
            else:
                break      
        
        print(num1 , str(op) , num2 , "=" , str(result))        
     
    except ValueError as err:     
        print(err)
        print("Enter only numbers!")  
    

                       
        
    
def trigonometry():
    print("1) sin")
    print("2) cos")
    print("3) tan")
    
    try:
        while True:
            choice = input("Do you want to perform another operation?(yes or no): ")
            if choice.lower()== "yes":
              op = int(input("Enter a trig(any between 1 and 3): "))
              num = float(input("Enter a number: "))
              if op == 1:
                  result = sin(num)
                  print("sin",str(num) , "=" , str(result))
              elif op == 2:
                   result = cos(num)
                   print("cos",str(num) , "=" , str(result))
              elif op == 3:
                   result = tan(num)
                   print("tan",str(num) , "=" , str(result))    
            
            else:
                break
    
    except ValueError as err:
        print(err)
        print("Enter numbers between 1 to 3")                
                      

print("\n\tWelcome to this Advnance calculator...")
print("Select the math type you want below")
print("1) ARITHMETIC(+,-,/,and *)")
print("2) TRIGINOMETRY(sin,cos and tan)")


type_math = input("Enter the type of math: ").lower()
if type_math == "arithmetic":
    arithmetic()
if type_math.isdigit():
     type_math = int(type_math)
     if type_math == 1:
      arithmetic()
     elif type_math == 2:
         trigonometry() 

elif type_math == "trigonometry":
    trigonometry()

else:
    print("Invalid option! Please try again")  

           
   
     
   
    
    