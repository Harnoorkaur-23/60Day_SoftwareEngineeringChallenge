  marks=int(input("Enter your marks"))
  if(marks>90):
  print("A \nPassed")
  elif(marks>75):
  print("B \nPassed")
  elif(marks>50):
  print("C \nPassed")
  elif(marks<0 or marks>100):
  print("Invalid marks")
  else:
  print("Fail \nFailed")

