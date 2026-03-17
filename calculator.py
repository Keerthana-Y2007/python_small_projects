print("        BASICS OPERATORS")
num1=float(input("enter first number\n"))
num2=float(input("enter second number\n"))
print("  \n Select the operation:\n")
print("1.add")
print("2.subract")
print("3.multiplication")
print("4.division")
choice=int(input("\n enter 1-4\n"))
if choice==1:
  result = num1+num2  
  print(f"{num1}+{num2}={result}")  
elif choice==2:
  result=num1-num2
  print(f"{num1}-{num2}={result}")
elif choice==3:
   result=num1*num2
   print(f"{num1}*{num2}={result}")
   
elif choice==4:
    if num2==0:
       print("it cannot be zero")
    else:
       result=num1/num2
       print(f"{num1}/{num2}={result}")  
else:
     print("invalid") 
     