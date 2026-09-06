num1=int(inpt("Enter the first number"))
num2=int(inpt("Enter the second number"))
operator=input("Enter the operator(+,-,*,/)")
    if operator =="+":
          result=num1 +num2
          print(f"Result:{result})
   elif opeartor =="-":
         result=num1-num2
         print(f"Result:{result})
   elif opeartor =="*":
         result=num1*num2
         print(f"Result:{result})
   elif opeartor =="/":
          if num2 == 0:
            print("Error division is not by zero")
         else:
            result=num1/num2
            print(f"Result:{result})
    else:
      print("Invalid operator use opeartor(+,-,*,/")
