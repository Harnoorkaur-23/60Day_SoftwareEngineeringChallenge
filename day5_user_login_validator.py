import pwinput
correct_username=input("Enter the username:")
correct_password=pwinput(input("Set a password:",mask='*')
attempts=0
print("*******************************")

while True:
   username=input("Enter username: ")
   password=input("Enter the password:")
   if username==correct_username and password==correct_password:
     print("Login Successful")
     print("*******************************")
     break
 else:
     print("Invalid credentials")
     print("*******************************")
     attempts=attempts+1
     if attempts==3:
        print("Account locked please try again later")
        print("*******************************")
        break
