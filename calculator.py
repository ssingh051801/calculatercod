print("  welcome Guys ")
x=int(input("Enter the First Number = "))
y=int(input("Enter the Second Number = "))
sign=input("Enter the Operater = ")

if (sign == '+' ) :
    z=x+y
    print("ADDINTION OF TWO NUMBER = ",z)
elif (sign == '-' ) :
    z=x-y
    print("SUBTRACTION OF TWO NUMBER = ",z)
elif (sign == '*' ) :
    z=x*y
    print("MULTIFY OF TWO NUMBER = ",z) 
elif (sign == '/' ) :
    z=x/y
    print("DIVISION OF TWO NUMBER = ",z)
elif(sign=='%'):
    z=x%y 
    print("MODULO IS = ",z)  
else:
    print("No exist sign")      

print("THANK YOU , END THE CODE")           