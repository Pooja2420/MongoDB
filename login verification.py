# !pip install dnspython
# !-m pip install pymongo[srv]
import re
import csv
print("Welcome...")
welcome = input("Do you have an acount? y/n: ")
if welcome == "n":
   while True:
       regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
       email = input("Enter a username:")
       if(re.search(regex,email)):   
        print("Valid Email") 
        file = open(email + ".txt", "w")
        break 
       else:
           print("Invalid Email")
def password_check(passwd):
    SpecialSym =['$', '@', '#', '%','!','^','&','*']
    val = True
    if (len(passwd) < 5):
        print('length should be at least 5')
        val = False
    if (len(passwd) > 16):
        print('length should be not be greater than 16')
        val = False
    if not any(char.isdigit() for char in passwd):
        print('Password should have at least one numeral')
        val = False
    if not any(char.isupper() for char in passwd):
        print('Password should have at least one uppercase letter')
        val = False
    if not any(char.islower() for char in passwd):
        print('Password should have at least one lowercase letter')
        val = False
    if not any(char in SpecialSym for char in passwd):
        print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        return val
def main():
    if(passwd==passwd1)  :
      if (password_check(passwd)):
          print("Password is valid")
      else:
          print("Invalid Password !!") 
    else:
      print("Password does not match")
    file.write(email + ":" + passwd)  
    file.close()
if __name__ == '__main__':
  passwd = input("Enter Password : ")
  passwd1=input("Confirm Password")
  main()
file.write(email + ":" + passwd)
file.close()
if welcome == "y":
   while True:
    login1 = input("Login:")
    login2 = input("Password:")
    file = open(login1 + ".txt", "r")
    data = file.readline()
    file.close()
    if data == login1 + ":" + login2:
      print("Welcome")
      break
print("Incorrect username or password.")
main()