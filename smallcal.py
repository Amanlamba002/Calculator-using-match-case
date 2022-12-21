# we make a small calculator
a = float(input("enter the first number :"))
b = input("enter the operation you want to perform :+,-,/,* :")
c=float(input("enter the second number :"))


match b:
  case _ if b == '+':
    print("sir,you want to perform addition :")
    print(f"adition of {a} and {c} is :",a+c)
    
  case _ if b == '-':
     print("sir,you want to perform substraction :")
     print(f"substraction of {a} and {c} is :",a-c)
   
  case _ if b == '*':
     print("sir,thanks for choosing multiplication here is your solution \n")
     print(f"multiplication of {a} and {c} is:\n",a*c)
  case _ if b == '/':
     print("sir,thanks for choosing divide here is your solution \n")
     print(f"divide {a} and {c} is :\n",a/c)
     print("\nsir do you want see even or odd\n")
    
     temp=input("enter yes or no :\n")
     if temp=='yes':
        if a%2==0 and c%2==0:
         print("both number is even \n")
        elif a%2==0 and c%2!=0:
            print(" a is even and b is odd \n")
        elif a%2!=0 and c%2==0:
             print("a is odd and b is even \n")
        else:
            print("both number is odd\n")
     elif temp=='no':
        print("Ok sir koi baat nahi\n ")
  case _:
     print("invalid! operation")    
         
           

        
        
        

        
    
    

      
      


      
          
       
        
      
      
      
    
    
  
    
      
      