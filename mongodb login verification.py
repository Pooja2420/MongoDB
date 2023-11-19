# !pip install dnspython
# !-m pip install pymongo[srv]
import pymongo
from pymongo import MongoClient


client = pymongo.MongoClient("mongodb+srv://Poojamohan2024:1234@cluster0.9i8eu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.login
records=db.login_collection
records.count_documents({})
user_1={
    "mail_id":"abc.ed123@gmail.com",
    "password":"dfvhjHR@123"
}
records.insert_one(user_1)
User_2={
    "mail_id":"wertyuio@gmail.com",
    "password":"unitedS@2021"
}
records.insert_one(User_2)
User_3={
    "mail_id":"xcvbn@gmail.com",
    "password":"Mondays@2021"
}
records.insert_one(User_3)
x=records.find_one()
print(x)
for x in records.find():
  print(x)
db=client.get_database('login_collection')
for x in records.find('pooja'):
  print(x)


# !pip install dnspython
# !-m pip install pymongo[srv]
import re
import pymongo
from pymongo import MongoClient

client = pymongo.MongoClient("mongodb+srv://pooja:2000@cluster0.9i8eu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.registrationlogin
records=db.registrationlogin_login

print("Hello! welcome")
welcome = input("Do you have an acount? y/n: ")
  #registration
if (welcome == "n"):
  while ( True):
    email=input("enter mail id: ")
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
    if(re.search(regex,email)):   
      print("Valid Email") 
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
    passwd = input("Enter Password : ")
      
    if (password_check(passwd)):
        print("Password is valid")
        credentials=[email+passwd]
        records.insert_one(credentials)
    
    else:
        print("Invalid Password !!")   
if __name__ == '__main__':
    main()
