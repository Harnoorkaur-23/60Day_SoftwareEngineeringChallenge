def fizzbuzz_automation(n,filename="fizzbuzz_output.txt"):
  with open(filename,"w") as file:
   for i in range(1,n+1):
     if i%3 === 0 and i%5==0 :
         file.write("FizzBuzz\n")
    elif i%3==0:
         file.write("Fizz\n")
    elif i%5==0:
         file.write("Buzz\n")
    else:
         file.write(f"{i}\n")
  print(f"successfully saved FizzBuzz resultup to {n} in '{filename}'!")
fizzbuzz_automation(20)
